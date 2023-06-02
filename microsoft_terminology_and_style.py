
import os
import time

import pandas as pd

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager



# Reject cookies popup
def reject_cookies(driver):

    wait = WebDriverWait(driver, 10)

    xpath_onetrust_policy = "//button[@id='onetrust-reject-all-handler']"
    print("Waiting for OneTrust cookie popup...")
    onetrust_reject_button = wait.until(EC.element_to_be_clickable((By.XPATH, xpath_onetrust_policy)))
    onetrust_reject_button.click()
    print("Onetrust cookies rejected successfully...")

# Check what is the latest downloaded file in path
def latest_download_file(path):
    # path = r'Downloads folder file path'
    os.chdir(path)
    files = sorted(os.listdir(os.getcwd()), key=os.path.getmtime)
    newest = files[-1]

    return newest

# Download zipfiles from Dolby Customer release, by xID and to folder
def download_content(site_url, language_name):
    downloaded=False

    print("----------")
    print("Handling: "+language_name)
    
    if not os.path.exists(language_name):
        os.makedirs(language_name)
    download_folder = os.path.abspath(language_name)

    # Create webdriver in headless mode to download to folder
    webdriver_options = webdriver.ChromeOptions()
    prefs = {"download.default_directory": download_folder}
    webdriver_options.add_experimental_option('prefs', prefs)
    #webdriver_options.add_argument('--headless=new')
    webdriver_options.add_argument('--incognito')
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=webdriver_options)

    driver.get(site_url)

    # Define Download button
    xpath_download_button = '//button[text()=" Download"]'
    # Define Language selection button
    xpath_selection_button = '//button[@aria-label="Select a language"]'

    # Define language entry on dropdown list
    # temp = "lntermdrpw34"
    # xpath_language_entry = '//ul[@class="c-menu"]/li[@id="%s"]'% str(temp)
    xpath_language_entry = '//p[text()="German"]/parent::*'

    wait = WebDriverWait(driver, 10)
    time.sleep(10)

    print("Selecting download language: "+language_name)
    try: 
        selection_button = wait.until(EC.element_to_be_clickable((By.XPATH, xpath_selection_button)))
    except:
        print ("No language selection")
        return (downloaded)
    try:
        selection_button.click()
    except Exception as e:
        print ("Failed to start selecting download language because: "+str(e))
        return (downloaded)
    
    print("Scrolling down to language: "+language_name)

    # language_entry = driver.find_element(By.XPATH, xpath_language_entry)
    language_entry = driver.find_element(By.XPATH, xpath_language_entry)

    try:
        driver.execute_script("arguments[0].scrollIntoView();", language_entry)
    except:
        print ("Failed to scroll to language")
        return (downloaded)
    
    time.sleep(10)
    
    print("Clicking language entry: "+language_name)
    try:
        language_entry.click()
    except Exception as e:
        print ("Failed to click language entry because: "+str(e))
        return (downloaded)

    
    print("Pressing Download button: "+language_name)
    try: 
        download_button = wait.until(EC.element_to_be_clickable((By.XPATH, xpath_download_button)))
    except:
        print ("No Download button")
        return (downloaded)
    try:
        download_button.click()
    except Exception as e:
        print ("Failed to press Download button because: "+str(e))
        return (downloaded)
    
    print("Downloading...")
    time.sleep(30)


    # Check if download has ended

    # fileends = "crdownload"
    # while "crdownload" == fileends:
    #     time.sleep(10)
    #     newest_file = latest_download_file(download_folder)
    #     if "crdownload" in newest_file:
    #         fileends = "crdownload"
    #     else:
    #         fileends = "none"

    downloaded=True
    print("Downloaded from page: "+driver.title)
    return(downloaded)


if __name__ == "__main__":

    assets = ['terminology', 'style_guide']
    languages = ['German']
    terminology_site = 'https://www.microsoft.com/language/Terminology'

    for language in languages:
        download_content(terminology_site, language)


