from flask import Blueprint

bp = Blueprint('characters_route', __name__)

@bp.route('/novo-personagem')
def cadastra_personagem():
    return {'status': 'server ok'}
    
