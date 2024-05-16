import requests
import json
from bs4 import BeautifulSoup

def get_lodestone_url(player_id) -> str:
    return 'https://na.finalfantasyxiv.com/lodestone/character/' + player_id + '/'

def get_player_classes(lodestone_url) -> list[str]:
    response = requests.get(lodestone_url)
    soup = BeautifulSoup(response.text, 'html.parser')

    character_level_lists = soup.find_all('div', class_ = 'character__level__list')

    job_dict = {}

    for level_list in character_level_lists:
        for div in level_list.find_all('li'):
            job_name = div.find('img', class_ = 'js__tooltip')['data-tooltip']
            job_level = div.text

            if(job_level == '-'):
                job_level = 0

            job_dict[job_name] = job_level
    
    return job_dict