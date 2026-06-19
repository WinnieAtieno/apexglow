import uuid
from ..extensions import db


class Staff(db.Model):
    __tablename__ = "staff"

    # ============================================================
    # Primary Key
    # ============================================================
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))

    # ============================================================
    # Core Attributes
    # ============================================================
    # Employment details (e.g., 'washer', 'cashier', 'manager')
    position = db.Column(
        db.String(50),
        nullable=False,
        default="washer"
    )

    # ============================================================
    # Multi-Tenant Bridge Foreign Keys
    # ============================================================
    user_id = db.Column(
        db.String(36),
        db.ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False,
        unique=True # Tight constraint: One authentication User can have exactly ONE staff tracking profile
    )

    carwash_id = db.Column(
        db.String(36),
        db.ForeignKey("carwashes.id", ondelete="CASCADE"), # Fixed: Dropped underscore to point to carwashes
        nullable=False
    )

    # ============================================================
    # Relationships
    # ============================================================
    user = db.relationship(
        "User",
        back_populates="staff_profile"
    )

    carwash = db.relationship(
        "CarWash",
        back_populates="staff_members"
    )

    def __repr__(self):
        return f"<Staff ID: {self.id} Position: {self.position} at Shop: {self.carwash_id}>"
