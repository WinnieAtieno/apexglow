import uuid
from datetime import datetime, timezone
from ..extensions import db

class Service(db.Model):
    __tablename__ = "services"

    # ============================================================
    # Primary Key
    # ============================================================
    id = db.Column(
        db.String(36), 
        primary_key=True, 
        default=lambda: str(uuid.uuid4())
    )

    # ============================================================
    # Core Service Attributes
    # ============================================================
    name = db.Column(
        db.String(100), 
        nullable=False
    )
    
    price = db.Column(
        db.Float, 
        nullable=False,
        default=0.0
    )

    # ============================================================
    # Multi-Tenant Workspace Links
    # ============================================================
    carwash_id = db.Column(
        db.String(36),
        db.ForeignKey("carwashes.id", ondelete="CASCADE"),
        nullable=False
    )

    # ============================================================
    # Metadata
    # ============================================================
    created_at = db.Column(
        db.DateTime,
        nullable=False,
        default=lambda: datetime.now(timezone.utc)
    )

    updated_at = db.Column(
        db.DateTime,
        nullable=False,
        default=lambda: datetime.now(timezone.utc),
        onupdate=lambda: datetime.now(timezone.utc)
    )

    # ============================================================
    # Relationships
    # ============================================================
    carwash = db.relationship(
        "CarWash",
        back_populates="services"
    )

    def __repr__(self):
        return f"<Service {self.name} (${self.price}) at Shop {self.carwash_id}>"
