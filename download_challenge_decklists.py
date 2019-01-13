from datetime import datetime, timedelta
from dateutil.parser import parse
import sys
from web_scraper import download_mothership_decklists
import time

"""
Example call: python download_challenge_decklists.py 2018-5-14
"""

def main(start_date, first_date, dest_dir):
	start_date = parse(start_date) #start date must be a valid Legacy Challenge date (Monday)
	first_date = parse(first_date)

	curdate = start_date

	i = 0
	while curdate >= first_date:
		print("Downloading Modern Challenge decklists from {}".format(curdate.date()))

		dest_folder = '{}/{}'.format(dest_dir, curdate.date())
		event_url = "https://magic.wizards.com/en/articles/archive/mtgo-standings/legacy-challenge-{}".format(curdate.date())

		
		download_mothership_decklists(event_url, dest_folder)

		print("Sleeping 2 seconds")
		time.sleep(2)

		curdate += timedelta(days=-1)
		i += 1

if __name__ == '__main__':
	main(*sys.argv[1:])

