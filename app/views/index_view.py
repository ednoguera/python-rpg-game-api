from flask import Blueprint

bp = Blueprint('index_route', __name__)

@bp.route('/', methods=['GET'])
def index():
    return {'status': 'ok', 'route':'index'}