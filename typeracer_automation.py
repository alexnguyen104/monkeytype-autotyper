import sys
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException

def typing():
    words = driver.find_element(By.XPATH, '//*[@id="gwt-uid-20"]/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table/tbody/tr[1]/td/div/div').text
    input_section = driver.find_element(By.CLASS_NAME, "txtInput")

    for i in range(len(words)):
        for j in words[i]:
            input_section.send_keys(j)
            if(i == len(words)-1 and j == "."):
                return
            sleep(0.05)

# Settings
options = Options()
options.add_experimental_option("excludeSwitches", ["enable-logging"]) #disable logging messages

driver = webdriver.Chrome(service=Service(
    ChromeDriverManager().install()),options=options)

driver.get("https://play.typeracer.com/")

while True:
    input("PRESS ENTER TO START...\n")
    try:
        typing()
        break
    except NoSuchElementException:
        print("Enter a game to start")
    except ElementNotInteractableException:
        print("Wait for the game to start")

input("PRESS ENTER TO QUIT...")

driver.quit()
sys.exit()
