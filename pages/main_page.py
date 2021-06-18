from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pages.base_page import Page
from selenium.webdriver.support.wait import WebDriverWait
from random import randint
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains

# Locators
TEXT_IS_HERE = (By.XPATH, "//div[@class='title__h2 set--bold']")
EKAT = (By.XPATH, "//li[@class='city-popover__link']")
EKAT_YES = (By.XPATH, "(//a[@class='city'])[2]")
MOSC = (By.XPATH, "(//a[@class='city'])[1]")
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
CLOSE_ALERT = (By.XPATH, "//span[@aria-hidden='true']")
QUICK_ORDER = (By.XPATH, "(//a[@data-toggle='modal'])[9]")
# FROM_WHERE = (By.ID, "calculateminiformpopup-city_out")
# TO_WHERE = (By.ID, "calculateminiformpopup-city_in")
FROM_TERMINAL = (By.XPATH, "//label[@for='pickupType-term_popup']")
TO_TERMINAL = (By.XPATH, "(//label[contains(text(), 'До терминала')])[2]")
KG = (By.ID, "weight_popup")
CUBIC_METERS = (By.ID, "volumepopup")
PLACES = (By.ID, "placespopup")
GOODS_PRICE = (By.ID, "pricepopup")
COUNT = (By.ID, "fastOrderpopup")
DAYS = (By.XPATH, "(//span[@class='value delivery_days'])[2]")
VALUE_DELIVERY_COSTS = (By.XPATH, "(//div[@class='right__position'])[4]")

