# 🚀 FastAPI CRUD Application

A simple and efficient **CRUD (Create, Read, Update, Delete)** API built using **FastAPI** — one of the fastest and most modern Python web frameworks.  
This project demonstrates how to build a production-ready REST API with clean architecture, data validation, and asynchronous operations.

---

## 🧩 Features

- ⚡ Built using **FastAPI** (high performance, easy syntax)
- 🧠 **Pydantic** models for data validation
- 🗄️ Supports **CRUD** operations
- 🔐 RESTful API design
- 📡 Ready to integrate with databases (SQLite, PostgreSQL, MongoDB)
- 🧰 Modular, scalable, and beginner-friendly codebase

---

## ⚙️ Installation & Setup
```bash
1️⃣ Clone the Repository
git clone https://github.com/ombhalodiya45/FastAPI_demo.git
cd fastAPI_demo

2️⃣ Create a Virtual Environment
python -m venv venv

3️⃣ Activate the Virtual Environment
## For Windows
venv\Scripts\activate


## For Mac/Linux
source venv/bin/activate

4️⃣ Install Dependencies
pip install fastapi uvicorn httpx pydantic

💡 What each one does:
Package	Purpose
fastapi	The main web framework to create APIs
uvicorn	The ASGI server that runs your FastAPI app
httpx For making async HTTP requests (used for calling Groq API)
pydantic Used by FastAPI for data validation and request models

✅ Steps to create it:

In your project folder, make a file named:
requirements.txt

Paste below content inside it.
fastapi
uvicorn
httpx
python-dotenv
pydantic


Then run:
pip install -r requirements.txt
