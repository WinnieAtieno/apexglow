from app import create_app
from werkzeug.security import generate_password_hash
from datetime import datetime, timedelta

from app.extensions import db
from app.models.user import User
from app.models.carwash import CarWash
from app.models.staff import Staff
from app.models.service import Service
from app.models.booking import Booking

app = create_app()


def seed_database():
    print("Starting database seeding...")

    # =========================
    # CLEAR DATA
    # =========================
    Booking.query.delete()
    Staff.query.delete()
    Service.query.delete()
    CarWash.query.delete()
    User.query.delete()

    db.session.commit()

    # =========================
    # OWNER
    # =========================
    owner1 = User(
        email="owner@test.com",
        password_hash=generate_password_hash("password123"),
        role="owner"
    )

    db.session.add(owner1)
    db.session.flush()
    

    owner2 = User(
        email="owner2@test.com",
        password_hash=generate_password_hash("password234"),
        role="owner"
    )


    db.session.add(owner2)
    db.session.flush()

    owner3 = User(
        email="owner3@test.com",
        password_hash=generate_password_hash("password456"),
        role="owner"
    )
    db.session.add(owner3)
    db.session.flush()

    # =========================
    # CARWASHES
    # =========================
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

    # =========================
    # SERVICES 
    # =========================

    # CARWASH 1
    s1 = Service(name="Basic Wash", price=500, carwash_id=carwash1.id)
    s2 = Service(name="Premium Wash", price=1000, carwash_id=carwash1.id)
    s3 = Service(name="Full Detailing", price=2500, carwash_id=carwash1.id)

    # CARWASH 2
    s4 = Service(name="Basic Wash", price=500, carwash_id=carwash2.id)
    s5 = Service(name="Premium Wash", price=1000, carwash_id=carwash2.id)
    s6 = Service(name="Full Detailing", price=2500, carwash_id=carwash2.id)

    # CARWASH 3
    s7 = Service(name="Basic Wash", price=500, carwash_id=carwash3.id)
    s8 = Service(name="Premium Wash", price=1000, carwash_id=carwash3.id)
    s9 = Service(name="Full Detailing", price=2500, carwash_id=carwash3.id)

    db.session.add_all([s1, s2, s3, s4, s5, s6, s7, s8, s9])
    db.session.flush()

    # =========================
    # STAFF USER
    # =========================
    staff1 = User(
        email="staff@test.com",
        password_hash=generate_password_hash("password123"),
        role="staff"
    )

    db.session.add(staff1)
    db.session.flush()

    manager = User(
        email="manager@test.com",
        password_hash=generate_password_hash("password123"),
        role="staff"
    )

    db.session.add(manager)
    db.session.flush()

    staff2 = User(
        email="staff2@test.com",
        password_hash=generate_password_hash("password123"),
        role="staff"
    )
    db.session.add(staff2)
    db.session.flush()

    staff3 = User(
        email="staff3@test.com",
        password_hash=generate_password_hash("password123"),
        role="staff"
    )
    db.session.add(staff3)
    db.session.flush()

    # =========================
    # STAFF PROFILE
    # =========================
    manager_profile = Staff(
        position="manager",
        user_id=manager.id,
        carwash_id=carwash1.id
    )
    db.session.add(manager_profile)
    db.session.flush()

    staff_profile1 = Staff(
        position="Washer",
        user_id=staff1.id,
        carwash_id=carwash1.id
    )
    db.session.add(staff_profile1)
    db.session.flush()

    staff_profile2 = Staff(
        position="Washer",
        user_id=staff2.id,
        carwash_id=carwash2.id
    )
    db.session.add(staff_profile2)
    db.session.flush()

    staff_profile3 = Staff(
        position="Washer",
        user_id=staff3.id,
        carwash_id=carwash3.id
    )
    db.session.add(staff_profile3)
    db.session.flush()

    # =========================
    # BOOKINGS 
    # =========================

    # CARWASH 1 BOOKINGS
    b1 = Booking(
    customer_name="John Kamau",
    customer_phone="0712345671",
    vehicle_plate="KAA 123A",
    booking_time=datetime.utcnow() + timedelta(days=1),
    status="pending",
    carwash_id=carwash1.id,
    service_id=s1.id,
    assigned_staff_id=staff1.id
)

    b2 = Booking(
        customer_name="Jane Wanjiku",
        customer_phone="0712345672",
        vehicle_plate="KBB 456B",
        booking_time=datetime.utcnow() + timedelta(days=2),
        status="confirmed",
        carwash_id=carwash1.id,
        service_id=s2.id,
        assigned_staff_id=staff2.id
    )

    b3 = Booking(
        customer_name="Peter Mwangi",
        customer_phone="0712345673",
        vehicle_plate="KCC 789C",
        booking_time=datetime.utcnow() + timedelta(days=3),
        status="in_progress",
        carwash_id=carwash1.id,
        service_id=s3.id,
        assigned_staff_id=staff3.id
    )

    b4 = Booking(
        customer_name="Amina Hassan",
        customer_phone="0712345674",
        vehicle_plate="KDD 321D",
        booking_time=datetime.utcnow() + timedelta(days=4),
        status="completed",
        carwash_id=carwash1.id,
        service_id=s1.id,
        assigned_staff_id=staff1.id
    )

    b5 = Booking(
        customer_name="James Otieno",
        customer_phone="0712345675",
        vehicle_plate="KEE 654E",
        booking_time=datetime.utcnow() + timedelta(days=5),
        status="cancelled",
        carwash_id=carwash1.id,
        service_id=s2.id,
        assigned_staff_id=staff3.id
    )

    # CARWASH 2 BOOKINGS
    b6 = Booking(
        customer_name="Mary Onyonka",
        customer_phone="0722345671",
        vehicle_plate="KFF 111F",
        booking_time=datetime.utcnow() + timedelta(days=1),
        status="pending",
        carwash_id=carwash2.id,
        service_id=s4.id,
        assigned_staff_id=staff1.id
    )

    b7 = Booking(
        customer_name="Brian Otieno",
        customer_phone="0722345672",
        vehicle_plate="KGG 222G",
        booking_time=datetime.utcnow() + timedelta(days=2),
        status="confirmed",
        carwash_id=carwash2.id,
        service_id=s5.id,
        assigned_staff_id=staff3.id
    )

    b8 = Booking(
        customer_name="Grace Nafula",
        customer_phone="0722345673",
        vehicle_plate="KHH 333H",
        booking_time=datetime.utcnow() + timedelta(days=3),
        status="in_progress",
        carwash_id=carwash2.id,
        service_id=s6.id,
        assigned_staff_id=staff2.id
    )

    b9 = Booking(
        customer_name="David Mbugua",
        customer_phone="0722345674",
        vehicle_plate="KJJ 444J",
        booking_time=datetime.utcnow() + timedelta(days=4),
        status="completed",
        carwash_id=carwash2.id,
        service_id=s4.id,
        assigned_staff_id=staff1.id
    )

    b10 = Booking(
        customer_name="Pauline Atieno",
        customer_phone="0722345675",
        vehicle_plate="KLL 555L",
        booking_time=datetime.utcnow() + timedelta(days=5),
        status="cancelled",
        carwash_id=carwash2.id,
        service_id=s5.id,
        assigned_staff_id=staff2.id
    )

    # CARWASH 3 BOOKINGS
    b11 = Booking(
        customer_name="Alex Karanja",
        customer_phone="0732345671",
        vehicle_plate="KMM 666M",
        booking_time=datetime.utcnow() + timedelta(days=1),
        status="pending",
        carwash_id=carwash3.id,
        service_id=s7.id,
        assigned_staff_id=staff3.id
    )

    b12 = Booking(
        customer_name="Susan Awino",
        customer_phone="0732345672",
        vehicle_plate="KNN 777N",
        booking_time=datetime.utcnow() + timedelta(days=2),
        status="confirmed",
        carwash_id=carwash3.id,
        service_id=s8.id,
        assigned_staff_id=staff2.id
    )

    b13 = Booking(
        customer_name="George Okello",
        customer_phone="0732345673",
        vehicle_plate="KOO 888O",
        booking_time=datetime.utcnow() + timedelta(days=3),
        status="in_progress",
        carwash_id=carwash3.id,
        service_id=s9.id,
        assigned_staff_id=staff1.id
    )

    b14 = Booking(
        customer_name="Nancy Ana",
        customer_phone="0732345674",
        vehicle_plate="KPP 999P",
        booking_time=datetime.utcnow() + timedelta(days=4),
        status="completed",
        carwash_id=carwash3.id,
        service_id=s7.id,
        assigned_staff_id=staff3.id
    )

    b15 = Booking(
        customer_name="Chris Tucker",
        customer_phone="0732345675",
        vehicle_plate="KQQ 000Q",
        booking_time=datetime.utcnow() + timedelta(days=5),
        status="cancelled",
        carwash_id=carwash3.id,
        service_id=s8.id,
        assigned_staff_id=staff2.id
    )

    db.session.add_all([
        b1, b2, b3, b4, b5,
        b6, b7, b8, b9, b10,
        b11, b12, b13, b14, b15
    ])

    # =========================
    # COMMIT
    # =========================
    db.session.commit()

    print("Database seeded successfully!")
    print("- 3 Owners")
    print("- 3 Carwashes")
    print("- 9 Services")
    print("- 3 Staff")
    print("- 1 Manager")
    print("- 15 Bookings")


if __name__ == "__main__":
    with app.app_context():
        seed_database()