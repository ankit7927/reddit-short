from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("https://www.reddit.com/r/AskReddit/comments/12eomgg/whats_a_small_thing_that_makes_you_unreasonably/?sort=new")

question  = driver.find_element(By.XPATH, "//div[@data-testid='comment']")

print(question.text)

driver.close()