#import relevant libraries
from selenium import webdriver
import requests, os
import urllib.request
from selenium.webdriver.common.keys import Keys
import time

#define login fn
def login (email, password):
    #find the email input
    emailElem = browser.find_element_by_xpath ("//input[@type='email']")

    #enter email
    emailElem.send_keys(email)

    #find the password input
    passwordElem = browser.find_element_by_xpath ("//input[@type='password']")

    #enter password
    passwordElem.send_keys(password)

    #define log in button
    loginElem = browser.find_element_by_xpath ("//input[@value='Log In']")

    #press log in
    loginElem.click()

def newMessage (person):
    #find message
    messageElem = browser.find_element_by_xpath("//a[@class='jewelButton _3eo8']")

    #press message
    messageElem.click()

    #find new message
    newMessageElem = browser.find_element_by_xpath("//a[@href='/messages/new/']")

    #press new message
    newMessageElem.click()

    #let it load
    time.sleep(3)

    #tell who
    toElem = browser.find_element_by_xpath("//div[@class='_3l9s']")

    #type persons name
    toElem.send_keys(person)

    #press enter
    toElem.send_keys(Keys.ENTER)

def sendText (text):
    #find type message
    typeElem = browser.find_element_by_xpath("//div[@aria-autocomplete='list']")

    #write message
    typeElem.send_keys(text)

    #press enter
    typeElem.send_keys(Keys.ENTER)

def sendStar ():

    #find star
    starElem = browser.find_element_by_xpath("//a[@class='_5j_u _6gb']")

    #send star
    starElem.send_keys(Keys.ENTER)

def sendGIF (gif):

    #find gif
    gifElem = browser.find_element_by_xpath("//a[@class='_6gb _6gs']")

    #select gif
    gifElem.click()

    #let it load
    time.sleep(3)

    #gif search bar
    gifSearchElem = browser.find_element_by_xpath("//input[@placeholder='Search GIFs across apps...']")

    #load hilary gifs
    gifSearchElem.send_keys(gif)

    #press enter
    gifSearchElem.send_keys(Keys.ENTER)

    #selectGIF
    gifSelectElem = browser.find_element_by_xpath("//img[@class='_358 _26n6 img']")

    #selectGIF
    gifSelectElem.click()

questionOne = input ('Would you like to open facebook (yes or y):')

if questionOne == ("yes") or ("y"):
    #open facebook
    browser = webdriver.Firefox()
    url = "https://www.facebook.com/"
    browser.get(url)

    #have the user enter email and  password
    email = input ('Enter your facebook username: ')
    password = input ('Enter your facebook password: ')

    #login with the userinputted email and password
    login (email, password)

    questionTwo = input ('Would you like to send someone a message (yes or y): ')

    if questionTwo == ("yes") or ("y"):
        #let the user pick who they send a message to
        person = input ('To whom would you like to send a message: ')

        #open a message to the users person
        newMessage(person)

        while questionThree != ('5'):
            print ('Option 1: send a text message')
            print ('Option 2: send a gif')
            print ('Option 3: send a thumbs up')
            print ('Option 4: do not send a message')
            print ('Option 5: quit the browser')
            questionThree = input ('Type the number answer you want to select (1, 2, 3, or 4): ')

            if  questionThree == ('1'):
                #let the user pick something to say
                text = input ('What would you like to say to ' + person + ' : ')

                #send the message
                sendText(text)

            if questionThree == ('2'):
                #send a star
                sendStar()

            if questionThree == ('3'):
                #select gif
                gif = input ('What kind of gif do you want to send: ')

                #send the gif
                sendGIF(gif)

            if questionThree == ('4'):
                continue

            if questionThree == ('5'):
                browser.quit()

            else:
                print ('That was not an option please select again.')
