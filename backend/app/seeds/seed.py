from app import create_app
from datetime import datetime, timedelta, timezone

from app.extensions import db
from app.models.user import User
from app.models.carwash import CarWash
from app.models.staff import Staff
from app.models.service import Service
from app.models.booking import Booking, BookingStatus  

app = create_app()


def seed_database():
    print("Starting database seeding...")

    # ============================================================
    # CLEAR DATA (Modern SQLAlchemy 2.0 Child → Parent Order)
    # ============================================================
    db.session.execute(db.delete(Booking))
    db.session.execute(db.delete(Staff))
    db.session.execute(db.delete(Service))
    db.session.execute(db.delete(CarWash))
    db.session.execute(db.delete(User))
    db.session.commit()

    # ============================================================
    # OWNERS
    # ============================================================
    owner1 = User(
        full_name="Owner One",
        email="owner@test.com",
        role="owner"
    )
    owner1.password = "password123"

    owner2 = User(
        full_name="Owner Two",
        email="owner2@test.com",
        role="owner"
    )
    owner2.password = "password234"

    owner3 = User(
        full_name="Owner Three",
        email="owner3@test.com",
        role="owner"
    )
    owner3.password = "password456"

    db.session.add_all([owner1, owner2, owner3])
    db.session.flush()

    # ============================================================
    # CARWASHES
    # ============================================================
    carwash1 = CarWash(
        name="ApexGlow Central",
        location="CBD, Nairobi",
        subdomain="central",
        owner_id=owner1.id
    )

    carwash2 = CarWash(
        name="ApexGlow Westlands",
        location="Westlands, Nairobi",
        subdomain="westlands",
        owner_id=owner2.id
    )

    carwash3 = CarWash(
        name="ApexGlow Karen",
        location="Karen, Nairobi",
        subdomain="karen",
        owner_id=owner3.id
    )

    db.session.add_all([carwash1, carwash2, carwash3])
    db.session.flush()

    # ============================================================
    # SERVICES
    # ============================================================
    services = [
        Service(name="Basic Wash", price=500.0, carwash_id=carwash1.id),
        Service(name="Premium Wash", price=1000.0, carwash_id=carwash1.id),
        Service(name="Full Detailing", price=2500.0, carwash_id=carwash1.id),

        Service(name="Basic Wash", price=500.0, carwash_id=carwash2.id),
        Service(name="Premium Wash", price=1000.0, carwash_id=carwash2.id),
        Service(name="Full Detailing", price=2500.0, carwash_id=carwash2.id),

        Service(name="Basic Wash", price=500.0, carwash_id=carwash3.id),
        Service(name="Premium Wash", price=1000.0, carwash_id=carwash3.id),
        Service(name="Full Detailing", price=2500.0, carwash_id=carwash3.id),
    ]

    db.session.add_all(services)
    db.session.flush()

    # ============================================================
    # STAFF USERS
    # ============================================================
    staff_user1 = User(
        full_name="Staff One",
        email="staff@test.com",
        role="staff"
    )
    staff_user1.password = "password123"

    manager_user = User(
        full_name="Manager One",
        email="manager@test.com",
        role="staff"
    )
    manager_user.password = "password123"

    staff_user2 = User(
        full_name="Staff Two",
        email="staff2@test.com",
        role="staff"
    )
    staff_user2.password = "password123"

    staff_user3 = User(
        full_name="Staff Three",
        email="staff3@test.com",
        role="staff"
    )
    staff_user3.password = "password123"

    db.session.add_all([staff_user1, manager_user, staff_user2, staff_user3])
    db.session.flush()

    # ============================================================
    # STAFF PROFILES
    # ============================================================
    p_manager = Staff(position="manager", user_id=manager_user.id, carwash_id=carwash1.id)
    p_washer1 = Staff(position="washer", user_id=staff_user1.id, carwash_id=carwash1.id)
    p_washer2 = Staff(position="washer", user_id=staff_user2.id, carwash_id=carwash2.id)
    p_washer3 = Staff(position="washer", user_id=staff_user3.id, carwash_id=carwash3.id)

    db.session.add_all([p_manager, p_washer1, p_washer2, p_washer3])
    db.session.flush()

    # ============================================================
    # BOOKINGS
    # ============================================================
    # Now using modern timezone elements, strict model keys, and native Enum objects
    bookings = [
        Booking(
            customer_name="John Kamau",
            customer_phone="0712345671",
            vehicle_plate="KAA 123A",
            booking_time=datetime.now(timezone.utc) + timedelta(hours=2),
            status=BookingStatus.PENDING,
            carwash_id=carwash1.id,
            service_id=services[0].id,
            assigned_staff_id=p_washer1.id 
        ),
        Booking(
            customer_name="Jane Wanjiku",
            customer_phone="0712345672",
            vehicle_plate="KBB 456B",
            booking_time=datetime.now(timezone.utc) + timedelta(hours=4),
            status=BookingStatus.PENDING, 
            carwash_id=carwash1.id,
            service_id=services[1].id,
            assigned_staff_id=p_washer1.id
        ),
        Booking(
            customer_name="Peter Mwangi",
            customer_phone="0712345673",
            vehicle_plate="KCC 789C",
            booking_time=datetime.now(timezone.utc) + timedelta(hours=6),
            status=BookingStatus.IN_PROGRESS, 
            carwash_id=carwash1.id,
            service_id=services[2].id,
            assigned_staff_id=p_washer1.id
        ),
    ]

    db.session.add_all(bookings)

    # ============================================================
    # COMMIT
    # ============================================================
    db.session.commit()

    print("Database seeded successfully!")
    print("- 3 Owners")
    print("- 3 Carwashes (Nairobi Regions)")
    print("- 9 Tier Menu Services")
    print("- 4 Staff authentication users")
    print("- 4 Staff operational tracking profiles")
    print("- 3 Active Enum Validated Vehicle Bookings")


if __name__ == "__main__":
    with app.app_context():
        seed_database()
