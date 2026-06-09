src/
│
├── app/
│   ├── App.jsx
│   ├── routes.jsx
│   └── ProtectedRoute.jsx
│
├── context/
│   ├── AuthContext.jsx
│   └── RoleContext.jsx
│
├── pages/
│   ├── auth/
│   │   ├── Login.jsx
│   │   └── Signup.jsx
│   │
│   ├── customer/
│   │   ├── CustomerDashboard.jsx
│   │   ├── BookWash.jsx
│   │   ├── MyBookings.jsx
│   │   └── MyCars.jsx
│   │
│   ├── admin/
│   │   ├── AdminDashboard.jsx
│   │   ├── Bookings.jsx
│   │   ├── Users.jsx
│   │   ├── Services.jsx
│   │   └── Analytics.jsx
│   │
│   ├── staff/
│   │   ├── StaffDashboard.jsx
│   │   └── AssignedJobs.jsx
│   │
│   └── public/
│       ├── Home.jsx
│       ├── About.jsx
│       └── NotFound.jsx
│
├── components/
│   ├── layout/
│   │   ├── Navbar.jsx
│   │   ├── Sidebar.jsx
│   │   └── Footer.jsx
│   │
│   ├── ui/
│   │   ├── Button.jsx
│   │   ├── Input.jsx
│   │   ├── Card.jsx
│   │   └── Modal.jsx
│   │
│   ├── booking/
│   │   ├── BookingCard.jsx
│   │   └── ServiceSelector.jsx
│   │
│   └── common/
│       ├── Loader.jsx
│       └── Toast.jsx
│
├── hooks/
│   ├── useAuth.js
│   └── useRole.js
│
├── utils/
│   ├── api.js
│   ├── formatDate.js
│   └── constants.js
│
└── assets/
    ├── images/
    └── icons/