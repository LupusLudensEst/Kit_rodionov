from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()

# Locators
EKAT = (By.XPATH, "//li[@class='city-popover__link']")
EKAT_YES = (By.XPATH, "(//a[@class='city'])[2]")

# Explicit wait
wait = WebDriverWait(driver, 15)

# 1. Open the url
driver.get( 'https://gtdel.com/' )

# 2. Click on Ekaterinburg/Yes
wait.until(EC.element_to_be_clickable(EKAT)).click()
wait.until(EC.element_to_be_clickable(EKAT_YES)).click()
driver.refresh()

# 3. Verify https://ekaterinburg.gtdel.com/ is here
expected_url = 'https://ekaterinburg.gtdel.com/'
actual_url = driver.current_url
print(actual_url)
assert expected_url in actual_url
print(f'Expected "{expected_url}", and got: "{actual_url}" ')


# Sleep to see what we have
sleep(2)

# Driver quit
driver.quit()
