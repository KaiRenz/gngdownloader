from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import configparser
import shutil
import os
import time
from art import *
from gtsprint import execute_gt_sprint
from gt4challenge import execute_gt4_challenge
from imsa import execute_imsa
from nec import execute_nec
from pcup import execute_pcup


# Initialization
config = configparser.RawConfigParser()
chrome_options = Options()
chrome_options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36')
chrome_options.add_argument('--headless=new')
chrome_options.add_argument('--disable-logging') 
chrome_options.add_argument('--log-level=3')
driver = webdriver.Chrome(options=chrome_options)
config.read('config.ini')
TimeoutInterval = config['DEFAULT']['TimeoutInterval']
downloads_folder_path = config['VARIABLES']['downloads_folder_path']
iracing_setup_folder_path = config['VARIABLES']['iracing_setup_path']

# Start
Art=text2art("GNGdownloader", font='small')
print(Art)
print('[+] Starting up...')

# Signin
print('[+] Signing in to app.grid-and-go.com')
driver.get("https://app.grid-and-go.com/")
driver.find_element(By.XPATH, "//*[text()='Sign in']").click()
element_username = driver.find_element(By.NAME, "username")
element_username.send_keys(config['GNGUSER']['username'])
element_password = driver.find_element(By.NAME, "password")
element_password.send_keys(config['GNGUSER']['password'])
element_singin = driver.find_element(By.NAME, "signInSubmitButton")
element_singin.click()

# Wait until page is loaded. We do that by checking for the GT-Sprint Series Button
WebDriverWait(driver,TimeoutInterval).until(EC.visibility_of_all_elements_located((By.XPATH, "//*[text()='GT-Sprint']")))

# GT-Sprint
if config['SERIES']['gt-sprint'] == "true":
    print('\n[+] Getting GT-Sprint setups')
    execute_gt_sprint(config, driver, TimeoutInterval, downloads_folder_path, iracing_setup_folder_path)

# GT4-Challenge
if config['SERIES']['gt4-challenge'] == "true":
    print('\n[+] Getting GT4-Challenge setups')
    execute_gt4_challenge(config, driver, TimeoutInterval, downloads_folder_path, iracing_setup_folder_path)

# IMSA
if config['SERIES']['imsa'] == "true":
    print('\n[+] Getting IMSA setups')
    execute_imsa(config, driver, TimeoutInterval, downloads_folder_path, iracing_setup_folder_path)

# NEC
if config['SERIES']['nec'] == "true":
    print('\n[+] Getting NEC setups')
    execute_nec(config, driver, TimeoutInterval, downloads_folder_path, iracing_setup_folder_path)

# PCUP
if config['SERIES']['pcup'] == "true":
    print('\n[+] Getting PCUP setups')
    execute_pcup(config, driver, TimeoutInterval, downloads_folder_path, iracing_setup_folder_path)


print('\n[+] ALL DONE [+]\n')
driver.close()
