from ..card import *
from ..player import *
from ..effect import *
from ..ui import *


def _can(self, state, player: Player):
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


def _janny(self, state, event):
  # if round has passed from this event: sewerside self
  for effect in event.effects:
    __janny(state, effect)


def __janny(self, state, effect):
  for eff in effect.effects:
    __janny(state, eff)
  if effect.typee == EffectType.Modify_Anything:
    for player in effect.statedelta["players"]:
      if player.uuid == self.target:
        if player["hp"] < 0:
          player.pop("hp") # na razie ok ale pewnie bedzie pozniej klopotliwe sprawdzanie oddzielnie pending efektow i dodawanie wlasnych efektow. wlasciwie moze i nie. chyba wlasnie to bedzie bardzo pasowac
# no hp loss (incident)
# incident does nothing for a round(card)
# shoot

# does shoot damage well yes since 

bagaznik = Card()
bagaznik.name = "Bagażnik"
bagaznik.can = _can
bagaznik.filter = _janny


