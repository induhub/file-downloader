from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import os
from time import sleep

chrome_options = Options()
chrome_options.add_argument("--incognito")
browser = webdriver.Chrome(chrome_options=chrome_options)

# aao login karein
browser.get("the url/") # Load page
browser.find_element_by_id("featurette-1").click()
username = ""#username
password = ""#password
sleep(2)

username_input = browser.find_element_by_id("user_session_email") # Find the query box

username_input.send_keys(username)


password_input = browser.find_element_by_id("user_session_password") # Find the query box

password_input.send_keys(password)

submit_button = browser.find_elements_by_xpath("//*[@type='submit']")[0]

submit_button.click()
# login ho gaya

topics = [" "," "," "]# topics
jumbo_file = open('downloads.txt', 'w')

for topic in topics:
	print 'processing topic =>', topic
	browser.get("the url"+topic)

	courses = browser.find_elements_by_css_selector(".title")
	
	for index, each_a_tag in enumerate(courses): 
		print 'processing topic ', topic, 'for item index ', index
		browser.get("the url:"+topic)
		courses = browser.find_elements_by_css_selector(".title")
		next_url = courses[index].get_attribute("href")
		print next_url		
		browser.get(next_url)
		sleep(5)
		# get the list of download links
		items = browser.find_elements_by_css_selector(".achievement-steps ul li a")		
		print 'items=>', len(items)
		for index, each in enumerate(items):
			href = each.get_attribute("href")
			url = href+'/download'
			print url			
			jumbo_file.write('\n'+url)
	
		
		
browser.close()





