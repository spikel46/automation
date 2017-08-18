#import relevant libraries
from selenium import webdriver
import requests, os
import urllib.request

directory = 'ch_comics'
os.makedirs(directory, exist_ok=True)

#open explosuuuuuuuum
browser = webdriver.Firefox()
url = 'http://explosm.net/comics/oldest'
browser.get(url)

count = 0

while not url.endswith('100'):


#inspect comic element, find unique xpath, Xpath=//tagname[@attribute='value']
    try:
        comicElem = browser.find_element_by_xpath("//img[@id='main-comic']")
        print (type(comicElem))
        #key value pair, in this case key source value is the url

        image_url = comicElem.get_attribute('src')
        print(image_url)
        filename = './' + directory + '/' + str(count) + 'ch.jpg'
        urllib.request.urlretrieve (image_url, filename)

        count += 1

        print('success')
        pass
    except Exception as e:
        print (e)
        pass

    nextElem = browser.find_element_by_xpath("//img [@src = '/img/nav-button_next@2x.png']")
    nextElem.click()

    pass
#close the browser
browser.quit()






#comicElem = browser.find_element_by_xpath("//img[@id='main-comic']")
#<img id="main-comic" src="//files.explosm.net/comics/kApplesauce0001.jpg">
#<img src="/img/nav-button_next@2x.png">

#os.makedirs('ch_comics', exist_ok=True)
#count = 0



#while not url.endswith ('latest')

#if vs try block, hard fail (the program stops) vs soft fail (because anticipates)
#script logs in to facebook and sends joey a message and logs out 
