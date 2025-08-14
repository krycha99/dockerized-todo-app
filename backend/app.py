from flask import Flask, jsonify, request
from pymongo import MongoClient
import os

app = Flask(__name__)

# MongoDB config
client = MongoClient("mongodb://localhost:27017/tododb")
tasks_collection = client["tododb"]["tasks"]

@app.route('/')
def home():
    return jsonify({"message": "this is home page"}), 200

@app.route('/tasks', methods=['GET'])
def get_tasks():
    tasks = list(tasks_collection.find({}, {"_id": 0}))
    return jsonify(tasks), 200

@app.route('/tasks', methods=['POST'])
def add_task():
    data = request.json
    if not data or "title" not in data:
        return jsonify({"error": "Title is required"}), 400
    tasks_collection.insert_one({"title": data["title"], "done": False})
    return jsonify({"message": "Task added"}), 201

@app.route("/tasks/<title>", methods=['DELETE'])
def delete_task(title):
    result = tasks_collection.delete_one({"title": title})
    if result.deleted_count == 0:
        return jsonify({"error": "Task not found"}), 404
    return jsonify({"message": "Taske deleted"}), 200

@app.route("/tasks/<title>", methods=['PATCH'])
def update_task(title):
    data = request.json
    if not data or "done" not in data:
        return jsonify({"error": "'done' field is required"}), 400

    result = tasks_collection.update_one(
        {"title": title},
        {"$set": {"done": data["done"]}}
    )

    if result.matched_count == 0:
        return jsonify({"error": "Task not found"}), 404

    task = tasks_collection.find_one({"title": title}, {"_id": 0})
    return jsonify(task), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)