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

    print('Downloading page %s...' % url)
    res = requests.get(url)
    #raise for status to end program if page isn't working
    res.raise_for_status()

#make html an object
    soup = bs(res.text)
    comicElem = soup.select('#comic img')
#initiate count to track images
    #count = 0
#print(soup.prettify())

    if comicElem == []:
        print('Could not find comic image.')
    else:

#find the images
#find relevant image
        try:
            #for image in soup.find_all("img"):
            image_url = 'https:' + comicElem[0].get('src')
            print('Downloading image %s...' %(image_url))
            res = requests.get(image_url)
            res.raise_for_status()
        #create filename for image
            count = 0
            filename = './xkcd/' + str(count) + "xkcd.jpg"
        #download image
            urllib.request.urlretrieve(image_url, filename)
            count+=1

        except requests.exceptions.MissingSchema:
            prevLink = soup.select('a[rel="prev"]')[0]
            url = 'http://xkcd.com' + prevLink.get('href')
            continue
    #only go to except block if try block failed"""
    #except Exception as e: pass
    prevLink = soup.select('a[rel="prev"]')[0]
    url = 'http://xkcd.com' + prevLink.get('href')
    #count += 1


print('Done.')
    #print(url)
    #print('Done.')
