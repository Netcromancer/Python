#Brandon Bruce 4/24/2018
#Kitchen Inventory tracks what items we currently have on hand. 
#This is done through a UPC/ Barcode scanner.

#imports here
import requests
import urllib.request
import urllib.error
import json
#Function to collect and convert UPC codes into items.
print ("Enter item")
item = input()
ready_item = item + '/'
api_key = '219860C974FF6AB2CDE9B1E152807F04'
address = 'https://api.upcdatabase.org/product/'
combined = address + ready_item + api_key
print(combined)

opener = urllib.request.build_opener()
f = opener.open(combined)
json = json.loads(f.read())
print(json)
print(json['title'])
#output = requests.get(combined)
#print(output)


#with urllib.request.urlopen(combined)
#	data = json.loads(url.read().decode())
#	print(data)


#output = requests.get((https://api.upcdatabase.org/product/%s/219860C974FF6AB2CDE9B1E152807F04) % (item))

#Function to add quantity to items.

#Function to print an inventory sheet.