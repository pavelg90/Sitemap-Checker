import csv


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

def make_name(url):
	lastSlashIndex =  url.rfind("/") + 1
	lastDotIndex = url.rfind(".") if url.rfind(".") > lastSlashIndex else len(url)
	return url[lastSlashIndex:lastDotIndex]

class Queue:
    def __init__(self):
        self.items = []
        self.counter = 0

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item, fileName=None):
        if size() >= 5:
        	writer()
        	self.items = []
        self.items.append(item)
        self.counter += 1

    def dequeue(self):
        self.items = self.items[1:len(self.items)]

    def size(self):
        return len(self.items)

    def count(self):
    	return self.counter 
	
    def deleteThisFunction(now):
	a = 1
	return a

    def writer(self):
    	for write_this in self.items:
    		csv_writer(write_this, 'TEST TEST')

if __name__ == '__main__':
	pass
