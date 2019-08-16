# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 11:39:37 2019

@author: USCHLAC
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select


driver = webdriver.Chrome()

url = "https://www.espn.com/nfl/scoreboard"
#url = "https://www.espn.com/nfl/scoreboard/_/year/2019/seasontype/1/week/2"

#Original
driver.get(url)



action = ActionChains(driver)

# Trying to Select Certain Week's Game Data:
firstLevelMenu =driver.find_element_by_xpath('//*[@id="scoreboard-page"]/div[2]/div[2]/button')
action.move_to_element(firstLevelMenu).perform()


#Need to Grab All X_Path for Weeks:
secondLevelMenu = driver.find_element_by_xpath('//*[@id="scoreboard-page"]/div[2]/div[2]/ul/li[7]/a')
action.move_to_element(secondLevelMenu).perform()
secondLevelMenu.click()











#
#
#
#
#
#
#
#
##Need to get game week as a string:
##Enter Code:
#
##Gets all links:
#links = driver.find_elements_by_link_text('PLAY-BY-PLAY')
#
##Goes into the first Game:
#links[0].click()
#
## Have Driver become syscned to new URL:
#driver.forward()
##driver.implicitly_wait(5)
#time.sleep(1)
#
##Find all dropdown arrows on the page:
#arrows = driver.find_elements_by_class_name('accordion-item')
#
#
##Game Location and Teams:
#teams = driver.find_elements_by_class_name('team-name')
#away_team_city_abb = teams[1].text
#away_team_nickname = teams[0].text
#home_team_city_abb = teams[2].text
#home_team_nickname = teams[3].text
#game_detail_string = away_team_city_abb + " " + away_team_nickname + " at " + home_team_city_abb + " " + home_team_nickname
#
#
##Open All Dropdown Arrows:
#for i in range(0,len(arrows)):
#    arrows[i].click()
#    # Need in order to open all arrows:
#    time.sleep(1)
#
#    
##Get Plays into a list:
#game_details = []
##Extract Plays:
#a = driver.find_elements_by_class_name('post-play')
#for i in range(0,len(a)):
#    print("Web Element: " + str(i))
#    play = a[i].text
#    print(play)
#    game_details.append(play)
#    
#
#game_details.insert(0,game_detail_string)







