#import relevant libraries
import urllib.request
from bs4 import BeautifulSoup as bs

#open page
page = page = urllib.request.urlopen('https://xkcd.com'')

#make html an object
soup = bs(page)

#initiate count to track images
count = 0 
