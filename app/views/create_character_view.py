from flask import Blueprint, request
from app.services.character_manage_csv import Personagem, cria_personagem

bp = Blueprint('characters_route', __name__)

@bp.route('/novo-personagem', methods=['POST'])
def cadastra_personagem():
    
    hero_1 = Personagem(request.get_json()['character_name'], request.get_json()['character_class'], request.get_json()['character_healthy'], request.get_json()['character_status'], request.get_json()['character_power'], request.get_json()['character_strength'], request.get_json()['character_intelligence'])
    print(hero_1.character_name)
    
    
    return {'status': [cria_personagem(hero_1.character_name, hero_1.character_class, hero_1.character_healthy, hero_1.character_status, hero_1.character_power, hero_1.character_strength, hero_1.character_intelligence)]}
    
