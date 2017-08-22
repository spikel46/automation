#import relevant libraries
from selenium import webdriver
import requests, os
import urllib.request
from selenium.webdriver.common.keys import Keys
import time

#open facebook
browser = webdriver.Firefox()
url = "https://www.facebook.com/"
browser.get(url)

#find the email input
emailElem = browser.find_element_by_xpath ("//input[@type='email']")

#enter email
emailElem.send_keys("mahnoor.mian95@gmail.com")

#find the password input
passwordElem = browser.find_element_by_xpath ("//input[@type='password']")

#enter password
passwordElem.send_keys("mahnoorforgets1007")

#define log in button
loginElem = browser.find_element_by_xpath ("//input[@value='Log In']")

#press log in
loginElem.click()

#find message
messageElem = browser.find_element_by_xpath("//a[@class='jewelButton _3eo8']")

#press message
messageElem.click()

#find new message
newMessageElem = browser.find_element_by_xpath("//a[@href='/messages/new/']")

#press new message
newMessageElem.click()

#let it load
time.sleep(5)

#tell who
toElem = browser.find_element_by_xpath("//div[@class='_3l9s']")

#type joey
toElem.send_keys("Joey Koblitz")

#pick joey
joeyElem = browser.find_element_by_xpath("//li[@title='Joey Koblitz']")

#click joey
joeyElem.click()




#find gif elements
#gifElem = browser.find_element_by_xpath("//a[@class='_6gb _6gs']")

#click gif button
#gifElem.click()

#let it load
time.sleep(3)

#gif search bar
#gifSearchElem = browser.find_element_by_xpath("//input[@placeholder='Search GIFs across apps...']")

#load hilary gifs
#gifSearchElem.send_keys("Hilary Clinton")

#select hilary gifS
#hilaryElem = browser.find_element_by_xpath ("//img[@class='_358 _26n6 img']")

#send hilary gifS
#hilaryElem.click()

#find type message
typeElem = browser.find_element_by_xpath("//div[@aria-autocomplete='list']")

#write message
typeElem.send_keys("This message was brought to you by selenium and xpaths and python!!!")

#press enter
typeElem.send_keys(Keys.ENTER)

"""#find the search bar
searchElem = browser.find_element_by_xpath("//input[@aria-label='Search']")

#find joey
searchElem.send_keys("Joey Koblitz")

#fnd enter button
enterElem = browser.find_element_by_xpath("//button[@type ='submit']")

#press enter
enterElem.click()"""
