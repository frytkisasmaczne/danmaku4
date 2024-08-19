from object import *
from effect import *


EventType = Enum("EventType",
  [
    "GAME_SETUP",
    "START_OF_TURN",
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
  effects = None


def GameSetup() -> Event:
  event = Event()
  event.typee = EventType.GAME_SETUP
  effect = Effect()
  effect.typee = EffectType.Game_Setup
  state = {
    "incident": "idk",
    "discard": {
      "incident": ["idk"]
    },
    "players": ["coper", "seether"],
    "callbacks": [],
    "history": [
                # Event(typee=EventType.GAME_SETUP, children=[Effect()])
                # Event(typee=EventType.TURN_START, children=[Effect(typee=EffectType.Modify_Anything)]),
                # Event(typee=EventType.EFFECT_RESET),
                # Event(typee=EventType.LIMIT_RESET),
                # Event(typee=EventType.INCIDENT_STEP),
                ],
  }

  event.effects = []
