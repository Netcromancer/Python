#Brandon Bruce 4/24/2018
#Kitchen Inventory tracks what items we currently have on hand. 
#This is done through a UPC/ Barcode scanner.

#imports here
import requests
import urllib.request
import urllib.error
import json

#Variables
#Need to register at https://api.upcdatabase.org and obtain API Key.
api_key = <API_KEY>
address = 'https://api.upcdatabase.org/product'
#Function to collect and convert UPC codes into items.
def upc():
	print ("Enter item")
	item = input()
	return item

def url(item):	
	ready_item = item + '/'
	combined = address + ready_item + api_key
	return combined

def request(combined):
	opener = urllib.request.build_opener()
	f = opener.open(combined)
	json1 = json.loads(f.read())
	try: urllib.request.urlopen(opener)
	except urllib.error.URLError as e:
		print(e.reason)
#Print the entire JSON. This is for debugging and will be removed later.
	print(json1)
#This is the intended output and should remain.
	print(json1['title'])


item = upc()
combined = url(item)
request(combined)




#Function to add quantity to items.

#Function to print an inventory sheet.
