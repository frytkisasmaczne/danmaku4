
# bro just
# delta = {
#   "before": {
#     "state": {
#       "step": "setup",
#       "round": 0,
#       "turn": 0,
#       "incident": ["idk"],
#       "discard": {
#         "incident": ["idk"]
#       },
#       "players": ["coper", "seether"],
#       "mods": []
#     },
#   },
#   "change": {}, # changed state subtree
# }



class Delta():
  action = None # "+,=,del"
  value = None

def applydelta(before, change):
  if isinstance(change, dict):
    for ch in change:
        applydelta(before[ch], change[ch])
  elif isinstance(change, list):
     for ch in enumerate(change):
        applydelta(before[ch], change[ch])
  elif isinstance(change, Delta):
    match change:
      case "+":
        before += change
      case "=":
        before = change
      case "del":
        del before
