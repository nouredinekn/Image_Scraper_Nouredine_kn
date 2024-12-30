from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os
import urllib

def scrapeImages(search_query,countPage ,totalImages):
    driver = webdriver.Chrome()
    driver.get(f"https://unsplash.com/s/photos/{search_query}")
    time.sleep(2)
    x=driver.find_elements(By.XPATH,"//button[contains(@class,'cDy10')]")
    x[2].click()
    src = []

    for _ in range(countPage):
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
        imgResults = driver.find_elements(By.XPATH,"//img[contains(@class,'tzC2N')]")
        for img in imgResults:
            src.append(img.get_attribute('src'))
        time.sleep(5) 
    src_unique =list(set(src))
    output_folder = f"images/{search_query}" 
    os.makedirs(output_folder, exist_ok=True)
    totalImages=totalImages if len(src_unique)>totalImages else len(src_unique)
    for i in range(totalImages+1):    
        urllib.request.urlretrieve(str(src_unique[i]),f"{output_folder}/{search_query}{i}.jpg")
search_query = "casablanca morocco" 
count=2
totalImages=10
scrapeImages(search_query,count,totalImages)