# 📘 Online Course Platform (Udemy Clone)

This is a Django-based online course platform that allows instructors to create courses with video and PDF lessons. Users can view course content, stream videos securely (via Supabase Storage), and interact through a modern frontend. Inspired by platforms like Udemy.

---

## 🚀 Features

- 📂 Course, Section, and Lesson structure
- 🎥 Secure video & PDF streaming using Supabase signed URLs
- 🧾 PDF lesson support alongside video lessons
- 📑 Collapsible sidebar with intuitive navigation (using Alpine.js)
- ✅ Custom authentication and registration
- 🔒 Email verification for account activation
- 📱 Mobile-friendly responsive design

---

## 🛠️ Tech Stack

- **Backend**: Django, Django ORM, Django Admin
- **Frontend**: Tailwind CSS, Alpine.js
- **Storage**: Supabase (for private video & PDF hosting)
- **Database**: SQLite / PostgreSQL (configurable)
- **Deployment-ready**: Can be deployed to Heroku, Vercel (for frontend), or DigitalOcean

---

## 📁 Project Structure

onlinecourse/
├── courses/ # Main app for course logic
│ ├── models.py # Course, Section, Lesson models
│ ├── views.py # course_list, lesson_detail logic
│ ├── templates/ # course_detail.html and others
│ └── admin.py # Django Admin customization
├── users/ # User registration, login, and verification
├── media/ # Uploaded images (if any)
├── static/ # Custom static files
├── templates/ # Base HTML templates
└── manage.py







