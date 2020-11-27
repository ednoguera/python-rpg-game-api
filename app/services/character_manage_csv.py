from environs import Env
import csv

env = Env()
env.read_env()

class Personagem:
    """Classe que representa um personagem jogável com todos os seus atributos"""
    
    def __init__(self, character_name, character_class, character_healthy, character_status, character_power, character_strength, character_intelligence):
        self.character_name = character_name
        self.character_class = character_class
        self.character_healthy = character_healthy
        self.character_status = character_status
        self.character_power = character_power
        self.character_strength = character_strength
        self.character_intelligence = character_intelligence
    
    def cure_character(self, cure):
        self.character_healthy += cure

    def take_damage(self, damage):
        self.character_healthy -= damage


def cria_personagem(character_name, character_class, character_healthy, character_status, character_power, character_strength, character_intelligence):
    with open(env('CHARACTER_STATUS'), 'w') as csv_file:
        writer = csv.writer(csv_file)
        csv_line = [character_name, character_class, character_healthy, character_status, character_power, character_strength, character_intelligence]
        writer.writerow(csv_line)




