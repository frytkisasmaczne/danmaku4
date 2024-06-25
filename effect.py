from object import *

EffectType = Enum("EffectType",
  [
    "Modify_Anything",
    "Attack",
    "Cancel",
    "Avoid"
    "Steal_Item",
  ])

class Effect():
  typee = None
  children = None
  statedelta = None
