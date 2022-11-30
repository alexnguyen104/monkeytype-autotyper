import sys
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=Service(
    ChromeDriverManager().install()))
driver.get("https://play.typeracer.com/")

sleep(1)

start_game_btn = driver.find_element(By.XPATH, '//*[@id="gwt-uid-1"]/a')
start_game_btn.click()

input("PRESS ENTER TO START")

first_word = driver.find_element(
    By.XPATH, '//*[@id="gwt-uid-20"]/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table/tbody/tr[1]/td/div/div').text

words = (first_word + driver.find_element(
    By.XPATH, '//*[@id="gwt-uid-20"]/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table/tbody/tr[1]/td/div/div/span[3]').text + " endhere").split(" ")


input_section = driver.find_element(By.CLASS_NAME, "txtInput")

for i in words:
    if(i == "endhere"):
        print("bye")
        break
    for j in i:
        input_section.send_keys(j)
        sleep(0.05)
    input_section.send_keys(" ")

# words = driver.find_element(By.ID, "words").text.split("\n")
# word_input = driver.find_element(By.ID, "wordsInput")
# word_index = 0


command = input("PRESS ENTER TO QUIT")

driver.quit()
sys.exit()
