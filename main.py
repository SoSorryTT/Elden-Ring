from utils.eldenring import Eldenring
from models.character_model import CharacterModel
from models.weapon_model import WeaponModel

elden_ring = Eldenring()

# print(elden_ring.character().get_all_character())
print(elden_ring.character().get_character_by_characterID("Will Smith"))