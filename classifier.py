
import os
import sys

def classify_deck(decklist):

	if "Brainstorm" in decklist:
		if "Force of Will" in decklist:
			"""4 main categories of FoW decks: Reanimator/Show and Tell decks, Delver decks, 4c/BUG Decks, and Miracles"""

			if "Entomb" in decklist:
				return "UB Reanimator"

			elif "Show and Tell" in decklist:
				if "Sneak Attack" in decklist:
					return "Sneak and Show"
				else:
					return "OmniTell"

			elif "Delver of Secrets" in decklist:
				if "Deathrite Shaman" in decklist:
					if "Gurmag Angler" in decklist and "Lightning Bolt" in decklist:
						return "Grixis Delver"
					if "Tarmogoyf" in decklist:
						if "Lightning Bolt" in decklist:
							return "4C Delver"
						else:
							return "BUG Delver"
				else:
					if "Nimble Mongoose" in decklist:
						return "RUG Delver"
					if "Monastery Swiftspear" in decklist or "Grim Lavamancer" in decklist:
						return "UR Delver"
			elif "Deathrite Shaman" in decklist: #indicates non-Delver blue DRS deck (BUG, Pile, Deathblade, Sardless BUG, Aluren or Food Chain)
				if "Kolaghan's Command" in decklist:
					if "Leovold, Emissary of Trest" in decklist:
						return "Czech Pile"
					elif "Dack Fayden" in decklist and "Punishing Fire" in decklist:
						return "Punishing Dack"
					else:
						return "Grixis Control"

				elif "Stoneforge Mystic" in decklist:
					if "Noble Hierarch" in decklist:
						return "Bant Deathblade"
					else:
						return "Esper Deathblade"
				elif "Shardless Agent" in decklist:
					if "Aluren" in decklist:
						return "Aluren"
					else:
						return "Shardless BUG"
				elif "Baleful Strix" in decklist and "Leovold, Emissary of Trest" in decklist:
					if "Food Chain" in decklist:
						return "Food Chain"
					else:
						return "BUG Control"
			elif "Terminus" in decklist:
				return "Miracles"
			elif "Inkmoth Nexus" in decklist:
				return "Infect"
		else: # no FoW means probably Storm, or maybe BUG Nic Fit, or Tins Fins with Brainstorm
			if "Veteran Explorer" in decklist:
				return "Nic Fit"
			elif "Entomb" in decklist and "Shallow Grave" in decklist:
				return "Tin Fins"
			elif "Dark Ritual" and "Tendrils of Agony" in decklist:
				return "Storm"
		
		return "Other (Brainstorm)"
	elif "Chalice of the Void" in decklist:
		if "Life from the Loam" in decklist and "Dark Confidant" in decklist:
			return "4c Loam"
		elif "Thought-Knot Seer" in decklist and "Eye of Ugin" in decklist:
			if "Cloudpost" in decklist:
				return "12 Post Eldrazi"
			else:
				return "Eldrazi Stompy"
		elif "Blood Moon" in decklist:
			if "Sneak Attack" in decklist:
				return "Big Red"
			elif "Chandra, Torch of Defiance" in decklist:
				return "Moon Stompy"
		elif "Arcbound Ravager" in decklist:
			return "Steel Stompy"
		else:
			return "Other (Chalice)"
	elif "Dark Depths" in decklist:
		if "Exploration" in decklist:
			return "Lands"
		elif "Vampire Hexmage" and "Crop Rotation" in decklist:
			return "Turbo Depths"
		elif "Griselbrand" in decklist:
			return "Reanimator Depths"
	elif "Veteran Explorer" in decklist and "Cabal Therapy" in decklist:
		return "Nic Fit"
	elif "Deathrite Shaman" in decklist:
		if "Glimpse of Nature" in decklist and "Elvish Visionary" in decklist:
			return "Elves"
		if "Green Sun's Zenith" and "Mother of Runes" in decklist:
			return "Maverick"
		if "Tarmogoyf" in decklist and "Lightning Bolt" in decklist:
			return "Jund"
	elif "Mother of Runes" in decklist and "Thalia, Guardian of Thraben" in decklist:
		return "Death and Taxes"
	elif "Entomb" in decklist and "Griselbrand" in decklist:
		if "Shallow Grave" in decklist:
			return "Tin Fins"
		else:
			return "BR Reanimator"
	elif "Stinkweed Imp" in decklist:
		if "Phantasmagorian" in decklist:
			return "Manaless Dredge"
		elif "Faithless Looting" in decklist:
			return "Mana Dredge"
	elif "Lava Spike" in decklist:
		return "Burn"
	elif "Goblin Charbelcher" in decklist:
		return "Belcher"
	elif "Undercity Informer" in decklist:
		return "Oops All Spells"
	return "Other (Rogue)"
		
def main():
	for f in os.listdir('./test_decklists/9-18'):
		if f.endswith('.txt'):
			with open(os.path.join('./test_decklists/9-18', f), 'r') as deck:
				decklist = deck.read()
				print(decklist)
				print(classify_deck(decklist))
				print("-" * 40)


if __name__ == '__main__':
	main()
