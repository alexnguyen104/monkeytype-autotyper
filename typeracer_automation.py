import sys
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def get_words():
    first_word = driver.find_element(
        By.XPATH, '//*[@id="gwt-uid-20"]/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table/tbody/tr[1]/td/div/div').text
    # words = wait.until(EC.visibility_of_element_located(
    #     (By.XPATH, '//*[@id="gwt-uid-20"]/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table/tbody/tr[1]/td/div/div/span[3]'))).text
    try:
        words = driver.find_element(
            By.XPATH, '//*[@id="gwt-uid-20"]/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table/tbody/tr[1]/td/div/div/span[3]').text
    except Exception:
        words = driver.find_element(
            By.XPATH, '//*[@id="gwt-uid-20"]/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table/tbody/tr[1]/td/div/div/span[2]').text
    return first_word + words


def typing():
    words = get_words()
    input_section = driver.find_element(By.CLASS_NAME, "txtInput")
    for i in range(len(words)):
        for j in words[i]:
            input_section.send_keys(j)
            if(i == len(words)/2 and j == "."):
                return

            sleep(0.05)

        input_section.send_keys(" ")


driver = webdriver.Chrome(service=Service(
    ChromeDriverManager().install()))
driver.get("https://play.typeracer.com/")

# wait = WebDriverWait(driver, 2)

input("PRESS ENTER TO START")
typing()

command = input("PRESS ENTER TO QUIT")

driver.quit()
sys.exit()
