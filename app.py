from flask import Flask
from blueprints.home import home as home_bp

app = Flask(__name__)
app.register_blueprint(home_bp)

if __name__ == "__main__":
    from waitress import serve
    serve(app, host="0.0.0.0", port=8080)