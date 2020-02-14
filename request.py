import requests
import xml.etree.ElementTree as et

# Getting the URL
xmlurl = requests.get("https://www.hindustantimes.com/rss/topnews/rssfeed.xml")
# specifying the document type
print(xmlurl.headers['content-type'])

data = xmlurl.text

# writing the document to an XML file
with open("scrapedXML.xml", "w", newline='', encoding='utf-8') as scrapeddata:
    scrapeddata.write(data)

# parsing the XML file
link = et.parse("scrapedXML.xml")
root = link.getroot()

for c in root:
    print(c.tag, c.attrib)

print(root.find('channel').find('title').text)
