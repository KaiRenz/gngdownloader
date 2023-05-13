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


def execute_gt4_challenge(config, driver, TimeoutInterval, downloads_folder_path, iracing_setup_folder_path):
    # Get GT4-Challenge Setup links for each car
    array_gt4challenge = []
    element_gt4challenge_button = driver.find_element(By.XPATH, "//*[text()='GT4-Challenge']");
    element_gt4challenge_button.click()
    WebDriverWait(driver,TimeoutInterval).until(EC.visibility_of_all_elements_located((By.CLASS_NAME, "cardgng")))
    elements_gt4challenge = driver.find_elements(By.CLASS_NAME, "cardgng")
    for element_gt4challenge in elements_gt4challenge:
        element_gt4challenge_track = element_gt4challenge.find_element(By.CLASS_NAME, "p-4").find_element(By.CLASS_NAME, "pt-1").text
        element_gt4challenge_car = element_gt4challenge.find_element(By.CLASS_NAME, "p-4").find_element(By.CLASS_NAME, "pt-1.font-bold").text
        element_gt4challenge_link = element_gt4challenge.find_element(By.CLASS_NAME, "items-end").find_element(By.CSS_SELECTOR, "a").get_attribute('href')
        array_gt4challenge.append([element_gt4challenge_car, element_gt4challenge_link.replace("/datapacks", "/#/datapacks"), element_gt4challenge_track])
    print('[++] Track: ' + element_gt4challenge_track)
    print('[++] Got the following cars: ')
    for car in array_gt4challenge:
        print(car[0])

    if config['DEFAULT']['MoveToSetupFolder'] == "true":
        print('\n[+] MoveToSetupFolder is enabled - downloading and trying to move setup files...')
    else:
        print('\n[+] MoveToSetupFolder is disabled - downloading setup files...')        

    # Go to each GT4-Challenge car and download the setups, the copy it to the correct location
    for gt4challengecar in array_gt4challenge:
        driver.get(gt4challengecar[1].replace("/#/#", "/#"))
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
                        if gt4challengecar[0] == "Aston Martin Vantage GT4":
                            print('[++] Moving Aston Martin Vantage GT4 setup (' + urllib.parse.unquote(sliced_url) + ') to ' + iracing_setup_folder_path + "\\" + "amvantagegt4" + "\\" + gt4challengecar[2])
                            # Check if folder exisits, otherwise create it, then move
                            os.makedirs(iracing_setup_folder_path + "\\" + "amvantagegt4", exist_ok=True)
                            os.makedirs(iracing_setup_folder_path + "\\" + "amvantagegt4" + "\\" + gt4challengecar[2], exist_ok=True)
                            shutil.move((downloads_folder_path + "/" + urllib.parse.unquote(sliced_url)), iracing_setup_folder_path + "\\" + "amvantagegt4" + "\\" + gt4challengecar[2] + "\\" + urllib.parse.unquote(sliced_url))
                        elif gt4challengecar[0] == "BMW M4 GT4":
                            print('[++] Moving BMW M4 GT4 setup (' + urllib.parse.unquote(sliced_url) + ') to ' + iracing_setup_folder_path + "\\" + "bmwm4gt4" + "\\" + gt4challengecar[2])
                            # Check if folder exisits, otherwise create it, then move
                            os.makedirs(iracing_setup_folder_path + "\\" + "bmwm4gt4", exist_ok=True)
                            os.makedirs(iracing_setup_folder_path + "\\" + "bmwm4gt4" + "\\" + gt4challengecar[2], exist_ok=True)
                            shutil.move((downloads_folder_path + "/" + urllib.parse.unquote(sliced_url)), iracing_setup_folder_path + "\\" + "bmwm4gt4" + "\\" + gt4challengecar[2] + "\\" + urllib.parse.unquote(sliced_url))
                        elif gt4challengecar[0] == "McLaren 570S GT4":
                            print('[++] Moving McLaren 570S GT4 setup (' + urllib.parse.unquote(sliced_url) + ') to ' + iracing_setup_folder_path + "\\" + "mclarenmp4" + "\\" + gt4challengecar[2])
                            # Check if folder exisits, otherwise create it, then move
                            os.makedirs(iracing_setup_folder_path + "\\" + "mclarenmp4", exist_ok=True)
                            os.makedirs(iracing_setup_folder_path + "\\" + "mclarenmp4" + "\\" + gt4challengecar[2], exist_ok=True)
                            shutil.move((downloads_folder_path + "/" + urllib.parse.unquote(sliced_url)), iracing_setup_folder_path + "\\" + "mclarenmp4" + "\\" + gt4challengecar[2] + "\\" + urllib.parse.unquote(sliced_url))
                        elif gt4challengecar[0] == "Mercedes-AMG GT4":
                            print('[++] Moving Mercedes-AMG GT4 setup (' + urllib.parse.unquote(sliced_url) + ') to ' + iracing_setup_folder_path + "\\" + "mercedesamggt4" + "\\" + gt4challengecar[2])
                            # Check if folder exisits, otherwise create it, then move
                            os.makedirs(iracing_setup_folder_path + "\\" + "mercedesamggt4", exist_ok=True)
                            os.makedirs(iracing_setup_folder_path + "\\" + "mercedesamggt4" + "\\" + gt4challengecar[2], exist_ok=True)
                            shutil.move((downloads_folder_path + "/" + urllib.parse.unquote(sliced_url)), iracing_setup_folder_path + "\\" + "mercedesamggt4" + "\\" + gt4challengecar[2] + "\\" + urllib.parse.unquote(sliced_url))
                        elif gt4challengecar[0] == "Porsche 718 Cayman GT4 Clubsport MR":
                            print('[++] Moving Porsche 718 Cayman GT4 Clubsport MR setup (' + urllib.parse.unquote(sliced_url) + ') to ' + iracing_setup_folder_path + "\\" + "porsche718gt4" + "\\" + gt4challengecar[2])
                            # Check if folder exisits, otherwise create it, then move
                            os.makedirs(iracing_setup_folder_path + "\\" + "porsche718gt4", exist_ok=True)
                            os.makedirs(iracing_setup_folder_path + "\\" + "porsche718gt4" + "\\" + gt4challengecar[2], exist_ok=True)
                            shutil.move((downloads_folder_path + "/" + urllib.parse.unquote(sliced_url)), iracing_setup_folder_path + "\\" + "porsche718gt4" + "\\" + gt4challengecar[2] + "\\" + urllib.parse.unquote(sliced_url))
                    except:
                        pass
        driver.get("https://app.grid-and-go.com/")
        # Wait until page is loaded. We do that by checking for the GT4-Challenge Series Button
        WebDriverWait(driver,TimeoutInterval).until(EC.visibility_of_all_elements_located((By.XPATH, "//*[text()='GT4-Challenge']")))
