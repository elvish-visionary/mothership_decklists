
import os
from classifier_post_drs import classify_deck
import pandas as pd
import numpy as np
from dateutil.parser import parse

challenge_deck_path = './challenge_lists_2018_legacy_postban'

raw_results_file = 'processed_results/raw_legacy_challenge_postban_results.csv'
player_rankings_file = 'processed_results/legacy_challenge_postban_player_rankings.csv'
deck_file = 'processed_results/legacy_challenge_postban_rankings.csv'

records = {
	'Player': [],
	'Deck': [],
	'Placement': [],
	'Top 8': [],
	'DRS': [],
	'Brainstorm': [],
	'Chalice': [],
	'Date': []
}

i = 0

for challenge_dir in os.listdir(challenge_deck_path):

	# if parse(challenge_dir) <= parse('2018-2-14'):
	# 	print("Skipping pre-unban challenge on {}".format(challenge_dir))
	# 	continue

	print("Challenge on {}".format(challenge_dir))
	
	for f in os.listdir(os.path.join(challenge_deck_path, challenge_dir)):

		if f.endswith('.csv'):
			continue
		place = f.split('-', 1)[0]
		place = int(place)

		player_name = f.split('-',1)[1].split('.txt')[0]

		decklist_file = os.path.join(challenge_deck_path, challenge_dir, f)

		with open(decklist_file, 'r') as deck:
			decklist = deck.read()
			deck_name = classify_deck(decklist)

		if "Other (Rogue)" in deck_name:
			i += 1
			print("{} got {} place with {}".format(player_name, place, deck_name))
			print(decklist)

		if place <= 8:
			records['Top 8'].append(1)
		else:
			records['Top 8'].append(0)

		records['Player'].append(player_name)
		records['Deck'].append(deck_name)
		records['Placement'].append(place)
		records['Date'].append(challenge_dir)

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

print("{} rogue decks found".format(i))



records = pd.DataFrame(records)
records.to_csv(raw_results_file, index=False)

by_player = records.groupby('Player').agg({'Top 8': ['count', 'sum'],
																 'Deck': lambda x: ', '.join(list(set(x)))}).reset_index()

by_player.columns = by_player.columns.droplevel()

by_player.rename(columns={'count': 'Top 32', 'sum': 'Top 8', '<lambda>': 'Decks used'}, inplace=True)

by_player.sort_values(['Top 8','Top 32'], ascending=False).to_csv(player_rankings_file, index=False)

bydeck = records.groupby('Deck').agg({'Top 8': ['count', 'sum']}).reset_index()

bydeck.columns = bydeck.columns.droplevel()

bydeck.rename(columns={'count': 'Top 32', 'sum': 'Top 8'}, inplace=True)

bydeck['Top 32 %'] = bydeck['Top 32'] / bydeck['Top 32'].sum()
bydeck['Top 8 %'] = bydeck['Top 8'] / bydeck['Top 8'].sum()

n = bydeck['Top 32']

p =  bydeck['Top 8'] / bydeck['Top 32']

CI_lower = p - 1.96 * np.sqrt(p * (1 - p) / bydeck['Top 32'])
CI_upper = p + 1.96 * np.sqrt(p * (1 - p) / bydeck['Top 32'])

bydeck['Conversion Rate'] = p
bydeck['CI_lower'] = CI_lower
bydeck['CI_upper'] = CI_upper

bydeck.sort_values(['Top 8','Top 32'], ascending=False).to_csv(deck_file, index=False)