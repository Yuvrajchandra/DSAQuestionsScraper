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
    PEPCODING_QUESTIONS_LIST_URL = 'https://www.pepcoding.com/most-important-interview-questions-list-for-product-based-companies'
    driver = webdriver.Chrome("C:/Users/chand/Downloads/chromedriver_win32/chromedriver.exe")
    driver.get(PEPCODING_QUESTIONS_LIST_URL)
    time.sleep(3)
    username = driver.find_element_by_xpath("//input[@type='email']")
    password = driver.find_element_by_xpath("//input[@type='password']")
    username.send_keys("Your Email Id")
    password.send_keys("Your Password")
    driver.find_element_by_xpath("//button[@type='submit']").click()
    # login_url = 'https://www.pepcoding.com/login'
    # data = {
    #     'username': 'Singhyuvraj179@gmail.com',
    #     'password': 'Qwerty@123'
    # }
    #
    time.sleep(5)
    soup = BeautifulSoup(driver.page_source, "html.parser")
    myuls = soup.find_all('a')
    myuls = soup.findAll('span', attrs={'class': 'questions-name'})
    for ele in myuls:
        print(ele)
    #
    # with requests.Session() as s:
    #     response = requests.post(login_url , data)
    #     # print(response.text)
    #     index_page= s.get('https://www.pepcoding.com/most-important-interview-questions-list-for-product-based-companies')
    #     soup = BeautifulSoup(index_page.text, 'html.parser')
    #     print(soup.title)
    # PEPCODING_QUESTIONS_LIST_URL = 'https://www.pepcoding.com/most-important-interview-questions-list-for-product-based-companies'
    # req = requests.get(PEPCODING_QUESTIONS_LIST_URL)
    # soup = BeautifulSoup(req.content, 'html.parser')
    #
    # # myuls = soup.findAll('span', attrs={'class': 'questions-name'})
    # # myuls = soup.findAll('span')
    # # myuls = soup.find_all('a', href=re.compile("^http"))
    # myuls = soup.find_all('a')
    # print(myuls)
    # print(len(myuls))
    # # for ele in myuls:
    # #     print(ele)





if __name__ == '__main__':
    scrape()
