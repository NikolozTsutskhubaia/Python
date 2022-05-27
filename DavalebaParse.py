import requests
from bs4 import BeautifulSoup
import csv

file = open('Players.csv', 'w', encoding='utf-8_sig', newline='\n')
f_obj = csv.writer(file)
f_obj.writerow(['Name'])

url = 'https://www.nba.com/75/team'
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')
sub_soup = soup.find('div', class_='flex flex-wrap text-left border-l')
top75_players = sub_soup.find_all('li', class_='List_player__3lt4L')

for each in top75_players:
    Players = each.find('a',class_='Anchor_complexLink__2NtkO')
    f_obj.writerow([Players])
    print(Players)

