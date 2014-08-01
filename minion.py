from selenium import webdriver

from selenium.common.exceptions import NoSuchElementException

from selenium.webdriver.common.keys import Keys

from selenium.webdriver.chrome.options import Options

import sys

import time
#import treehouse
import os
#print treehouse.funky()
import subprocess

username = sys.argv[1]

password = sys.argv[2]

topic = sys.argv[3]


chrome_options = Options()

#chrome_options.add_argument("--incognito")

browser = webdriver.Chrome(chrome_options=chrome_options)

"""
browser.get("http://teamtreehouse.com/") # Load page
browser.find_element_by_id("featurette-1").click()

time.sleep(2)

username_input = browser.find_element_by_id("user_session_email") # Find the query box

username_input.send_keys(username)


password_input = browser.find_element_by_id("user_session_password") # Find the query box

password_input.send_keys(password)

submit_button = browser.find_elements_by_xpath("//*[@type='submit']")[0]

submit_button.click()
"""
#time.sleep(2)
browser.get("http://teamtreehouse.com/tracks")

#time.sleep(2)
browser.get("http://teamtreehouse.com/library")
#time.sleep(2)

#selenium.isElementPresent("css=a[data-filter-value]:contains('2')@")

# Makes topic directories
'''
topics = browser.find_elements_by_css_selector("#topic li a")
for each_a_tag in topics[1:]: # each_a_tag ka naam kuch bhi ho sakta hai. its a variable name. x, y , z, kuch bhi chalega
	folder_name = each_a_tag.get_attribute("data-filter-value")
	if not os.path.exists(folder_name):
		os.makedirs(folder_name)
	
'''	


	


if not os.path.exists(topic):
		os.makedirs(topic)

topic_url = "http://teamtreehouse.com/library/topic:"+topic
browser.get(topic_url)

# Makes course/workshop directories
courses = browser.find_elements_by_css_selector(".title")
for each_a_tag in courses: 
# each_a_tag ka naam kuch bhi ho sakta hai. its a variable name. x, y , z, kuch bhi chalega
	folder_name = each_a_tag.get_attribute("href").replace("http://teamtreehouse.com/library/","")
	if not os.path.exists(os.path.join(os.getcwd(),topic,folder_name)):
		os.makedirs(os.path.join(os.getcwd(),topic,folder_name))
		print folder_name
	#course_url = "http://teamtreehouse.com/library/"+folder_name
	subprocess.Popen(['python','bapples.py',topic, folder_name])
	#browser.get(course_url)
	#print len(course_url)
	time.sleep(5)

""" 
contents = browser.find_elements_by_css_selector(".trigger-steps toggle-steps")
print len(contents)

for each_content in contents:
	if not os.path.exists(os.path.join(os.getcwd(),folder_name,each_content)):
		os.makedirs(os.path.join(os.getcwd(),topic,folder_name,each_content))
		print 

time.sleep(5)

"""

browser.close()

