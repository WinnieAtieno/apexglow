import enum  # Added for strict state boundary management
import uuid
from datetime import datetime, timezone
from ..extensions import db


class BookingStatus(str, enum.Enum):
    """
    Defines the structural boundaries for vehicle tracking.
    Inheriting from 'str' ensures seamless JSON serialization.
    """
    PENDING = "Pending"
    IN_PROGRESS = "In Progress"
    COMPLETED = "Completed"
    CANCELLED = "Cancelled"


class Booking(db.Model):
    __tablename__ = "bookings"

    # ============================================================
    # Primary Key
    # ============================================================
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))

    # ============================================================
    # Customer Details
    # ============================================================
    customer_name = db.Column(db.String(100), nullable=False)
    customer_phone = db.Column(db.String(20), nullable=False)

    # ============================================================
    # Operational Tracking
    # ============================================================
    # Swapped from a plain String to a native DB Enum for performance and integrity
    status = db.Column(
        db.Enum(BookingStatus),
        nullable=False,
        default=BookingStatus.PENDING,
        index=True
    )
    
    # Vehicle identification plate
    vehicle_plate = db.Column(db.String(50), nullable=False, index=True) 

    booking_time = db.Column(
        db.DateTime, 
        nullable=False,
        default=lambda: datetime.now(timezone.utc)  # Uniform timezone strategy match
    )

    # ============================================================
    # Multi-Tenant Foreign Keys
    # ============================================================
    carwash_id = db.Column(
        db.String(36), 
        db.ForeignKey("carwashes.id", ondelete="CASCADE"), 
        nullable=False
    )
    
    service_id = db.Column(
        db.String(36), 
        db.ForeignKey("services.id", ondelete="RESTRICT"), 
        nullable=False
    )
    
    assigned_staff_id = db.Column(
        db.String(36), 
        db.ForeignKey("staff.id", ondelete="SET NULL"), 
        nullable=True
    )

    # ============================================================
    # Relationships
    # ============================================================
    carwash = db.relationship("CarWash", back_populates="bookings")
    service = db.relationship("Service")
    assigned_staff = db.relationship("Staff")

    def __repr__(self):
       
        return f"<Booking {self.vehicle_plate} [{self.status.value}] at Shop {self.carwash_id}>"
