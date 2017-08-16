#import relevant libraries
import requests, os
import urllib.request
from bs4 import BeautifulSoup as bs

#open page, make directory to download comics to
url = "http://xkcd.com"
os.makedirs('xkcd', exist_ok=True)

#page = urllib.request.urlopen(url)


#the farthest back url will end with a hashtag
while not url.endswith('#'):

    page = requests.get(url)
    #raise for status to end program if page isn't working
    page.raise_for_status()

#make html an object
    soup = bs(page,"html.parser")
    comicElem = soup.select('#comic img')
#initiate count to track images
    count = 0
#print(soup.prettify())

if comicElem == []:
    print('Could not find comic image.')
else:

#find the images
#find relevant image
    try:
        for image in soup.find_all("img"):
            image_url = 'https:' + image["src"]
            print(image_url)
            page = requests.get(image_url)
            page.raise_for_status()
        #create filename for image
            filename = './xkcd/' + str(count) + "xkcd.jpg"
        #download image
            urllib.request.urlretrieve(image_url, filename)
            count += 1

    #except Exception as e: pass

        prevLink = soup.select('a[rel="prev"]')[0]
        url = 'http://xkcd.com' + prevLink.get('href')
    #print(url)
    #print('Done.')
