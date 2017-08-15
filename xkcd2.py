#import relevant libraries
import requests, os
import urllib.request
from bs4 import BeautifulSoup as bs

#open page, make directory to download comics to
url = "http://xkcd.com"
page = urllib.request.urlopen(url)
os.makedirs('xkcd', exist_ok=True)

#the farthest back url will end with a hashtag
#while not url.endswith('#')

#make html an object
soup = bs(page,"html.parser")

#initiate count to track images
count = 0
#print(soup.prettify())
#find the images
for image in soup.find_all("img"):
#find relevant image
    try:
        image_url = 'https:' + image["src"]
        print(image_url)
        #create filename for image
        filename = './xkcd/' + str(count) + "xkcd.jpg"
        #download image
        urllib.request.urlretrieve(image_url, filename)
        count += 1
    #only go to except block if try block failed
    except Exception as e:
        pass

prevLink = soup.select('a[rel="prev"]')[0]
url = 'http://xkcd.com' + prevLink.get('href')
print(url)

page = urllib.request.urlopen(url)

soup = bs(page, "html.parser")

for image in soup.find_all("img"):
#find relevant image
    try:
        image_url = 'https:' + image["src"]
        print(image_url)
        #create filename for image
        filename = './xkcd/' + str(count) + "xkcd.jpg"
        #download image
        urllib.request.urlretrieve(image_url, filename)
        count += 1
    #only go to except block if try block failed
    except Exception as e:
        pass
