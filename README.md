# 📊 TradeVault – Asset Management System API

A scalable Asset Management REST API built with **Django REST Framework (DRF)** that enables secure user authentication, role-based access control, and user-specific asset management using **JWT authentication**.

---

## ✨ Features

### 🔐 **Authentication**
- **JWT-based Authentication** using `djangorestframework-simplejwt`
- User Registration and Login
- Secure token-based API access
- Password hashing using Django’s built-in authentication system

### 👥 **Role-Based Access Control (RBAC)**
- Two roles:
  - `USER`
  - `ADMIN`
- Role-based permission handling
- Users can only access their own assets
- Admin can manage users and assets via Django Admin panel

### 📦 **Asset Management**
- ✅ **Create Assets** (Crypto / Stock)
- 👁️ **View Assets** (User-specific data isolation)
- ✏️ **Update Asset Details**
- ❌ **Delete Assets**
- 📅 Automatic timestamp tracking

### 🛡️ **Security & Validation**
- JWT-secured endpoints
- Field-level validation:
  - Quantity must be greater than 0
  - Purchase price must be positive
  - Unique email validation
- CORS configuration enabled
- Clean and scalable project structure

---

## 🛠 Tech Stack

![Django](https://img.shields.io/badge/DJANGO-092E20?style=for-the-badge&logo=django&logoColor=white)
![Django REST](https://img.shields.io/badge/DJANGO%20REST-FF0000?style=for-the-badge&logo=django&logoColor=white)
![JWT](https://img.shields.io/badge/JWT-000000?style=for-the-badge&logo=jwt&logoColor=white)

---

## 🧰 Tools Used

![Swagger](https://img.shields.io/badge/SWAGGER-85EA2D?style=for-the-badge&logo=swagger&logoColor=black)
![Postman](https://img.shields.io/badge/POSTMAN-FF6C37?style=for-the-badge&logo=postman&logoColor=white)
![VS Code](https://img.shields.io/badge/VISUAL%20STUDIO%20CODE-0078d7?style=for-the-badge&logo=visual-studio-code&logoColor=white)

---
## 📁 Project Structure
```
tradevault/
│
├── users/                      # Authentication & role management
│   ├── migrations/             # Database migration files
│   ├── admin.py                # Django admin configuration
│   ├── models.py               # Custom User model
│   ├── permissions.py          # Role-based permission classes
│   ├── serializers.py          # User serializers & validation
│   ├── urls.py                 # Authentication routes
│   └── views.py                # Register & auth views
│
├── assets/                     # Asset management module
│   ├── migrations/             # Asset model migrations
│   ├── admin.py                # Admin configuration for assets
│   ├── models.py               # Asset model definition
│   ├── serializers.py          # Asset validation logic
│   ├── urls.py                 # Asset routes
│   └── views.py                # Asset CRUD APIs
│
├── vault/                      # Project configuration
│   ├── settings.py             # Global settings
│   ├── urls.py                 # Root URL configuration
│   ├── asgi.py
│   └── wsgi.py
│
└── manage.py                   # Django management entry point
```
# 🚀 Setup and Installation Instructions

## 🔹 Prerequisites
- Python 3.8+
- pip
- Git

---

## 1️⃣ Clone the Repository

```bash
git clone https://github.com/yourusername/tradevault-api.git
cd tradevault-api
```

---

## 2️⃣ Create Virtual Environment

```bash
python -m venv env
```

Activate environment:

**Windows:**
```bash
env\Scripts\activate
```

**Mac/Linux:**
```bash
source env/bin/activate
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4️⃣ Database Setup

```bash
python manage.py makemigrations
python manage.py migrate
```

---

## 5️⃣ Create Superuser (Admin)

```bash
python manage.py createsuperuser
```

---

## 6️⃣ Run Development Server

```bash
python manage.py runserver
```

API will be available at:

```
http://127.0.0.1:8000/
```

---

# 📖 API Documentation

## 📘 Swagger UI

Visit:

```
http://127.0.0.1:8000/swagger/
```

---

## 🌐 Base URL

```
http://127.0.0.1:8000/api/v1/
```

---

# 🔑 Authentication Endpoints

## 📝 User Registration

```http
POST /api/v1/auth/register/
Content-Type: application/json

{
    "username": "anurag",
    "email": "anurag@email.com",
    "password": "Password@123"
}
```

**Response:**

```json
{
    "message": "User registered successfully"
}
```

---

## 🔓 User Login

```http
POST /api/v1/auth/login/
Content-Type: application/json

{
    "username": "anurag",
    "password": "Password@123"
}
```

**Response:**

```json
{
    "access": "<access_token>",
    "refresh": "<refresh_token>"
}
```

---

## 🔄 Refresh Token

```http
POST /api/v1/auth/refresh/

{
    "refresh": "<refresh_token>"
}
```

---

# 📦 Asset Management Endpoints (JWT Required)

Authorization Header:

```
Authorization: Bearer <access_token>
```

---

## ➕ Create Asset

```http
POST /api/v1/assets/

{
    "asset_name": "Bitcoin",
    "asset_type": "CRYPTO",
    "quantity": 2,
    "purchase_price": 30000
}
```

---

## 📄 Get All Assets

```http
GET /api/v1/assets/
```

---

## 📄 Get Single Asset

```http
GET /api/v1/assets/<id>/
```

---

## ✏️ Update Asset

```http
PUT /api/v1/assets/<id>/
```

---

## ❌ Delete Asset

```http
DELETE /api/v1/assets/<id>/
```

---

# 👑 Admin Panel

Django Admin available at:

```
http://127.0.0.1:8000/admin/
```

Admin capabilities:
- View all users
- Modify roles
- Suspend users
- Manage all assets

---

# 📊 HTTP Status Codes

- `200 OK` – Request successful
- `201 Created` – Resource created
- `400 Bad Request` – Validation error
- `401 Unauthorized` – Authentication required
- `403 Forbidden` – Role restriction
- `404 Not Found` – Resource not found
- `500 Internal Server Error` – Server error

---

# ⚡ Scalability Considerations

- SQLite can be replaced with PostgreSQL in production
- Redis can be added for caching heavy queries
- Celery for asynchronous tasks
- Docker + Gunicorn + NGINX for deployment
- Horizontal scaling with load balancers
- Modular structure supports microservice expansion

---


⭐ **Star this repository if you found it helpful!**
