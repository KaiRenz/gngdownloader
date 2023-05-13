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


def execute_nec(config, driver, TimeoutInterval, downloads_folder_path, iracing_setup_folder_path):
    # Get NEC Setup links for each car
    array_nec = []
    element_nec_button = driver.find_element(By.XPATH, "//*[text()='NEC']");
    element_nec_button.click()
    WebDriverWait(driver,TimeoutInterval).until(EC.visibility_of_all_elements_located((By.CLASS_NAME, "cardgng")))
    elements_nec = driver.find_elements(By.CLASS_NAME, "cardgng")
    for element_nec in elements_nec:
        element_nec_track = element_nec.find_element(By.CLASS_NAME, "p-4").find_element(By.CLASS_NAME, "pt-1").text
        element_nec_car = element_nec.find_element(By.CLASS_NAME, "p-4").find_element(By.CLASS_NAME, "pt-1.font-bold").text
        element_nec_link = element_nec.find_element(By.CLASS_NAME, "items-end").find_element(By.CSS_SELECTOR, "a").get_attribute('href')
        array_nec.append([element_nec_car, element_nec_link.replace("/datapacks", "/#/datapacks"), element_nec_track])
    print('[++] Track: ' + element_nec_track)
    print('[++] Got the following cars: ')
    for car in array_nec:
        print(car[0])

    if config['DEFAULT']['MoveToSetupFolder'] == "true":
        print('\n[+] MoveToSetupFolder is enabled - downloading and trying to move setup files...')
    else:
        print('\n[+] MoveToSetupFolder is disabled - downloading setup files...')        

    # Go to each NEC car and download the setups, the copy it to the correct location
    for neccar in array_nec:
        driver.get(neccar[1].replace("/#/#", "/#"))
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
                        if neccar[0] == "Aston Martin Vantage GT4":
                            print('[++] Moving Aston Martin Vantage GT4 setup (' + urllib.parse.unquote(urllib.parse.unquote(sliced_url)) + ') to ' + iracing_setup_folder_path + "\\" + "amvantagegt4" + "\\" + neccar[2])
                            # Check if folder exisits, otherwise create it, then move
                            os.makedirs(iracing_setup_folder_path + "\\" + "amvantagegt4", exist_ok=True)
                            os.makedirs(iracing_setup_folder_path + "\\" + "amvantagegt4" + "\\" + neccar[2], exist_ok=True)
                            shutil.move((downloads_folder_path + "/" + urllib.parse.unquote(sliced_url)), iracing_setup_folder_path + "\\" + "amvantagegt4" + "\\" + neccar[2] + "\\" + urllib.parse.unquote(sliced_url))
                        elif neccar[0] == "Audi RS 3 LMS":
                            print('[++] Moving Audi RS 3 LMS setup (' + urllib.parse.unquote(urllib.parse.unquote(sliced_url)) + ') to ' + iracing_setup_folder_path + "\\" + "audirs3lms" + "\\" + neccar[2])
                            # Check if folder exisits, otherwise create it, then move
                            os.makedirs(iracing_setup_folder_path + "\\" + "audirs3lms", exist_ok=True)
                            os.makedirs(iracing_setup_folder_path + "\\" + "audirs3lms" + "\\" + neccar[2], exist_ok=True)
                            shutil.move((downloads_folder_path + "/" + urllib.parse.unquote(sliced_url)), iracing_setup_folder_path + "\\" + "audirs3lms" + "\\" + neccar[2] + "\\" + urllib.parse.unquote(sliced_url))
                        elif neccar[0] == "BMW M4 GT3":
                            print('[++] Moving BMW M4 GT3 setup (' + urllib.parse.unquote(urllib.parse.unquote(sliced_url)) + ') to ' + iracing_setup_folder_path + "\\" + "bmwm4gt3" + "\\" + neccar[2])
                            # Check if folder exisits, otherwise create it, then move
                            os.makedirs(iracing_setup_folder_path + "\\" + "bmwm4gt3", exist_ok=True)
                            os.makedirs(iracing_setup_folder_path + "\\" + "bmwm4gt3" + "\\" + neccar[2], exist_ok=True)
                            shutil.move((downloads_folder_path + "/" + urllib.parse.unquote(sliced_url)), iracing_setup_folder_path + "\\" + "bmwm4gt3" + "\\" + neccar[2] + "\\" + urllib.parse.unquote(sliced_url))
                        elif neccar[0] == "Mercedes-AMG GT3 2020":
                            print('[++] Moving Mercedes-AMG GT3 2020 setup (' + urllib.parse.unquote(urllib.parse.unquote(sliced_url)) + ') to ' + iracing_setup_folder_path + "\\" + "mercedesamgevogt3" + "\\" + neccar[2])
                            # Check if folder exisits, otherwise create it, then move
                            os.makedirs(iracing_setup_folder_path + "\\" + "mercedesamgevogt3", exist_ok=True)
                            os.makedirs(iracing_setup_folder_path + "\\" + "mercedesamgevogt3" + "\\" + neccar[2], exist_ok=True)
                            shutil.move((downloads_folder_path + "/" + urllib.parse.unquote(sliced_url)), iracing_setup_folder_path + "\\" + "mercedesamgevogt3" + "\\" + neccar[2] + "\\" + urllib.parse.unquote(sliced_url))
                        elif neccar[0] == "Porsche 718 Cayman GT4 Clubsport MR":
                            print('[++] Moving Porsche 718 Cayman GT4 Clubsport MR setup (' + urllib.parse.unquote(urllib.parse.unquote(sliced_url)) + ') to ' + iracing_setup_folder_path + "\\" + "porsche718gt4" + "\\" + neccar[2])
                            # Check if folder exisits, otherwise create it, then move
                            os.makedirs(iracing_setup_folder_path + "\\" + "porsche718gt4", exist_ok=True)
                            os.makedirs(iracing_setup_folder_path + "\\" + "porsche718gt4" + "\\" + neccar[2], exist_ok=True)
                            shutil.move((downloads_folder_path + "/" + urllib.parse.unquote(sliced_url)), iracing_setup_folder_path + "\\" + "porsche718gt4" + "\\" + neccar[2] + "\\" + urllib.parse.unquote(sliced_url))
                        elif neccar[0] == "Porsche 911 GT3 Cup (992)":
                            print('[++] Moving Porsche 911 GT3 Cup (992) setup (' + urllib.parse.unquote(urllib.parse.unquote(sliced_url)) + ') to ' + iracing_setup_folder_path + "\\" + "porsche992cup" + "\\" + neccar[2])
                            # Check if folder exisits, otherwise create it, then move
                            os.makedirs(iracing_setup_folder_path + "\\" + "porsche992cup", exist_ok=True)
                            os.makedirs(iracing_setup_folder_path + "\\" + "porsche992cup" + "\\" + neccar[2], exist_ok=True)
                            shutil.move((downloads_folder_path + "/" + urllib.parse.unquote(sliced_url)), iracing_setup_folder_path + "\\" + "porsche992cup" + "\\" + neccar[2] + "\\" + urllib.parse.unquote(sliced_url))
                        elif neccar[0] == "Toyota GR86":
                            print('[++] Moving Toyota GR86 setup (' + urllib.parse.unquote(urllib.parse.unquote(sliced_url)) + ') to ' + iracing_setup_folder_path + "\\" + "toyotagr86" + "\\" + neccar[2])
                            # Check if folder exisits, otherwise create it, then move
                            os.makedirs(iracing_setup_folder_path + "\\" + "toyotagr86", exist_ok=True)
                            os.makedirs(iracing_setup_folder_path + "\\" + "toyotagr86" + "\\" + neccar[2], exist_ok=True)
                            shutil.move((downloads_folder_path + "/" + urllib.parse.unquote(sliced_url)), iracing_setup_folder_path + "\\" + "toyotagr86" + "\\" + neccar[2] + "\\" + urllib.parse.unquote(sliced_url))
                        elif neccar[0] == "Porsche 911 GT3 R":
                            print('[++] Moving Porsche 911 GT3 R setup (' + urllib.parse.unquote(urllib.parse.unquote(sliced_url)) + ') to ' + iracing_setup_folder_path + "\\" + "porsche911rgt3" + "\\" + neccar[2])
                            # Check if folder exisits, otherwise create it, then move
                            os.makedirs(iracing_setup_folder_path + "\\" + "porsche911rgt3", exist_ok=True)
                            os.makedirs(iracing_setup_folder_path + "\\" + "porsche911rgt3" + "\\" + neccar[2], exist_ok=True)
                            shutil.move((downloads_folder_path + "/" + urllib.parse.unquote(sliced_url)), iracing_setup_folder_path + "\\" + "porsche911rgt3" + "\\" + neccar[2] + "\\" + urllib.parse.unquote(sliced_url))
                    except:
                        pass
        driver.get("https://app.grid-and-go.com/")
        # Wait until page is loaded. We do that by checking for the NEC Series Button
        WebDriverWait(driver,TimeoutInterval).until(EC.visibility_of_all_elements_located((By.XPATH, "//*[text()='NEC']")))
