from typing import Any
from relatedQuest import RelatedQuest


class Servant:
	name = ""
	rarity = 0
	
	related : list[int] = []
	relatedQuests : list[RelatedQuest] = []
	
	def __init__(self, name = "", related = [], className = "", rarity = 0):
		self.name = name
		self.related = related
		self.className = className
		self.rarity = rarity
		self.relatedQuests = []


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


	@staticmethod
	def createFromDict(d : dict[str, Any]) -> 'Servant' :
		if "name" in d.keys() and "relateQuestIds" in d.keys() and "className" in d.keys():
			return Servant(name = d['name'], related = d['relateQuestIds'], className=d['className'], rarity=d["rarity"])
		else:
			return None