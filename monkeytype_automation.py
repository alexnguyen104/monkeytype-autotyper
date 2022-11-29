import sys
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://monkeytype.com/")

sleep(0.5)

close_cookie_btn = driver.find_element(By.CLASS_NAME, "rejectAll")
close_cookie_btn.click()

words = driver.find_element(By.ID, "words")


command = input("PRESS ENTER TO QUIT")

driver.quit()
sys.exit()
