from selenium import webdriver
import time
from bs4 import BeautifulSoup
import re
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from find_games import game_links

driver = webdriver.Chrome(ChromeDriverManager().install())

for link in game_links:

    url= "https://www.ncaa.com/" + link + "/play-by-play"
    # driver.maximize_window()
    driver.get(url)

    time.sleep(5)
    content = driver.page_source.encode('utf-8').strip()
    soup = BeautifulSoup(content,"html.parser")
    descriptions = soup.findAll("td",{"class":"description"})
    # print(descriptions)

    game = []
    for div in soup.find_all("tr"):
        team = div.find("td",{"class":"team"})
        play = div.find("td",{"class":"description"})
        if team == None:
            continue
        else:
            img = team.find('img',alt=True)
            team_name = img["alt"]
            team_play = play.text
            x = team_name + ";" + team_play
            game.append(x)

    # print(game)
    file_name = (link.split("/"))[-1]
    print(file_name)
    import csv
    with open(r'C:\\Users\saman\Desktop\\Independent Study\Softball Project\\' + file_name + '.csv', 'w') as file:
        writer = csv.writer(file)
        for play in game:
            writer.writerow([play])
 