import time
import json
from undetected_chromedriver import Chrome, ChromeOptions
from datetime import datetime
import pyautogui
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium import webdriver

class microjob():
    def __init__(self):
        date_today = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.chrome_options = ChromeOptions()
        self.chrome_options.binary_location = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
        self.driver = Chrome(options=self.chrome_options)
        my_email="kashifalikhan093@gmail.com"
        self.driver.get("https://careers.microsoft.com/v2/global/en/home.html")
        time.sleep(5)
        signin=self.driver.find_element('xpath','//*[@id="meControl"]')
        signin.click()
        time.sleep(8)
        signin=self.driver.find_element('xpath','/html/body/div[2]/div/div/div/div[2]/div[2]/div[3]/div[1]/div/div[3]/div/div[1]')
        signin.click()
        time.sleep(7)
        user_input=self.driver.find_element('xpath','//*[@id="identifierId"]')
        user_input.send_keys(my_email)
        time.sleep(1)
        user_next=self.driver.find_element('xpath','//*[@id="identifierNext"]/div/button')
        user_next.click()
        time.sleep(7)
        user_next=self.driver.find_element('xpath','//*[@id="yDmH0d"]/c-wiz/div/div[3]/div/div[2]/div/div/button')
        user_next.click()
        time.sleep(7)
        user_next=self.driver.find_element('xpath','//*[@id="yDmH0d"]/c-wiz/div/div[2]/div/div/div/form/span/section[2]/div/div/section/div/div/div/ul/li[2]/div')
        user_next.click()
        time.sleep(9)
        # pyautogui.typewrite('6172')
        # pyautogui.press('enter')
        time.sleep(20)

    def apply_ready(self,job_link):
        self.driver.refresh()
        time.sleep(1)
        self.driver.get('https://jobs.careers.microsoft.com/global/en/search?lc=India')
        time.sleep(10)
        job=self.driver.find_element('xpath','//*[@id="job-search-app"]/div/div[2]/div/div[2]/div[1]/div/div[1]/div[2]')
        job.click()
        time.sleep(7)

        self.driver.get(f'{job_link}')
        time.sleep(7)
        apply=self.driver.find_element('xpath','//*[@id="job-search-app"]/div/div[2]/div/div/div/div[3]/div/div[1]/div/button')
        apply.click()
        time.sleep(7)
        try:
            apply=self.driver.find_element('xpath','/html/body/div[3]/div/div/div/div[2]/div[2]/div[3]/div[1]/div/div[3]/div/div[1]')
            apply.click()
            time.sleep(10)
        except:
            pass
    def apply_on_job(self):

        submit_button=self.driver.find_element('xpath','/html/body/div[1]/main/div[4]/div[2]/div/div[2]/div/div/div/div[3]/div/div[1]/div/button')
        ActionChains(self.driver).key_down(Keys.CONTROL).click(submit_button).key_up(Keys.CONTROL).perform()
        time.sleep(5)

        window_handles = self.driver.window_handles
        self.driver.switch_to.window(window_handles[-1])
        time.sleep(3)
        tick=self.driver.find_element('xpath','//*[@id="apply-appaction"]/div/div/div/div[2]/div[2]/div[3]/div[1]/label')
        tick.click()
        time.sleep(1)
        tick=self.driver.find_element('xpath','//*[@id="apply-appaction"]/div/div/div/div[2]/div[2]/div[3]/div[2]/label')
        tick.click()
        time.sleep(1)
        apply_2=self.driver.find_element('xpath','//*[@id="apply-appaction"]/div/div/div/div[2]/div[2]/div[5]/button')
        apply_2.click()
        time.sleep(8)

        dropdown = self.driver.find_element('id', 'isLegallyAuthorized-option')
        dropdown.click()
        time.sleep(1)
        yes_option = self.driver.find_element('xpath', '/html/body/div[3]/div/div/div/div/div/div/div/button[1]')
        yes_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'isLegallyAuthorized-list0'))
        )
        yes_button.click()
        time.sleep(1)

        dropdown = self.driver.find_element('id', 'isImmigrationBenefitEligible-option')
        dropdown.click()
        time.sleep(1)
        yes_option = self.driver.find_element('xpath', '/html/body/div[3]/div/div/div/div/div/div/div/button[1]')
        yes_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'isImmigrationBenefitEligible-list1'))
        )
        yes_button.click()
        time.sleep(1)

        sandc = self.driver.find_element('xpath', '/html/body/div[1]/main/div[4]/div[2]/div/div/div/div[2]/div[2]/div[2]/button[2]')
        sandc.click()
        time.sleep(15)
        print("Clicked on yes no page")
        try:
            sandc = self.driver.find_element('xpath', '/html/body/div[3]/div/div/div/div/div[2]/div[2]/div/div[2]/div[2]/div/span[1]/button')
            sandc.click()
            time.sleep(15)
            print("Clicked on yes")
        except:
            print("Clicked on yes afetr error")
            end = self.driver.find_element('xpath', '/html/body/div[1]/div[5]/form/div/div[12]/div[2]/input[2]')
            end.click()
            time.sleep(5)
            print("Clicked on yes afetr error")
        print("3rd page click atlast")


        #page3
        iframe = self.driver.find_element('xpath', '//*[@id="icims_content_iframe"]')
        self.driver.switch_to.frame(iframe)
        try:
            submit_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, 'quesp_form_submit_i')))
            submit_button.click()
        except:
            pass
        self.driver.switch_to.default_content()


        #page4
        self.driver.refresh()
        iframe = self.driver.find_element('xpath', '//*[@id="icims_content_iframe"]')
        self.driver.switch_to.frame(iframe)

        dropdown = self.driver.find_element('xpath', '/html/body/div[1]/div[5]/form/div/div[1]/div[2]/select')
        dropdown.click()
        select = Select(dropdown)
        select.select_by_visible_text('Yes')
        dropdown.click()
        time.sleep(1)
        try:
            dropdown = self.driver.find_element('xpath', '/html/body/div[1]/div[5]/form/div/div[2]/div[2]/select')
            dropdown.click()
            select = Select(dropdown)
            select.select_by_visible_text('Yes')
            time.sleep(1)
        except:
            pass
        end = self.driver.find_element('xpath', '//*[@id="quesp_form_submit_i"]')
        end.click()
        self.driver.switch_to.default_content()
        time.sleep(10)