# Flask Backend Events

This project is a Flask-based backend for managing events and their participants.
This project was created in the Next Level Week (NLW) from Rocketseat

## Project Structure

```
├── init
│   └── schema.sql
├── run.py
├── requirements.txt
├── src
│   ├── __init__.py
│   ├── controllers
│   │   ├── events
│   │   │   └── events_creator.py
│   │   └── inscritos
│   │       └── inscritos_creator.py
│   ├── http_types
│   │   ├── http_request.py
│   │   └── http_response.py
│   ├── main
│   │   └── server
│   │       └── server.py
│   └── model
│       └── repositories
│           └── interfaces
│               └── inscritos_repository.py
│               └── eventos_repository.py
└── .vscode
    └── settings.json
```

## Setup Instructions

1. **Clone the repository:**
    ```sh
    git clone https://github.com/yourusername/flask-backend-events.git
    cd flask-backend-events
    ```

2. **Create a virtual environment:**
    ```sh
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Install dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

4. **Initialize the database:**
    ```sh
    sqlite3 database.db < init/schema.sql
    ```

5. **Run the application:**
    ```sh
    python run.py
    ```

## Usage

- The application will be available at `http://0.0.0.0:3000`.
- Use a tool like Postman to interact with the API endpoints.

## License
