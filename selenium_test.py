from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

driver1 = webdriver.Chrome()
driver1.get("C:/Users/Amit Tal/Desktop/Devops/tip_calc/index.html")
billamt = driver1.find_element("id", "billamt")
billamt.send_keys("100")
driver1.find_element("xpath", "//*[@id=\"serviceQual\"]/option[3]").click()
peopleamt = driver1.find_element("id", "peopleamt")
peopleamt.send_keys("5")
musicqual = driver1.find_element("id", "musicqual")
musicqual.send_keys("4")
driver1.find_element("xpath", "//*[@id=\"calculate\"]").click()
expected = "9"
actual = driver1.find_element("id", "tip").text

print(f"actual tip is: {actual}")
assert expected == actual

sleep(100)

