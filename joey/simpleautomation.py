import requests, urllib.parse, urllib.request

from bs4 import BeautifulSoup as bs

page = urllib.request.urlopen("https://www.buzzfeed.com/claudiarosenbaum/kardashians-blac-chyna-nda-drama?utm_term=.gpl57nnA9#.ao0XLVV12")
soup = bs(page)

count = 0

for image in soup.find_all("img"):
    try:
        image_url = image["data-src"]
        print(image_url)
        filename = './' + str(count) + "kimk.jpg"
        urllib.request.urlretrieve(image_url, filename)
        count += 1
    except Exception as e:
        pass
