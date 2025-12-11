# app.py

from flask import Flask, request, jsonify
import sqlite3
import os

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

# PUT /workouts
@app.route('/workouts/<int:id>', methods=["PUT"])
def update_workout(id):
    data = request.get_json()
    type_ = data.get("type")
    duration = data.get("duration")
    date = data.get("date")

    if not all([type_, duration, date]):
        return {"error": "Missing fields"}, 400
    
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(
        "UPDATE workouts SET type = ?, duration = ?, date = ? WHERE id = ?",
        (type_, duration, date, id)
    )
    conn.commit()
    updated = cur.rowcount
    conn.close()

    if updated == 0:
        return {"error": f"No workout with id {id} found"}, 404

    return {"message": f"Workout {id} updated"}, 200

# DELETE /workouts/<id>
@app.route('/workouts/<int:id>', methods=["DELETE"])
def delete_workout(id):
    conn = get_db_connection()
    conn.execute("DELETE FROM workouts WHERE id = ?", (id,))
    conn.commit()
    conn.close()
    return {"message": "Workout deleted"}, 204

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
