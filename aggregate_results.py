
import os
from classifier import classify_deck
import pandas as pd

challenge_deck_path = './challenge_lists'

records = {
	'Player': [],
	'Deck': [],
	'Placement': [],
	'Top 8': [],
	'DRS': [],
	'Brainstorm': [],
	'Chalice': []
}

i = 0
for challenge_dir in os.listdir(challenge_deck_path):
	print("Legacy Challenge on {}".format(challenge_dir))
	i += 1
	for f in os.listdir(os.path.join(challenge_deck_path, challenge_dir)):
		place = f.split('-', 1)[0]
		place = int(place)

		player_name = f.split('-',1)[1].split('.txt')[0]

		decklist_file = os.path.join(challenge_deck_path, challenge_dir, f)

		with open(decklist_file, 'r') as deck:
			decklist = deck.read()
			deck_name = classify_deck(decklist)

		if place <= 8:
			print("{} got {} place with {}".format(player_name, place, deck_name))
			records['Top 8'].append(1)
		else:
			records['Top 8'].append(0)

		records['Player'].append(player_name)
		records['Deck'].append(deck_name)
		records['Placement'].append(place)

		if "Deathrite Shaman" in decklist:
			records['DRS'].append(1)
		else:
			records['DRS'].append(0)

		if "Brainstorm" in decklist:
			records['Brainstorm'].append(1)
		else:
			records['Brainstorm'].append(0)

		if "Chalice of the Void" in decklist:
			records['Chalice'].append(1)
		else:
			records['Chalice'].append(0)
	print("=" * 50)

print("Data for {} challenges found".format(i))

records = pd.DataFrame(records)
records.to_csv('aggregate_challenge_results.csv', index=False)