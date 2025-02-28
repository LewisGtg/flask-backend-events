from flask import Flask
from src.main.routes.event import event_route_bp
from src.main.routes.inscrito import inscrito_route_bp

app = Flask(__name__)
app.register_blueprint(event_route_bp)
app.register_blueprint(inscrito_route_bp)