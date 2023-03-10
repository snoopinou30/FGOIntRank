import json

from typing import Any
from relatedQuest import RelatedQuest
from relatedQuest import Interlude
from relatedQuest import RankUp
from ascensions import Ascensions, parseAsc

class Servant:
	name = ""
	rarity = 0
	
	related : list[int] = []
	relatedQuests : list[RelatedQuest] = []
	ascensions : Ascensions = []
	
	def __init__(self, name = "", related = [], className = "", rarity = 0, ascensions : Ascensions = []):
		self.name = name
		self.related = related
		self.className = className
		self.rarity = rarity
		self.relatedQuests = []
		self.ascensions = ascensions


	def maxBond(self):
		"""Get the bond value needed to unlock all strengthening

		Returns:
			int: The bond value
		"""

		m = 0
		for q in self.relatedQuests:
			for c in q.releaseConditions:
				if c.name == "svtFriendship":
					m = max(c.value, m)
					break
		return m

	def maxAsc(self):
		"""Get the ascension needed to unlock all strengthening

		Returns:
			int: The ascension value
		"""

		m = 0
		for q in self.relatedQuests:
			for c in q.releaseConditions:
				if c.name == "svtLimit":
					m = max(c.value, m)
					break
		return m

	def getInterludes(self) -> list[Interlude]:
		return list(filter(lambda x: isinstance(x, Interlude), self.relatedQuests))

	def getRankUps(self) -> list[RankUp]:
		return list(filter(lambda x: isinstance(x, RankUp), self.relatedQuests))

def createFromDict(d : dict[str, Any]) -> 'Servant' :
	if "name" in d.keys() and "relateQuestIds" in d.keys() and "className" in d.keys():
		return Servant(name = d['name'], related = d['relateQuestIds'], 
			className=d['className'], rarity=d["rarity"], ascensions = parseAsc(d["ascensionMaterials"]))
	else:
		return d

# file : Chemin vers le json de servants
def parseServants(file : str) -> list[Servant]:
	with open(file) as f:
		l = json.load(f, object_hook = createFromDict)
		return list(filter(lambda x: x is not None, l))