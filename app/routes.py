from os import abort
from flask import Blueprint, jsonify, make_response, request, abort
from app import db
from app.models.task import Task


tasks_bp = Blueprint("tasks",__name__, url_prefix="/tasks")

@tasks_bp.route("", methods=["POST"])
def create_task():
    request_body = request.get_json()

    new_task = Task(
        # id = request_body["id"],
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
        tasks_response.append(
            {
            "task": {
            "id": task.task_id,
            "title": task.title,
            "description": task.description,
            "is_complete": task.completed_at
            }
        })
    
    return jsonify(tasks_response)

#Error Handling an invalid task or non-existing task
def validate_task(task_id):
    try:
        task_id = int(task_id)
    except:
        abort(make_response({"message":f"task {task_id} invalid"}, 400))

    task = Task.query.get(task_id)

    if not task:
        abort(make_response({"message":f"task {task_id} not found"}, 404))

    return task

#Get a single task
@tasks_bp.route("/<task_id>", methods=["GET"])
def read_one_task(task_id):
    task = validate_task(task_id)

    return {
        "id": task.task_id,
        "title": task.title,
        "description": task.description
    }