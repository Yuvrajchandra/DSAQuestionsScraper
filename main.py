from bs4 import BeautifulSoup
import requests
import re
import json
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait




def scrape():

    questions_data = []
    PEPCODING_QUESTIONS_LIST_URL = 'https://www.pepcoding.com/most-important-interview-questions-list-for-product-based-companies'

    # Setting up Chrome Driver Using Selenium
    driver = webdriver.Chrome("C:/Users/chand/Downloads/chromedriver_win32/chromedriver.exe")
    driver.get(PEPCODING_QUESTIONS_LIST_URL)
    time.sleep(3)

    # Loggin into Pepcoding portal
    username = driver.find_element_by_xpath("//input[@type='email']")
    password = driver.find_element_by_xpath("//input[@type='password']")
    username.send_keys("Singhyuvraj179@gmail.com")
    password.send_keys("Qwerty@123")
    driver.find_element_by_xpath("//button[@type='submit']").click()
    time.sleep(5)

    id = 1

    soup = BeautifulSoup(driver.page_source, "html.parser")

    collections = soup.findAll('li', attrs={'class': 'collection-item'})
    for collection in collections:
        a_tags = collection.findChildren("a" , recursive=False)
        question = {}


        # Question Id
        question['id'] = id


        # Question Names
        for a_tag in a_tags:
            span_tag = a_tag.findChildren("span", attrs={'class': 'questions-name'}, recursive=False)
            question_name = span_tag[0]
            question['name'] = question_name.text.strip()



        # Question Urls
        for a_tag in a_tags:
            question['link'] = a_tag['href']




        questions_data.append(question)
        id = id + 1


    print(questions_data)
    print(len(questions_data))






if __name__ == '__main__':
    scrape()
