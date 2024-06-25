from ..card import *
from ..player import *
from ..effect import *
from ..ui import *


def can(self, state, player: Player):
  if state["turn"] != player.uuid:
    return False
  results = []
  if cards_uncommited[-1].name == self.name: # TODO flimsy and gay
    for uuid, obj in objects.items():
      if type(obj) == Player:
        results.append(obj)
        # TODO commit
      results.remove(player)
      return results


def janny(self, state, event):
  for effect in event.effects:
    _janny(state, effect)


def _janny(self, state, effect):
  for eff in effect.effects:
    _janny(state, eff)
  if effect.typee == EffectType.Modify_Anything:
    for player in effect.statedelta["players"]:
      if player.uuid == self.target:
        if player["hp"] < 0:
          player.pop("hp")


bagaznik = Card()
bagaznik.name = "Bagażnik"
bagaznik.can = can
bagaznik.filter = janny
