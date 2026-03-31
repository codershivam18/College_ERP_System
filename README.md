# Maa Saraswati Devi Shiksha Sansthan - School ERP

A professional, state-of-the-art Education Resource Planning (ERP) system designed for **Maa Saraswati Devi Shiksha Sansthan**, located in Patauhan, Gola Bazar, Gorakhpur. Built with Python/Django, this system provides a seamless digital experience for administrators, teachers, and students.

## 🌟 Key Features

### 💎 Premium Interface
- **Glassmorphism UI**: High-end aesthetic with backdrop-blur and vibrant gradients.
- **Dynamic Dashboards**: Role-specific portals with interactive analytics via **Chart.js**.
- **Responsive Design**: Fully optimized for Desktop, Tablet, and Mobile devices.

### 🍎 Teacher Portal
- **Attendance Management**: Record, update, and manage daily presence.
- **Academic Results**: Seamlessly input exam marks and generate report cards.
- **Classroom Insights**: View student distribution and performance trends visually.

### 🎓 Student Portal
- **Performance Tracking**: View subject-wise results with progress bars.
- **Attendance History**: Check presence percentage and history at any time.
- **Fee Management**: Review payment status, dues, and transaction records.

### 🛠️ Admin Authority
- **System Overview**: High-level metrics (Total Students, Teachers, Classrooms).
- **Control Panel**: Direct access to the robust Django Admin portal for master data management.

## 🚀 Tech Stack
- **Backend**: Python 3.12+ / Django 5.x
- **Frontend**: Vanilla CSS / Bootstrap 5 / Font Awesome 6
- **Analytics**: Chart.js
- **Forms**: Django Crispy Forms (Bootstrap 5)
- **Database**: SQLite (Development) / PostgreSQL (Ready)

## 🔧 Installation & Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/school-erp.git
   cd school-erp
   ```

2. **Create and activate a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
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

## 🔐 Security
The system uses a **Custom User Model** with role-based access controls to ensure data privacy and integrity across all levels.

---
Developed with ❤️ for Maa Saraswati Devi Shiksha Sansthan.
