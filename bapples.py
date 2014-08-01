from selenium import webdriver

from selenium.common.exceptions import NoSuchElementException

from selenium.webdriver.common.keys import Keys

from selenium.webdriver.chrome.options import Options

import sys

import time
#import treehouse
import os

chrome_options = Options()
browser = webdriver.Chrome(chrome_options=chrome_options)
topic = sys.argv[1]
folder_name = sys.argv[2]
course_url = "http://teamtreehouse.com/library/"+folder_name
browser.get(course_url)
contents = browser.find_elements_by_css_selector("h3 .trigger-steps")
print len(contents)
for each in contents:
	dir_name=each.text
	dir_name = dir_name.replace(' ', '-')
	path = os.path.join(os.getcwd(),topic, folder_name,dir_name)
	print path
	if not os.path.exists(path):
		os.makedirs(path)
browser.close()

