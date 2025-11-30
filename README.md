# 📰 Visernic News Portal

![Python](https://img.shields.io/badge/Python-3.13-blue.svg)
![Framework](https://img.shields.io/badge/Flask-3.0-green.svg)
![Status](https://img.shields.io/badge/Status-Production%20Ready-brightgreen.svg)
![License](https://img.shields.io/badge/License-MIT-orange.svg)

**Visernic News Portal** is a scalable, modular, and high-performance content management system (CMS) engineered for modern digital news outlets. Built with a focus on **clean architecture**, security, and speed, it leverages the **Flask Application Factory Pattern** to ensure maintainability and scalability for enterprise needs.

---

## 🚀 Key Features

### Backend Architecture
- **Modular Blueprint Structure:** Codebase is separated into logical modules (`main`, `news`, `errors`) for better organization.
- **Application Factory Pattern:** Allows for dynamic configuration switching (Development, Testing, Production).
- **ORM Integration:** Robust database management using **SQLAlchemy** with relationship mapping.
- **Scalable Database:** Supports **SQLite** for development and **PostgreSQL** for high-load production environments.

### Frontend Experience
- **Modern UI/UX:** Designed with **Tailwind CSS** for a fully responsive and mobile-first experience.
- **Dynamic Templating:** Utilizes **Jinja2** for server-side rendering and efficient data presentation.
- **SEO Optimized:** Clean URL slugs (e.g., `/news/ai-revolution-2025`) generated automatically for better search engine ranking.

---

## 🛠️ Technology Stack

| Component | Technology |
|-----------|------------|
| **Core** | Python 3.13 |
| **Framework** | Flask (Microframework) |
| **Database** | PostgreSQL (Prod) / SQLite (Dev) |
| **Server** | Gunicorn (WSGI) |
| **Frontend** | HTML5, Tailwind CSS, JavaScript |
| **Templating** | Jinja2 |

---
