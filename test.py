# python script to batch add emoji to slack.
# USAGE
# requires chromedriver (brew install chromedriver) and selenium
# see LINK TO GITHUB for more info.
import getpass
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import sys


# Get user input
slack_team_name = raw_input("Slack team name: ")
img_path = raw_input("Path to image directory: ")
email = raw_input("Email address: ")
# Get slack password safely using getpass
# https://docs.python.org/2/library/getpass.html
password = getpass.getpass('Slack Password:')

# open the browser and get the page
driver = webdriver.Chrome()
driver.get("https://%s.slack.com/emoji" % slack_team_name)
# login
elem = driver.find_element_by_id("email")
elem.send_keys(email)
elem = driver.find_element_by_id("password")
elem.send_keys(password)
elem.send_keys(Keys.RETURN)

# go to emoji page
# driver.get("https://%s.slack.com/emoji" % sys.argv[1])

# loop and upload the images in user given path
for filename in os.listdir(img_path):
    if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
        # put in file name
        elem = driver.find_element_by_id('emojiname')
        elem.send_keys(filename.split('.')[0])
        # put in path to file
        elem = driver.find_element_by_id('emojiimg')
        path = os.getcwd() + '/' + img_path + '/' + filename
        print path
        elem.send_keys(path)
        # submit the form
        driver.find_element_by_xpath("//input[@type='submit' and @value='Save New Emoji']").click()


#driver.close()
