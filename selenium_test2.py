from selenium import webdriver

driver1 = webdriver.Chrome()
driver1.get("https://www.ycombinator.com")

assert driver1.title == 'Y Combinator'

driver2 = webdriver.Chrome()
driver2.get("https://hub.docker.com")

assert driver2.title == 'Docker Hub Container Image Library | App Containerization'