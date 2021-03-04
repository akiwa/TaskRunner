from flask import Flask
from .routes import routes

app = Flask(__name__)
app.register_blueprint(routes)


def main():
    app.run()

if __name__ == "__main__":
    main()
