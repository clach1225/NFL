# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 11:39:37 2019

@author: USCHLAC
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome()

url = "https://www.espn.com/nfl/scoreboard"
driver.get(url)

#Need to get game week as a string:
#Enter Code:

#Gets all links:
links = driver.find_elements_by_link_text('PLAY-BY-PLAY')

#Goes into the first Game:
links[0].click()

# Have Driver become syscned to new URL:
driver.forward()
#driver.implicitly_wait(5)
time.sleep(1)

#Find all dropdown arrows on the page:
arrows = driver.find_elements_by_class_name('accordion-item')


#Game Location and Teams:
teams = driver.find_elements_by_class_name('team-name')
away_team_city_abb = teams[1].text
away_team_nickname = teams[0].text
home_team_city_abb = teams[2].text
home_team_nickname = teams[3].text
game_detail_string = away_team_city_abb + " " + away_team_nickname + " at " + home_team_city_abb + " " + home_team_nickname


#Open All Dropdown Arrows:
for i in range(0,len(arrows)):
    arrows[i].click()
    # Need in order to open all arrows:
    time.sleep(1)

    
#Get Plays into a list:
game_details = []
#Extract Plays:
a = driver.find_elements_by_class_name('post-play')
for i in range(0,len(a)):
    print("Web Element: " + str(i))
    play = a[i].text
    print(play)
    game_details.append(play)
    

game_details.insert(0,game_detail_string)







