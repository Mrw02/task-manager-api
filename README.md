# Task Manager API

A production-ready REST API for managing tasks with categories, priorities, and filtering — built with Django REST Framework.

## Features

- JWT Authentication (register, login, token refresh)
- Full CRUD for tasks and categories
- Filter by status, priority, category, and due date range
- Search by title and description
- Pagination (10 tasks per page)
- Swagger UI documentation
- Dockerized with PostgreSQL

## Tech Stack

- **Backend:** Python 3.11, Django 4.2, Django REST Framework
- **Database:** PostgreSQL 15
- **Auth:** JWT via `djangorestframework-simplejwt`
- **Docs:** Auto-generated Swagger via `drf-spectacular`
- **DevOps:** Docker, docker-compose

## Getting Started

### Prerequisites
- Docker & docker-compose installed

### Run locally

```bash
git clone https://github.com/your-username/task-manager-api.git
cd task-manager-api
cp .env.example .env
docker-compose up --build
```

API available at: `http://localhost:8000`  
Swagger docs: `http://localhost:8000/api/docs/`

### Run migrations

```bash
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py createsuperuser
```

## API Endpoints

### Auth
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/auth/register/` | Create account |
| POST | `/api/auth/login/` | Get JWT tokens |
| POST | `/api/auth/refresh/` | Refresh access token |
| GET | `/api/auth/me/` | Current user info |

### Tasks
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/tasks/` | List tasks (paginated) |
| POST | `/api/tasks/` | Create task |
| GET | `/api/tasks/{id}/` | Get task |
| PUT/PATCH | `/api/tasks/{id}/` | Update task |
| DELETE | `/api/tasks/{id}/` | Delete task |

### Categories
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/tasks/categories/` | List categories |
| POST | `/api/tasks/categories/` | Create category |
| PUT/PATCH | `/api/tasks/categories/{id}/` | Update category |
| DELETE | `/api/tasks/categories/{id}/` | Delete category |

## Filtering & Search

```
# Filter by status
GET /api/tasks/?status=todo

# Filter by priority
GET /api/tasks/?priority=high

# Filter by due date range
GET /api/tasks/?due_date_from=2024-01-01&due_date_to=2024-12-31

# Search in title/description
GET /api/tasks/?search=meeting

# Order by due date
GET /api/tasks/?ordering=due_date
```

## Example Request

```bash
# Register
curl -X POST http://localhost:8000/api/auth/register/ \
  -H "Content-Type: application/json" \
  -d '{"username": "john", "email": "john@example.com", "password": "pass1234", "password2": "pass1234"}'

# Login
curl -X POST http://localhost:8000/api/auth/login/ \
  -H "Content-Type: application/json" \
  -d '{"username": "john", "password": "pass1234"}'

# Create task (with token)
curl -X POST http://localhost:8000/api/tasks/ \
  -H "Authorization: Bearer <your_token>" \
  -H "Content-Type: application/json" \
  -d '{"title": "Buy groceries", "priority": "medium", "status": "todo"}'
```

## License

MIT
