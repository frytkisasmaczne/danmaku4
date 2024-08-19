from object import *


EffectType = Enum("EffectType",
  [
    "Modify_Anything",
    "Attack",
    "Cancel",
    "Avoid"
    "Steal_Item",
    "Game_Setup"
  ])


class Effect():
  typee = None
  parents_uuids = []
  statebefore = None
  statedelta = None
