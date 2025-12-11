# app.py

from flask import Flask
from flask import request

app = Flask(__name__)

workouts = []
next_id = 1

@app.route('/workouts', methods=["GET"])
def get_workout():
    return {"workouts": workouts}

@app.route('/workouts', methods=["POST"])
def add_workout():
    global next_id
    data = request.get_json()
    data["id"] = next_id
    workouts.append(data)
    next_id += 1
    return {"message": "Workout added", "workout": data}, 201

@app.route('/workouts/<int:id>', methods=["DELETE"])
def delete_workout(id):
    global workouts
    workouts = [w for w in workouts if w.get("id") != id]
    return {"message": "Workout deleted"}, 204

if __name__ == '__main__':
    app.run(debug=True)