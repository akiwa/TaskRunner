from flask import Blueprint, request

routes = Blueprint("", __name__)


@routes.route("/")
def index():
    return "Welcome to the Task Runner!"


@routes.route("/tasks", methods=["GET"])
def task_list():
    return "List of running tasks"


@routes.route("/tasks", methods=["POST"])
def task_started_internally():
    return "Route to start process internally"


@routes.route("/tasks/external", methods=["POST"])
def task_started_externally():
    return "Route to register externally started processes"


@routes.route("/tasks/<task_id>", methods=["PUT"])
def task_finished(task_id):
    assert task_id == request.view_args['task_id']
    return "Updates task state to finished"


@routes.route("/tasks/<task_id>", methods=["DELETE"])
def delete_task(task_id):
    assert task_id == request.view_args['task_id']
    return "Delete finished task after examination"
