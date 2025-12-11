# app.py

from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

# Connect to the SQLite database
def get_db_connection():
    conn = sqlite3.connect("workouts.db")
    conn.row_factory = sqlite3.Row
    return conn

# GET /workouts
@app.route('/workouts', methods=["GET"])
def get_workout():
    conn = get_db_connection()
    workouts = conn.execute("SELECT * FROM workouts").fetchall()
    conn.close()
    return jsonify([dict(row) for row in workouts])

# POST /workouts
@app.route('/workouts', methods=["POST"])
def add_workout():
    data = request.get_json()
    type_ = data.get("type")
    duration = data.get("duration")
    date = data.get("date")

    if not all([type_, duration, date]):
        return {"error": "Missing fields"}, 400
    
    conn = get_db_connection()
    conn.execute(
        "INSERT INTO workouts (type, duration, date) VALUES (?, ?, ?)",
        (type_, duration, date)
    )
    conn.commit()
    conn.close()

    return {"message": "Workout added"}, 201

# DELETE /workouts/<id>
@app.route('/workouts/<int:id>', methods=["DELETE"])
def delete_workout(id):
    conn = get_db_connection()
    conn.execute("DELETE FROM workouts WHERE id = ?", (id,))
    conn.commit()
    conn.close()
    return {"message": "Workout deleted"}, 204

if __name__ == '__main__':
    app.run(debug=True)