from urllib.request import urlopen
from bs4 import BeautifulSoup
import os
import time


def download_decklist_from_page(url, filepath):

    # to make sure we don't load too many pages, we'll wait before downloading the decklist
    for i in range(3):
        print('.', end=' ')
        time.sleep(1)

    page = urlopen(url)

    soup = BeautifulSoup(page, 'html.parser')

    # find link to direct download of MTGO text file
    for link in soup.find_all('a'):
        if 'MTGO' in link:

            href = link.get('href')
            href = 'http://mtgtop8.com/' + href
            print("downloading " + href)

            # write to file
            f = urlopen(href)
            with open(filepath, "wb") as local_file:
                local_file.write(f.read())


def get_lists_from_mtgtop8_event(event_url):

    page = urlopen(event_url)
    soup = BeautifulSoup(page, 'html.parser')

    # find the event name and name the download directory after it
    event_name = ''
    for div in soup.find_all('div', class_='w_title'):
        for td in div.find_all('td', class_ = 'S18'):
            event_name = td.string

    lists_path = './decklists/%s' % event_name
    if not os.path.isdir(lists_path):
        os.makedirs(lists_path)

    print("Downloading decklists for ", event_name)

    # print soup.prettify()

    # look for links to the decklists
    # searching by text size (I think that's what "s14" means) is a really dumb way to do it, but I'm not sure how else
    # to identify the links to lists

    i = 1 #used to add a placement # to each deck name
    for div in soup.find_all('div', class_=["S14", "W14"]):
        for link in div.find_all('a'):
            print("=" * 50)
            deck_url = 'http://mtgtop8.com/event' + link.get('href')

            # follow link to download the list
            print("Downloading decklist for %s at %s" % (link.string, deck_url))
            download_decklist_from_page(deck_url, '%s/%s_%s .txt' % (lists_path, i, link.string))
        i = i + 1

def download_mothership_decklists(event_url, destination_folder, verbose=False):

    page = urlopen(event_url)
    soup = BeautifulSoup(page, 'html.parser')

    decklists = soup.find('div', class_='decklists')

    try:
        deck_sections = decklists.find_all('div', class_="deck-group")
    except AttributeError:
        print("Couldn't find data for this date")
        return

    if not os.path.isdir(destination_folder):
        os.makedirs(destination_folder)
    
    for i, deck in enumerate(deck_sections):

        #player_name = deck.get('id').upper().split('_TH_PLACE')[0].split('_ND_PLACE')[0].split('_ST_PLACE')[0].split('_RD_PLACE')[0]
        player_name = deck.find('h4').string.split(' (')[0]

        print("{} place: ".format(i+1), player_name.upper())

        with open(os.path.join(destination_folder, '{}-{}.txt'.format(i+1, player_name)), 'w') as f:
            decklist = deck.find('div', class_='deck-list-text').find('div', class_='sorted-by-overview-container sortedContainer')
            cards = decklist.find_all('span', class_="card-name")
            quants = decklist.find_all('span', class_="card-count")
            card_count = 0
            for quant, card in zip(quants, cards):
                if verbose:
                    print(quant.string, card.string)
                f.write("{} {}\n".format(quant.string, card.string))
                card_count += int(quant.string)
            print("Total maindeck cards: ", card_count)
        print('-' * 50)

    # record top 8 information if available

    brackets = {'Quarterfinals': 'bracket quarterfinals first',
                'Semifinals': 'bracket semifinals ',
                            'Finals': 'bracket finals '}

    with open(os.path.join(destination_folder, 'top8bracket.csv'), 'w') as f:
        f.write('Winner,Loser,Round\n')
        for bround, tag in brackets.items():
            print(bround)
            qf = soup.find('div', class_=tag)
            for match in qf.find_all('div', class_='dual-players'):
                winner = match.find('strong').string.split(') ')[1].split(',')[0]
                loser = match.find_all('p')[1].string.split(') ')[1].rstrip()
                print("{} beat {}".format(winner, loser))
                f.write("{},{},{}\n".format(winner,loser,bround))



if __name__ == '__main__':

    event_url = 'https://magic.wizards.com/en/articles/archive/mtgo-standings/legacy-challenge-2017-09-18'
    download_mothership_decklists(event_url, './test_decklists/9-18')