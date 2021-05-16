from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

link = "https://www.kahoot.it"
code = input("Enter Game Code: ")
name = input("Enter Nickname: ")

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")
chromedriver = "C:/Users/Abhi/Downloads/chromedriver_win32/chromedriver.exe"
driver1 = webdriver.Chrome(chromedriver,chrome_options=chrome_options)
driver2 = webdriver.Chrome(chromedriver,chrome_options=chrome_options)
driver3 = webdriver.Chrome(chromedriver,chrome_options=chrome_options)
driver4 = webdriver.Chrome(chromedriver,chrome_options=chrome_options)
driver5 = webdriver.Chrome(chromedriver,chrome_options=chrome_options)

driver1.get(link)
driver2.get(link)
driver3.get(link)
driver4.get(link)
driver5.get(link)
time.sleep(5)

search = driver1.find_element_by_id("game-input")
search.send_keys(code)
search.send_keys(Keys.RETURN)
search = driver2.find_element_by_id("game-input")
search.send_keys(code)
search.send_keys(Keys.RETURN)
search = driver3.find_element_by_id("game-input")
search.send_keys(code)
search.send_keys(Keys.RETURN)
search = driver4.find_element_by_id("game-input")
search.send_keys(code)
search.send_keys(Keys.RETURN)
search = driver5.find_element_by_id("game-input")
search.send_keys(code)
search.send_keys(Keys.RETURN)

time.sleep(5)

search = driver1.find_element_by_id("nickname")
search.send_keys(name + "1")
search.send_keys(Keys.RETURN)
search = driver2.find_element_by_id("nickname")
search.send_keys(name + "2")
search.send_keys(Keys.RETURN)
search = driver3.find_element_by_id("nickname")
search.send_keys(name + "3")
search.send_keys(Keys.RETURN)
search = driver4.find_element_by_id("nickname")
search.send_keys(name + "4")
search.send_keys(Keys.RETURN)
search = driver5.find_element_by_id("nickname")
search.send_keys(name + "5")
search.send_keys(Keys.RETURN)

choice = "0"

while True:
    choice = input("Enter Choice: ")

    if choice == "0":
        break

    if choice == "1":
        button1 = driver1.find_element_by_id("triangle-button")
        button2 = driver2.find_element_by_id("triangle-button")
        button3 = driver3.find_element_by_id("triangle-button")
        button4 = driver4.find_element_by_id("triangle-button")
        button5 = driver5.find_element_by_id("triangle-button")
        button1.click()
        button2.click()
        button3.click()
        button4.click()
        button5.click()

    if choice == "2":
        button1 = driver1.find_element_by_id("diamond-button")
        button2 = driver2.find_element_by_id("diamond-button")
        button3 = driver3.find_element_by_id("diamond-button")
        button4 = driver4.find_element_by_id("diamond-button")
        button5 = driver5.find_element_by_id("diamond-button")
        button1.click()
        button2.click()
        button3.click()
        button4.click()
        button5.click()

    if choice == "3":
        button1 = driver1.find_element_by_id("circle-button")
        button2 = driver2.find_element_by_id("circle-button")
        button3 = driver3.find_element_by_id("circle-button")
        button4 = driver4.find_element_by_id("circle-button")
        button5 = driver5.find_element_by_id("circle-button")
        button1.click()
        button2.click()
        button3.click()
        button4.click()
        button5.click()

    if choice == "4":
        button1 = driver1.find_element_by_id("square-button")
        button2 = driver2.find_element_by_id("square-button")
        button3 = driver3.find_element_by_id("square-button")
        button4 = driver4.find_element_by_id("square-button")
        button5 = driver5.find_element_by_id("square-button")
        button1.click()
        button2.click()
        button3.click()
        button4.click()
        button5.click()


driver1.quit()
driver2.quit()
driver3.quit()
driver4.quit()
driver5.quit()
