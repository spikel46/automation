#Imports: make our lives easier by giving us pre-built code
import urllib.request
from bs4 import BeautifulSoup as bs

#grabs html page like requests.
page = urllib.request.urlopen("https://www.buzzfeed.com/claudiarosenbaum/kardashians-blac-chyna-nda-drama?utm_term=.gpl57nnA9#.ao0XLVV12")

#turns raw html into beautiful soup object (has functions we can use to parse html easily)
soup = bs(page)

#so that we can name the images uniquely
count = 0

<html>
  <head>
  </head>
  <body>
    <p> this is my image </p>
    <img data-src="thisismyrealsource.net"></img>
  </body>
</html>
#for individual images found by soup.find_all("img")
for image in soup.find_all("img"): #find all a,div,li,ul,body,p,h1-6
    #if error is thrown in try block go to except block
    try:
        #see if image has this data-src tag
        image_url = image["data-src"]
        print(image_url)
        #create filename for image
        filename = './' + str(count) + "kimk.jpg"
        #actual downloading done here
        urllib.request.urlretrieve(image_url, filename)
        count += 1
    #only go to except block if try block failed
    except Exception as e:
        pass
