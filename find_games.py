from selenium import webdriver
import time
from bs4 import BeautifulSoup
import re
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

months = ["02","03","04","05","06"]
days1 = ["01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31"]
days2 = ["01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30"]
days3 = ["01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28"]
game_links = []
for month in months:
    if month == "02":
        for day in days3:
            url = "https://www.ncaa.com/scoreboard/softball/d1/2019/" + month + "/" + day + "/big-ten"
            # driver.maximize_window()
            driver.get(url)

            time.sleep(5)
            content = driver.page_source.encode('utf-8').strip()
            soup = BeautifulSoup(content,"html.parser")
            for div in soup.findAll('div',{'class': 'gamePod_content'}):
                for link in div.find_all("a", {"class": "gamePod-link"}):
                    try:
                        game_links.append(link["href"])
                    except KeyError:
                        pass
    if month == "03":
        for day in days1:
            url = "https://www.ncaa.com/scoreboard/softball/d1/2019/" + month + "/" + day + "/big-ten"
            # driver.maximize_window()
            driver.get(url)

            time.sleep(5)
            content = driver.page_source.encode('utf-8').strip()
            soup = BeautifulSoup(content,"html.parser")
            for div in soup.findAll('div',{'class': 'gamePod_content'}):
                for link in div.find_all("a", {"class": "gamePod-link"}):
                    try:
                        game_links.append(link["href"])
                    except KeyError:
                        pass
    if month == "04":
        for day in days2:
            url = "https://www.ncaa.com/scoreboard/softball/d1/2019/" + month + "/" + day + "/big-ten"
            # driver.maximize_window()
            driver.get(url)

            time.sleep(5)
            content = driver.page_source.encode('utf-8').strip()
            soup = BeautifulSoup(content,"html.parser")

            for div in soup.findAll('div',{'class': 'gamePod_content'}):
                for link in div.find_all("a", {"class": "gamePod-link"}):
                    try:
                        game_links.append(link["href"])
                    except KeyError:
                        pass
    if month == "05":
        for day in days1:
            url = "https://www.ncaa.com/scoreboard/softball/d1/2019/" + month + "/" + day + "/big-ten"
            # driver.maximize_window()
            driver.get(url)

            time.sleep(5)
            content = driver.page_source.encode('utf-8').strip()
            soup = BeautifulSoup(content,"html.parser")
            for div in soup.findAll('div',{'class': 'gamePod_content'}):
                for link in div.find_all("a", {"class": "gamePod-link"}):
                    try:
                        game_links.append(link["href"])
                    except KeyError:
                        pass
    if month == "06":
        for day in days2:
            url = "https://www.ncaa.com/scoreboard/softball/d1/2019/" + month + "/" + day + "/big-ten"
            # driver.maximize_window()
            driver.get(url)

            time.sleep(5)
            content = driver.page_source.encode('utf-8').strip()
            soup = BeautifulSoup(content,"html.parser")
            for div in soup.findAll('div',{'class': 'gamePod_content'}):
                for link in div.find_all("a", {"class": "gamePod-link"}):
                    try:
                        game_links.append(link["href"])
                    except KeyError:
                        pass
    





# url = "https://www.ncaa.com/scoreboard/softball/d1/2019/03/22/big-ten"
# driver.maximize_window()
# driver.get(url)

# time.sleep(5)
# content = driver.page_source.encode('utf-8').strip()
# soup = BeautifulSoup(content,"html.parser")


# game_links = []
# for div in soup.findAll('div',{'class': 'gamePod_content'}):
#     for link in div.find_all("a", {"class": "gamePod-link"}):
#         try:
#             game_links.append(link["href"])
#         except KeyError:
#             pass

# for game in game_links:
#     url = "https://www.ncaa.com" + game + "/play-by-play"
#     driver.maximize_window()
#     driver.get(url)

#     time.sleep(5)
#     content = driver.page_source.encode('utf-8').strip()
#     soup = BeautifulSoup(content,"html.parser")

print("GameLinks:")
print(game_links)