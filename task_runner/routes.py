from flask import Blueprint, request
from task_runner.request_handler import RequestHandler


def construct_routes(request_handler: RequestHandler) -> Blueprint:
    routes = Blueprint("", __name__)

    @routes.route("/")
    def index():
        return "Welcome to the Task Runner!"

    @routes.route("/tasks", methods=["GET"])
    def task_list():
        return request_handler.list_tasks()

    @routes.route("/tasks", methods=["POST"])
    def task_started_internally():
        body = request.json
        assert body["task"] and body["task"]["name"] and body["task"]["command"]
        return request_handler.start_task(body["task"]["name"], body["task"]["command"])

    @routes.route("/tasks/external", methods=["POST"])
    def task_started_externally():
        return request_handler.register_task()

    @routes.route("/tasks/<task_id>", methods=["PUT"])
    def task_finished(task_id):
        assert task_id == request.view_args['task_id']
        return request_handler.finish_task()

    @routes.route("/tasks/<task_id>", methods=["DELETE"])
    def delete_task(task_id):
        assert task_id == request.view_args['task_id']
        return request_handler.delete_task()

    return routes
