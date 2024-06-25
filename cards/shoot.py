from ..card import *
from ..player import *
from ..effect import *
from ..ui import *


# what can be used right now
# most cards will either return itself or nothing, but for example shoot after it's been chosen, will not commit and return other danmaku cards and attackable players
def can(self, state, player: Player) -> list[UUID]:
  if state["turn"] != player.uuid:
    return False
  if player.danmaku < 1:
    return False
  results: list[UUID] = []
  if cards_uncommited[-1].name == shoot.name: # TODO flimsy only one danmaku card can be added in theory
    for uuid, obj in objects.items():
      if type(obj) == Player:
        results.append(obj.uuid)
        # TODO commit
      elif type(obj) == Card:
        if "danmaku" in obj.icons:
          results.append(obj.uuid)
    results.remove(self.uuid)
    
  return results


shoot = Card()
shoot.name = "Shoot"
shoot.can = can
