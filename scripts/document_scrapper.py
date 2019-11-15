'''
Crawler for  foreverdreaming
'''

from urllib import request, parse
from bs4 import BeautifulSoup
from lemmertizer import lemmatize
from document_indexer import create_script_index


series_name = 'The Good Place'
base_url = 'https://transcripts.foreverdreaming.org/viewforum.php?f=713'
seed_url = 'https://transcripts.foreverdreaming.org'

'''
List up Phase
'''
def get_episode_entries(entry_page_url):
    links = []
    with request.urlopen(entry_page_url) as response:
        html = response.read()
        soup = BeautifulSoup(html, 'html.parser')

        episode_entries = soup.find_all('a', {'class': 'topictitle'})
        links = [{ 'episode': x.getText(), 'url': x['href'][1:] } for x in episode_entries][2:]
    return links

'''
Parse Phase
'''
def get_episode_lines(episode_page_url):
    lines = []
    with request.urlopen(episode_page_url) as response:
        html = response.read()
        soup = BeautifulSoup(html, 'html.parser')

        line_entries = soup.find('div', {'class': 'postbody'}).find_all('p')
        links = [x.getText() for x in line_entries]
    return links

start_idx = 0
while True:
    entry_url = base_url + '&start=' + str(start_idx) 
    links = get_episode_entries(entry_url)
    
    for link in links:
        print(link['episode'])
        lines = get_episode_lines(seed_url+link['url'])
        for idx, line in enumerate(lines):
            sentence = lemmatize(line)
            create_script_index(series_name, link['episode'], entry_url, idx, line, sentence)

    start_idx += 25
    if len(links) < 25:
        break

print(lines)