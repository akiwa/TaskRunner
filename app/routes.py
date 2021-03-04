from flask import Blueprint

routes = Blueprint("", __name__)


@routes.route("/")
def index():
    return "Welcome to the Task Runner!"


@routes.route("/task_started_externally")
def task_started_externally():
    return "Route to register externally started processes"


@routes.route("/task_finished")
def task_finished():
    return "Updates task state to finished"


@routes.route("/task_list")
def task_list():
    return "List of running tasks"


@routes.route("/delete_task")
def delete_task():
    return "Delete finished task after examination"
