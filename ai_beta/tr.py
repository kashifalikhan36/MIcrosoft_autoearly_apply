import time
import json
from undetected_chromedriver import Chrome, ChromeOptions
from datetime import datetime

class GptScrap:
    def __init__(self):
        self.date_today = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.chrome_options = ChromeOptions()
        self.chrome_options.binary_location = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
        self.driver = Chrome(options=self.chrome_options)
    
    # def load_cookies(self, file_path):
    #     with open(file_path, "r") as file:
    #         cookies = json.load(file)
    #         for cookie in cookies:
    #             # Ensure `expiry` key exists and is an integer
    #             if "expiry" in cookie:
    #                 cookie["expiry"] = int(cookie["expiry"])

    #             # Set a default value for `sameSite` if it's missing
    #             if "sameSite" not in cookie:
    #                 cookie["sameSite"] = "Lax"  # Set to "Lax", "Strict", or "None" as needed

    #             self.driver.add_cookie(cookie)

    def Login(self):
        my_email="kashifalikhan093@gmail.com"
        passw="Aquatype123!"
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
        time.sleep(20)
    def apply_jobs(self):
        time.sleep(1)
        self.driver.get('https://jobs.careers.microsoft.com/global/en/search?lc=India')
        time.sleep(10)
        job=self.driver.find_element('xpath','//*[@id="job-search-app"]/div/div[2]/div/div[2]/div[1]/div/div[1]/div[2]')
        job.click()
        time.sleep(7)
        apply=self.driver.find_element('xpath','//*[@id="job-search-app"]/div/div[2]/div/div/div/div[3]/div/div[1]/div/button')
        apply.click()
        time.sleep(7)
        apply=self.driver.find_element('xpath','/html/body/div[3]/div/div/div/div[2]/div[2]/div[3]/div[1]/div/div[3]/div/div[1]')
        apply.click()
        time.sleep(9)
        try:
            apply=self.driver.find_element('xpath','//*[@id="job-search-app"]/div/div[2]/div/div/div/div[3]/div/div[1]/div/button')
            apply.click()
            time.sleep(9)
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
            # Locate the 'Yes' option and click it
            yes_option = self.driver.find_element('xpath', '//span[text()="Yes"]')
            yes_option.click()
            time.sleep(1)
            dropdown = self.driver.find_element('id', 'isImmigrationBenefitEligible-option')
            dropdown.click()
            time.sleep(1)
            # Locate the 'Yes' option and click it
            yes_option = self.driver.find_element('xpath', '//span[text()="No"]')
            yes_option.click()
            sandc = self.driver.find_element('xpath', '/html/body/div[1]/main/div[4]/div[2]/div/div/div/div[2]/div[2]/div[2]/button[2]')
            sandc.click()
            time.sleep(10)
            try:
                sandc = self.driver.find_element('xpath', '/html/body/div[3]/div/div/div/div/div[2]/div[2]/div/div[2]/div[2]/div/span[1]/button')
                sandc.click()
                time.sleep(5)
            except:
                end = self.driver.find_element('xpath', '//*[@id="quesp_form_submit_i"]')
                end.click()
                time.sleep(5)
            try:
                
                end = self.driver.find_element('xpath', '//*[@id="quesp_form_submit_i"]')
                end.click()
            except:
                user_input=self.driver.find_element('xpath','//*[@id="Q401887"]')
                user_input.send_keys("10 years")
                end = self.driver.find_element('xpath', '//*[@id="quesp_form_submit_i"]')
                end.click()
                
            time.sleep(100000)
            self.driver.refresh()
            time.sleep(5)
            

            self.driver.quit()
        except:
            print("error")
            time.sleep(100000)