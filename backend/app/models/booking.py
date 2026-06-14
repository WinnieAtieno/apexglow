import uuid
from ..extensions import db


class Booking(db.Model):
    __tablename__ = "bookings"

    # Unique Identifier
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))

    # Customer Details
    customer_name = db.Column(db.String(100), nullable=False)
    customer_phone = db.Column(db.String(20), nullable=False)

    # Operational Tracking
    status = db.Column(db.String(20), default="Pending")
    
    # ============================================================
    # THE CRITICAL SAAS ADDITION: Vehicle identification plate
    # ============================================================
    vehicle_plate = db.Column(db.String(50), nullable=False) # Marked False so operators MUST type it

    booking_time = db.Column(db.DateTime, default=db.func.now())

    # Multi-Tenant Foreign Keys
    carwash_id = db.Column(db.String(36), db.ForeignKey("car_washes.id", ondelete="CASCADE"), nullable=False)
    service_id = db.Column(db.String(36), db.ForeignKey("services.id"), nullable=False)
    assigned_staff_id = db.Column(db.String(36), db.ForeignKey("staff.id", ondelete="SET NULL"), nullable=True)

    # Relationships
    carwash = db.relationship("CarWash", back_populates="bookings")
    service = db.relationship("Service", back_populates="bookings")
    assigned_staff = db.relationship("Staff", back_populates="bookings")
