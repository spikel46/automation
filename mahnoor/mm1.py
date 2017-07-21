#import relevant libraries
import urllib.request
from bs4 import BeautifulSoup as bs

#open page
'link'= 'http://xkcd.com'
page = urllib.request.urlopen('link')

#make html an object
soup = bs(page)

#initiate count to track images
count = 0 

for i in range(0,5):  
   #find the images
    for image in soup.find_all("img"):
 
  #find relevant image
      try:
        image_url = image["img src"]
        print(image_url)
        #create filename for image
        filename = './' + str(count) + "xkcd.jpg"
        #download image
        urllib.request.urlretrieve(image_url, filename)
        count += 1
    #only go to except block if try block failed
   except Exception as e:
        pass
                                     
  #open previous link
  prevLink = soup.select('a[rel="prev"]')
  link = 'http://xkcd.com' + prevLink.get('href')
