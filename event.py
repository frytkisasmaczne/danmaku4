from object import *
from effect import *


EventType = Enum("EventType",
  [
    "TURN_START",
    "EFFECT_RESET",
    "LIMIT_RESET",
    "INCIDENT_STEP",
    "INCIDENT_SET",
    "INCIDENT_EFFECT",
    "DRAW_STEP",
    "PLAYER_DRAW",
    "MAIN_STEP",
    "CARD_PLAY",
    "SPELLCARD_PLAY",
    "DISCARD_STEP",
    "CARD_DISCARD",
  ])

class Event():
  typee: EventType = None
  children = None
