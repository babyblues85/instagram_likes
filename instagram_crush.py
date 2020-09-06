from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random
import sys


def print_same_line(text):
    sys.stdout.write('\r')
    sys.stdout.flush()
    sys.stdout.write(text)
    sys.stdout.flush()

username = "**********" #Your username
password = "************"  #Your password
crush_username = "***********" #Your ig Crush's user id

class insta_crush:

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Firefox()

    def closeBrowser(self):
        self.driver.close()

    def login(self):
        driver = self.driver
        driver.get("https://www.instagram.com/")
        time.sleep(2)
        user_name_elem = driver.find_element_by_xpath("//input[@name='username']")
        user_name_elem.clear()
        user_name_elem.send_keys(self.username)
        passworword_elem = driver.find_element_by_xpath("//input[@name='password']")
        passworword_elem.clear()
        button_elem = driver.find_element_by_xpath("//*[@id='loginForm']/div/div[3]/button")
        passworword_elem.send_keys(self.password)
        button_elem.click()
        time.sleep(2)

    def crush_find(self,crush_username):
        driver = self.driver
        driver.get("https://www.instagram.com/" + crush_username + "/")
        time.sleep(2)

        #gathering photos
        pic_hrefs = []
        for i in range(1, 2):
            try:
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(2)
                # get tags
                hrefs_in_view = driver.find_elements_by_tag_name('a')
                # finding relevant hrefs
                hrefs_in_view = [elem.get_attribute('href') for elem in hrefs_in_view
                                 if '.com/p/' in elem.get_attribute('href')]
                # building list of unique photos
                [pic_hrefs.append(href) for href in hrefs_in_view if href not in pic_hrefs]
                # print("Check: pic href length " + str(len(pic_hrefs)))
            except Exception:
                continue

        #Liking photos

        for pic_href in pic_hrefs:
            try:
                driver.get(pic_href)
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(2)
                like_button = driver.find_element_by_xpath("//html/body/div[1]/section/main/div/div[1]/article/div[3]/section[1]/span[1]/button")
                like_button.click()
                print("Photo Liked Successfully")
            except Exception:
                continue

ig = insta_crush(username, password)
ig.login()
ig.crush_find(crush_username)
