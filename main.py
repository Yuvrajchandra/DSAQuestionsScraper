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
    Question_urls = []

    soup = BeautifulSoup(driver.page_source, "html.parser")

    myuls = soup.findAll('li', attrs={'class': 'collection-item'})
    for ele in myuls:
        children = ele.findChildren("a" , recursive=False)
        question = {}


        # Question Urls
        for child in children:
            question['link'] = child['href']
            # Question_urls.append(child['href'])
            # print(child['href'])

        # Question Names
        for child in children:
            qwe=child.findChildren("span", attrs={'class': 'questions-name'}, recursive=False)
            rty=qwe[0]
            question['name'] = rty.text.strip()
            # print(rty.text.strip())
        questions_data.append(question)

    # print(len(myuls))
    # print(len(Question_urls))
    print(questions_data)
    print(len(questions_data))






if __name__ == '__main__':
    scrape()
