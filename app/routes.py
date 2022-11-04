from flask import Blueprint, jsonify, make_response, request
from app import db
from app.models.task import Task



tasks_bp = Blueprint("tasks",__name__, url_prefix="/tasks")

@tasks_bp.route("", methods=["POST"])
def create_task():
    request_body = request.get_json()

    new_task = Task(
        title = request_body["title"],
        description = request_body["description"],
        completed_at = request_body["completed_at"]
    )

    db.session.add(new_task)
    db.session.commit()

  
    return make_response(jsonify(f"Task {new_task.title} has been successfully created."), 201)

@tasks_bp.route("", methods=["GET"])
def get_task():
    tasks_response = []
    tasks = Task.query.all()
    for task in tasks:
        tasks_response.append({
            "title": task.title,
            "description": task.description,
            "is_complete": task.completed_at
            })
    return jsonify(tasks_response)
