import uuid
from ..extensions import db


class Staff(db.Model):
    __tablename__ = "staff"

    # Unique Identifier (36-character UUID string)
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))

    #  Employment details (e.g., 'washer', 'cashier', 'manager')
    position = db.Column(
        db.String(50)
    )

    # 3. Multi-Tenant Bridge Keys (Upgraded to match the 36-character UUID strings)
    user_id = db.Column(
        db.String(36),
        db.ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False,
        unique=True # Ensures one User can only have ONE active employee profile
    )

    carwash_id = db.Column(
        db.String(36),
        db.ForeignKey("car_washes.id", ondelete="CASCADE"),
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

    bookings = db.relationship(
        "Booking",
        back_populates="assigned_staff"
    )
