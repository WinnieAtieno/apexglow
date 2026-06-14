import uuid
from datetime import datetime
from ..extensions import db

class CarWash(db.Model):
    __tablename__ = "car_washes"

    
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))

    #  Business Information
    name = db.Column(
        db.String(100),
        nullable=False
    )

    location = db.Column(
        db.String(150)
    )

    #  SaaS Multi-Tenant Routing (Essential for separating tenant web traffic)
    subdomain = db.Column(
        db.String(100), 
        unique=True, 
        nullable=False, 
        index=True
    )

    #  Multi-Tenant Links (Foreign key type updated to String(36) to match User.id)
    owner_id = db.Column(
        db.String(36),
        db.ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False
    )

    # Record Metadata
    created_at = db.Column(
        db.DateTime,
        default=db.func.now()
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
