#!/usr/bin/python3

# import statements for the script to work
import sys
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# local variables that are set to take in info by the bash program called
project = sys.argv[1]
pub_priv = sys.argv[2]


# sets username and password from enviroment variables
user = 'DavidLBallard'
pwd = 'HardWork88DLB'

# sets the chromedriver
CHROMEDRIVER = '/home/david/projects/python/AutomatingProjects/chromedriver'
# initalizes the driver and sets the webpage
driver = webdriver.Chrome(CHROMEDRIVER)
driver.get('https://github.com/login')

# navigates to the username and password elements and enters the info and clicks
# login button
navigate = driver.find_elements_by_xpath("//input[@name='login']")[0]
navigate.clear()
navigate.send_keys(user)
navigate = driver.find_elements_by_xpath("//input[@name='password']")[0]
navigate.clear()
navigate.send_keys(pwd)
navigate = driver.find_elements_by_xpath("//input[@name='commit']")[0]
navigate.click()

# navigates to the new repository page on github and enters in the name based
# on the user input
driver.get('https://github.com/new')
navigate = driver.find_elements_by_xpath("//input[@name='repository[name]']")[0]
navigate.send_keys(project)

#d etermines to make repository public or private
if pub_priv == 'public':
    driver.find_element_by_id("repository_visibility_public").click()
else:
    driver.find_element_by_id("repository_visibility_private").click()

# initalizes an initial commit
driver.find_element_by_id("repository_auto_init").click()
#s leeps program to make sure that the create repository button is active
time.sleep(1)
# navigate to the create repository button and clicks it
navigate = driver.find_elements_by_xpath('//*[@id="new_repository"]/div[3]/button')[0]
navigate.click()

driver.quit()
