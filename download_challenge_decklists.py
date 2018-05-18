from datetime import datetime, timedelta
from dateutil.parser import parse
import sys
from web_scraper import download_mothership_decklists
import time

"""
Example call: python download_challenge_decklists.py 2018-5-14
"""

def main():
	start_date = parse(sys.argv[1]) #start date must be a valid Legacy Challenge date (Monday)

	curdate = start_date

	i = 0
	while curdate > parse('2017-5-11'):
		print("Downloading Legacy Challenge decklists from {}".format(curdate.date()))

		dest_folder = './challenge_lists/{}'.format(curdate.date())
		event_url = "https://magic.wizards.com/en/articles/archive/mtgo-standings/legacy-challenge-{}".format(curdate.date())

		try:
			download_mothership_decklists(event_url, dest_folder)
		except AttributeError:
			print("Couldn't find challenge data for this date")

		print("Sleeping 2 seconds")
		time.sleep(2)

		curdate += timedelta(days=-7)
		i += 1

if __name__ == '__main__':
	main()

