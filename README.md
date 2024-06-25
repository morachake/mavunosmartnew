# Mavuno Smart Project

## Overview
Mavuno Smart is a Django-based application designed to support African smallholder farmers by providing tools for sustainable, profitable, and resilient farming. The application leverages AI and blockchain technology to analyze farm data using remote sensing. The project consists of a backend built with Django, an API using Django REST Framework, and a frontend interface for user interactions.

## Features
- User Authentication (JWT-based)
- Data Collection from Farms
- Remote Sensing Integration
- Admin Dashboard
- Swagger API Documentation
- Static File Handling with WhiteNoise

## Project Structure
```
mavunosmartnew/
│
├── core/
│   ├── __pycache__/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│
├── env/
│
├── mavuno_smart/
│   ├── __pycache__/
│   ├── migrations/
│   ├── static/
│   │   ├── css/
│   │   │   ├── styles.css
│   │   ├── js/
│   │       ├── scripts.js
│   ├── templates/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   ├── views.py
│
├── mavuno_smart_api/
│
├── static/
├── staticfiles/
├── .env
├── .gitignore
├── docker-compose.yml
├── Dockerfile
├── dockerignore
├── entrypoint.sh
├── manage.py
├── requirements.txt
├── wait-for-it.sh
```

## Getting Started

### Prerequisites
- Docker
- Docker Compose

### Installation

1. **Clone the repository:**
   ```sh
   git clone https://github.com/yourusername/mavunosmartnew.git
   cd mavunosmartnew
   ```

2. **Create and configure environment variables:**
   Create a `.env` file in the root directory with the following content:
   ```sh
   DJANGO_SECRET_KEY=your_secret_key
   DJANGO_DEBUG=True
   DJANGO_ALLOWED_HOSTS=localhost
   POSTGRES_DB=mavunosmart
   POSTGRES_USER=postgres
   POSTGRES_PASSWORD=your_password
   POSTGRES_HOST=db
   POSTGRES_PORT=5432
   ```

3. **Build and run the Docker containers:**
   ```sh
   docker-compose up --build
   ```

4. **Run database migrations:**
   ```sh
   docker-compose exec web python manage.py migrate
   ```

5. **Collect static files:**
   ```sh
   docker-compose exec web python manage.py collectstatic --noinput
   ```

6. **Access the application:**
   Open your web browser and navigate to `http://localhost:8000`.

## API Documentation
The API documentation is available at `http://localhost:8000/swagger/`. This documentation is powered by Swagger and provides interactive API exploration.

## Static Files Handling
Static files (CSS, JavaScript, Images) are managed using Django's staticfiles app with WhiteNoise for efficient static file serving.

### Static File Directories
- **Static Files:** `mavuno_smart/static/`
- **Collected Static Files:** `staticfiles/`



## Troubleshooting

### Common Issues
1. **Static files not loading:**
   - Ensure `collectstatic` command is run successfully.
   - Verify `STATIC_URL` and `STATIC_ROOT` settings in `settings.py`.

2. **Database connection errors:**
   - Verify PostgreSQL service is running.
   - Check database connection settings in the `.env` file.

### Logs
Check Docker container logs for detailed error messages:
```sh
docker-compose logs
```

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request for any improvements or bug fixes.

## License
This project is licensed under the MIT License.

## Acknowledgements
Special thanks to the Django and Docker communities for their excellent tools and documentation.

---
