from selenium import webdriver
import streamlit as st
import pandas as pd
import os

from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

st.title("JOB Locator")

page = st.sidebar.radio("Navigation",['Home','About me'],index=0)

if page == 'Home':
    url = st.text_input("Job title link ")
    if st.button('Search'):
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

        st.text("RECCOMENDED LOCATIONS TO APPLY")
        st.dataframe(sorted.head(5))

        st.text("WORST LOCATIONS TO APPLY")
        st.dataframe(sorted.tail(5))

if page == 'About me':
    st.image('d.png')
    st.subheader('''I'M Vidwan Gowda H M
Data Science & Machine Learning
Enthusiast''')
    st.text('“Passionate Explorer, Innovative Learner, Collaborative Builder”')
    sourcecode = 'https://github.com/gowdavidwan2003/numberofjobsfinder'
    st.markdown(f'<a href={sourcecode}><button style="background-color:grey;display: block; width: 100%">Source - Code </button></a>', unsafe_allow_html=True)
    st.markdown(f'<a href={dataset}><button style="background-color:grey;display: block; width: 100%">Dataset used</button></a>', unsafe_allow_html=True)
    st.subheader("Contact me")
    first , last = st.columns(2)
    first1 , last1 = st.columns(2)
    first2 , last2 = st.columns(2)
    
    portfolio = 'https://gowdavidwan2003.github.io/portfolio'
    linkedin = 'www.linkedin.com/in/gowdavidwan2003'
    github = 'https://github.com/gowdavidwan2003'
    whatsapp = 'https://wa.me/917975045560'
    phone = 'tel:+917975045560'
    first.markdown(f'<a href={portfolio}><button style="background-color:grey;display: block; width: 100%">Portfolio website</button></a>', unsafe_allow_html=True)
    last.markdown(f'<a href={linkedin}><button style="background-color:grey;display: block; width: 100%">Linked In</button></a>', unsafe_allow_html=True)
    first1.markdown(f'<a href={github}><button style="background-color:grey;display: block; width: 100%">Github</button></a>', unsafe_allow_html=True)
    last1.markdown(f'<button style="background-color:grey;display: block; width: 100%">Email - gowdavidwan2003@gmail.com</button>', unsafe_allow_html=True)
    first2.markdown(f'<a href={whatsapp}><button style="background-color:grey;display: block; width: 100%">Whatsapp</button></a>', unsafe_allow_html=True)
    last2.markdown(f'<a href={phone}><button style="background-color:grey;display: block; width: 100%">Phone</button></a>', unsafe_allow_html=True)
