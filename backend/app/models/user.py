import uuid
from datetime import datetime, timezone
from werkzeug.security import generate_password_hash, check_password_hash

from ..extensions import db


class User(db.Model):
    __tablename__ = "users"

    # ============================================================
    # Primary Key
    # ============================================================
    id = db.Column(
        db.String(36),
        primary_key=True,
        default=lambda: str(uuid.uuid4())
    )

    # ============================================================
    # Profile Information
    # ============================================================
    full_name = db.Column(
        db.String(100),
        nullable=False,
        index=True  
    )

    # ============================================================
    # Authentication
    # ============================================================
    email = db.Column(
        db.String(120),
        unique=True,
        nullable=False,
        index=True
    )

    # Prepended with an underscore to denote internal storage
    _password_hash = db.Column(
        "password_hash",  
        db.String(255),
        nullable=False
    )

    # ============================================================
    # Access Control & Status
    # ============================================================
    role = db.Column(
        db.String(20),
        nullable=False,
        default="owner",
        index=True
    )

    is_active = db.Column(
        db.Boolean, 
        default=True, 
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
    carwashes = db.relationship(
        "CarWash",
        back_populates="owner",
        lazy="select"
    )

    staff_profile = db.relationship(
        "Staff",
        back_populates="user",
        uselist=False,
        lazy="select"
    )

    # ============================================================
    # Password Handlers
    # ============================================================
    @property
    def password(self):
        """Prevent plain-text reading of passwords."""
        raise AttributeError("Password is not a readable attribute.")

    @password.setter
    def password(self, password):
        """Automatically intercept plain text and hash it on assignment."""
        self._password_hash = generate_password_hash(password)

    def check_password(self, password):
        """Verify checking incoming password against database hash."""
        return check_password_hash(self._password_hash, password)

    # ============================================================
    # Access Helpers
    # ============================================================
    @property
    def accessible_carwash_ids(self):
        """
        Returns all carwash UUIDs this user can access.
        """
        if not self.is_active:
            return []

        if self.role == "owner":
            return [wash.id for wash in self.carwashes]

        if self.role == "staff" and self.staff_profile:
            return [self.staff_profile.carwash_id]

        return []

    def can_access_carwash(self, carwash_id):
        """
        Central permission check.
        """
        return carwash_id in self.accessible_carwash_ids

    # ============================================================
    # Serialization Helper
    # ============================================================
    def to_dict(self):
        return {
            "id": self.id,
            "full_name": self.full_name,
            "email": self.email,
            "role": self.role,
            "is_active": self.is_active,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat()
        }

 
    def __repr__(self):
        return f"<User {self.email} ({self.role})>"
