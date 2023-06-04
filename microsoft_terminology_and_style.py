
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

    # Define Reject button for Microsoft page cookies
    xpath_reject_button = "//button[text()='Reject']"
    print("Waiting for cookie popup...")
    reject_button = wait.until(EC.element_to_be_clickable((By.XPATH, xpath_reject_button)))
    reject_button.click()
    print("Cookies rejected successfully...")

# Check what is the latest downloaded file in path
def latest_download_file(path):
    os.chdir(path)
    files = sorted(os.listdir(os.getcwd()), key=os.path.getmtime)
    newest = files[-1]

    return newest

# Download files from Microsoft Language Portal, by sub-page and language name
def download_content(site_url, languages_list):

    # Define Download button
    xpath_download_button = '//button[normalize-space()="Download"]'

    # Define Language selection button
    xpath_selection_button = '//button[@aria-label="Select a language"]'

    download_name = 'microsoft_assets'
            
    if not os.path.exists(download_name):
        os.makedirs(download_name)
    download_folder = os.path.abspath(download_name)

    # Create webdriver in headless mode to download to folder
    webdriver_options = webdriver.ChromeOptions()
    prefs = {"download.default_directory": download_folder}
    webdriver_options.add_experimental_option('prefs', prefs)
    webdriver_options.add_argument('--headless=new')
    webdriver_options.add_argument('--incognito')
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=webdriver_options)

    driver.get(site_url)
    driver.maximize_window()
    wait = WebDriverWait(driver, 10)
    
    time.sleep(10)
    reject_cookies(driver)
    
    # Loop download for each language
    for language_name in languages_list:

        downloaded=False

        print("----------")
        print("Handling: "+language_name+" "+site_url)

        # Add subfolder per language?

        # Define language entry on dropdown list
        xpath_language_entry = '//p[text()="%s"]/ancestor::li'% str(language_name)

        time.sleep(10)

        print("Selecting download language: "+language_name)
        try: 
            selection_button = wait.until(EC.element_to_be_clickable((By.XPATH, xpath_selection_button)))
        except:
            print ("No language selection")
            return (downloaded)
        
        print("Giving focus to selection button")
        try:
            driver.execute_script("arguments[0].focus();", selection_button)
        except:
            print ("No focus to selection button")
            return (downloaded)

        try:
            selection_button.click()
        except Exception as e:
            print ("Failed to start selecting download language because: "+str(e))
            return (downloaded)
        
        print("Scrolling down to language: "+language_name)

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

        # Rename file per language name
        newest_file = latest_download_file(download_folder)
        file_name = os.path.splitext(newest_file)[0]
        file_ext = os.path.splitext(newest_file)[1]
        file_rename = file_name+"_"+language_name+file_ext

        # Force rename if file already existed
        try:
            os.rename(newest_file, file_rename)
        except FileExistsError:
            print("File already exists, removing existing file: "+file_rename)
            print("Removing existing file")
            os.remove(file_rename)
            os.rename(newest_file, file_rename)

        # Check if download has ended
        # Makes sense for large downloads

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


if __name__ == "__main__":

    # LIST OF LANGUAGES AS USED ON https://www.microsoft.com/language/Terminology
    languages = ['Arabic','German','Polish']
    
    terminology = 'https://www.microsoft.com/language/Terminology'
    styleguides = 'https://www.microsoft.com/language/StyleGuides'

    assets = [terminology, styleguides]

    for asset in assets:
        started_in = os.getcwd()
        download_content(asset, languages)
        os.chdir(started_in)
