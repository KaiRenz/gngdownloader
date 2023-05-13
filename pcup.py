from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import os
import time
import shutil
import urllib.parse


def execute_pcup(config, driver, TimeoutInterval, downloads_folder_path, iracing_setup_folder_path):
    # Get pcup Setup links for each car
    array_pcup = []
    element_pcup_button = driver.find_element(By.XPATH, "//*[text()='PCUP']");
    element_pcup_button.click()
    WebDriverWait(driver,TimeoutInterval).until(EC.visibility_of_all_elements_located((By.CLASS_NAME, "cardgng")))
    elements_pcup = driver.find_elements(By.CLASS_NAME, "cardgng")
    for element_pcup in elements_pcup:
        element_pcup_track = element_pcup.find_element(By.CLASS_NAME, "p-4").find_element(By.CLASS_NAME, "pt-1").text
        element_pcup_car = element_pcup.find_element(By.CLASS_NAME, "p-4").find_element(By.CLASS_NAME, "pt-1.font-bold").text
        element_pcup_link = element_pcup.find_element(By.CLASS_NAME, "items-end").find_element(By.CSS_SELECTOR, "a").get_attribute('href')
        array_pcup.append([element_pcup_car, element_pcup_link.replace("/datapacks", "/#/datapacks"), element_pcup_track])
    print('[++] Track: ' + element_pcup_track)
    print('[++] Got the following cars: ')
    for car in array_pcup:
        print(car[0])

    if config['DEFAULT']['MoveToSetupFolder'] == "true":
        print('\n[+] MoveToSetupFolder is enabled - downloading and trying to move setup files...')
    else:
        print('\n[+] MoveToSetupFolder is disabled - downloading setup files...')        

    # Go to each pcup car and download the setups, the copy it to the correct location
    for pcupcar in array_pcup:
        driver.get(pcupcar[1].replace("/#/#", "/#"))
        WebDriverWait(driver,TimeoutInterval).until(EC.visibility_of_all_elements_located((By.XPATH, "//*[text()='Setup files']")))
        elems = driver.find_elements(By.XPATH, "//a[@href]")
        for elem in elems:
            if ".sto" in elem.get_attribute("href"):
                current_url = elem.get_attribute("href")
                sliced_url = current_url.split("?")[0].split("/")[-1]
                driver.get(current_url)
                # Move the downloaded setups to the correct folder if enabled
                if config['DEFAULT']['MoveToSetupFolder'] == "true":
                    # Check if file is there, otherwise might still be downloading
                    while not os.path.exists(downloads_folder_path + "/" + urllib.parse.unquote(urllib.parse.unquote(sliced_url))):
                        time.sleep(1)
                    # Now move it
                    try:
                        if pcupcar[0] == "Porsche 911 GT3 Cup (992)":
                            print('[++] Moving Porsche 911 GT3 Cup (992) setup (' + urllib.parse.unquote(urllib.parse.unquote(sliced_url)) + ') to ' + iracing_setup_folder_path + "\\" + "porsche992cup" + "\\" + pcupcar[2])
                            # Check if folder exisits, otherwise create it, then move
                            os.makedirs(iracing_setup_folder_path + "\\" + "porsche992cup", exist_ok=True)
                            os.makedirs(iracing_setup_folder_path + "\\" + "porsche992cup" + "\\" + pcupcar[2], exist_ok=True)
                            shutil.move((downloads_folder_path + "/" + urllib.parse.unquote(sliced_url)), iracing_setup_folder_path + "\\" + "porsche992cup" + "\\" + pcupcar[2] + "\\" + urllib.parse.unquote(sliced_url))
                    except:
                        pass
        driver.get("https://app.grid-and-go.com/")
        # Wait until page is loaded. We do that by checking for the pcup Series Button
        WebDriverWait(driver,TimeoutInterval).until(EC.visibility_of_all_elements_located((By.XPATH, "//*[text()='PCUP']")))