class MainPage(Page):

    # Verify text "GTD - доступно, выгодно, надежно." is here
    def vrfy_txt_here(self, txt):
        wait = WebDriverWait(self.driver, 10)
        expected_text = 'GTD - доступно, выгодно, надежно.'
        actual_text = wait.until(EC.presence_of_element_located((TEXT_IS_HERE))).text
        print(actual_text)
        assert expected_text in actual_text
        print(f'Expected "{expected_text}", and got: "{actual_text}" ')
        # Driver quit
        self.driver.quit()
    # End of the above code

    # Enter the main page and verify https://ekaterinburg.gtdel.com/ is here
    # Click on Ekaterinburg/Yes
    def clck_ekat_is_hr(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(EKAT)).click()
        wait.until(EC.element_to_be_clickable(EKAT_YES)).click()
        self.driver.refresh()
    # Verify "https://ekaterinburg.gtdel.com/" is here
    def ek_url_is_here(self):
        expected_url = 'https://ekaterinburg.gtdel.com/'
        actual_url = self.driver.current_url
        print(actual_url)
        assert expected_url in actual_url
        print(f'Expected "{expected_url}", and got: "{actual_url}" ')
    # End of the above code

    # Enter the main page, click on Ekaterinburg/Moscow and https://moscow.gtdel.com/ is here
    # Click on Ekaterinburg/Moscow
    def clck_mosc_is_hr(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(EKAT)).click()
        wait.until(EC.element_to_be_clickable(MOSC)).click()
        self.driver.refresh()
    # Verify "https://moscow.gtdel.com/" is here
    def mosc_url_is_here(self):
        sleep(3.5)
        expected_url = 'https://moscow.gtdel.com/'
        actual_url = self.driver.current_url
        print(actual_url)
        assert expected_url in actual_url
        print(f'Expected "{expected_url}", and got: "{actual_url}" ')
    # End of the above code

    # Enter the main page as a new user and verify Подтверждение доступа is here
    # Click on Enter button
    def rgstr_as_nw_usr(self):
        wait = WebDriverWait(self.driver, 10)
        # Click on Enter button
        wait.until(EC.element_to_be_clickable(ENTER)).click()
        # Click on Registration button
        wait.until(EC.element_to_be_clickable(REG)).click()
        # Send phone number to Phone field
        password = str(randint(1000000000, 9999999999))
        name = 'name' + password
        email = (name + '@sample.com')
        print(f'\nName: {name}, password: {password} and email: {email}')
        wait.until(EC.presence_of_element_located(PHONE_FLD)).clear()
        wait.until(EC.presence_of_element_located(PHONE_FLD)).send_keys(password)
        # Send password to Password field
        wait.until(EC.presence_of_element_located(PSWD_FLD)).clear()
        wait.until(EC.presence_of_element_located(PSWD_FLD)).send_keys(password)
        # 7. Send confirmed password to Password confirmation field
        wait.until(EC.presence_of_element_located(CNFRMTN_PSWD_FLD)).clear()
        wait.until(EC.presence_of_element_located(CNFRMTN_PSWD_FLD)).send_keys(password)
        #Click on checkbox
        wait.until(EC.presence_of_element_located(CHCK_BX)).click()
        #Click on Get password button
        wait.until(EC.presence_of_element_located(GT_PSWD)).click()
        #Verify text is here: Введите данные физического лица
        expected_txt = 'Введите данные физического лица'
        actual_txt = wait.until(EC.presence_of_element_located((TXT_HERE))).text
        print(f'Actual text: {actual_txt}')
        assert expected_txt in actual_txt
        print(f'Expected "{expected_txt}", and got: "{actual_txt}" ')
        # Choose Россия from drop-down menu
        wait.until(EC.presence_of_element_located(CNTRY_DRP_DWN_MN)).click()
        wait.until(EC.presence_of_element_located(CNTRY_DRP_DWN_MN)).send_keys('Россия')
        #Input Верхний Уфалей into city field
        wait.until(EC.element_to_be_clickable(CTY_FLD)).click()
        wait.until(EC.presence_of_element_located(CTY_FLD)).send_keys('Верхний Уфалей')
        wait.until(EC.element_to_be_clickable(CLCK_AFTR_CTY)).click()
        #Input randomly generated address into the email field
        wait.until(EC.presence_of_element_located(EML_FLD)).clear()
        wait.until(EC.presence_of_element_located(EML_FLD)).send_keys(email)
        #Input randomly generated name into the name field
        wait.until(EC.presence_of_element_located(LST_MDL_SR_NMS_FLD)).clear()
        wait.until(EC.presence_of_element_located(LST_MDL_SR_NMS_FLD)).send_keys('Иван Иваныч Иванов')
        # Click on Submit button
        button = self.driver.find_element(By.XPATH, "//button[text()='Добавить']")
        self.driver.execute_script("arguments[0].click();", button)
    # Verify text: Подтверждение доступа is here
    def text_here(self):
        expected_txt = 'Подтверждение доступа'
        wait = WebDriverWait(self.driver, 10)
        actual_txt = wait.until(EC.presence_of_element_located((CNFRMTN_OF_CD_TXT))).text
        print(f'Actual text: {actual_txt}')
        assert expected_txt.lower() in actual_txt.lower()
        print(f'Expected "{expected_txt}", and got: "{actual_txt}" ')
    # End of the above code

    # Click on "ЗАКАЗАТЬ"
    def click_on_order(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(CLOSE_ALERT)).click()
        target = wait.until(EC.element_to_be_clickable(QUICK_ORDER))
        actions = ActionChains(self.driver)
        actions.move_to_element(target)
        sleep(2)
        actions.click(on_element=target)
        actions.perform()

    # Click on "от терминала"
    def click_on_from_terminal(self):
        wait = WebDriverWait(self.driver, 10)
        sleep(3)
        wait.until(EC.element_to_be_clickable(FROM_TERMINAL)).click()

    # Click on "до терминала"
    def click_on_to_terminal(self):
        wait = WebDriverWait(self.driver, 10)
        sleep(3)
        wait.until(EC.element_to_be_clickable(TO_TERMINAL)).click()

    # Send "999" to "кг"
    def send_weight(self, kgs):
        wait = WebDriverWait(self.driver, 10)
        sleep(3)
        wait.until(EC.presence_of_element_located(KG)).clear()
        wait.until(EC.presence_of_element_located(KG)).send_keys(kgs)

    # Send "3.500" to "м3"
    def send_volume(self, volume):
        wait = WebDriverWait(self.driver, 10)
        sleep(3)
        wait.until(EC.presence_of_element_located(CUBIC_METERS)).clear()
        wait.until(EC.presence_of_element_located(CUBIC_METERS)).send_keys(volume)

    # Send "3" to "мест"
    def send_places(self, places):
        wait = WebDriverWait(self.driver, 10)
        sleep(3)
        wait.until(EC.presence_of_element_located(PLACES)).clear()
        wait.until(EC.presence_of_element_located(PLACES)).send_keys(places)

    # Send "30000" to "₽"
    def send_goods_value(self, goods_value):
        wait = WebDriverWait(self.driver, 10)
        sleep(3)
        wait.until(EC.presence_of_element_located(GOODS_PRICE)).clear()
        wait.until(EC.presence_of_element_located(GOODS_PRICE)).send_keys(goods_value)

    # Click on "рассчитать"
    def click_count(self):
        wait = WebDriverWait(self.driver, 10)
        sleep(3)
        wait.until(EC.element_to_be_clickable(COUNT)).click()
        sleep(3)

    # Verify "4 дня" is here as text
    def days_are_here(self):
        expected_txt = '4 дня'
        wait = WebDriverWait(self.driver, 10)
        actual_txt = wait.until(EC.presence_of_element_located((DAYS))).text
        print(f'Actual text: {actual_txt}')
        assert expected_txt in actual_txt
        print(f'Expected "{expected_txt}", and got: "{actual_txt}" ')

    # Verify "8 941 ₽/8&nbsp;941 ₽" is here as text
    def freight_cost_is_here(self):
        expected_txt = '9 341 ₽'
        wait = WebDriverWait(self.driver, 10)
        actual_txt = wait.until(EC.presence_of_element_located((VALUE_DELIVERY_COSTS))).text
        print(f'Actual text: {actual_txt}')
        assert expected_txt in actual_txt
        print(f'Expected "{expected_txt}", and got: "{actual_txt}" ')
    # End of the above code















