from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pages.base_page import Page
from selenium.webdriver.support.wait import WebDriverWait
from random import randint
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver

# Locators
TEXT_IS_HERE = (By.XPATH, "//div[@class='title__h2 set--bold']")
EKAT = (By.XPATH, "//li[@class='city-popover__link']")
EKAT_YES = (By.XPATH, "(//a[@class='city'])[2]")
MOSC = (By.XPATH, "(//a[@class='city'])[1]")

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
        expected_url = 'https://moscow.gtdel.com/'
        actual_url = self.driver.current_url
        print(actual_url)
        assert expected_url in actual_url
        print(f'Expected "{expected_url}", and got: "{actual_url}" ')
    # End of the above code









