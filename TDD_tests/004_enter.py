from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from random import randint
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.maximize_window()

# Locators
EKAT = (By.XPATH, "//li[@class='city-popover__link']")
EKAT_YES = (By.XPATH, "(//a[@class='city'])[2]")
ENTER = (By.XPATH, "//i[@class='horda--user']")
REG = (By.XPATH, "//a[@class='kick-down-the-door f--clr title__h4 no--decoration']")
PHONE_FLD = (By.ID, "registrationform-phone")
PSWD_FLD = (By.XPATH, "(//input[@type='password'])[1]") # (By.ID, "registrationform-password")
CNFRMTN_PSWD_FLD = (By.ID, "registrationform-comfirmpassword")
CHCK_BX = (By.XPATH, "(//label[@class='title__h4 color_checkbox'])[1]") # (By.XPATH, "//input[@type='checkbox']") # (By.CSS_SELECTOR, "label.title__h4.color_checkbox")
GT_PSWD = (By.XPATH, "(//button[@type='submit'])[2]")
TXT_HERE = (By.XPATH, "//div[@class='type_2 ']")
CNTRY_DRP_DWN_MN = (By.XPATH, "(//select[@class='form-control'])[1]")
CTY_FLD = (By.ID, "debitoraddform-city")
EML_FLD = (By.XPATH, "//input[@title='Email']")
CLCK_AFTR_CTY = (By.XPATH, "//li[@class='ui-menu-item']")
LST_MDL_SR_NMS_FLD = (By.XPATH, "//input[@title='Фамилия Имя Отчество']")
CLS_PP_UP_WNW = (By.XPATH, "(//button[@class='close'])[1]")
SBMT_BTN = (By.XPATH, "//button[text()='Добавить']")
CNFRMTN_OF_CD_TXT = (By.XPATH, "//h2[@class='text-uppercase text-light']")

# Explicit wait
wait = WebDriverWait(driver, 15)

# 1. Open the url
driver.get( 'https://gtdel.com/' )

# 2. Click on Ekaterinburg/Yes
wait.until(EC.element_to_be_clickable(EKAT)).click()
wait.until(EC.element_to_be_clickable(EKAT_YES)).click()
driver.refresh()

# 3. Click on Enter button
wait.until(EC.element_to_be_clickable(ENTER)).click()

# 4. Click on Registration button
wait.until(EC.element_to_be_clickable(REG)).click()

# 5. Send phone number to Phone field
password = str(randint(1000000000, 9999999999))
name = 'name' + password
email = (name + '@sample.com')
print(f'\nName: {name}, password: {password} and email: {email}')

wait.until(EC.presence_of_element_located(PHONE_FLD)).clear()
wait.until(EC.presence_of_element_located(PHONE_FLD)).send_keys(password)

# 6. Send password to Password field
wait.until(EC.presence_of_element_located(PSWD_FLD)).clear()
wait.until(EC.presence_of_element_located(PSWD_FLD)).send_keys(password)

# 7. Send confirmed password to Password confirmation field
wait.until(EC.presence_of_element_located(CNFRMTN_PSWD_FLD)).clear()
wait.until(EC.presence_of_element_located(CNFRMTN_PSWD_FLD)).send_keys(password)

# 8. Click on checkbox
wait.until(EC.presence_of_element_located(CHCK_BX)).click()

# 9. Click on Get password button
wait.until(EC.presence_of_element_located(GT_PSWD)).click()

# 10. Verify text is here: Введите данные физического лица
expected_txt = 'Введите данные физического лица'
actual_txt = wait.until(EC.presence_of_element_located((TXT_HERE))).text
print(f'Actual text: {actual_txt}')
assert expected_txt in actual_txt
print(f'Expected "{expected_txt}", and got: "{actual_txt}" ')

# 11. Choose Россия from drop-down menu
wait.until(EC.presence_of_element_located(CNTRY_DRP_DWN_MN)).click()
wait.until(EC.presence_of_element_located(CNTRY_DRP_DWN_MN)).send_keys('Россия')

# 12. Input Верхний Уфалей into city field
wait.until(EC.element_to_be_clickable(CTY_FLD)).click()
wait.until(EC.presence_of_element_located(CTY_FLD)).send_keys('Верхний Уфалей')
wait.until(EC.element_to_be_clickable(CLCK_AFTR_CTY)).click()

# 13.  Input randomly generated address into the email field
wait.until(EC.presence_of_element_located(EML_FLD)).clear()
wait.until(EC.presence_of_element_located(EML_FLD)).send_keys(email)

# 14.  Input randomly generated name into the name field
wait.until(EC.presence_of_element_located(LST_MDL_SR_NMS_FLD)).clear()
wait.until(EC.presence_of_element_located(LST_MDL_SR_NMS_FLD)).send_keys('Иван Иваныч Иванов')

# 15. Click on Submit button
button = driver.find_element(By.XPATH, "//button[text()='Добавить']")
driver.execute_script("arguments[0].click();", button)

# 16. Verify text: Подтверждение доступа is here
expected_txt = 'Подтверждение доступа'
actual_txt = wait.until(EC.presence_of_element_located((CNFRMTN_OF_CD_TXT))).text
print(f'Actual text: {actual_txt}')
assert expected_txt.lower() in actual_txt.lower()
print(f'Expected "{expected_txt}", and got: "{actual_txt}" ')


# Sleep to see what we have
sleep(2)

# Driver quit
driver.quit()


