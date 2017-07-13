import multiprocessing
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
import csv
import os 
import time
from datetime import datetime
import codecs
from bs4 import BeautifulSoup
import sys
#reload(sys)
#sys.setdefaultencoding('utf-8')


currentTime = " " + str(datetime.now()).replace("-", " ").replace(":", " ").replace(".", " ")
start_time = time.time()
row_counter = 0 


allSiteMaps = "http://appsitemap.forexpros.com/tmp/xml/ru/sitemap.xml"
#allSiteMaps = "https://www.utab.com/sitemap/sitemapindex.xml"

def csv_writer(write_this, file_name):
	header = ['Crawled URL', 'Status Code', 'Redirects', 'Comments']
	global row_counter, currentTime
	if row_counter >= 25000:
		currentTime = " " + str(datetime.now()).replace("-", " ").replace(":", " ").replace(".", " ")	
		row_counter = 0
	try:
		with open(file_name + currentTime + '.csv') as f:
			f.close()
		with open(file_name + currentTime + '.csv', 'ab') as f:
			writer = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_NONE)
			try:
				writer.writerow(write_this)
			except:
				print "Something went wrong. Here's the link: "
				print write_this
			f.close()
	except: # When you creat a file for the 1st time:
		with open(file_name + currentTime + '.csv', 'ab') as f:
			writer = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_NONE)
			try:
				writer.writerow(header)
				writer.writerow(write_this)
			except:
				print "Something went wrong. Here's the link: "
				print write_this
			f.close()
	row_counter += 1

#------------------------------------------------------------------------------------------------------
#     TEMPORARY %% TEMPORARY %% TEMPORARY %% TEMPORARY %% TEMPORARY %% TEMPORARY %% TEMPORARY %%
#------------------------------------------------------------------------------------------------------
def tempSiteMap_urlConverter(url):
	dashIndex = url.rfind("-")
	temp_storageLocation = "http://appsitemap.forexpros.com/tmp/xml/ru/maps/sitemap"
	return temp_storageLocation + url[dashIndex:len(url) - 3]	

def temp_url_Retrieval(url):
	time.sleep(1.7)
	response = requests.get(url, timeout = 20.0)
	statusCode = response.status_code
	urlList = []
	soup = BeautifulSoup(response.content, "html5lib", from_encoding="utf-8")
	

	for a in soup.findAll("loc"):
		a = str(a)
		a = a[5:-6]
		urlList.append(tempSiteMap_urlConverter(a))
	return urlList	

#------------------------------------------------------------------------------------------------------
#######################################################################################################
#------------------------------------------------------------------------------------------------------
def url_Retrieval(url):
	url = url
	time.sleep(1.7)
	response = requests.get(url, timeout = 20.0)
	statusCode = response.status_code
	urlList = []

	soup = BeautifulSoup(response.content, "html5lib", from_encoding="utf-8")
	for a in soup.findAll("loc"):
		a = str(a).replace('<loc><!--[CDATA[', '').replace(']]--></loc>', '')
		urlList.append(a)
	return urlList	


def checked_url_status(url):
	#time.sleep(1.4)
	urlList = [] # ['Crawled URL', 'Status Code', 'Redirects', 'Comments']
	
	comments = "Didn't wrote the full URL because it has a comma" if "," in url else ''

	try:
		response = requests.get(url)
		soup = BeautifulSoup(response.content, "html5lib", from_encoding="utf-8")
		statusCode = response.status_code
		numOfRedirects = 0 
		for redirect in response.history:
			numOfRedirects += 1 if '3' in str(redirect) else 0
		urlList.append(url.replace(',', ''))
		urlList.append(statusCode)
		urlList.append(numOfRedirects)
		urlList.append(comments)	
	except:
		comments = "Can't crawl this URL - don't know why"	
		urlList.append(url.replace(',', ''))
		urlList.append('')
		urlList.append('')
		urlList.append(comments)	
	
	if int(urlList[1]) == 200 and int(urlList[2]) == 0:
		return []
	else:	
		return urlList
			

def make_name(url):
	lastSlashIndex =  url.rfind("/") + 1
	lastDotIndex = url.rfind(".") if url.rfind(".") > lastSlashIndex else len(url)
	return url[lastSlashIndex:lastDotIndex]


def runSimulation(sectionList):
	urls_to_crawl = url_Retrieval(sectionList)
	name_the_file = make_name(sectionList)
	
	for url in urls_to_crawl:
		print url
		write_this = checked_url_status(url)
		if write_this != []:
			csv_writer(write_this, name_the_file)
    	end_time = time.time()


if __name__ == '__main__':
    sectionList = temp_url_Retrieval('http://appsitemap.forexpros.com/tmp/xml/ru/sitemap.xml')

    pool = multiprocessing.Pool(100)

    results = pool.map(runSimulation, sectionList)
    
    time.sleep(2)
		
		    
		    
