from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.maximize_window()

# Locators
CLOSE_ALERT = (By.XPATH, "//span[@aria-hidden='true']")
QUICK_ORDER = (By.XPATH, "(//a[@data-toggle='modal'])[9]")
FROM_WHERE = (By.ID, "calculateminiformpopup-city_out")
TO_WHERE = (By.ID, "calculateminiformpopup-city_in")
FROM_TERMINAL = (By.XPATH, "//label[@for='pickupType-term_popup']")
TO_TERMINAL = (By.XPATH, "(//label[contains(text(), 'До терминала')])[2]")
KG = (By.ID, "weight_popup")
CUBIC_METERS = (By.ID, "volumepopup")
PLACES = (By.ID, "placespopup")
GOODS_PRICE = (By.ID, "pricepopup")
COUNT = (By.ID, "fastOrderpopup")
DAYS = (By.XPATH, "(//span[@class='value delivery_days'])[2]")
VALUE_DELIVERY_COSTS = (By.XPATH, "(//div[@class='right__position'])[4]")
# VALUE_DELIVERY_COSTS = (By.XPATH, "(//span[@class='value delivery_costs'])[2]")

# Explicit wait
wait = WebDriverWait(driver, 15)

# 1. Open the url
driver.get( 'https://gtdel.com/' )

# 2. Click on "ЗАКАЗАТЬ"
wait.until(EC.element_to_be_clickable(CLOSE_ALERT)).click()
target = wait.until(EC.element_to_be_clickable(QUICK_ORDER))
actions = ActionChains(driver)
actions.move_to_element(target)
sleep(2)
actions.click(on_element = target)
actions.perform()


# 3. # Click on "от терминала"
wait = WebDriverWait(driver, 10)
sleep(3)
wait.until(EC.element_to_be_clickable(FROM_TERMINAL)).click()


# 4. # Click on "до терминала"
sleep(3)
wait.until(EC.element_to_be_clickable(TO_TERMINAL)).click()


# 5. # Send "999" to "кг"
sleep(3)
wait.until(EC.presence_of_element_located(KG)).clear()
wait.until(EC.presence_of_element_located(KG)).send_keys('999')


# 6. # Send "3.500" to "м3"
sleep(3)
wait.until(EC.presence_of_element_located(CUBIC_METERS)).clear()
wait.until(EC.presence_of_element_located(CUBIC_METERS)).send_keys('3.500')


# 7. # Send "3" to "мест"
sleep(3)
wait.until(EC.presence_of_element_located(PLACES)).clear()
wait.until(EC.presence_of_element_located(PLACES)).send_keys('3')

# 8. # Send "30000" to "₽"
sleep(3)
wait.until(EC.presence_of_element_located(GOODS_PRICE)).clear()
wait.until(EC.presence_of_element_located(GOODS_PRICE)).send_keys('30000')

# 9.# Click on "рассчитать"
sleep(3)
wait.until(EC.element_to_be_clickable(COUNT)).click()
sleep(3)

# 10. # Verify "4 дня" is here as text
expected_txt = '4 дня'
actual_txt = wait.until(EC.presence_of_element_located((DAYS))).text
print(f'Actual text: {actual_txt}')
assert expected_txt in actual_txt
print(f'Expected "{expected_txt}", and got: "{actual_txt}" ')

# 11. Click on "рассчитать"
wait.until(EC.element_to_be_clickable(COUNT)).click()

# 12. Verify "4 дня" is here as text
sleep(3)
expected_txt = '4 дня'
actual_txt = wait.until(EC.presence_of_element_located((DAYS))).text
print(f'Actual text: {actual_txt}')
assert expected_txt in actual_txt
print(f'Expected "{expected_txt}", and got: "{actual_txt}" ')

# 13. # Verify "9 341 ₽/8&nbsp;341 ₽" is here as text
expected_txt = '9 341 ₽'
actual_txt = wait.until(EC.presence_of_element_located((VALUE_DELIVERY_COSTS))).text
print(f'Actual text: {actual_txt}')
assert expected_txt in actual_txt
print(f'Expected "{expected_txt}", and got: "{actual_txt}" ')

# Sleep to see what we have
sleep(2)

# Driver quit
driver.quit()
