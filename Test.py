# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 11:39:37 2019

@author: USCHLAC
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import re
import pandas as pd

from selenium.webdriver.common.action_chains import ActionChains


driver = webdriver.Chrome()

url = "https://www.espn.com/nfl/scoreboard"
#url = "https://www.espn.com/nfl/scoreboard/_/year/2019/seasontype/1/week/2"

#Original
driver.get(url)
action = ActionChains(driver)


game_week_dict = {"Hall of Fame" : '//*[@id="scoreboard-page"]/div[2]/div[2]/ul/li[1]/a',
                  "Preseason Week 1" : '//*[@id="scoreboard-page"]/div[2]/div[2]/ul/li[2]/a',
                  "Preseason Week 2" : '//*[@id="scoreboard-page"]/div[2]/div[2]/ul/li[3]/a',
                  "Preseason Week 3" : '//*[@id="scoreboard-page"]/div[2]/div[2]/ul/li[4]/a',
                  "Preseason Week 4" : '//*[@id="scoreboard-page"]/div[2]/div[2]/ul/li[5]/a',
                  "Week 1" : '//*[@id="scoreboard-page"]/div[2]/div[2]/ul/li[6]/a',
                  "Week 2" : '//*[@id="scoreboard-page"]/div[2]/div[2]/ul/li[7]/a',
                  "Week 3" : '//*[@id="scoreboard-page"]/div[2]/div[2]/ul/li[8]/a',
                  "Week 4" : '//*[@id="scoreboard-page"]/div[2]/div[2]/ul/li[9]/a',
                  "Week 5" : '//*[@id="scoreboard-page"]/div[2]/div[2]/ul/li[10]/a',
                  "Week 6" : '//*[@id="scoreboard-page"]/div[2]/div[2]/ul/li[11]/a',
                  "Week 7" : '//*[@id="scoreboard-page"]/div[2]/div[2]/ul/li[12]/a',
                  "Week 8" : '//*[@id="scoreboard-page"]/div[2]/div[2]/ul/li[13]/a',
                  "Week 9" : '//*[@id="scoreboard-page"]/div[2]/div[2]/ul/li[14]/a',
                  "Week 10" : '//*[@id="scoreboard-page"]/div[2]/div[2]/ul/li[15]/a',
                  "Week 11" : '//*[@id="scoreboard-page"]/div[2]/div[2]/ul/li[16]/a',
                  "Week 12" : '//*[@id="scoreboard-page"]/div[2]/div[2]/ul/li[17]/a',
                  "Week 13" : '//*[@id="scoreboard-page"]/div[2]/div[2]/ul/li[18]/a',
                  "Week 14" : '//*[@id="scoreboard-page"]/div[2]/div[2]/ul/li[19]/a',
                  "Week 15" : '//*[@id="scoreboard-page"]/div[2]/div[2]/ul/li[20]/a',
                  "Week 16" : '//*[@id="scoreboard-page"]/div[2]/div[2]/ul/li[21]/a',
                  "Week 17" : '//*[@id="scoreboard-page"]/div[2]/div[2]/ul/li[22]/a',
                  "Wild Card" : '//*[@id="scoreboard-page"]/div[2]/div[2]/ul/li[23]/a',
                  "Divisional Round" : '//*[@id="scoreboard-page"]/div[2]/div[2]/ul/li[24]/a',
                  "Conference Championships" : '//*[@id="scoreboard-page"]/div[2]/div[2]/ul/li[25]/a',
                  "Pro Bowl" : '//*[@id="scoreboard-page"]/div[2]/div[2]/ul/li[26]/a',
                  "Super Bowl" : '//*[@id="scoreboard-page"]/div[2]/div[2]/ul/li[27]/a'}




# This selects the game week tab selector:
firstLevelMenu = driver.find_element_by_xpath('//*[@id="scoreboard-page"]/div[2]/div[2]/button')
action.move_to_element(firstLevelMenu).perform()

#Pause:
time.sleep(1)

#Reads from the game dictionary to select which week's games to scrape:
secondLevelMenu = driver.find_element_by_xpath(game_week_dict["Preseason Week 2"])
action.move_to_element(secondLevelMenu).perform()
secondLevelMenu.click()

time.sleep(2)
driver.forward()
time.sleep(2)



#Gets all links:
links = driver.find_elements_by_link_text('PLAY-BY-PLAY')

#Goes into the first Game:
links[0].click()

# Have Driver become syscned to new URL:
driver.forward()
#driver.implicitly_wait(5)
time.sleep(2)

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

    
##Get Plays into a list:
#game_details = []
##Extract Plays:
#a = driver.find_elements_by_class_name('post-play')
#for i in range(0,len(a)):
#    print("Web Element: " + str(i))
#    play = a[i].text
#    print(play)
#    game_details.append(play)



drive_details = []

dr = driver.find_elements_by_class_name("drive-list")
# If there is () it means there was a play.

down_and_distance = []
play_details = []

all_drive_df = pd.DataFrame(columns = ['Play_Description', 'Down_and_Distance'])

for drive in range(0,len(dr)):
#for drive in range(18,19):
    drive_details = dr[drive].text
    drive_details_list = drive_details.split("\n")
    
    #Play Result Info:
    paren = re.compile("\(")
    plays = list(filter(paren.match, drive_details_list))
    play_details.append(plays)
    
    play_count_list = []
    play_count = 0
    play_df = pd.DataFrame(columns = ["Play_Description"])
    play_without_down = []
    
    for play in plays:
        play_count_list.append(play_count)
        play_df = play_df.append({"Play_Description":play}, ignore_index = True)
        
         #Need to Account for Kicks, Timeouts, and Two Minute Warnings:
        if 'kicks' in play:
            play_without_down.append(play_count)
            
        if 'Timeout' in play:
            play_without_down.append(play_count)
            
        if 'Two-Minute Warning' in play:
            play_without_down.append(play_count)
    
        play_count += 1
    
    #Down and Distance Info:
    down = re.compile("^\d\w* & ?\w* ?\d* at ?\w* \d*$")
    downs = list(filter(down.match, drive_details_list))
    down_and_distance.append(downs)
    down_df = pd.DataFrame(columns = ["Down_and_Distance"])
    down_count_list = []
    down_count = 0
    for down in downs:
        down_count_list.append(down_count)
        down_df = down_df.append({"Down_and_Distance":down}, ignore_index = True)
        down_count +=1
         
    # Add in Plays without Down and Distance:
    if len(play_without_down) >= 1:
        for i in play_without_down:
            if play_without_down == [0]:
                down_df.loc[-1] = ["No Distance"]
                down_df.index = down_df.index + 1
                down_df = down_df.sort_index()
                
                
            else:
                down_df.loc[max(down_df.index)+1, :] = None
                down_df[down_df.index >= i] = down_df[down_df.index >= i].shift(1)
                down_df.loc[i] = ["No Distance"]
                down_df = down_df.sort_index()
    
    drive_df = pd.merge(left = play_df, right = down_df, left_on = play_df.index, right_on = down_df.index)
    drive_df = drive_df.drop(columns = ["key_0"])
    drive_df["Drive_Number"] = drive
    all_drive_df = pd.concat([all_drive_df,drive_df])
    

        
        
    








