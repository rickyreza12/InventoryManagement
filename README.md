# 🧺 InventoryManagement

Multi-outlet inventory management system for laundry and drycleaning businesses.  
Supports secure login, role-based access, outlet-specific inventory control, real-time stock monitoring, and a responsive UI.

---

## ✨ Features

- 🏢 Multi-outlet (branch-based) support
- 👥 Role-based access (Admin / Staff)
- 🔐 JWT-secured authentication
- 📦 Inventory CRUD operations per outlet
- 📊 Dashboard with low-stock alerts
- ✅ Unit-tested backend (pytest)
- 📱 Responsive frontend (React + Vite)

---

## 🛠 Tech Stack

| Layer      | Stack                               |
|------------|-------------------------------------|
| Frontend   | React.js (Vite, Axios, TailwindCSS) |
| Backend    | FastAPI (Python)                    |
| Database   | PostgreSQL (SQLite for dev)         |
| Auth       | JWT Bearer Tokens                   |
| Testing    | Pytest                              |
| Deployment | Docker, GitHub Actions (optional)   |

---

## 🧱 Project Structure

### 📂 Backend (FastAPI)

```
backend/
├── main.py                 # FastAPI app initialization
├── models/                # ORM models
│   ├── user.py
│   ├── item.py
│   └── outlet.py
├── schemas/               # Pydantic request/response models
│   ├── user_schema.py
│   ├── item_schema.py
│   └── outlet_schema.py
├── routers/               # API route definitions
│   ├── auth.py
│   ├── users.py
│   ├── items.py
│   └── outlets.py
├── utils/                 # Utility modules
│   └── auth_handler.py
├── database.py            # DB connection
├── config.py              # Settings (env)
└── tests/                 # Pytest unit tests
    ├── test_auth.py
    ├── test_users.py
    ├── test_items.py
    └── test_outlets.py
```

---

### 📂 Frontend (React.js + Vite)

```
frontend/
├── src/
│   ├── components/
│   │   ├── InventoryTable.jsx
│   │   ├── AddItemForm.jsx
│   │   ├── EditItemForm.jsx
│   │   ├── LoginForm.jsx
│   │   └── UserManagement.jsx
│   ├── pages/
│   │   ├── DashboardPage.jsx
│   │   ├── InventoryPage.jsx
│   │   ├── AddItemPage.jsx
│   │   ├── EditItemPage.jsx
│   │   ├── LoginPage.jsx
│   │   └── UserManagementPage.jsx
│   ├── services/
│   │   ├── authService.js
│   │   └── inventoryService.js
│   ├── utils/
│   │   └── axiosInstance.js
│   ├── App.jsx
│   ├── main.jsx
│   └── router.jsx
├── tailwind.config.js
├── package.json
└── vite.config.js
```

---

## 🔐 API Overview

### Authentication
| Method | Endpoint         | Description              | Access      |
|--------|------------------|--------------------------|-------------|
| POST   | `/auth/login`    | Login and get JWT token  | Public      |
| POST   | `/auth/register` | Create user (Admin only) | Admin       |

### Users
| Method | Endpoint | Description         | Access |
|--------|----------|---------------------|--------|
| GET    | `/users` | List all users      | Admin  |

### Outlets
| Method | Endpoint          | Description               | Access |
|--------|-------------------|---------------------------|--------|
| GET    | `/outlets`        | List all outlets          | Admin  |
| POST   | `/outlets`        | Create new outlet         | Admin  |
| PUT    | `/outlets/{id}`   | Update outlet             | Admin  |
| DELETE | `/outlets/{id}`   | Delete outlet             | Admin  |

### Inventory Items
| Method | Endpoint          | Description                       | Access        |
|--------|-------------------|-----------------------------------|---------------|
| GET    | `/items`          | List items (per outlet)           | Admin/Staff   |
| POST   | `/items`          | Create inventory item             | Admin         |
| PUT    | `/items/{id}`     | Update inventory item             | Admin/Staff   |
| DELETE | `/items/{id}`     | Delete inventory item             | Admin         |

---

## 🧪 Unit Testing

Run backend tests:
```bash
cd backend
pytest
```

---

## 🚀 Getting Started

### Backend (FastAPI)
```bash
cd backend
python -m venv env
source env/bin/activate  # or .\env\Scripts\activate on Windows
pip install -r requirements.txt
uvicorn main:app --reload
```

### Frontend (React + Vite)
```bash
cd frontend
npm install
npm run dev
```

---

## 🔧 Deployment

- Docker setup planned (`docker-compose.yml`)
- CI/CD with GitHub Actions (optional)

---

## 📃 License

This project is for learning, portfolio, and freelance project demonstration.  
© 2025 Muhammad Ricky Reza

---

## 🙌 Contributions

PRs, forks, and feedback are welcome for future improvements or forks.

