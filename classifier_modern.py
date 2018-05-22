import os, sys

def deck_includes(decklist, *cards):
	return all(card in decklist for card in cards)

def classify_deck(decklist):

	if deck_includes(decklist, "Champion of the Parish", "Thalia's Lieutenant"):
		return "Humans"

	if deck_includes(decklist, "Arcbound Ravager", "Cranial Plating"):
		return "Affinity"

	if deck_includes(decklist, "Hollow One", "Burning Inquiry", "Bloodghast"):
		return "Hollow One"

	if "Death's Shadow" in decklist:
		if "Traverse the Ulvenwald" in decklist:
			return "Traverse Shadow"
		if "Snapcaster Mage" in decklist and "Kolaghan's Command" in decklist:
			return "Grixis Shadow"
		return "Other (Shadow)"

	if "Scapeshift" in decklist:
		if "Primeval Titan" in decklist:
			return "Titan Shit"
		if "Cryptic Command" in decklist:
			return "RUG Scapeshift"
		return "Other (Scapeshift)" 

	if deck_includes(decklist, "Liliana of the Veil", "Tarmogoyf"):
		if "Bloodbraid Elf" in decklist:
			return "Jund"

		if "Lingering Souls" in decklist:
			return "Abzan"

		if "Tireless Tracker" in decklist:
			return "BG Rock"

		return "Other (BGx)"

	if deck_includes(decklist, "Cryptic Command", "Snapcaster Mage"):
		if deck_includes(decklist, "Lightning Bolt"):
			if "Path to Exile" in decklist:
				return "Jeskai Control"
			if "Kolaghan's Command" in decklist:
				return "Grixis Control"
			if "Blood Moon" in decklist:
				return "Blue Moon"
			return "Other (URx)"
		if "Supreme Verdict" in decklist:
			if "Watery Grave" in decklist:
				return "Esper Control"
			else:
				return "UW Control"
		return "Other (Blue Control)"

	if deck_includes(decklist, "Snapcaster Mage", "Kolaghan's Command", "Jace"):
		return "Grixis Control"

	if deck_includes(decklist, "Goblin Guide", "Lava Spike"):
		return "Burn"

	if deck_includes(decklist, "Sliver Hive"):
		return "Slivers"

	if deck_includes(decklist, "Bedlam Reveler", "Young Pyromancer"):
		return "Mardu Pyromancer"

	if "Urza's Tower" in decklist:
		if "Island" in decklist:
			return "U Tron"
		if "Reality Smasher" in decklist:
			return "Eldrazi Tron"
		return "Gx Tron"

	if deck_includes(decklist, "Gifts Ungiven", "Baral, Chief of Compliance"):
		return "Gifts Storm"

	if deck_includes(decklist, "Spreading Seas", "Path to Exile", "Cryptic Command"):
		return "UW Control"

	if "Slippery Bogle" in decklist:
		return "Bogles"

	if deck_includes(decklist, "Krark-Clan Ironworks", "Chromatic Star"):
		return "KCI"

	if deck_includes(decklist, "Collected Company", "Duskwatch Recruiter", "Vizier of Remedies"):
		return "Counters Company"

	if deck_includes(decklist, "Stone Rain", "Arbor Elf"):
		return "Ponza"

	if deck_includes(decklist, "Hall of the Bandit Lord", "Devoted Druid"):
		return "Turbo Druid"

	if deck_includes(decklist, "Arbor Elf", "Shrine to Nyx"):
		return "Green Devotion"

	if deck_includes(decklist, "Amulet of Vigor", "Primeval Titan"):
		return "Amulet Bloom"

	if deck_includes(decklist, "Phyrexian Unlife", "Angel's Grace"):
		return "Ad Nauseam"

	if deck_includes(decklist, "Leonin Arbiter", "Aether Vial"):
		return "Death and Taxes"

	if deck_includes(decklist, "Living End"):
		return "Living End"

	if deck_includes(decklist, "Elvish Mystic", "Heritage Druid"):
		return "Elves"

	if deck_includes(decklist, "Thought-Knot Seer", "Noble Hierarch"):
		if "Bloodbraid Elf" in decklist:
			return "RG Eldrazi"
		if "Eldrazi Skyspawner" in decklist:
			return "Bant Eldrazi"

	if deck_includes(decklist, "Lantern of Insight", "Ensnaring Bridge"):
		return "Lantern Control"

	if deck_includes(decklist, "Courser of Kruphix", "Noble Hierarch", "Ramunap Excavator"):
		return "GW Company"

	if deck_includes(decklist, "Simian Spirit Guide", "Blood Moon"):
		return "Free Win Red"

	if deck_includes(decklist, "Collected Company", "Spell Queller"):
		if deck_includes(decklist, "Mausoleum Wanderer", "Rattlechains"):
			return "Bant Spirits"
		return "Bant Company"

	if "Glistener Elf" in decklist:
		return "Infect"

	if deck_includes(decklist, "Stinkweed Imp", "Life from the Loam"):
		return "Dredge"

	# if deck_includes(decklist, "Blood Moon", "Nahiri"):
	# 	return "RW Prison"

	if deck_includes(decklist, "Kiki-Jiki", "Chord of Calling"):
		return "Kiki Chord"

	if "Lord of Atlantis" in decklist:
		return "Merfolk"

	if deck_includes(decklist, "Saheeli Rai", "Felidar Guardian"):
		return "CopyCat"

	if deck_includes(decklist, "Griselbrand", "Nourishing Shoal"):
		return "Grishoalbrand"

	if deck_includes(decklist, "The Rack", "Shrieking Affliction"):
		return "8Rack"

	if deck_includes(decklist, "Bitterblossom", "Spellstutter Sprite"):
		return "Faeries"

	if deck_includes(decklist, "Tribal Flames", "Wild Nacatl"):
		return "Tribal Zoo"

	if deck_includes(decklist, "Soul Warden", "Soul's Attendant"):
		return "Soul Sisters"

	if deck_includes(decklist, "Ramunap Ruins"):
		return "Sligh"

	if "Tezzeret, Agent of Bolas" in decklist:
		return "Tezzerator"

	if "Delver of Secrets" in decklist:
		return "Delver"

	if "Archive Trap" in decklist:
		return "Mill"

	if deck_includes(decklist, "Narnam Renegade", "Reckless Bushwhacker"):
		return "Bushwhacker Zoo"

	if "Skred" in decklist:
		return "Skred Red"

	if "Smallpox" in decklist:
		return "Smallpox"

	if deck_includes(decklist, "Martyr of Sands", "Proclamation of Rebirth"):
		return "Martyr Proc"

	if deck_includes(decklist, "Intangible Virtue"):
		return "BW Tokens"

	if deck_includes(decklist, "Time Warp"):
		return "Time Walks"

	if deck_includes(decklist, "Primeval Titan", "Through the Breach"):
		return "Titan Breach"

	if deck_includes(decklist, "Relic of Progenitus", "Wasteland Strangler"):
		return "BW Eldrazi"

	if "Goblin Bushwhacker" in decklist:
		return "Goblins"

	if "Jeskai Ascendancy" in decklist:
		return "Jeskai Ascendancy"

	if deck_includes(decklist, "Thought-Knot Seer", "Serum Powder"):
		return "Eldrazi Stompy"

	if deck_includes(decklist, "Hollow One", "Vengevine"):
		return "RG Hollow One"

	return "Other (Rogue)"



if __name__ == '__main__':
	test_folder = sys.argv[1]
		
	for f in os.listdir(test_folder):
		path = os.path.join(test_folder, f)

		with open(path, 'r') as d:
			decklist = d.read()

			print(decklist)
			print(classify_deck(decklist))

		print("=" * 50)	
