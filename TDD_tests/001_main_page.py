from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()

# Locators
TEXT_IS_HERE = (By.XPATH, "//div[@class='title__h2 set--bold']")

# Explicit wait
wait = WebDriverWait(driver, 15)

# 1. Open the url
driver.get( 'https://gtdel.com/' )

# 2. Verify text "GTD - доступно, выгодно, надежно." is here
expected_text = 'GTD - доступно, выгодно, надежно.'
actual_text = wait.until(EC.presence_of_element_located((TEXT_IS_HERE))).text
print(actual_text)
assert expected_text in actual_text
print(f'Expected "{expected_text}", and got: "{actual_text}" ')

# Sleep to see what we have
sleep(2)

# Driver quit
driver.quit()
