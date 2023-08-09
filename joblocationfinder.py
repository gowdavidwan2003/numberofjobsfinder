from selenium import webdriver
import time
import pandas as pd
import os
import matplotlib.pyplot as plt


from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


def scrape_data(url):


 


 chromedriver_path = r'C:\Users\gowda\OneDrive\Desktop\chromedriver_win32\chromedriver.exe'
 os.environ["PATH"] += os.pathsep + chromedriver_path
 driver = webdriver.Chrome()
 driver.get(url)
 driver.implicitly_wait(10)



 element = driver.find_element('css selector', '.results-context-header__new-jobs')


 number = element.text.replace(',', '')
 number = number.replace('new', '')
 number = number.replace(')', '')
 number = number.replace('(', '')

 number = int(number)
 #number


 i=0


 while(i<number*2):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    i=i+1
 location=[]



 job_postings = driver.find_elements(By.CLASS_NAME, 'base-search-card--link')
 for job_posting in job_postings:
    location_element = job_posting.find_element(By.CLASS_NAME, 'job-search-card__location')
    job_location = location_element.text
    location.append(job_location)
 #location
 driver.quit()




 print(len(location))




 setlocation = set(location)
 njob=[]
 for ele in setlocation:
    a=location.count(ele)
    njob.append(int(a))
 #njob
    




 LOCATION = pd.DataFrame(setlocation,columns=["Location"])
 NJOB = pd.DataFrame(njob,columns=["Openings"])
 result=LOCATION.join(NJOB)
 #result





 sorted = result.sort_values(by='Openings',ascending=False)
 #sorted




 print("RECCOMENDED LOCATIONS TO APPLY")
 print(sorted.head(5))




 print("WORST LOCATIONS TO APPLY")
 print(sorted.tail(5))

 


if __name__ == "__main__":
    url = input("Enter the URL: ")
    data = scrape_data(url)
    print(data)
