
# 🚀 TaskTango API

**TaskTango** is a secure, modern task management API built with **FastAPI** and **CockroachDB**.  
Manage tasks with ease, backed by a scalable, distributed SQL database and protected with JWT authentication.  
Perfect for personal to-do lists 📝, team productivity tools, or microservices in larger applications! 🎯

---

## 🌟 Core Functionality

- 🆕 **Create Tasks**: Add tasks with title, description, and completion status, tied to authenticated users.  
- 📖 **Read Tasks**: Retrieve user-specific tasks in structured JSON format.  
- ✏️ **Update Tasks**: Modify tasks by ID, restricted to the task owner.  
- 🗑️ **Delete Tasks**: Remove tasks by ID, ensuring user authorization.  
- 🔒 **JWT Authentication**: Secure endpoints with user registration and token-based access.  
- 🌐 **RESTful API**: Built using FastAPI for high performance, scalability, and auto-generated documentation.  
- 🗄️ **CockroachDB Backend**: Fault-tolerant, distributed SQL database for reliable data storage.

---

## 🛠️ Tech Stack

- ⚡ **FastAPI** – High-performance, async Python web framework.  
- 🐓 **CockroachDB** – Resilient, distributed SQL database for scalability.  
- 🔌 **psycopg2** – PostgreSQL adapter for Python, compatible with CockroachDB.  
- 🔐 **python-jose & passlib** – JWT authentication and password hashing.  
- 📋 **python-multipart** – Form data processing for login endpoints.  
- 🐳 **Docker & Docker Compose** – Containerized setup for portability.  
- 🚀 **Uvicorn** – Lightning-fast ASGI server for FastAPI.  
- 🤖 **GitHub Actions** – CI/CD pipeline for automated Docker image builds and pushes.

---

## 📦 Prerequisites

- 🐳 Docker + Docker Compose – For running the app and CockroachDB in containers.  
- 🐍 Python 3.11+ – Optional, for local development outside Docker.  
- 🔑 DockerHub Account – For CI/CD pipeline to push images (if deploying).  
- 😄 A sense of adventure – To explore modern backend and DevOps tooling.



## 📡 API Endpoints Overview

| Method | Endpoint          | Description                       | Auth Required |
| ------ | ----------------- | --------------------------------- | ------------- |
| GET    | /tasks/           | List tasks for authenticated user | Yes           |
| POST   | /tasks/           | Create a new task for user        | Yes           |
| PUT    | /tasks/{task\_id} | Update a task by ID               | Yes           |
| DELETE | /tasks/{task\_id} | Delete a task by ID               | Yes           |
| POST   | /register         | Register a new user               | No            |
| POST   | /token            | Obtain JWT token for login        | No            |
| GET    | /health           | Health check of the API           | No            |

---

## 🔐 Authentication Flow

1. **Register**:
   `POST /register` with

   ```json
   {"username": "user", "password": "pass"}
   ```

2. **Login**:
   `POST /token` with

   ```
   username=user&password=pass
   ```

   to get a JWT.

3. **Use JWT**:
   Include

   ```
   Authorization: Bearer <token>
   ```

   in headers for protected endpoints.

---

## 📝 Development Notes

### 🧱 Schema Design:

* **users**: Stores `id`, `username`, and `hashed_password`.
* **tasks**: Includes `id`, `title`, `description`, `completed`, and `user_id` (foreign key to users).

### 🔐 Security:

* JWT-based authentication ensures tasks are user-specific.

### ♻️ Scalable Architecture:

* Extensible for features like task categories, deadlines, or roles.

### 🧪 Swagger UI Support:

* Auto-generated docs for easy testing.

---

## 🤖 CI/CD Pipeline

A GitHub Actions workflow (`docker-publish.yml`) automates building and pushing the Docker image to DockerHub:

### Trigger:

* Pushes to the `main` branch.

### Steps:

* Checks out code.
* Sets up Python 3.11 and Docker Buildx.
* Logs into DockerHub using secrets (`DOCKERHUB_USERNAME`, `DOCKERHUB_TOKEN`).
* Builds and pushes the image as `dhiraj918106/tasktango:latest`.

### Setup:

* Add `DOCKERHUB_USERNAME` and `DOCKERHUB_TOKEN` as GitHub repository secrets.
* Push to `main` to trigger the pipeline.

---

## 💡 Why TaskTango?

✅ Clean, modular FastAPI project with secure authentication
✅ Leverages CockroachDB for distributed SQL in microservices
✅ CI/CD integration for streamlined deployments
✅ Ideal boilerplate for task apps, productivity tools, or learning modern APIs

---

## 🧠 Ideal For

* Learning to build secure, containerized REST APIs with FastAPI
* Exploring distributed databases like CockroachDB
* Practicing DevOps with GitHub Actions and Docker
* Integrating into microservice ecosystems

---

## 👨‍💻 Maintained By

**Dhiraj Kumar** – Backend Developer | Python Enthusiast | System Design Learner


