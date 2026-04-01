# 🎓 Maa Saraswati Devi Shiksha Sansthan — School ERP System

<div align="center">

[![Live Demo](https://img.shields.io/badge/🚀_Live_Demo-Online-brightgreen?style=for-the-badge)](https://college-erp-system-l76g.onrender.com)
[![Python](https://img.shields.io/badge/Python-3.14-blue?style=for-the-badge&logo=python)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-6.0-green?style=for-the-badge&logo=django)](https://www.djangoproject.com/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Neon-blue?style=for-the-badge&logo=postgresql)](https://neon.tech/)
[![Render](https://img.shields.io/badge/Deployed_on-Render-purple?style=for-the-badge)](https://render.com/)

**A professional, full-stack Education Resource Planning (ERP) system for Maa Saraswati Devi Shiksha Sansthan, Patauhan, Gola Bazar, Gorakhpur.**

🌐 **Live URL**: [https://college-erp-system-l76g.onrender.com](https://college-erp-system-l76g.onrender.com)

</div>

---

## ✨ Key Features

### 🎨 Premium Glassmorphism UI
- **Modern Aesthetic**: Glassmorphism design with backdrop-blur, gradients, and micro-animations.
- **Dynamic Dashboards**: Role-specific portals with interactive analytics via **Chart.js**.
- **Fully Responsive**: Optimized for Desktop, Tablet, and Mobile.

### 👩‍🏫 Teacher Portal
- **Attendance Management**: Record, update, and manage daily student attendance.
- **Academic Results**: Input exam marks and generate report cards.
- **Classroom Insights**: View student distribution and performance trends visually.

### 🎓 Student Portal
- **Performance Tracking**: View subject-wise results with progress bars.
- **Attendance History**: Check presence percentage and history at any time.
- **Fee Management**: Review payment status, dues, and transaction records.

### 🛡️ Admin Authority
- **System Overview**: High-level metrics (Total Students, Teachers, Classrooms).
- **Control Panel**: Full Django Admin portal for master data management.
- **Admin URL**: [/admin/](https://college-erp-system-l76g.onrender.com/admin/)

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| **Backend** | Python 3.14 / Django 6.x |
| **Frontend** | Bootstrap 5, Vanilla CSS, Font Awesome 6 |
| **Analytics** | Chart.js |
| **Forms** | Django Crispy Forms (Bootstrap 5) |
| **Database** | PostgreSQL (Neon) |
| **Static Files** | WhiteNoise |
| **Deployment** | Render |
| **Version Control** | Git / GitHub |

---

## 🚀 Local Development Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/codershivam18/College_ERP_System.git
   cd College_ERP_System
   ```

2. **Create and activate a virtual environment**:
   ```bash
   python -m venv venv
   venv\Scripts\activate   # Windows
   # source venv/bin/activate  # Mac/Linux
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations and seed data**:
   ```bash
   python manage.py migrate
   python seed_data.py
   ```

5. **Start the development server**:
   ```bash
   python manage.py runserver
   ```

6. **Access the app** at `http://127.0.0.1:8000/` with:
   - **Username**: `admin`
   - **Password**: `admin123`

---

## ☁️ Deployment (Render + Neon PostgreSQL)

This project is deployed on **Render** with a **Neon PostgreSQL** database.

### Environment Variables Required:
| Variable | Description |
|----------|-------------|
| `SECRET_KEY` | Django secret key |
| `DEBUG` | Set to `False` in production |
| `DATABASE_URL` | PostgreSQL connection string from Neon |
| `RENDER_EXTERNAL_HOSTNAME` | Your Render app's hostname |

### Build Command:
```bash
./render-build.sh
```

### Start Command:
```bash
gunicorn school_erp.wsgi
```

---

## 🔐 Security
- Custom User Model with role-based access control (Admin / Teacher / Student).
- Environment variables for all sensitive settings.
- CSRF protection enabled.
- WhiteNoise for secure static file serving.

---

<div align="center">

Developed with ❤️ for **Maa Saraswati Devi Shiksha Sansthan**

🌐 [Live Demo](https://college-erp-system-l76g.onrender.com) | 💻 [GitHub](https://github.com/codershivam18/College_ERP_System)

</div>
