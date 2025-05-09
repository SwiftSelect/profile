# SwiftSelect Profile Service

The profile management service for SwiftSelect, handling user profiles, preferences, and related data.

## Overview

This service manages:
- User profile information
- Profile preferences and settings
- Profile data storage and retrieval
- Profile updates and modifications
- Profile data validation

## Tech Stack

- Python
- FastAPI
- SQLAlchemy
- Pydantic for data validation
- PostgreSQL (database)

## Prerequisites

- Python 3.8+
- pip (Python package manager)
- Virtual environment (recommended)
- PostgreSQL database

## Setup

1. Create and activate a virtual environment:
```bash
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up environment variables:
Create a `.env` file in the root directory with the following variables:
```
DATABASE_USER=
DATABASE_PASSWORD=
DATABASE_HOST=
DATABASE_PORT=
SECRET_KEY=

AUTH_SERVICE_URL=

SUPABASE_URL=
SUPABASE_KEY=
SUPABASE_S3_ACCESS_KEY=

KAFKA_BOOTSTRAP_SERVERS=
KAFKA_SASL_USERNAME=
KAFKA_SASL_PASSWORD=
KAFKA_CLIENT_ID=
```

## Running the Service

Development server:
```bash
uvicorn app.main:app --reload
```

Production server:
```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

## API Documentation

Once the server is running, you can access:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## Features

- CRUD operations for user profiles
- Profile data validation
- Profile image handling
- Profile preferences management
- Profile search and filtering

## Testing

Run tests using pytest:
```bash
pytest
```

## Data Models

The service uses the following main data models:
- UserProfile
- ProfilePreferences
- ProfileSettings
- ProfileImage

## Contributing

1. Create a new branch for your feature
2. Make your changes
3. Add tests for new functionality
4. Submit a pull request

## License

This project is proprietary and confidential.
