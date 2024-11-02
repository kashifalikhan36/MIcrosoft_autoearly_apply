import time
import json
from undetected_chromedriver import Chrome, ChromeOptions
from datetime import datetime
from email.message import EmailMessage
import ssl
import smtplib
from Microjob import microjob

class microalert():
    def __init__(self):
        self.apply_bot=microjob()
        self.password="dfxxbiihhbonnxua"
        self.email="kashifalikhan093@gmail.com"
        self.email_to="kashifalikhan78677868@gmail.com"

        # Set up Chrome options
        self.options = ChromeOptions()
        self.options.add_argument('--headless')  # Run in headless mode (no GUI)
        self.options.add_argument('--no-sandbox')
        self.options.add_argument('--disable-dev-shm-usage')
        self.chrome_options = ChromeOptions()
        self.chrome_options.binary_location = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
                
        # Initialize WebDriver
        self.driver = Chrome(options=self.chrome_options)

        # URL to scrape
        self.url = 'https://jobs.careers.microsoft.com/global/en/search?lc=India'

    # Function to get job titles from the page
    def get_job_titles(self):
        self.driver.get(self.url)
        time.sleep(10)  # Wait for the page to load

        # Find job titles; adjust the selector based on actual page structure
        job_elements = self.driver.find_elements('xpath', '//*[@id="job-search-app"]/div/div[2]/div/div[2]/div[1]/div/div[1]/div[1]/div/div/div[2]/div[1]/h2')
        
        job_titles = []
        for job in job_elements:
            title_text = job.text.strip()
            job_titles.append(title_text)
        
        return job_titles

    # Function to monitor new job postings
    def monitor_jobs(self,check_interval=60):
        previous_jobs = set(self.get_job_titles())
        
        while True:
            print(f"{datetime.now()}: Checking for new job postings...")
            current_jobs = set(self.get_job_titles())
            print(current_jobs)

            new_jobs = current_jobs - previous_jobs
            
            if new_jobs:
                print("New Job Postings Found:")
                for job in new_jobs:
                    print(f"- {job}")
                
                current_url = self.driver.current_url
                cnt=""
                try:
                    self.apply_bot.apply_ready(current_url)
                    time.sleep(5)
                    self.apply_bot.apply_on_job()
                    time.sleep(1)
                    cnt="I had submitted your profile for this job"
                except:
                    cnt="I have some kind of erro can you fill it manually"

                subject=f"New Job Post On Microsoft :-{job}"
                body=f"Here is the link :- {current_url} and here is the current info :- {cnt}"

                em=EmailMessage()
                em['From']=self.email
                em['To']=self.email_to
                em['Subject']=subject
                em.set_content(body)

                context=ssl.create_default_context()
                with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
                    smtp.login(self.email,self.password)
                    smtp.sendmail(self.email,self.email_to,em.as_string())

                # Print the most recent job posting
                most_recent_job = sorted(current_jobs, key=lambda x: x.lower())[-1]  # Assuming last in alphabetical order is recent
                print(f"Most Recent Job Posting: {most_recent_job}")
            else:
                print("No new job postings found.")
            
            # Update the previous jobs for the next check
            previous_jobs = current_jobs
            
            # Wait for the specified interval before checking again
            time.sleep(check_interval)