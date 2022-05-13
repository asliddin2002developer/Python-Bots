from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException
import time

chrome_path = "C:\Development\chromedriver.exe"
similar_account = 'buzzfeedtasty'
USERNAME = 'asldev2002'
PASSWORD = 'T##/*g:S+_4ChPR'

class InstaFollower:

    def __init__(self, path):
        self.driver = webdriver.Chrome(executable_path=path)

    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")

        time.sleep(2)
        username = self.driver.find_element_by_name("username")
        password = self.driver.find_element_by_name("password")

        username.send_keys(USERNAME)
        password.send_keys(PASSWORD)

        time.sleep(2)
        password.send_keys(Keys.ENTER)


    def find_followers(self):
        time.sleep(4)
        self.driver.get(f'https://www.instagram.com/{similar_account}')

        time.sleep(2)
        followers = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')
        followers.click()

        time.sleep(5)
        follow_btn = self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div[2]')
        for i in range(15):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", follow_btn)
            time.sleep(2)


    def follow(self):
        all_buttons = self.driver.find_elements_by_css_selector("li button")
        for button in all_buttons:
            try:
                button.click()
                time.sleep(1)
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[2]')
                cancel_button.click()

bot = InstaFollower(chrome_path)
bot.login()
bot.find_followers()
bot.follow()
