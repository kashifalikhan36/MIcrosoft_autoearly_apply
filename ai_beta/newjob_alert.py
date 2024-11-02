import time
import json
from undetected_chromedriver import Chrome, ChromeOptions
from datetime import datetime
from email.message import EmailMessage
import ssl
import smtplib

password="dfxxbiihhbonnxua"
email="kashifalikhan093@gmail.com"
email_to="kashifalikhan78677868@gmail.com"

# Set up Chrome options
options = ChromeOptions()
options.add_argument('--headless')  # Run in headless mode (no GUI)
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
chrome_options = ChromeOptions()
chrome_options.binary_location = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
        
# Initialize WebDriver
driver = Chrome(options=chrome_options)

# URL to scrape
url = 'https://jobs.careers.microsoft.com/global/en/search?lc=India'

# Function to get job titles from the page
def get_job_titles():
    driver.get(url)
    time.sleep(10)  # Wait for the page to load

    # Find job titles; adjust the selector based on actual page structure
    job_elements = driver.find_elements('xpath', '//*[@id="job-search-app"]/div/div[2]/div/div[2]/div[1]/div/div[1]/div[1]/div/div/div[2]/div[1]/h2')
    
    job_titles = []
    for job in job_elements:
        title_text = job.text.strip()
        job_titles.append(title_text)
    
    return job_titles

# Function to monitor new job postings
def monitor_jobs(check_interval=60):
    previous_jobs = set(get_job_titles())
    
    while True:
        print(f"{datetime.now()}: Checking for new job postings...")
        current_jobs = set(get_job_titles())
        print(current_jobs)
        # Check for new jobs
        new_jobs = current_jobs - previous_jobs
        
        if new_jobs:
            print("New Job Postings Found:")
            for job in new_jobs:
                print(f"- {job}")
            
            subject=f"New Job Post On Microsoft :-{job}"
            body="Here is the link :- https://jobs.careers.microsoft.com/global/en/search?lc=India"

            em=EmailMessage()
            em['From']=email
            em['To']=email_to
            em['Subject']=subject
            em.set_content(body)

            context=ssl.create_default_context()
            with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
                smtp.login(email,password)
                smtp.sendmail(email,email_to,em.as_string())

            # Print the most recent job posting
            most_recent_job = sorted(current_jobs, key=lambda x: x.lower())[-1]  # Assuming last in alphabetical order is recent
            print(f"Most Recent Job Posting: {most_recent_job}")
        else:
            print("No new job postings found.")
        
        # Update the previous jobs for the next check
        previous_jobs = current_jobs
        
        # Wait for the specified interval before checking again
        time.sleep(check_interval)

if __name__ == "__main__":
    try:
        monitor_jobs(check_interval=60)  # Check every 60 seconds
    except KeyboardInterrupt:
        print("Monitoring stopped by user.")
    finally:
        driver.quit()  # Ensure the WebDriver is closed on exit