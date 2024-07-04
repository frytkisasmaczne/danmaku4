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
  children = None
  statebefore = None
  statedelta = None
