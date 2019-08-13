# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 11:39:37 2019

@author: USCHLAC
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


driver = webdriver.Chrome()


url = "https://www.espn.com/nfl/scoreboard"
driver.get(url)

# Gets first Link:
#link = driver.find_element_by_link_text('PLAY-BY-PLAY')


#Gets all links:
#links = driver.find_elements_by_link_text('PLAY-BY-PLAY')

#Goes into the first Game:
#links[0].click()


driver.find_element_by_link_text('PLAY-BY-PLAY').click()
driver.forward()

driver.find_element_by_link_text('NBA').click()



