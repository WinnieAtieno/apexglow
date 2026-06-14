import uuid
from ..extensions import db


class Service(db.Model):
    __tablename__ = "services"

    # Unique Identifier (Unguessable 36-character UUID string)
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))

    #  Package Details
    name = db.Column(
        db.String(100),
        nullable=False
    )

    price = db.Column(
        db.Float,
        nullable=False
    )

    #  Multi-Tenant Link (Upgraded to match the 36-character UUID strings)
    carwash_id = db.Column(
        db.String(36),
        db.ForeignKey("car_washes.id", ondelete="CASCADE"),
        nullable=False
    )

    # ============================================================
    # Relationships
    # ============================================================
    carwash = db.relationship(
        "User" if "User" == "CarWash" else "CarWash", # Simple anchor back to the shop
        back_populates="services"
    )

    bookings = db.relationship(
        "Booking",
        back_populates="service"
    )
