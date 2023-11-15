import requests
import json
import sys

#give the package.json url

#url = sys.argv[1]

url = input("Enter package.json url :  ")

#get the pack package.json values in response
response = requests.get(url)


#parse the text

jsontext = response.text


#convert jsontext to dictionary

jsondictionary = json.loads(jsontext)



#print if name of package is available or not

if "name" in jsondictionary:
 name=jsondictionary["name"]
 url='https://npmjs.com/package/'+name
 res=requests.get(url)
 print(url)
 print(res.status_code)




#print dependencies

if "dependencies" in jsondictionary:
 depend= jsondictionary["dependencies"]
 #print(depend)
 for x in depend:
   url='https://npmjs.com/package/'+x
   res=requests.get(url)
   print(url)
   print(res.status_code)



#print peer dependencies

if "peerDependencies" in jsondictionary:
 peerdepend = jsondictionary["peerDependencies"]
 for y in peerdepend:
   url='https://npmjs.com/package/'+y
   res=requests.get(url)
   print(url)
   print(res.status_code)


#print(peerdepend)

# print Devdepencies 

if "devDependencies" in jsondictionary:
 devdepend = jsondictionary["devDependencies"]
 for z in devdepend:
   url='https://npmjs.com/package/'+z
   res=requests.get(url)
   print(url)
   print(res.status_code)
