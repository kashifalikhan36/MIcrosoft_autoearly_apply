from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By
from undetected_chromedriver import Chrome, ChromeOptions
from bs4 import BeautifulSoup
from datetime import datetime
HEADER={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.35",
    "Accept-Language":"en-GB,en;q=0.9,en-US;q=0.8"
}
class GptScrap():
    def __init__(self):
        self.date_today=datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.chrome_options = ChromeOptions()
        self.chrome_options.binary_location="C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
        for key, value in HEADER.items():
            self.chrome_options.add_argument(f"--header={key}:{value}")
        self.driver = Chrome(options=self.chrome_options)
    def Login(self):
        Login_credential=True
        while True:
            my_email = "astroknestrok@gmail.com"
            passw = "Aqua"
            try:
                self.driver.get('https://jobs.careers.microsoft.com/global/en/search?lc=India&l=en_us&pg=1&pgSz=20&o=Relevance&flt=true')
                time.sleep(400)
                login=self.driver.find_element('xpath','/html/body/div[1]/div[1]/div[1]/div[4]/button[1]')
                login.click()
                time.sleep(5)
                google=self.driver.find_element('xpath','/html/body/div/main/section/div/div/div/div[4]/form[2]/button')
                google.click()
                time.sleep(3)
                user_input=self.driver.find_element('xpath','//*[@id="identifierId"]')
                user_input.send_keys(my_email)
                user_next=self.driver.find_element('xpath','//*[@id="identifierNext"]/div/button')
                user_next.click()
                time.sleep(6)
                password_input=self.driver.find_element('xpath','//*[@id="password"]/div[1]/div/div[1]/input')
                password_input.send_keys(passw)
                time.sleep(1)
                password_next=self.driver.find_element('xpath','//*[@id="passwordNext"]/div/button')
                password_next.click()
                time.sleep(13)
                break
            except:
                print('There is some Error')
    def formality(self):
        next=self.driver.find_element('xpath','//*[@id="radix-:r8:"]/div/div/div[4]/button')
        next.click()
        time.sleep(1)
        for i in range(0,2):
            next=self.driver.find_element('xpath','//*[@id="radix-:r8:"]/div/div/div[4]/button[2]')
            next.click()
            time.sleep(1)