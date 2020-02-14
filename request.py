import requests
import xml.etree.ElementTree as et

xmlurl = requests.get("https://www.hindustantimes.com/rss/topnews/rssfeed.xml")
print(xmlurl.headers['content-type'])

data = xmlurl.text

with open("scrapedXML.xml", "w", newline='', encoding='utf-8') as scrapeddata:
    scrapeddata.write(data)

link = et.parse("scrapedXML.xml")
root = link.getroot()

for c in root:
    print(c.tag, c.attrib)

print(root.find('channel').find('title').text)
