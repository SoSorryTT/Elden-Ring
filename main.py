from utils.eldenring import Eldenring
from models.character_model import CharacterModel
from models.weapon_model import WeaponModel

elden_ring = Eldenring()

# print(elden_ring.character().get_all_character())
print(elden_ring.character().get_character_info(5))
# print(elden_ring.character().get_character_by_characterID("Will Smith"))

# print(elden_ring.weapon().get_all_weapon())
# print(elden_ring.weapon().get_weapon_info(20))
# print(elden_ring.weapon().get_weapon_by_type("Glintstone"))
# print(elden_ring.weapon().get_weapon_by_name("Hand of Malenia"))
# print(elden_ring.weapon().get_weapon_by_weight(3.5))
# print(elden_ring.weapon().get_weapon_by_weapon_skill("None"))

# new_character = CharacterModel(CharacterID="TEST ADD", 
#     Gender="TEST ADD", Str=0, Dex=0,
#     Int=0,Fai=0,Arc=0,Weight=0
#     )
# elden_ring.character().add_new_character(new_character)
# print(elden_ring.character().get_character_by_characterID("TEST ADD"))

# new_weapon = WeaponModel(WeaponType="TEST ADD", WeaponName="TEST ADD", 
#     Str=0, Dex=0, Int=0, Fai=0, Arc=0, WeaponWeight=0, WeaponSkill="TEST ADD"
#     )
# elden_ring.weapon().add_new_weapon(new_weapon)
# print(elden_ring.weapon().get_weapon_by_name("TEST ADD"))