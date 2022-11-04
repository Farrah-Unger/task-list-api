from flask import Blueprint, request, jsonify, make_response
from app import db
from app.models.task import Task


task_bp = Blueprint("tasks", __name__, url_prefix="/tasks")

#Create a new task
@task_bp.route("", methods=["POST"])
def create_task():
    request_body = request.get_json()
    new_task = Task(
        title = request_body["title"],
        description = request_body["description"],
        completed_at = request_body["completed_at"]
    )

    db.session.add(new_task)
    db.session.commit()
    
    return make_response(jsonify(f"Book {new_task.title} successfully created"), 201)

    
    
#Read All Tasks
@task_bp.route("", methods=["GET"])
def read_all_task():
    tasks_response = []
    tasks = Task.query.all()
    for task in tasks:
        tasks_response.append(
            {
                "id": task.id,
                "title": task.title,
                "description": task.description,
                "is_complete": task.null 
            }
        )
    return jsonify(tasks_response)