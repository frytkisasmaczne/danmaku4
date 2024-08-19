from card import *
from event import *
from effect import *


def main():
  next = Event(typee=EventType.GAME_SETUP)
  while True:
    next = tick(next, state, sstate)


def tick(event: Event, state, sstate):
  i = 0
  while True:
    mods_acted = 0
    for i in range(len(state["mods"])):
      if state["mods"][i](event, state, sstate):
        mods_acted += 1
    if mods_acted == 0:
      break
    # if no Mod in for returned True, meaning no Mod did anything
    # then break the while
  match event.typee:
    case EventType.GAME_SETUP:
      # deal roles characters somehow idk
      return Event(typee=EventType.START_OF_TURN)
    case EventType.START_OF_TURN:
      # reset danmaku sc limits are in mods
      return Event(typee=EventType.INCIDENT_STEP)
    case EventType.INCIDENT_STEP:
      
      return Event


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


def _reset_danmaku_sc_limits(state):
  if (
    ("_reset_danmaku_sc_limits" not in executed
    or not executed["_reset_danmaku_sc_limits"])
    and state["step"] == "start of turn"
    ):
    executed["_reset_danmaku_sc_limits"] = 1 #limit access
    for player in state["players"]:
      player["danmaku"] = player["danmaku_max"] #todo replace with danmaku_max() maybe
      player["sc"] = player["sc_max"]


def _incident_draw(state, sstate):
  if (
    ("_incident_draw" not in executed
    or not executed["_incident_draw"])
    and state["step"] == "start of turn"
    ):
    executed["_incident_draw"] = 1
    if not state["incident"]:
      #out with it to draw_incident()
      state["incident"].append(sstate["draw"]["incident"].pop())
      

executed = {}

state = {
  "step": "setup",
  "round": 0,
  "turn": 0,
  "incident": ["idk"],
  "discard": {
    "incident": ["idk"]
  },
  "players": ["coper", "seether"],
  "mods": [
    _reset_danmaku_sc_limits,
    _incident_draw
    ],
  "pending": [],
}

history = [
              # Event(typee=EventType.GAME_SETUP, children=[Effect(typee=EffectType.)])
              # Event(typee=EventType.TURN_START, children=[Effect(typee=EffectType.Modify_Anything)]),
              # Event(typee=EventType.EFFECT_RESET),
              # Event(typee=EventType.LIMIT_RESET),
              # Event(typee=EventType.INCIDENT_STEP),
              ]

sstate = {
  "draw": {
    "incident": ["idk", "idk"]
  },
  "player_hands": {"coper": [], "seether": []},
}


# jeśli jedna niestandardowa karta robi zmianę
# to druga niestandardowa karta może jej nie wykryć
# trzeba konwertować zmiany na wspólny format
# generowanie delt jako wyników custom funckcji
# no thats stupid


if __name__ == "__main__":
  main()
