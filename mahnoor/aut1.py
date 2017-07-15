import requests
from bs4 import BeautifulSoup as bs
import urllib.parse
import urllib.request

"""res = requests.get('https://www.buzzfeed.com/claudiarosenbaum/kardashians-blac-chyna-nda-drama?utm_term=.fp48VA32e#.dheVlbnwv')
res.raise_for_status()
noStarchSoup = bs4.BeautifulSoup(res.text)
type(noStarchSoup)"""

url = "https://www.buzzfeed.com/claudiarosenbaum/kardashians-blac-chyna-nda-drama?utm_term=.fp48VA32e#.dheVlbnwv"
page = urllib.request.urlopen(url)
soup= bs(page)
#res.raise_for_status()
#type(noStarchSoup)

for image in soup.find_all("img"):
    #print ("Image: {}".format(image))
    try:
        image_url = image["data-src"]
        print (image_url)
        res = requests.get(image_url)
        filename = str (count) + "kimk.jpg"
        urllib.request.urlretrieve(image_url,'./'+filename)
        """if(res.status_code == requests.codes.ok):
            print(image_url)
            playFile.open('filename','wb')
            for chunk in res.iter_content(100000):
                playFile.write(chunk)
            playFile.close()"""
        count +=1
    except Exception as e:
        pass

    """image_url = image ["data-src"]
    res = requests.get(image_url)
    playFile =
    if(res.status_code == requests.codes.ok):
        for chunk in res.iter_content(100000):
            playFile.write(chunk)"""
