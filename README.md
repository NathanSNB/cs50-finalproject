# NataBoards

[![CS50x Final Project](https://img.shields.io/badge/CS50x-Final%20Project-blue.svg?style=flat-square)](https://cs50.harvard.edu/x/)
[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Framework-Flask-000000?style=flat-square&logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![SQLite](https://img.shields.io/badge/Database-SQLite-003B57?style=flat-square&logo=sqlite&logoColor=white)](https://www.sqlite.org/)

> A lightweight, web-based Kanban task management board built with Python, Flask, and SQLite. Inspired by workflow tools like Trello and Padlet.

---

## 📹 Video Demo

Watch the comprehensive video demonstration of NataBoards on YouTube:  
👉 **[Watch the Demo on YouTube](https://youtu.be/bQwpvN5TBos)**

---

## 📌 Project Overview

**NataBoards** provides an intuitive, distraction-free environment for organizing projects, homework, and software features into customizable visual boards. It replaces cluttered desktop workflows with a horizontally structured interface powered by dynamic data rendering.

### Key Highlights
* **Dynamic Multi-Board Workspace**: Create, navigate, and remove distinct project boards seamlessly from a central hub.
* **Horizontal Board Hierarchy**: Structured columns (categories) arranged horizontally with tailored scrolling mechanics for ergonomic navigation on large screens.
* **Rich Markdown Integration**: Support for standard **Markdown syntax** within cards (bullet lists, code blocks, bold text, links) and direct image embedding through URL parsing.
* **Full CRUD Operations**: Complete Create, Read, Update, and Delete coverage across boards, columns, and tasks with real-time UI updates.

---

## 🏛️ Architecture & System Design

```text
[ Client Browser ]
        │
        ├── HTTP GET / POST (Jinja2 Templates & Forms)
        ▼
[ Flask Application (app.py) ]
        │
        ├── Markdown Filter Engine (misaka / markdown)
        └── Database Connector
                ▼
      [ SQLite3 (nataboards.db) ]
          ├── boards (id, name)
          ├── columns (id, board_id, name, position, color)
          └── items (id, column_id, title, content, type, position, color)

```

---

## 📂 Repository Structure

```text
.
├── app.py              # Application controller, routing logic, and database transactions
├── helpers.txt         # Development notes, SQL queries, and layout checklists
├── nataboards.db       # Relational SQLite database schema and persistent storage
├── static/
│   └── styles.css      # CSS styling: Flexbox/Grid systems, responsive layout, custom scrollbar
└── templates/
    ├── layout.html     # Base HTML skeleton (navigation bar, viewport meta, footer)
    ├── index.html      # Main dashboard displaying board selection and creation forms
    └── board.html      # Interactive workspace displaying columns, items, and action modals

```

---

## 🚀 Quickstart & Installation

Follow these instructions to clone, set up, and run NataBoards locally.

### Prerequisites

* Python 3.9+
* `pip` package manager

### Setup Steps

1. **Clone the repository:**
```bash
git clone [https://github.com/NathanSNB/cs50-finalproject.git](https://github.com/NathanSNB/cs50-finalproject.git)
cd cs50-finalproject

```


2. **Create and activate a virtual environment (recommended):**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

```


3. **Install dependencies:**
```bash
pip install Flask cs50 markdown

```


4. **Launch the Flask server:**
```bash
flask run

```


Open your browser and navigate to `http://127.0.0.1:5000/`.

---

## 👤 Author & Contact

Developed by **NathanSNB** as the Capstone Project for **Harvard CS50x**.

* **GitHub**: [@NathanSNB](https://www.google.com/search?q=https://github.com/NathanSNB&utm_source=gemini)
* **Website**: [natsnb68.mathysie.eu](https://natsnb68.mathysie.eu?utm_source=gemini)
* **Email**: [natsnb68@proton.me](https://www.google.com/search?q=mailto%3Anatsnb68%40proton.me)

*Special thanks to David J. Malan and the CS50 instructional team for providing the curriculum and foundational tools for this project.*
