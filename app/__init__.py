from flask import Flask

from app.views.index_view import bp as index_bp
from app.views.create_character_view import bp as character_bp

def create_app():
    app = Flask(__name__)
    
    app.register_blueprint(index_bp)
    app.register_blueprint(character_bp)

    return app