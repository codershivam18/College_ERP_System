
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
=======
I have built this School ERP System using a modern, professional technology stack and a custom-designed academic architecture. Here is a comprehensive list of everything used in this project:

⚙️ Core Backend (The Brain)
Python 3: The primary programming language.
Django 5.x+: The high-level web framework used for secure and scalable backend logic.
SQLite: A reliable, file-based database for development.
Custom User Model: A specialized authentication system that supports multiple roles (Admin, Teacher, Student) in a single database.
🎨 Frontend & Design (The Interface)
Glassmorphism UI: High-end styling using modern CSS with backdrop-blur, gradients, and transparency.
Bootstrap 5: Used for the layout grid, responsive design, and professional UI components (like badges and buttons).
Vanilla CSS Variables: Powering the project's theme and consistent colors across all pages.
Font Awesome 6: Used for a professional icon set throughout the dashboards.
HTML5 & Semantic Tags: For structure, accessibility, and SEO.
📊 Advanced Interactive Features
Chart.js: A powerful JavaScript library used to create:
Student Dashboard: Attendance percentage Doughnut chart.
Teacher Dashboard: Classroom distribution Bar chart.
Admin Dashboard: Overall School metrics (Students vs Teachers vs Classrooms).
Dynamic Role-Switching (JavaScript): The registration page automatically updates its fields when you switch between "Student" and "Teacher" roles.
🏛️ System Architecture (The Logic)
Linked Profiles: Automatic creation of StudentProfile and TeacherProfile upon registration.
Modular Features: Specialized modules for:
Attendance Management (Mark, delete, and history).
Academic Result Tracking (Input marks, view pass/fail report cards).
Fee Management (Tracking billing and payment status).
Django Crispy Forms: For perfectly styled, Bootstrap-ready forms.
🛠️ DevOps & Industry Standards
Git: For version control and GitHub integration.
.gitignore: To protect your database and sensitive settings.
requirements.txt: For easy, one-command installation of all dependencies.
README.md: A professional guide for anyone viewing your GitHub repository.
seed_data.py: A custom script I wrote to populate your database with initial data (like your first admin, classrooms, and subjects) for testing.
This project is now a "State-of-the-Art" ERP system, ready for the school's official use!


