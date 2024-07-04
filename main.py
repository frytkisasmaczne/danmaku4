from card import *
from event import *
from effect import *


state = {
  "incident": "idk",
  "discard": {
    "incident": ["idk"]
  },
  "players": ["coper", "seether"],
  "effects": [],
  "history": [
              Event(typee=EventType.GAME_SETUP, children=[Effect(typee=EffectType.)])
              Event(typee=EventType.TURN_START, children=[Effect(typee=EffectType.Modify_Anything)]),
              Event(typee=EventType.EFFECT_RESET),
              Event(typee=EventType.LIMIT_RESET),
              Event(typee=EventType.INCIDENT_STEP),
              ],
}

sstate = {
  "draw": {
    "incident": ["idk", "idk"]
  },
  "player_hands": {"coper": [], "seether": []},
}


def main():
  
  while True:
    # round
    for player in state["players"]:
      # turn
      turn()


def turn():
  # step
  # start of turn
  # reset single round effects, danmaku limit and spell card limit

  # incident
  # put new into play
  if not state["incident"]:
    state.incident = sstate["draw"]["incident"].pop()
  # incident callbacks
  for uuid, obj in objects.items():
    if obj.callbacks:
      for cb in obj["callbacks"]:
        # call every callback, it should check inside if this is the moment and stuff
        # add to history
        pass
  # pass



# jeśli jedna niestandardowa karta robi zmianę
# to druga niestandardowa karta może jej nie wykryć
# trzeba konwertować zmiany na wspólny format
# generowanie delt jako wyników custom funckcji
# no thats stupid


if __name__ == "__main__":
  main()
