## Features

- CRUD operations for news articles, categories, and tags.
- Admin interface with full access to manage content.
- User interface with read-only access to published news articles.
- Redis caching for improved performance.
- Separate containers for user and admin applications.

## Project Structure
```
├── Dockerfile.admin
├── Dockerfile.user
├── docker-compose.yml
├── init_db/
│   └── init.sql
├── news/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── urls.py
│   ├── views.py
├── news_project/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
└── README.md
```

## Project Setup

### 1. Clone the Repository

```bash
git clone https://github.com/DauletKalesh/News_test.git

cd news_project

docker-compose up --build

docker-compose exec user_app python manage.py migrate
docker-compose exec admin_app python manage.py migrate
docker-compose exec admin_app python manage.py createsuperuser
