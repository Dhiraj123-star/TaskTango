# 🚀 TaskTango API

**TaskTango** is a modern, lightweight **task management API** built with **FastAPI** and **CockroachDB**.  
Easily create, read, update, and delete tasks — all backed by a scalable, distributed SQL database.  
Perfect for personal to-do lists 📝 or as a microservice in larger applications! 🎯

---

## 🌟 Core Functionality

- 🆕 **Create Tasks**: Add new tasks with title, description, and completion status.
- 📖 **Read Tasks**: Retrieve all tasks in structured JSON format.
- ✏️ **Update Tasks**: Modify existing tasks by ID to update details.
- 🗑️ **Delete Tasks**: Remove tasks by ID when they're completed or obsolete.
- 🌐 **RESTful API**: Built using FastAPI for performance, scalability, and built-in documentation.
- 🗄️ **CockroachDB Backend**: Uses a distributed SQL database for fault-tolerant, scalable data storage.

---

## 🛠️ Tech Stack

- ⚡ **FastAPI** – High-performance, async Python web framework.
- 🐓 **CockroachDB** – Resilient, distributed SQL database built for scale.
- 🔌 **psycopg2** – PostgreSQL adapter for Python to connect with CockroachDB.
- 🐳 **Docker & Docker Compose** – Containerized setup for portability and deployment.
- 🚀 **Uvicorn** – Lightning-fast ASGI server for serving FastAPI apps.

---

## 📦 Prerequisites

- 🐳 **Docker + Docker Compose** – For running the app and CockroachDB in containers.
- 🐍 **Python 3.11+** – Optional, for local development outside Docker.
- 😄 **A sense of adventure** – To explore and learn modern backend tooling.

---

## 🏁 Getting Started

1. **Clone the Repository**
2. **Set Up Environment Variables**
   - Includes settings for database connection and app config.
3. **Run with Docker**
   - Starts both the FastAPI app and CockroachDB service.
4. **Explore the API**
   - Visit the auto-generated **Swagger UI** to test endpoints.
   - Use the health check endpoint to verify service status.

---

## 📡 API Endpoints Overview

| Method | Endpoint             | Description              |
|--------|----------------------|--------------------------|
| GET    | `/tasks/`            | List all tasks           |
| POST   | `/tasks/`            | Create a new task        |
| PUT    | `/tasks/{task_id}`   | Update a task by ID      |
| DELETE | `/tasks/{task_id}`   | Delete a task by ID      |
| GET    | `/health`            | Health check of the API  |

---

## 📝 Development Notes

- 🧱 **Schema Design**: A simple tasks table with `id`, `title`, `description`, and `completed` fields.
- ♻️ **Scalable Architecture**: Easily extendable to support user accounts, tagging, or deadlines.
- 🧪 **Swagger UI Support**: Makes it easy to test and document your API automatically.

---

## 💡 Why TaskTango?

- Clean and modular FastAPI project structure
- Uses CockroachDB to explore distributed SQL in real-world microservices
- Excellent boilerplate for task apps, productivity tools, or project managers

---

## 🧠 Ideal For

- Learning how to build containerized REST APIs with FastAPI
- Exploring distributed databases like CockroachDB
- Integrating into a broader ecosystem of microservices

---

## 👨‍💻 Maintained By

**Dhiraj Kumar** – Backend Developer | Python Enthusiast | System Design Learner

---

