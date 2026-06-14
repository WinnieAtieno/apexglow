import uuid
from datetime import datetime
from ..extensions import db

class User(db.Model):
    __tablename__ = "users"

    
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))

    # Authentication & Profile Details
    email = db.Column(db.String(120), unique=True, nullable=False, index=True)
    password_hash = db.Column(db.String(255), nullable=False)

    #  System Access Control Roles ('owner', 'staff')
    role = db.Column(
        db.String(20),
        nullable=False,
        default="owner"
    )

    # 4. Record Metadata
    created_at = db.Column(
        db.DateTime,
        default=db.func.now()
    )

    # ============================================================
    # Relationships
    # ============================================================
    # Links an owner to the multiple car wash locations they run
    carwashes = db.relationship(
        "CarWash",
        back_populates="owner"
    )

    # Links an employee to their underlying work station record
    staff_profile = db.relationship(
        "Staff",
        back_populates="user",
        uselist=False
    )

    # ============================================================
    # Dynamic Multi-Tenant Context Helper
    # ============================================================
    @property
    def accessible_carwash_ids(self):
        """
        Dynamically extracts a list of string UUIDs this specific user can view.
        Protects your SaaS data routes from multi-tenant leaks.
        """
        if self.role == "owner":
            return [wash.id for wash in self.carwashes]
        
        if self.role == "staff" and self.staff_profile:
            return [self.staff_profile.carwash_id]
        
        return []
