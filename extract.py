import urllib2
import os
import sys

#request = urllib2.Request(url)

#handle = urllib2.urlopen(request)

#content = handle.read()

#.contained secondary <li> <a class="button-reveal" title="Download" 
#href="/library/css-foundations/media-queries/media-features-and-media-types-2/download">
#</li>
#/library/build-a-simple-php-application/getting-started-with-php/previewing-the-final-project/download">


def download(download_link, folder_name):
	"""
	documentation and example for test 
	"""
	video_file = urllib2.urlopen(download_link)
	video_content = video_file.read()
	if not os.path.exists(folder_name):
		os.makedirs(folder_name)

	filehandler = open(os.path.join(os.getcwd(),folder_name, "test.mp4"),"w") # write in file test.mp4 in write mode 
	filehandler.write(video_content)
download("http://teamtreehouse.com/library/javascript-foundations/variables/basics/download","pepsi")

	# your code goes here
	# it saves the file in a directory
	
