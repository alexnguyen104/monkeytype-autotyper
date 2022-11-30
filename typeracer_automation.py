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

def typing():
    first_word = driver.find_element(
        By.XPATH, '//*[@id="gwt-uid-20"]/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table/tbody/tr[1]/td/div/div').text

    words = (first_word + driver.find_element(
        By.XPATH, '//*[@id="gwt-uid-20"]/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table/tbody/tr[1]/td/div/div/span[3]').text).split(" ")


    input_section = driver.find_element(By.CLASS_NAME, "txtInput")
    for i in range(len(words)):
        for j in words[i]:
            input_section.send_keys(j) 
            if(i == len(words)/2 and j == "."):
                return
            print(len(words))
            print(words)
            print(i)
            print(j)

            sleep(0.05)
        
        input_section.send_keys(" ")

# words = driver.find_element(By.ID, "words").text.split("\n")
# word_input = driver.find_element(By.ID, "wordsInput")
# word_index = 0

typing()
command = input("PRESS ENTER TO QUIT")

driver.quit()
sys.exit()
