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


        # Question Topic
        if id<=49:
            question['topic'] = "Array"
        elif id>49 and id<=79:
            question['topic'] = "Searching & Sorting"
        elif id>79 and id<=133:
            question['topic'] = "String"
        elif id>133 and id<=152:
            question['topic'] = "Matrix"
        elif id>152 and id<=171:
            question['topic'] = "BackTracking"
        elif id>171 and id<=193:
            question['topic'] = "Greedy"
        elif id>193 and id<=247:
            question['topic'] = "Dynamic Programming"
        elif id>247 and id<=268:
            question['topic'] = "Stacks & Queues"
        elif id>268 and id<=299:
            question['topic'] = "LinkedList"
        elif id>299 and id<=311:
            question['topic'] = "Generic Trees"
        elif id>311 and id<=363:
            question['topic'] = "Binary Trees"
        elif id>363 and id<=391:
            question['topic'] = "Binary Search Trees"
        elif id>391 and id<=421:
            question['topic'] = "Order Statistics & Heap & Hash"
        elif id>421 and id<=457:
            question['topic'] = "Graphs"
        elif id>457 and id<=477:
            question['topic'] = "Bit Manipulation"
        elif id>477 and id<=487:
            question['topic'] = "Maths"
        elif id>487 and id<=499:
            question['topic'] = "Geometry"
        elif id>499 and id<=506:
            question['topic'] = "Trie"
        elif id>506 and id<=508:
            question['topic'] = "Union Find"


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


    with open('data.json', 'w') as f:
        json.dump(questions_data, f, indent = 4)





if __name__ == '__main__':
    scrape()
