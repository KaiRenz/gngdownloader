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


def execute_gt_sprint(config, driver, TimeoutInterval, downloads_folder_path, iracing_setup_folder_path):
    # Get GT-Sprint Setup links for each car
    array_gtsprint = []
    element_gtsprint_button = driver.find_element(By.XPATH, "//*[text()='GT-Sprint']");
    element_gtsprint_button.click()
    WebDriverWait(driver,TimeoutInterval).until(EC.visibility_of_all_elements_located((By.CLASS_NAME, "cardgng")))
    elements_gtsprint = driver.find_elements(By.CLASS_NAME, "cardgng")
    for element_gtsprint in elements_gtsprint:
        element_gtsprint_track = element_gtsprint.find_element(By.CLASS_NAME, "p-4").find_element(By.CLASS_NAME, "pt-1").text
        element_gtsprint_car = element_gtsprint.find_element(By.CLASS_NAME, "p-4").find_element(By.CLASS_NAME, "pt-1.font-bold").text
        element_gtsprint_link = element_gtsprint.find_element(By.CLASS_NAME, "items-end").find_element(By.CSS_SELECTOR, "a").get_attribute('href')
        array_gtsprint.append([element_gtsprint_car, element_gtsprint_link.replace("/datapacks", "/#/datapacks"), element_gtsprint_track])
    print('[++] Track: ' + element_gtsprint_track)
    print('[++] Got the following cars: ')
    for car in array_gtsprint:
        print(car[0])

    if config['DEFAULT']['MoveToSetupFolder'] == "true":
        print('\n[+] MoveToSetupFolder is enabled - downloading and trying to move setup files...')
    else:
        print('\n[+] MoveToSetupFolder is disabled - downloading setup files...')        

    # Go to each GT-Sprint car and download the setups, the copy it to the correct location
    for gtsprintcar in array_gtsprint:
        driver.get(gtsprintcar[1])
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
                        if gtsprintcar[0] == "Audi R8 LMS GT3":
                            print('[++] Moving Audi R8 LMS GT3 setup (' + urllib.parse.unquote(sliced_url) + ') to ' + iracing_setup_folder_path + "\\" + "audir8gt3" + "\\" + gtsprintcar[2])
                            # Check if folder exisits, otherwise create it, then move
                            os.makedirs(iracing_setup_folder_path + "\\" + "audir8gt3", exist_ok=True)
                            os.makedirs(iracing_setup_folder_path + "\\" + "audir8gt3" + "\\" + gtsprintcar[2], exist_ok=True)
                            shutil.move((downloads_folder_path + "/" + urllib.parse.unquote(sliced_url)), iracing_setup_folder_path + "\\" + "audir8gt3" + "\\" + gtsprintcar[2] + "\\" + urllib.parse.unquote(sliced_url))
                        elif gtsprintcar[0] == "BMW M4 GT3":
                            print('[++] Moving BMW M4 GT3 setup (' + urllib.parse.unquote(sliced_url) + ') to ' + iracing_setup_folder_path + "\\" + "bmwm4gt3" + "\\" + gtsprintcar[2])
                            # Check if folder exisits, otherwise create it, then move
                            os.makedirs(iracing_setup_folder_path + "\\" + "bmwm4gt3", exist_ok=True)
                            os.makedirs(iracing_setup_folder_path + "\\" + "bmwm4gt3" + "\\" + gtsprintcar[2], exist_ok=True)
                            shutil.move((downloads_folder_path + "/" + urllib.parse.unquote(sliced_url)), iracing_setup_folder_path + "\\" + "bmwm4gt3" + "\\" + gtsprintcar[2] + "\\" + urllib.parse.unquote(sliced_url))
                        elif gtsprintcar[0] == "Ferrari 488 GT3 Evo 2020":
                            print('[++] Moving Ferrari 488 GT3 Evo 2020 setup (' + urllib.parse.unquote(sliced_url) + ') to ' + iracing_setup_folder_path + "\\" + "ferrarievogt3" + "\\" + gtsprintcar[2])
                            # Check if folder exisits, otherwise create it, then move
                            os.makedirs(iracing_setup_folder_path + "\\" + "ferrarievogt3", exist_ok=True)
                            os.makedirs(iracing_setup_folder_path + "\\" + "ferrarievogt3" + "\\" + gtsprintcar[2], exist_ok=True)
                            shutil.move((downloads_folder_path + "/" + urllib.parse.unquote(sliced_url)), iracing_setup_folder_path + "\\" + "ferrarievogt3" + "\\" + gtsprintcar[2] + "\\" + urllib.parse.unquote(sliced_url))
                        elif gtsprintcar[0] == "Lamborghini Huracán GT3 EVO":
                            print('[++] Moving Lamborghini Huracán GT3 EVO setup (' + urllib.parse.unquote(sliced_url) + ') to ' + iracing_setup_folder_path + "\\" + "lamborghinievogt3" + "\\" + gtsprintcar[2])
                            # Check if folder exisits, otherwise create it, then move
                            os.makedirs(iracing_setup_folder_path + "\\" + "lamborghinievogt3", exist_ok=True)
                            os.makedirs(iracing_setup_folder_path + "\\" + "lamborghinievogt3" + "\\" + gtsprintcar[2], exist_ok=True)
                            shutil.move((downloads_folder_path + "/" + urllib.parse.unquote(sliced_url)), iracing_setup_folder_path + "\\" + "lamborghinievogt3" + "\\" + gtsprintcar[2] + "\\" + urllib.parse.unquote(sliced_url))
                        elif gtsprintcar[0] == "McLaren MP4-12C GT3":
                            print('[++] Moving McLaren MP4-12C GT3 setup (' + urllib.parse.unquote(sliced_url) + ') to ' + iracing_setup_folder_path + "\\" + "mclarenmp4" + "\\" + gtsprintcar[2])
                            # Check if folder exisits, otherwise create it, then move
                            os.makedirs(iracing_setup_folder_path + "\\" + "mclarenmp4", exist_ok=True)
                            os.makedirs(iracing_setup_folder_path + "\\" + "mclarenmp4" + "\\" + gtsprintcar[2], exist_ok=True)
                            shutil.move((downloads_folder_path + "/" + urllib.parse.unquote(sliced_url)), iracing_setup_folder_path + "\\" + "mclarenmp4" + "\\" + gtsprintcar[2] + "\\" + urllib.parse.unquote(sliced_url))
                        elif gtsprintcar[0] == "Mercedes-AMG GT3 2020":
                            print('[++] Moving Mercedes-AMG GT3 2020 setup (' + urllib.parse.unquote(sliced_url) + ') to ' + iracing_setup_folder_path + "\\" + "mercedesamgevogt3" + "\\" + gtsprintcar[2])
                            # Check if folder exisits, otherwise create it, then move
                            os.makedirs(iracing_setup_folder_path + "\\" + "mercedesamgevogt3", exist_ok=True)
                            os.makedirs(iracing_setup_folder_path + "\\" + "mercedesamgevogt3" + "\\" + gtsprintcar[2], exist_ok=True)
                            shutil.move((downloads_folder_path + "/" + urllib.parse.unquote(sliced_url)), iracing_setup_folder_path + "\\" + "mercedesamgevogt3" + "\\" + gtsprintcar[2] + "\\" + urllib.parse.unquote(sliced_url))
                        elif gtsprintcar[0] == "Porsche 911 GT3 R":
                            print('[++] Moving Porsche 911 GT3 R setup (' + urllib.parse.unquote(sliced_url) + ') to ' + iracing_setup_folder_path + "\\" + "porsche911rgt3" + "\\" + gtsprintcar[2])
                            # Check if folder exisits, otherwise create it, then move
                            os.makedirs(iracing_setup_folder_path + "\\" + "porsche911rgt3", exist_ok=True)
                            os.makedirs(iracing_setup_folder_path + "\\" + "porsche911rgt3" + "\\" + gtsprintcar[2], exist_ok=True)
                            shutil.move((downloads_folder_path + "/" + urllib.parse.unquote(sliced_url)), iracing_setup_folder_path + "\\" + "porsche911rgt3" + "\\" + gtsprintcar[2] + "\\" + urllib.parse.unquote(sliced_url))
                    except:
                        pass
        driver.get("https://app.grid-and-go.com/")
        # Wait until page is loaded. We do that by checking for the GT-Sprint Series Button
        WebDriverWait(driver,TimeoutInterval).until(EC.visibility_of_all_elements_located((By.XPATH, "//*[text()='GT-Sprint']")))