import multiprocessing
from customQueue import Queue
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
reload(sys)
sys.setdefaultencoding('utf-8')

q = Queue()

currentTime = " " + str(datetime.now()).replace("-", " ").replace(":", " ").replace(".", " ")
start_time = time.time()
row_counter = 0 


allSiteMaps = "http://appsitemap.forexpros.com/tmp/xml/ru/sitemap.xml"
#allSiteMaps = "https://www.utab.com/sitemap/sitemapindex.xml"

def tempSiteMap_urlConverter(url):
	dashIndex = url.rfind("-")
	temp_storageLocation = "http://appsitemap.forexpros.com/tmp/xml/ru/maps/sitemap"
	return temp_storageLocation + url[dashIndex:len(url) - 3]	

def temp_url_Retrieval(url):
	time.sleep(1.7)
	response = requests.get(url, timeout = 20.0)
	statusCode = response.status_code
	urlList = []
	soup = BeautifulSoup(response.content, "html5lib")
	
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
		print a
		urlList.append(a)
	return urlList	



def runSimulation(sectionList):
	global q
	urls_to_crawl = url_Retrieval(sectionList)


if __name__ == '__main__':
	sectionList = temp_url_Retrieval('http://appsitemap.forexpros.com/tmp/xml/ru/sitemap.xml')	
	runSimulation(sectionList[0])  
	time.sleep(3) 
		    