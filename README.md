# Career AI Platform 🚀

An AI-powered career assistance platform that helps users manage resumes, improve ATS compatibility, and streamline career development workflows.

---

## 📌 Overview

Career AI Platform is a full-stack career management system built with Django and PostgreSQL. The platform is designed to provide:

- 👤 User authentication and profile management
- 📄 Resume management and storage
- 🤖 ATS (Applicant Tracking System) analysis
- 🔗 REST APIs for frontend integration
- 🐳 Dockerized PostgreSQL database

The goal of this project is to create a scalable backend architecture for modern AI-powered career applications.

---

## ✨ Features

### User Management
- User registration and authentication
- Profile management
- RESTful API endpoints

### Resume Module
- Create and manage resumes
- Store resume-related information
- Future support for AI-generated resume suggestions

### ATS Module
- ATS compatibility analysis
- Resume scoring system
- Extensible architecture for AI-based evaluation

### Database
- PostgreSQL integration
- Docker support for easy setup
- Persistent storage using Docker volumes

---

## 🛠 Tech Stack

| Category | Technology |
|----------|------------|
| Backend | Django 6 |
| API Framework | Django REST Framework |
| Database | PostgreSQL |
| Containerization | Docker |
| Language | Python |
| Version Control | Git & GitHub |

---

## 📂 Project Structure

```bash
career-ai-platform/
│
├── backend/
│   ├── users/          # User authentication & profiles
│   ├── resume/         # Resume management
│   ├── ats/            # ATS analysis module
│   ├── backend/        # Django project settings
│   └── manage.py
│
├── docker-compose.yml  # PostgreSQL container setup
│
└── .gitignore
