
import os
from classifier import classify_deck
import pandas as pd
import numpy as np
from dateutil.parser import parse

def get_player_deck_name(player_name, deck_folder):
    for f in os.listdir(deck_folder):
        if f.endswith('.txt') and f.split('-', 1)[1] == player_name + '.txt':
            path = os.path.join(deck_folder, f)
            with open(path, 'r') as deck:
                decklist = deck.read()
                return classify_deck(decklist)

def main():
	challenge_path = './challenge_lists'
	all_records = []

	for challenge in os.listdir(challenge_path):
		
		df = pd.read_csv(os.path.join(challenge_path, challenge, 'top8bracket.csv'))
		for match in df.to_dict('records'):
			match['Winning deck'] = get_player_deck_name(match['Winner'], os.path.join(challenge_path, challenge))
			match['Losing deck'] = get_player_deck_name(match['Loser'], os.path.join(challenge_path, challenge))
			match['Date'] = challenge

			all_records.append(match)

	df = pd.DataFrame(all_records)
	df = df[['Date','Round','Winner','Winning deck','Loser','Losing deck']]
	print(df.info())
	df.to_csv('legacy_top_8.csv')

if __name__ == '__main__':
	main()
