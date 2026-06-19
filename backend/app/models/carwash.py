import uuid
from datetime import datetime, timezone
from ..extensions import db

class CarWash(db.Model):
    __tablename__ = "carwashes"  
    
    # ============================================================
    # Primary Key
    # ============================================================
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))

    # ============================================================
    # Business Information
    # ============================================================
    name = db.Column(
        db.String(100),
        nullable=False
    )

    location = db.Column(
        db.String(150),
        nullable=True
    )

    # Multi-Tenant Routing for separating tenant web traffic
    subdomain = db.Column(
        db.String(100), 
        unique=True, 
        nullable=False, 
        index=True
    )

    # Multi-Tenant Links (Foreign key matches User.id perfectly)
    owner_id = db.Column(
        db.String(36),
        db.ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False
    )

    # Record Metadata
    created_at = db.Column(
        db.DateTime,
        nullable=False,
        default=lambda: datetime.now(timezone.utc)  # Uniform time zoning match
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
    owner = db.relationship(
        "User",
        back_populates="carwashes"
    )

    services = db.relationship(
        "Service",
        back_populates="carwash",
        cascade="all, delete-orphan"
    )

    staff_members = db.relationship(
        "Staff",
        back_populates="carwash",
        cascade="all, delete-orphan"
    )

    bookings = db.relationship(
        "Booking",
        back_populates="carwash",
        cascade="all, delete-orphan"
    )

    # ============================================================
    # Serialization Helper (Required by Business routes!)
    # ============================================================
    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "subdomain": self.subdomain,
            "location": self.location,
            "owner_id": self.owner_id,
            "created_at": self.created_at.isoformat()
        }

    def __repr__(self):
        return f"<CarWash {self.subdomain} (Owner ID: {self.owner_id})>"
