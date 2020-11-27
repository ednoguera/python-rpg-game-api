from flask import Blueprint, request
from app.services.character_manage_csv import Personagem, cria_personagem

bp = Blueprint('characters_route', __name__)

@bp.route('/novo-personagem', methods=['POST'])
def cadastra_personagem():
    hero_1 = Personagem('Cloud', 'Warrior', 100, 'normal', 5, 7, 8)
    #character_name, character_class, character_healthy, character_status, character_power, character_strength, character_intelligence
    cria_personagem(request.get_json()['character_name'], request.get_json()['character_class'], request.get_json()['character_healthy'], request.get_json()['character_status'], request.get_json()['character_power'], request.get_json()['character_strength'], request.get_json()['character_intelligence'])
    return {'status': "ok"}
    
