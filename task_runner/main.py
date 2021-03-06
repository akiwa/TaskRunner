from flask import Flask
from task_runner.routes import construct_routes
from task_runner.request_handler import RequestHandler
from task_runner.task_manager import TaskManager


def construct_flask_app(request_handler: RequestHandler) -> Flask:
    app = Flask(__name__)
    app.register_blueprint(construct_routes(request_handler))
    return app


def main():
    request_handler = RequestHandler(TaskManager())
    construct_flask_app(request_handler).run()


if __name__ == "__main__":
    main()
