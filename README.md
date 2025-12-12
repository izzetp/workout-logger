# Workout Logger API
A simple RESTful API built with Python and Flask to log and manage workouts.

**Live Demo**: [https://workout-logger-njdc.onrender.com](https://workout-logger-njdc.onrender.com/workouts)

## Features
- Add, update, delete, view workouts
- Data persistence via SQLite
- Tested using Thunder Client

## Tech Stack

- [Python](https://www.python.org/)
- [SQLite](https://sqlite.org/)
- [Flask](https://flask.palletsprojects.com/)
- [Thunder Client](https://www.thunderclient.com/) (for testing)

## Getting Started
**Clone the repository**
```bash
git clone https://github.com/izzetp/workout-logger
cd workout-logger
```

**Install dependencies**
```
pip install -r requirements.txt
```

**Create the database**
```
python db.py
```

**Run the app**
```
python app.py
```

## API Endpoints

| Method | Route              | Description            |
|--------|--------------------|------------------------|
| GET    | `/workouts`        | Get all workouts       |
| POST   | `/workouts`        | Add a new workout      |
| PUT    | `/workouts/<id>`   | Update workout by ID   |
| DELETE | `/workouts/<id>`   | Delete workout by ID   |

## Example: Add a Workout

**POST** `/workouts`  
```json
{
  "type": "Run",
  "duration": 30,
  "date": "2025-12-10"
}
```
## Testing
You can test the endpoints using:

- [Thunder Client](https://www.thunderclient.com/)
- [Postman](https://www.postman.com/) or curl

## Resources
- [Developing RESTful APIs with Python and Flask](https://auth0.com/blog/developing-restful-apis-with-python-and-flask/)
