from selenium import webdriver
import time
from bs4 import BeautifulSoup
import re
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from lxml import etree


driver = webdriver.Chrome(ChromeDriverManager().install())

big_ten_team_names = ["Indiana", "Maryland", "Michigan", "Michigan State", "Ohio State", "Penn State", "Rutgers", "Iowa", "Minnesota", "Nebraska", "Northwestern", "Purdue", "Illinois"]
big_ten_team_codes = [3356765, 3354369, 3358500, 3353539, 3353925, 3600487, 3356153, 3600450, 3630041, 3352093, 3626098, 3626077, 3626117]


rosters_list = []
for code in big_ten_team_codes:
    url= "https://www.ncaa.com/game/" + str(code)
    #driver.maximize_window()
    driver.get(url)

    time.sleep(5)
    content = driver.page_source.encode('utf-8').strip()
    soup = BeautifulSoup(content,"html.parser")
    div = soup.find_all("div", {"class":"boxscore-table"})


    tr_list =[]
    for table in div:
        for tr in table.find_all("tr"):
            tr_list.append(tr)


    tds_list = []
    for container in tr_list:
        tds = container.find_all("td")
        tds_list.append(tds)
        
    list_names = []
    for lst in tds_list:
        if len(lst) == 0:
            continue
        if len(lst) > 0:
            name = lst[1]
            clean_name = name.text.replace('\n', '')
            if clean_name not in list_names:
                if not bool(re.search(r'\d', clean_name)):
                    list_names.append(clean_name)
        
    rosters_list.append(list_names)

team_rosters = dict(zip(big_ten_team_names, rosters_list))
new_dict = {}
for key, value in team_rosters.items():
    for name in value:
        new_dict[name] = key

print(new_dict)

import csv
import itertools
csv_file = "team_rosters.csv"
csv_columns = ["Indiana", "Maryland", "Michigan", "Michigan State", "Ohio State", "Penn State", "Rutgers", "Iowa", "Minnesota", "Nebraska", "Northwestern", "Purdue", "Illinois"]
try:
    # with open(csv_file, "w") as csvfile:
    #     writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
    #     writer.writeheader()
    #     for name in team_rosters.values():
    #         writer.writerow(name)
#separated names 
    # with open(csv_file, "w") as csvfile:
    #     writer = csv.writer(csvfile)
    #     writer.writerow(team_rosters.keys())
    #     writer.writerows(itertools.zip_longest(*team_rosters.values()))

#list of names
    # with open(csv_file, "w") as csvfile:
    #     writer = csv.DictWriter(csvfile, fieldnames=csv_columns)  
    #     writer.writeheader()
    #     writer.writerow(team_rosters)

#name, team name
    with open(csv_file, "w") as csvfile:
        writer = csv.writer(csvfile)
        for key, value in new_dict.items():
            writer.writerow([key, value])

except IOError:
    print("error")