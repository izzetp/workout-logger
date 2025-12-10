# Workout Logger API
A simple RESTful API built with Python and Flask to log workouts.

## Features
- Add a workout (type, duration, data)
- List workouts
- Delete a workout (by ID)

## Tech

- [Python](https://www.python.org/)
- [SQLite](https://sqlite.org/)
- [Flask](https://flask.palletsprojects.com/)

## Testing the API

You can test the endpoints using:

- [Thunder Client](https://www.thunderclient.com/)
- [Postman](https://www.postman.com/) or curl

### Example: Add a Workout

**POST** `/workouts`  
```json
{
  "type": "Run",
  "duration": 30,
  "date": "2025-12-10"
}
```

## Resources
- [Developing RESTful APIs with Python and Flask](https://auth0.com/blog/developing-restful-apis-with-python-and-flask/)
