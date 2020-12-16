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
LOGIN_EMAIL = (By.XPATH, "//input[@placeholder='Email address']")
LOGIN_PASSWORD = (By.XPATH, "//input[@placeholder='Password']")
LOGIN_BTN = (By.CSS_SELECTOR, "button.btn.btn-primary.text-uppercase.w-100.font-weight-bold.gradient-btn.shadow-1.border-0")
POP_UP_WNDW_OK_BTN = (By.XPATH, "//div[@class='swal2-actions']//button[@class='swal2-confirm btn btn-outline-primary btn-sm btn-custom swal2-styled']")
USERS = (By.XPATH, "(//li[@class='ng-star-inserted'])[5]")
QUICK_ACTIONS = (By.XPATH, "//div[@class='btn-group action-button dropdown']//span[contains(text(), 'Quick actions')]")
ADD_MENU = (By.CSS_SELECTOR, "i.fa.fa-user-plus")
FIRST_NAME = (By.XPATH, "//input[@formcontrolname='firstName']")
LAST_NAME = (By.XPATH, "//input[@formcontrolname='lastName']")
EMAIL = (By.XPATH, "//input[@formcontrolname='email']")
TELEPHONE = (By.XPATH, "//input[@formcontrolname='telephone']")
SELECT_ROLE = (By.ID, "role")
ADDRESS_1 = (By.XPATH, "//input[@formcontrolname='address1']")
ADDRESS_2 = (By.XPATH, "//input[@formcontrolname='address2']")
CITY = (By.XPATH, "//input[@formcontrolname='city']")
ZIP_CODE = (By.XPATH, "//input[@formcontrolname='zipCode']")
COUNTRY = (By.CSS_SELECTOR, "select.form-control.ng-touched.ng-dirty.ng-valid")
STATE = (By.XPATH, "//select[@formcontrolname='state']")
ADD_BTN = (By.CSS_SELECTOR, "button.btn.btn-sm.btn-primary.px-4.py-2.text-uppercase")
TEXT_HR = (By.XPATH, "//td[@style='text-align: left;']")
ADMIN = (By.XPATH, "//b[contains(text(), 'admin')]")
USER = (By.XPATH, "//b[contains(text(), 'user')]")
THREE_DOTS = (By.ID, "dropdownBasic1")
DELETE_BTN = (By.XPATH, "//div[@class='dropdown']//a[contains(text(), 'Delete')]")
DELETE_OK_BTN = (By.CSS_SELECTOR, "button.swal2-confirm.btn.btn-outline-primary.btn-sm.btn-custom.swal2-styled")
INVLD_LGN_PSWRD_HR = (By.XPATH, "//div[contains(text(), 'Invalid Login or Password')]")
CLCK_TRNGL = (By.XPATH, "//button[@class='d-block btn-togglr']")
USR_NM = (By.CSS_SELECTOR, "a.dropdown-toggle.user-name")
LGT_BTN = (By.CSS_SELECTOR, "i.fas.fa-power-off")
CLCK_LGT = (By.CSS_SELECTOR, "a.icon-menu.d-none.d-sm-block")
CHNG_PSWD = (By.XPATH, "//i[@class='fas fa-unlock-alt']")
NW_VLD_PSWD = (By.XPATH, "//input[@placeholder='New Password']")
CNFRM_NW_VLD_PSWD = (By. XPATH, "//input[@placeholder='Confirm New Password']")
SV_BTN = (By.CSS_SELECTOR, "i.fa.fa-save.mr-1")
SCSS_TXT_HR = (By.CSS_SELECTOR, "span.alert.w-100.alert-warning")
DVC_ONLN_TXT = (By.XPATH, "(//div[@class='card overflowhidden number-chart d-flex flex-column'])[1]")
DVC_ONLN = (By.CSS_SELECTOR, "div.number>span")
DVC_OFFLN_TAB = (By.XPATH, "(//div[@class='body information-card'])[2]")
INVNTR = (By.XPATH, "(//div[@class='body information-card'])[3]")
ALRT_NTFCTN = (By.XPATH, "(//div[@class='body information-card'])[4]")
DT_USG = (By.XPATH, "//h6[@class='tile-title text-uppercase']")
DT_USG_DTLS = (By.XPATH, "(//h2[@class='ng-tns-c6-0'])[1]")
NTFCTNS_ALRTS = (By.XPATH, "(//h2[@class='ng-tns-c6-0'])[2]")
GRPS = (By.XPATH, "(//h2[@class='ng-tns-c6-0'])[3]")
SGNL_STRNTH = (By.XPATH, "(//h2[@class='ng-tns-c6-0'])[4]")
DVC_LCTN = (By.XPATH, "//div[@class='col-6']//h2[@class='ng-tns-c6-0']")
DVC_MNGMNT_PRTL = (By.XPATH, "//h5[@class='fw-300 m-0 pl-4 text-truncate']")
ONLN_HERE = (By.CSS_SELECTOR, "span.pr-2")
DVCS_TBL = (By.XPATH, "//input[@name='checkbox1']")
NO_DATA = (By.XPATH, "//div[@class='no-data']")
DVCS_OFFLN = (By.XPATH, "(//div[@class='card overflowhidden number-chart d-flex flex-column'])[2]")
OFFLN_TXT = (By.XPATH, "//span[@class='pr-2']")
DVC_OFFLN = (By.CSS_SELECTOR, "div.number>span")
DVCS_TBL_EMPT = (By.XPATH, "//tr[@class='ng-star-inserted']")
DVC_INVNTR = (By.CSS_SELECTOR, "div.number>span")
INVNTR_ELMNT = (By.CSS_SELECTOR, "div.card.overflowhidden.number-chart.d-flex.flex-column")
INVNTR_TXT = (By.CSS_SELECTOR, "span.pr-2")
ALRT_VRFCTN_CRT = (By.XPATH, "(//div[@class='body information-card'])[4]")
ALRT_DSHBRD_HR = (By.CSS_SELECTOR, "div.d-inline-block.mr-4")
WAN = (By.XPATH, "(//strong[@class='ng-tns-c6-0'])[4]")
DT_USG_CRD = (By.CSS_SELECTOR, "div.card.overflowhidden.number-chart.p-4")
CLLR = (By.XPATH, "(//strong[@class='ng-tns-c6-0'])[1]")
DSCH_BRD_ICN = (By.XPATH, "(//a[@class='ng-star-inserted'])[1]")
DSCH_BRD_TXT = (By.XPATH, "//h2[@class='mb-0']")
USG_DTLS_TXT = (By.XPATH, "(//h6[@class='tile-title text-uppercase'])[1]")
QSTN_CRCL_MRK = (By.XPATH, "//i[@class='fa fa-question-circle']")
TL_TIP_TXT = (By.XPATH, "//span[@tool-tip='WAN/Cellular data usage classified periodically.']")
DT_USG_DRP_DWN_MN = (By.XPATH, "//select[@class='form-control']")
NO_DT_ABLBL = (By.XPATH, "(//div[@class='no-data'])[1]")
GB_INCTV_CLMN = (By.XPATH, "(//li[@class='nav-item ng-star-inserted'])[3]")
NTFCTNS_ALRTS_TXT = (By.XPATH, "(//div[@class='card dashboard-card notification-card'])")
NTFCTNS_ALRTS_TL_TIP = (By.XPATH, "//span[@tool-tip='Alerts related to device(s)/group(s).']")
CLCK_ON_GRPS_TB = (By.XPATH, "(//a[@class='nav-link'])[5]")
DVC_GRY = (By.XPATH, "(//li[@class='nav-item ng-star-inserted'])[4]")
NO_DT_WHEN_GRPS = (By.XPATH, "(//div[@class='no-data'])[2]")
CLCK_ON_DVC_TB = (By.XPATH, "(//li[@class='nav-item ng-star-inserted'])[4]")
NO_DT_WHEN_DVC = (By.XPATH, "(//div[@class='no-data'])[2]")
GRPS_TXT_HR = (By.XPATH, "(//h2[@class='ng-tns-c6-0'])[3]")
QSTN_CRCL_MRK_GRPS_SCTN = (By.XPATH, "(//i[@class='fa  fa-question-circle'])[2]")
QSTN_CRCL_TL_TP_TXT = (By.XPATH, "(//span[@class='ml-2'])[1]")
NO_DT_IN_GRPS_BLCK = (By.XPATH, "(//div[@class='no-data'])[3]")
GRPS_DRP_DWN_MN = (By.ID, "more")
GRPS_DRP_DWN_MN_LST = (By.XPATH, "//div[@class='list-group']")
GRPS_TL_TIP = (By.XPATH, "//span[@tool-tip='Device(s) status based on groups.']")
SGNL_STRNGT_TXT_HR = (By.XPATH, "(//h2[@class='ng-tns-c6-0'])[4]")
QSTN_CRCL_SGNL_STRNGT_SCTN = (By.XPATH, "(//i[@class='fa  fa-question-circle'])[3]")
QSTN_CRCL_SGNL_STRNGT_TXT = (By.XPATH, "//span[@tool-tip='Overall signal strength statistics of device(s).']")
NO_DT_IN_SGNL_STRNGT_SCTN = (By.XPATH, "(//div[@class='no-data'])")
DVC_LCTNS_TXT_HR = (By.XPATH, "(//h2[@class='ng-tns-c6-0'])[5]")
QSTN_CRCL_DVC_LCTNS_SCTN = (By.XPATH, "(//i[@class='fa  fa-question-circle'])[4]")
QSTN_CRCL_DVC_LCTNS_TXT = (By.XPATH, "//span[@tool-tip='Current locations of the device(s).']")
DVC_LCTNS_DRP_DWN_MN = (By.ID, "groups")
DVC_LCTNS_DRP_DWN_MN_LST = (By.XPATH, "//option[@class='ng-tns-c6-0']")
DVC_ONLN_ICN = (By.XPATH, "(//div[@class='card overflowhidden number-chart d-flex flex-column'])[1]")
FLTR_DVC_FUNNEL = (By.XPATH, "//i[@class='fa fa-filter']")
CHCK_BX_DVC_ONLN = (By.NAME, "checkbox1")
CHCK_BX_DVC_OFFLN =(By.XPATH, "//span[contains(text(), 'Offline Devices')]")
CHCK_BX_INVENTORY = (By.XPATH, "//span[contains(text(), 'Inventory')]")
DVCS_ICN = (By. XPATH, "//i[@class='fa fa-hdd-o']")
ADD_NW_DVC_RGHT_CRNR = (By.XPATH, "//span[contains(text(), ' Add New Device ')]")
DVC_IMEI_FLD = (By.XPATH, "//input[@placeholder='IMEI']")
DVC_NAME_FLD = (By.XPATH, "//input[@placeholder='Device name']")
DVC_SRL_NMBR_FLD = (By.XPATH, "//input[@placeholder='Serial number']")
DVC_ADD_SAVE_BTN = (By.XPATH, "(//button[@type='submit'])[1]")
IMEI_HR = (By.XPATH, "//a[contains(text(), '356961071557824')]")
CHCK_BX_FOR_DLT = (By.XPATH, "(//div[@class='fancy-checkbox devicelist-checkbox select-all'])[1]")
GEAR_BTN = (By.XPATH, "//button[@class='btn btn-default btn-sm dropdown-toggle px-3 dropdown-toggle']")
RMV_DVCS_BTN = (By.XPATH, "(//a[@class='dropdown-item ng-star-inserted'])[2]")
DLT_BTN_DVCS = (By.XPATH, "//button[@class='btn btn-sm btn-danger']")
SCCSS_DLT_NO_DT_AVLBL = (By.XPATH, "//div[contains(text(), 'No Data Available')]")
DVC_ALRD_EXSTS = (By.XPATH, "//p[contains(text(), 'Device already exists.')]")
CROSS_TO_CLOSE = (By.XPATH, "//span[contains(text(), '×')]")
EMEI_CLCK = (By.XPATH, "(//a[@class='ng-star-inserted'])[5]")
QUICK_ACTION_BTN = (By.XPATH, "//div[@class='btn-group action-button dropdown']")
QUICK_ACTION_ID = (By.XPATH, "(//a[@class='dropdown-item'])[1]")
STNGS_BTN = (By.XPATH, "(//button[@class='btn btn-default btn-sm dropdown-toggle dropdown-toggle'])[2]")
REBOOT_ELMNT_HR = (By.XPATH, "(//a[@class='dropdown-item'])[2]")
MODEL_TYPE = (By.XPATH, "//*[contains(text(), 'ER2000T-NA-CAT1')]")
DVC_PCTR = (By.XPATH, "//img[@src='https://connectedio.s3-us-west-1.amazonaws.com/l/products/ER2000T1.png']")
FRM_VRSN = (By.XPATH, "(//span[@class='ng-tns-c8-1'])[11]")
MDM_FRM = (By.XPATH, "(//span[@class='ng-tns-c8-1'])[12]")
LAST_HEARD = (By.XPATH, "(//strong[@class='d-block mb-1'])[5]")
UPTIME = (By.XPATH, "(//strong[@class='d-block mb-1'])[6]")
IP_ADDRESS = (By.XPATH, "(//div[@class='dvc-ip flex-grow-1 w-100 text-truncate small ng-star-inserted'])[1]")
TX_DATA_FRM_LST_RBT = (By.XPATH, "(//i[@class='far fa-arrow-alt-circle-up'])[1]")
RX_DATA_FRM_LST_RBT = (By.XPATH, "(//i[@class='far fa-arrow-alt-circle-down'])[1]")
MAC_ADDRESS = (By.XPATH, "(//span[@class='text-truncate small d-block w-100'])[1]")
PIE_CHART = (By.XPATH, "(//div[@class='pieChart'])[1]")
SIM_IP_ADDRESS = (By.XPATH, "(//div[@class='dvc-ip flex-grow-1 w-100 text-truncate small ng-star-inserted'])[2]")
SIM_TX_DATA_FRM_LST_RBT = (By.XPATH, "(//i[@class='far fa-arrow-alt-circle-up'])[2]")
SIM_RX_DATA_FRM_LST_RBT = (By.XPATH, "(//i[@class='far fa-arrow-alt-circle-down'])[2]")
ICC_NUMBER = (By.XPATH, "(//li[@class='ng-star-inserted'])[24]")
APN = (By.XPATH, "(//li[@class='ng-star-inserted'])[25]")
SIM_PIE_CHART = (By.XPATH, "(//div[@class='pieChart'])[2]")
LAN_IP_ADDRESS = (By.XPATH, "(//div[@class='dvc-ip flex-grow-1 w-100 text-truncate small ng-star-inserted'])[3]")
LAN_TX_DATA_FRM_LST_RBT = (By.XPATH, "(//i[@class='far fa-arrow-alt-circle-up'])[3]")
LAN_RX_DATA_FRM_LST_RBT = (By.XPATH, "(//i[@class='far fa-arrow-alt-circle-down'])[3]")
LAN_MAC_ADDRESS = (By.XPATH, "(//li[@class='ng-star-inserted'])[26]")
LAN_PIE_CHART = (By.XPATH, "(//div[@class='pieChart'])[3]")
REFRESH_BTN = (By.XPATH, "//i[@class='fa fa-refresh']")
FTCHNG_DT_FRM_DVC = (By.XPATH, "//p[contains(text(),'Fetching data from device...')]")
ADD_NEW_DVC_ONLN = (By.XPATH, "//button[@class='btn btn-default btn-sm ng-star-inserted']")
SYSTEM_LOG = (By.XPATH, "//i[@class='fa fa-history']")
SYSTEM_LOG_TXT_HR = (By.XPATH, "//h5[@class='modal-title']")
CLOSE_SYSTEM_LOG = (By.XPATH, "//a[@class='close']")

class MainPage(Page):

    # Add new user
    sleep(2)
    def lgn_w_gn_crdntls(self):
        wait = WebDriverWait(self.driver, 10)
        # 2. Send Login e-mail
        wait.until(EC.presence_of_element_located(LOGIN_EMAIL)).clear()
        wait.until(EC.presence_of_element_located(LOGIN_EMAIL)).send_keys('gurovvic@gmail.com') # vadim@mailinator.com
        # 3. Send Password
        wait.until(EC.presence_of_element_located(LOGIN_PASSWORD)).clear()
        wait.until(EC.presence_of_element_located(LOGIN_PASSWORD)).send_keys('MyUSA2016!@') # manicpiano731
        # 4. Click on Login buclck_usr_nmtton
        wait.until(EC.element_to_be_clickable(LOGIN_BTN)).click()
        # 5. Click on pop-window OK button
        wait.until(EC.element_to_be_clickable(POP_UP_WNDW_OK_BTN)).click()
        sleep(2)

    def clck_usrs_btn(self):
        wait = WebDriverWait(self.driver, 10)
        # 6. Click on Users button
        wait.until(EC.element_to_be_clickable(USERS)).click()

    def clck_qck_actns_btn(self):
        wait = WebDriverWait(self.driver, 10)
        # 7. Click on Quick Actions button
        wait.until(EC.element_to_be_clickable(QUICK_ACTIONS)).click()

    def slct_add_drp_dwn_mn(self):
        wait = WebDriverWait(self.driver, 10)
        # 8. Click on Add button
        wait.until(EC.element_to_be_clickable(ADD_MENU)).click()

    def fll_rqrd_flds(self):
        wait = WebDriverWait(self.driver, 10)
        # 9. Fill out the First Name field
        wait.until(EC.presence_of_element_located(FIRST_NAME)).clear()
        wait.until(EC.presence_of_element_located(FIRST_NAME)).send_keys('Roman')

        # 10. Fill out the Last Name field
        wait.until(EC.presence_of_element_located(LAST_NAME)).clear()
        wait.until(EC.presence_of_element_located(LAST_NAME)).send_keys('Ivanov')

        # Generators of password, name and email
        password = str(randint(999, 9999))
        name = 'name' + password
        email = (name + '@sample.com')

        # 11. Fill out the Email field
        wait.until(EC.presence_of_element_located(EMAIL)).clear()
        wait.until(EC.presence_of_element_located(EMAIL)).send_keys(email)

        # 12. Fill out the Telephone field
        wait.until(EC.presence_of_element_located(TELEPHONE)).clear()
        wait.until(EC.presence_of_element_located(TELEPHONE)).send_keys('7895678956')

        # 13. Choose admin in the drop-down menu
        element = wait.until(EC.visibility_of_element_located((SELECT_ROLE)))
        select = Select(element)
        select.select_by_value("admin")

        # 14. Fill out the Adress1 field
        wait.until(EC.presence_of_element_located(ADDRESS_1)).clear()
        wait.until(EC.presence_of_element_located(ADDRESS_1)).send_keys('1933, 84 street')

        # 14. Fill out the Adress2 field
        wait.until(EC.presence_of_element_located(ADDRESS_2)).clear()
        wait.until(EC.presence_of_element_located(ADDRESS_2)).send_keys('Just test')

        # 15. Fill out the City field
        wait.until(EC.presence_of_element_located(CITY)).clear()
        wait.until(EC.presence_of_element_located(CITY)).send_keys('Brooklyn')

        # 16. Fill out the Zip Code field
        wait.until(EC.presence_of_element_located(ZIP_CODE)).clear()
        wait.until(EC.presence_of_element_located(ZIP_CODE)).send_keys('11214')

        # 17. Choose Select Country in the drop-down menu United States
        wait.until(EC.element_to_be_clickable(COUNTRY)).click()
        wait.until(EC.presence_of_element_located(COUNTRY)).send_keys('United States')

        # 18. Choose Select State in the drop-down menu New York
        wait.until(EC.element_to_be_clickable(STATE)).click()
        wait.until(EC.presence_of_element_located(STATE)).send_keys('New York')

    def clck_n_add_btn(self):
        wait = WebDriverWait(self.driver, 10)
        # 19. Click on Add button
        wait.until(EC.element_to_be_clickable(ADD_BTN)).click()

    def vrf_usr_is_hr(self, text_hr):
        wait = WebDriverWait(self.driver, 10)
        expected_text = text_hr
        actual_text = wait.until(EC.presence_of_element_located((TEXT_HR))).text
        assert expected_text in actual_text
        print(f'Expected "{text_hr}", and got "{actual_text}" ')
        # End of the above code
        sleep(2)

    def admns_n_usrs(self):
        # 7. Make sure there are at list two Admins and one User role in the list of users
        wait = WebDriverWait(self.driver, 15)
        expected_text = 'ADMIN'
        actual_text = wait.until(EC.presence_of_element_located((ADMIN))).text
        assert expected_text in actual_text
        print(f'Expected "{expected_text}", and got: "{actual_text}" ')
        len_admins = len(wait.until(EC.presence_of_all_elements_located((ADMIN))))
        print(f'Admins: {len_admins}, type: {type(len_admins)}')
        if len_admins < 2:
            print(f'ADMINS < 2, NOT OK, there is: {len_admins} admin, add to 2 admins')
            # Driver quit
            self.driver.quit()
        else:
            print(f'ADMINS >=2, OK, there are: {len_admins} admins')

            expected_text = 'USER'
            actual_text = wait.until(EC.presence_of_element_located((USER))).text
            assert expected_text in actual_text
            print(f'Expected "{expected_text}", and got: "{actual_text}" ')
            len_users = len(wait.until(EC.presence_of_all_elements_located((USER))))
            if len_users >= 2:
                print(f'USERS >=1, OK, there are: {len_users} users')
            else:
                print(f'USERS !>=1, NOT OK, there are: {len_users} users')

            total_users_admins_before_delete = len_admins + len_users
            print(f'Total admins and users before delete: {total_users_admins_before_delete}')

    def take_usr_t_dlt(self):
        # 8. Choose any username with Admin or User role except yours.
        # Click on the "Settings" (three vertical dots) from the rightmost side of the user.
        wait = WebDriverWait(self.driver, 15)
        wait.until(EC.element_to_be_clickable(THREE_DOTS)).click()

    def dlt_drp_dwn_mn(self):
        # 9. Select "Delete" from the dropdown menu.
        wait = WebDriverWait(self.driver, 15)
        wait.until(EC.visibility_of_element_located(DELETE_BTN)).click()

    def cnfrm_dlt(self):
        # 10. The pop-up dialog window "Delete user" appears after clicking on the "Delete" button.
        wait = WebDriverWait(self.driver, 15)
        wait.until(EC.element_to_be_clickable(DELETE_OK_BTN)).click()

    def vrf_usr_dltd(self):
        # 11. The "Users" page has opened and user is not in the list of users.
        wait = WebDriverWait(self.driver, 15)
        len_admins = len(wait.until(EC.presence_of_all_elements_located((ADMIN))))
        len_users = len(wait.until(EC.presence_of_all_elements_located((USER))))
        total_users_admins_before_delete = len_admins + len_users
        self.driver.refresh()
        len_admins = len(wait.until(EC.presence_of_all_elements_located((ADMIN))))
        len_users = len(wait.until(EC.presence_of_all_elements_located((USER))))
        total_admins_users_after_delete = len_admins + len_users
        if total_users_admins_before_delete - total_admins_users_after_delete == 1:
            print(
                f'Delete is OK: {total_users_admins_before_delete} - {total_admins_users_after_delete} = {total_users_admins_before_delete - total_admins_users_after_delete}')
        else:
            print(f'Delete is not OK')
        print(f'Total admins and users after delete: {total_admins_users_after_delete}')

        # End of the above code

    def entr_vld_wrng_eml(self, email):
        # 1. Enter valid, but the incorrect email address in the line "Email address"
        wait = WebDriverWait(self.driver, 15)
        # Send Login e-mail
        wait.until(EC.presence_of_element_located(LOGIN_EMAIL)).clear()
        wait.until(EC.presence_of_element_located(LOGIN_EMAIL)).send_keys(email)

    def entr_vld_crct_pswd(self, pswd):
        # 2. Send Correct Password
        wait = WebDriverWait(self.driver, 15)
        wait.until(EC.presence_of_element_located(LOGIN_PASSWORD)).clear()
        wait.until(EC.presence_of_element_located(LOGIN_PASSWORD)).send_keys(pswd)
        # Click on Login button
        wait.until(EC.element_to_be_clickable(LOGIN_BTN)).click()

    def vrf_invld_lgn_r_pswd_hr(self, expected_text):
        # 3. Verify Invalid Login or Password is here
        wait = WebDriverWait(self.driver, 15)
        actual_text = wait.until(EC.presence_of_element_located((INVLD_LGN_PSWRD_HR))).text
        print(actual_text)
        assert expected_text in actual_text
        print(f'Expected "{expected_text}", and got: "{actual_text}" ')

        # End of the above code

    def clck_usr_nm(self):
        # 6. Click on triangle to enter the user
        wait = WebDriverWait(self.driver, 15)
        target = wait.until(EC.element_to_be_clickable(CLCK_TRNGL))
        actions = ActionChains(self.driver)
        actions.move_to_element(target)
        sleep(2)
        actions.click(target)
        actions.perform()

        # 7. Click on the User name in the Sidebar menu
        wait.until(EC.element_to_be_clickable(USR_NM)).click()

    def clck_lgt_btn(self):
        # 8. Hover over the "Logout" button in the dropdown menu and click on the button "Logout"
        wait = WebDriverWait(self.driver, 15)
        sleep(2)
        wait.until(EC.element_to_be_clickable(LGT_BTN)).click()
        self.driver.refresh()

        # End of the above code

    def clck_hdr_lgt_btn(self):
        # Hover over the "Logout" button at the right corner of the Header and click on the button "Logout"
        wait = WebDriverWait(self.driver, 15)
        target = wait.until(EC.element_to_be_clickable(CLCK_LGT))
        actions = ActionChains(self.driver)
        actions.move_to_element(target)
        actions.click(target)
        actions.perform()

        # End of the above code

    def go_to_chng_pswrd_pg(self):
        # Click on triangle to enter the user
        wait = WebDriverWait(self.driver, 15)
        target = wait.until(EC.element_to_be_clickable(CLCK_TRNGL))
        actions = ActionChains(self.driver)
        actions.move_to_element(target)
        sleep(2)
        actions.click(target)
        actions.perform()

        # Click on the User name in the Sidebar menu
        wait.until(EC.element_to_be_clickable(USR_NM)).click()

        # Click on the Change Password button
        wait.until(EC.element_to_be_clickable(CHNG_PSWD)).click()

    def cng_pswd_url_opn(self, url_is_here):
        # https://devcloud.connectedio.com/* is open
        expected_text = url_is_here
        actual_text = self.driver.current_url
        assert expected_text in actual_text
        if expected_text == actual_text:
            print(f'Expected "{expected_text}", and got: "{actual_text}" ')
        else:
            print(f'Expected "{expected_text}", but got: "{actual_text}" ')

    def ntr_old_pswd(self, old_pswd):
        # Enter the old password in the field "New Password" MyUSA2016!@
        wait = WebDriverWait(self.driver, 15)
        sleep(2)
        wait.until(EC.presence_of_element_located(NW_VLD_PSWD)).clear()
        wait.until(EC.presence_of_element_located(NW_VLD_PSWD)).send_keys(old_pswd)

    def cfrm_old_pswd(self, old_pswd):
        # Enter the same old password in the field "Confirm New Password"
        wait = WebDriverWait(self.driver, 15)
        wait.until(EC.visibility_of_element_located(CNFRM_NW_VLD_PSWD)).clear()
        wait.until(EC.visibility_of_element_located(CNFRM_NW_VLD_PSWD)).send_keys(old_pswd)

    def clck_on_btn_save(self):
        # Click on the button "Save"
        wait = WebDriverWait(self.driver, 15)
        wait.until(EC.element_to_be_clickable(SV_BTN)).click()

    def old_new_r_nt_same(self, old_nw_r_nt_same):
        # Verify the words Old and new password cannot be same. is on the page
        wait = WebDriverWait(self.driver, 15)
        expected_text = old_nw_r_nt_same
        actual_text = wait.until(EC.element_to_be_clickable(SCSS_TXT_HR)).text
        assert expected_text in actual_text
        if expected_text == actual_text:
            print(f'Expected "{expected_text}", and got: "{actual_text}" ')
        else:
            print(f'Expected "{expected_text}", but got: "{actual_text}" ')

        # End of the above code

    def ll_lmnts_r_prsnt(self):
        # 6. Check if all elements are present.
        # 6.1. Cards: "DEVICE ONLINE", 6.2. "DEVICE OFFLINE",
        # 6.3. "INVENTORY", 6.4. "ALERT/NOTIFICATION", 6.5. "DATA USAGE"
        wait = WebDriverWait(self.driver, 15)
        # 1
        expected_text = 'DEVICE ONLINE'
        actual_text = wait.until(EC.presence_of_element_located((DVC_ONLN_TXT))).text
        assert expected_text in actual_text
        print(f'Expected "{expected_text}", and got: "{actual_text}" ')
        # 2
        expected_text = 'DEVICE OFFLINE'
        actual_text = wait.until(EC.presence_of_element_located((DVC_OFFLN_TAB))).text
        assert expected_text in actual_text
        print(f'Expected "{expected_text}", and got: "{actual_text}" ')
        # 3
        expected_text = 'INVENTORY'
        actual_text = wait.until(EC.presence_of_element_located((INVNTR))).text
        assert expected_text in actual_text
        print(f'Expected "{expected_text}", and got: "{actual_text}" ')
        # 4
        expected_text = 'ALERT/NOTIFICATION'
        actual_text = wait.until(EC.presence_of_element_located((ALRT_NTFCTN))).text
        assert expected_text in actual_text
        print(f'Expected "{expected_text}", and got: "{actual_text}" ')
        # 5
        expected_text = 'DATA USAGE'
        actual_text = wait.until(EC.presence_of_element_located((DT_USG))).text
        assert expected_text in actual_text
        print(f'Expected "{expected_text}", and got: "{actual_text}" ')

    def ll_sctns_r_prsnt(self):
        # 7. Check if sections are present.
        # 7.1 "Data Usage Details", 7.2. "Notifications/Alerts",
        # 7.3. "Groups", 7.4. "Signal Strength", 7.5. "Device Location".
        # 1
        wait = WebDriverWait(self.driver, 15)
        expected_text = 'Data Usage Details'
        actual_text = wait.until(EC.presence_of_element_located((DT_USG_DTLS))).text
        assert expected_text in actual_text
        print(f'Expected "{expected_text}", and got: "{actual_text}" ')
        # 2
        expected_text = 'Notifications / Alerts'
        actual_text = wait.until(EC.presence_of_element_located((NTFCTNS_ALRTS))).text
        assert expected_text in actual_text
        print(f'Expected "{expected_text}", and got: "{actual_text}" ')
        # 3
        expected_text = 'Groups'
        actual_text = wait.until(EC.presence_of_element_located((GRPS))).text
        assert expected_text in actual_text
        print(f'Expected "{expected_text}", and got: "{actual_text}" ')
        # 4
        expected_text = 'Signal Strength'
        actual_text = wait.until(EC.presence_of_element_located((SGNL_STRNTH))).text
        assert expected_text in actual_text
        print(f'Expected "{expected_text}", and got: "{actual_text}" ')
        # 5
        expected_text = 'Device   Locations'
        actual_text = wait.until(EC.presence_of_element_located((DVC_LCTN))).text
        assert expected_text in actual_text
        print(f'Expected "{expected_text}", and got: "{actual_text}" ')

        # Pictures
        options = webdriver.ChromeOptions()
        options.add_argument('--ignore-certificate-errors')
        options.add_argument("--test-type")
        options.binary_location = "/usr/bin/chromium"
        # driver = webdriver.Chrome(chrome_options=options)
        images = self.driver.find_elements_by_tag_name('img')
        pics_on_page = len(images)
        for image in images:
            print(image.get_attribute('src'))
        print(f'There are: {pics_on_page} images on the page')

        # End of the above code

    def clck_on_dvc_nln(self):
        # Click on DEVICE ONLINE card
        wait = WebDriverWait(self.driver, 15)
        wait.until(EC.element_to_be_clickable(DVC_ONLN_TXT)).click()

    def dvc_mngmnt_ptrl_hr(self, dvc_mngmnt_ptrl_hr):
        # Verify words Device Management Portal are here
        wait = WebDriverWait(self.driver, 15)
        expected_text = dvc_mngmnt_ptrl_hr
        actual_text = wait.until(EC.presence_of_element_located((DVC_MNGMNT_PRTL))).text
        assert expected_text in actual_text
        print(f'Expected "{expected_text}", and got: "{actual_text}" ')

    def onln_hr(self, onln_hr):
        # Verify words Device Management Portal are here
        wait = WebDriverWait(self.driver, 15)
        expected_text = onln_hr
        actual_text = wait.until(EC.presence_of_element_located((ONLN_HERE))).text
        assert expected_text in actual_text
        print(f'Expected "{expected_text}", and got: "{actual_text}" ')

        # End of the above code

    def vrf_qntty_is_the_same(self):
        # Pay attention to the number of devices on the "DEVICE ONLINE" card
        wait = WebDriverWait(self.driver, 15)
        sleep(2)
        txt_frm_dvc_onln = wait.until(EC.visibility_of_element_located(DVC_ONLN)).text

        # Click on DEVICE ONLINE card
        wait.until(EC.element_to_be_clickable(DVC_ONLN)).click()

        # And if there are no data in Device Management Portal verify text No Data Available is here
        no_data_available = wait.until(EC.element_to_be_clickable(NO_DATA)).text

        # If txt_frm_dvc_onln = 0 and no_data_available = 'No Data Available' stop and exit program
        if txt_frm_dvc_onln == '0' and no_data_available == 'No Data Available':
            print(
                f'Number of devices from DEVICE ONLINE element: {txt_frm_dvc_onln}, type: {type(txt_frm_dvc_onln)};\nNo data avalable is here: {no_data_available}, type {type(no_data_available)}.')
            # Driver quit
            self.driver.quit()
        else:

            # Count the number of devices with online status on the Devices page
            len_tbl = len(wait.until(EC.presence_of_all_elements_located(DVCS_TBL)))
            print(f'Quantity of the strings in the devices table: {len_tbl}')

            # Verify if the number of devices on the DEVICE ONLINE card should match the number of devices with online status on the Devices page
            assert txt_frm_dvc_onln in str(len_tbl)
            print(f'Expected "{txt_frm_dvc_onln}", and got: "{str(len_tbl)}" ')

            # End of the above code

    def clk_dvcs_onlc(self):
        # Click on DEVICE OFFLINE card
        wait = WebDriverWait(self.driver, 15)
        wait.until(EC.element_to_be_clickable(DVCS_OFFLN)).click()

    def offln_sts_hr(self):
        # Verify Offline status in FILTERS field is seen
        wait = WebDriverWait(self.driver, 15)
        expected_text = 'Offline'
        actual_text = wait.until(EC.presence_of_element_located((OFFLN_TXT))).text
        assert expected_text in actual_text
        print(f'Expected "{expected_text}", and got: "{actual_text}" ')

        # End of the above code

    def vrf_qntty_ofldvcs_is_the_same(self):
        # 6. Pay attention to the number of devices on the "DEVICE OFFLINE" card
        wait = WebDriverWait(self.driver, 15)
        txt_frm_dvc_offln = (wait.until(EC.visibility_of_all_elements_located(DVC_OFFLN)))[1].text
        print(f'Devices offline: {txt_frm_dvc_offln}')

        # 7.1 Click on DEVICE OFFLINE card
        (wait.until(EC.visibility_of_all_elements_located(DVC_OFFLN)))[1].click()

        # # 7.2 And if there are no data in Device Management Portal verify text No Data Available is here
        no_data_available = wait.until(EC.element_to_be_clickable(NO_DATA)).text

        # 7.3 If txt_frm_dvc_offln = 0 and no_data_available = 'No Data Available' stop and exit program
        if txt_frm_dvc_offln == '0' and no_data_available == 'No Data Available':
            print(
                f'Number of devices from DEVICE OFFLINE element: {txt_frm_dvc_offln}, type: {type(txt_frm_dvc_offln)};\nNo data avalable is here: {no_data_available}, type {type(no_data_available)}.')
            # Driver quit
            self.driver.quit()
        else:

            # Count the number of devices with offline status on the Devices page
            len_tbl = len(wait.until(EC.presence_of_all_elements_located(DVCS_TBL_EMPT)))
            print(f'Quantity of the strings in the devices table: {len_tbl}')

            # Verify if the number of devices on the DEVICE ONLINE card should match the number of devices with online status on the Devices page
            assert txt_frm_dvc_offln in str(len_tbl)
            print(f'Expected "{txt_frm_dvc_offln}", and got: "{str(len_tbl)}" ')

            # End of the above code

    def clck_on_invntr_elmnt(self):
        # Click on the INVENTORY card
        wait = WebDriverWait(self.driver, 15)
        invntr_elmnt = (wait.until(EC.presence_of_all_elements_located(INVNTR_ELMNT)))[2]
        invntr_elmnt.click()

    def invntr_sts_hr(self):
        # Inventory status in FILTERS field
        wait = WebDriverWait(self.driver, 15)
        expected_text = 'Inventory'
        actual_text = wait.until(EC.presence_of_element_located((INVNTR_TXT))).text
        assert expected_text in actual_text
        print(f'Expected "{expected_text}", and got: "{actual_text}" ')

        # End of the above code

    def invntr_qntty_is_the_same(self):
        # Verify if the number of devices on the INVENTORY card should match the number of devices with online status on the Devices page
        wait = WebDriverWait(self.driver, 15)
        # Pay attention to the number of devices on the "INVENTORY" card
        sleep(2)
        txt_frm_invntr = (wait.until(EC.visibility_of_all_elements_located(DVC_INVNTR)))[2].text
        print(f'Devices inventory: {txt_frm_invntr}')

        # Click on INVENTORY card
        (wait.until(EC.visibility_of_all_elements_located(DVC_INVNTR)))[1].click()

        # And if there are no data in Device Management Portal verify text No Data Available is here
        no_data_available = wait.until(EC.element_to_be_clickable(NO_DATA)).text

        # If txt_frm_dvc_offln = 0 and no_data_available = 'No Data Available' stop and exit program
        if txt_frm_invntr == '0' and no_data_available == 'No Data Available':
            print(
                f'Number of devices from INVENTORY element: {txt_frm_invntr}, type: {type(txt_frm_invntr)};\nNo data avalable is here: {no_data_available}, type {type(no_data_available)}.')
            # Driver quit
            self.driver.quit()
        else:

            # Count the number of devices with offline status on the Devices page
            len_tbl = len(wait.until(EC.presence_of_all_elements_located(DVCS_TBL_EMPT)))
            print(f'Quantity of the strings in the devices table: {len_tbl}')

            # Verify if the number of devices on the DEVICE ONLINE card should match the number of devices with online status on the Devices page
            assert txt_frm_invntr in str(len_tbl)
            print(f'Expected "{txt_frm_invntr}", and got: "{str(len_tbl)}" ')

            # End of the above code

    def clck_on_alrt_ntfctn_crd(self):
        # Click on ALERT/NOTIFICATION card
        wait = WebDriverWait(self.driver, 15)
        (wait.until(EC.element_to_be_clickable(ALRT_VRFCTN_CRT))).click()

    def alrt_dshbrd_wrds_on_pg(self):
        # Verify Alert Dashboard words on the page
        wait = WebDriverWait(self.driver, 15)
        sleep(2)
        txt_frm_invntr = (wait.until(EC.visibility_of_element_located(ALRT_DSHBRD_HR))).text
        print(f'"{txt_frm_invntr}" is on the page')

    # End of the above code

    def clck_on_dt_usg(self):
        # Click on the DATA USAGE card with Cellular data used
        wait = WebDriverWait(self.driver, 15)
        wait.until(EC.element_to_be_clickable(DT_USG_CRD)).click()

    def cllr_or_wan_txts_hr(self):
        # Verify that the DATA USAGE card has rotated to WAN data used and he DATA USAGE card has rotated back to Cellular data used
        wait = WebDriverWait(self.driver, 15)
        cllr_txt = wait.until(EC.visibility_of_element_located(CLLR)).text
        wan_txt = wait.until(EC.visibility_of_element_located(WAN)).text
        print(f'Text is here: "{cllr_txt}" or "{wan_txt}"')

    # End of the above code

    def clck_on_dsch_brd_mn_icn(self, dsbrd_txt):
        # Click Dashboard menu icon and make sure Dashboard page reloaded
        wait = WebDriverWait(self.driver, 15)
        wait.until(EC.visibility_of_element_located(DSCH_BRD_ICN)).click()
        dsch_brd_txt = wait.until(EC.visibility_of_element_located(DSCH_BRD_TXT)).text
        print(f'Text is here: "{dsch_brd_txt}"\n')
        assert dsbrd_txt in dsch_brd_txt

    def mk_sr_dt_usg_dtls_blck_hr(self, dt_usg_blk):
        # Make sure Data Usage Details block DATA USAGE is present on the screen
        wait = WebDriverWait(self.driver, 15)
        usg_dtls_txt = wait.until(EC.visibility_of_element_located(USG_DTLS_TXT)).text
        print(f'Text is here: "{usg_dtls_txt}"')
        assert dt_usg_blk in usg_dtls_txt

    def hvr_ovr_qstn_mrk_tl_tps_hr(self, tl_tp_txt):
        # Hover over question mark in top right of the block and make sure tooltip WAN/Cellular data usage classified periodically. appears
        wait = WebDriverWait(self.driver, 15)
        target = wait.until(EC.element_to_be_clickable(TL_TIP_TXT))
        actions = ActionChains(self.driver)
        actions.move_to_element(target)
        actions.click_and_hold(target)
        actions.perform()
        question_mark = wait.until(EC.visibility_of_element_located(TL_TIP_TXT))
        tool_tip_text = question_mark.get_attribute('tool-tip')
        print(f'Text is here: "{tool_tip_text}"')
        expected_text = tl_tp_txt
        actual_text = tool_tip_text
        if expected_text in actual_text:
            print(f'Expected "{expected_text}", and got: "{actual_text}" ')
        else:
            print(f'Expected "{expected_text}", but got: "{actual_text}" ')

    def clck_on_tdy_optn_drp_mn(self):
        # Change in drop-down changes the columns = click on Today option from drop-down menu
        wait = WebDriverWait(self.driver, 15)
        wait.until(EC.element_to_be_clickable(DT_USG_DRP_DWN_MN)).click()
        wait.until(EC.presence_of_element_located(DT_USG_DRP_DWN_MN)).send_keys(' Today ')

    def no_dt_avlbl_hr(self):
        # The inscription No Data Available is in the center
        wait = WebDriverWait(self.driver, 15)
        usg_dtls_txt = wait.until(EC.visibility_of_element_located(NO_DT_ABLBL)).text
        expected_text = 'No Data Available'
        actual_text = usg_dtls_txt
        if expected_text in actual_text:
            print(f'Expected "{expected_text}", and got: "{actual_text}" ')
        else:
            print(f'Expected "{expected_text}", but got: "{actual_text}" ')

    def gb_inctv_clmn_is_grey(self, clr_gr):
        # Verify GB inactive column highlighted grey when hover over it and hold
        wait = WebDriverWait(self.driver, 15)
        target = wait.until(EC.element_to_be_clickable(GB_INCTV_CLMN))
        actions = ActionChains(self.driver)
        actions.move_to_element(target)
        actions.click_and_hold(target)
        actions.perform()
        gb_inctv_clmn = wait.until(EC.visibility_of_element_located(GB_INCTV_CLMN)).value_of_css_property("color")
        assert clr_gr in gb_inctv_clmn
        expected_text = clr_gr
        actual_text = gb_inctv_clmn
        if expected_text in actual_text:
            print(f'Expected "{expected_text}", and got: "{actual_text}" ')
        else:
            print(f'Expected "{expected_text}", but got: "{actual_text}" ')

    # End of the above code

    def alrts_blk_prsnt(self, alrts_blk_txt):
        # Make sure Notifications / Alerts block is present on the screen
        wait = WebDriverWait(self.driver, 15)
        ntfctbs_alrts_txt = wait.until(EC.visibility_of_element_located(NTFCTNS_ALRTS_TXT)).text
        print(f'Notifications / Alerts is here: "{ntfctbs_alrts_txt}"\n')
        assert alrts_blk_txt in ntfctbs_alrts_txt

    def hvr_ovr_qstn_mrk(self):
        # Hover over question mark in top right of the block and make sure tooltip appears
        wait = WebDriverWait(self.driver, 15)
        target = wait.until(EC.element_to_be_clickable(NTFCTNS_ALRTS_TL_TIP))
        actions = ActionChains(self.driver)
        actions.move_to_element(target)
        actions.click_and_hold(target)
        actions.perform()
        question_mark = wait.until(EC.visibility_of_element_located(NTFCTNS_ALRTS_TL_TIP))
        tool_tip_text = question_mark.get_attribute('tool-tip')
        print(f'Text is here: "{tool_tip_text}"\n')
        expected_text = 'Alerts related to device(s)/group(s).'
        actual_text = tool_tip_text
        if expected_text in actual_text:
            print(f'Expected "{expected_text}", and got: "{actual_text}"\n')
        else:
            print(f'Expected "{expected_text}", but got: "{actual_text}"\n')

    def undrscr_hr(self, undr_scr):
        # Make sure that click on column header Groups makes it active by moving underscore sign = 0px none to it
        wait = WebDriverWait(self.driver, 15)
        wait.until(EC.element_to_be_clickable(CLCK_ON_GRPS_TB)).click()
        undescore_line = wait.until(EC.visibility_of_element_located(CLCK_ON_GRPS_TB)).value_of_css_property(
            "border-bottom")
        print(f'Underscore symbol: "{undescore_line}"\n')
        assert undr_scr in undescore_line
        expected_text = undr_scr
        actual_text = undescore_line
        if expected_text in actual_text:
            print(f'Expected "{expected_text}", and got: "{actual_text}"\n')
        else:
            print(f'Expected "{expected_text}", but got: "{actual_text}"\n')

    def gry_clr_inctv_clmn_hr(self, gry_clr_inctv_clmn_hr):
        # Verify Device inactive column highlighted grey = 128, 128, 128, 1 when hover over it and hold
        wait = WebDriverWait(self.driver, 15)
        target = wait.until(EC.element_to_be_clickable(DVC_GRY))
        actions = ActionChains(self.driver)
        actions.move_to_element(target)
        actions.click_and_hold(target)
        actions.perform()
        gb_inctv_clmn = wait.until(EC.visibility_of_element_located(DVC_GRY)).value_of_css_property("color")
        assert gry_clr_inctv_clmn_hr in gb_inctv_clmn
        expected_text = gry_clr_inctv_clmn_hr
        actual_text = gb_inctv_clmn
        if expected_text in actual_text:
            print(f'Expected "{expected_text}", and got: "{actual_text}"\n')
        else:
            print(f'Expected "{expected_text}", but got: "{actual_text}"\n')

    def no_dt_vlbl_on_ntfctn_alrt(self, no_dt_vlbl_on_ntfctn_alrt):
        # The inscription No Data Available is in the center and does not shift when switching columns
        wait = WebDriverWait(self.driver, 15)
        no_dt_when_grps = wait.until(EC.visibility_of_element_located(NO_DT_WHEN_GRPS)).text
        print(f'Text is here: "{no_dt_when_grps}"\n')
        assert no_dt_vlbl_on_ntfctn_alrt in no_dt_when_grps

    def clck_on_dvc_no_dt_avlb(self, clck_on_dvc_no_dt_avlb):
        # Click on Device and verify text No Data Available is here
        wait = WebDriverWait(self.driver, 15)
        wait.until(EC.element_to_be_clickable(CLCK_ON_DVC_TB)).click()
        no_dt_when_dvc = wait.until(EC.visibility_of_element_located(NO_DT_WHEN_DVC)).text
        print(f'Text is here: "{no_dt_when_dvc}"\n')
        assert clck_on_dvc_no_dt_avlb in no_dt_when_dvc

    def lctns_no_dt_avlbl_grps(self):
        # Locations of the No Data Available if Groups is active=undescored 0px none
        wait = WebDriverWait(self.driver, 15)
        e_grps = wait.until(EC.visibility_of_element_located(NO_DT_WHEN_GRPS))
        location_grps = e_grps.location
        size_grps = e_grps.size
        print(f'Groups is active=undescored location: "{location_grps}"\n')
        print(f'Groups is active=undescored size: "{size_grps}"\n')

    def lctns_no_dt_avlbl_dvc(self):
        # Locations of the No Data Available if Device is active=undescored 0px none
        wait = WebDriverWait(self.driver, 15)
        e_dvc = wait.until(EC.visibility_of_element_located(NO_DT_WHEN_DVC))
        location_dvc = e_dvc.location
        size_dvc = e_dvc.size
        print(f'Device is active=undescored location: "{location_dvc}"\n')
        print(f'Device is active=undescored size: "{size_dvc}"\n')

    def vrf_if_lctn_and_sz_of_n_dt_avlbl(self):
        # Verify the inscription No Data Available is in the center and does not shift when switching columns
        wait = WebDriverWait(self.driver, 15)
        e_grps = wait.until(EC.visibility_of_element_located(NO_DT_WHEN_GRPS))
        location_grps = e_grps.location
        size_grps = e_grps.size
        e_dvc = wait.until(EC.visibility_of_element_located(NO_DT_WHEN_DVC))
        location_dvc = e_dvc.location
        size_dvc = e_dvc.size
        if location_grps == location_dvc and size_grps == size_dvc:
            print(f'Ok, because "{location_grps}"="{location_dvc}" and\n "{size_grps}"="{size_dvc}"\n')

    # End of the above code

    def grps_blck_is_on_scrn(self, grps_blck_is_on_scrn):
        # Make sure Groups block is present on the screen
        wait = WebDriverWait(self.driver, 15)
        grps_txt_hr = wait.until(EC.visibility_of_element_located(GRPS_TXT_HR)).text
        print(f'Groups is here: "{grps_txt_hr}"\n')
        assert grps_blck_is_on_scrn in grps_txt_hr

    def ms_hvr_qstn_mrk_tp_rgt(self):
        # Mouse hover question mark in top right of the Groups block and make sure tooltip appears
        wait = WebDriverWait(self.driver, 15)
        target = wait.until(EC.element_to_be_clickable(QSTN_CRCL_MRK_GRPS_SCTN))
        actions = ActionChains(self.driver)
        actions.move_to_element(target)
        actions.click_and_hold(target)
        actions.perform()
        question_mark = wait.until(EC.visibility_of_element_located(QSTN_CRCL_TL_TP_TXT))
        tool_tip_text = question_mark.get_attribute('tool-tip')
        print(f'Text is here: "{tool_tip_text}"\n')
        expected_text = 'Device(s) status based on groups.'
        actual_text = tool_tip_text
        if expected_text in actual_text:
            print(f'Expected "{expected_text}", and got: "{actual_text}"\n')
        else:
            print(f'Expected "{expected_text}", but got: "{actual_text}"\n')

    def inscrptn_no_dt_avlbl_in_cntr_grps(self, inscrptn_no_dt_avlbl_in_cntr_grps):
        # The inscription No Data Available is in the center of Groups block
        wait = WebDriverWait(self.driver, 15)
        no_dt_in_grps_blck = wait.until(EC.visibility_of_element_located(NO_DT_IN_GRPS_BLCK)).text
        print(f'Text is here: "{no_dt_in_grps_blck}"\n')
        assert inscrptn_no_dt_avlbl_in_cntr_grps in no_dt_in_grps_blck
        # is in the center of Groups block
        e_grps = wait.until(EC.visibility_of_element_located(NO_DT_IN_GRPS_BLCK))
        location_grps = e_grps.location
        print(f'Location of "No Data Available": "{location_grps}"\n')
        if {'x': 90, 'y': 1168} == location_grps:
            print(f'"No Data Available" is in the center of Groups block\n')
        else:
            print(f'"No Data Available" is NOT in the center of Groups block\n')

    def drp_dwn_grps_hr(self):
        # Make sure that click on Groups drop-down list is working
        wait = WebDriverWait(self.driver, 15)
        target = wait.until(EC.element_to_be_clickable(GRPS_DRP_DWN_MN))
        actions = ActionChains(self.driver)
        actions.move_to_element(target)
        actions.click_and_hold(target)
        actions.perform()
        len_gprs_drp_dwn_mn = len(wait.until(EC.presence_of_all_elements_located(GRPS_DRP_DWN_MN_LST)))
        print(f'Elements in the Drop-down menu: "{len_gprs_drp_dwn_mn}"\n')

    def tl_tip_grps_hr(self):
        # Tooltip appears when mouse hover question mark in top right of the Groups block
        wait = WebDriverWait(self.driver, 15)
        target = wait.until(EC.element_to_be_clickable(GRPS_TL_TIP))
        actions = ActionChains(self.driver)
        actions.move_to_element(target)
        actions.click_and_hold(target)
        actions.perform()
        question_mark = wait.until(EC.visibility_of_element_located(GRPS_TL_TIP))
        tool_tip_text = question_mark.get_attribute('tool-tip')
        print(f'Text is here: "{tool_tip_text}"\n')
        expected_text = 'Device(s) status based on groups.'
        actual_text = tool_tip_text
        if expected_text in actual_text:
            print(f'Expected "{expected_text}", and got: "{actual_text}"\n')
        else:
            print(f'Expected "{expected_text}", but got: "{actual_text}"\n')

        # End of the above code

    def sgnl_strngt_txt_hr(self, sgnl_strngt_txt_hr):
        # Make sure Signal Strength is on the screen
        wait = WebDriverWait(self.driver, 15)
        sgnl_strngt_txt_hr = wait.until(EC.visibility_of_element_located(SGNL_STRNGT_TXT_HR)).text
        print(f'Signal Strength: "{sgnl_strngt_txt_hr}"\n')
        assert sgnl_strngt_txt_hr in sgnl_strngt_txt_hr

    def ms_hvr_qstn_mrk_sgnl_strngt(self):
        # Mouse hover question mark in top right of the Signal Strength block and make sure tooltip appears
        wait = WebDriverWait(self.driver, 15)
        target = wait.until(EC.element_to_be_clickable(QSTN_CRCL_SGNL_STRNGT_SCTN))
        actions = ActionChains(self.driver)
        actions.move_to_element(target)
        actions.click_and_hold(target)
        actions.perform()
        question_mark = wait.until(EC.visibility_of_element_located(QSTN_CRCL_SGNL_STRNGT_TXT))
        tool_tip_text = question_mark.get_attribute('tool-tip')
        print(f'Tool-tip text is here: "{tool_tip_text}"\n')
        expected_text = 'Overall signal strength statistics of device(s).'
        actual_text = tool_tip_text
        if expected_text in actual_text:
            print(f'Expected "{expected_text}", and got: "{actual_text}"\n')
        else:
            print(f'Expected "{expected_text}", but got: "{actual_text}"\n')

    def inscrptn_no_dt_avlbl_in_sgnl_strngt(self, inscrptn_no_dt_avlbl_in_sgnl_strngt):
        # The inscription No Data Available is in the center of Signal Strength block
        wait = WebDriverWait(self.driver, 15)
        no_dt_in_grps_blck = wait.until(EC.visibility_of_element_located(NO_DT_IN_SGNL_STRNGT_SCTN)).text
        print(f'Text is here: "{no_dt_in_grps_blck}"\n')
        assert inscrptn_no_dt_avlbl_in_sgnl_strngt in no_dt_in_grps_blck
        # is in the center of Groups block
        e_sgnl_strngt = wait.until(EC.visibility_of_element_located(NO_DT_IN_SGNL_STRNGT_SCTN))
        location_grps = e_sgnl_strngt.location
        print(f'Location of "No Data Available": "{location_grps}"\n')
        if {'x': 689, 'y': 1168} == location_grps:
            print(f'"No Data Available" is in the center of Groups block\n')
        else:
            print(f'"No Data Available" is NOT in the center of Groups block\n')

        # End of the above code

    def dvc_lctns_txt_hr(self, dvc_lctns_txt_hr):
        # Make sure Device Locations words are on the screen
        wait = WebDriverWait(self.driver, 15)
        dvc_lctns_txt_hr = wait.until(EC.visibility_of_element_located(DVC_LCTNS_TXT_HR)).text
        print(f'Device Locations: "{dvc_lctns_txt_hr}"\n')
        assert dvc_lctns_txt_hr in dvc_lctns_txt_hr

    def qstn_crcl_dvc_lctn_sctn(self):
        # Mouse hover question mark in top right of the block and make sure tooltip appears
        wait = WebDriverWait(self.driver, 15)
        target = wait.until(EC.element_to_be_clickable(QSTN_CRCL_DVC_LCTNS_SCTN))
        actions = ActionChains(self.driver)
        actions.move_to_element(target)
        actions.click_and_hold(target)
        actions.perform()
        question_mark = wait.until(EC.visibility_of_element_located(QSTN_CRCL_DVC_LCTNS_TXT))
        tool_tip_text = question_mark.get_attribute('tool-tip')
        print(f'Tool-tip text is here: "{tool_tip_text}"\n')
        expected_text = 'Current locations of the device(s).'
        actual_text = tool_tip_text
        if expected_text in actual_text:
            print(f'Expected "{expected_text}", and got: "{actual_text}"\n')
        else:
            print(f'Expected "{expected_text}", but got: "{actual_text}"\n')

    def dvc_lctns_drp_dwn_mn(self):
        # Make sure that click on Device Locations drop-down list is working
        wait = WebDriverWait(self.driver, 15)
        target = wait.until(EC.element_to_be_clickable(DVC_LCTNS_DRP_DWN_MN))
        actions = ActionChains(self.driver)
        actions.move_to_element(target)
        actions.click_and_hold(target)
        actions.perform()
        len_gprs_drp_dwn_mn = len(wait.until(EC.presence_of_all_elements_located(DVC_LCTNS_DRP_DWN_MN_LST)))
        print(f'Elements in the Drop-down menu: "{len_gprs_drp_dwn_mn}"\n')

        # End of the above code

    def clck_on_fltr_dvcs(self):
        # Click on Filter Devices and open Search page
        wait = WebDriverWait(self.driver, 15)
        wait.until(EC.element_to_be_clickable(FLTR_DVC_FUNNEL)).click()

    def onln_dvcs_chck_box_chkd(self):
        # Make sure that only Online Devices checkbox is checked in the Search page
        wait = WebDriverWait(self.driver, 15)
        onln_dvc_chck_chckd = wait.until(EC.presence_of_element_located(CHCK_BX_DVC_ONLN)).is_selected()
        print(f'Online Devices checkbox is checked: "{onln_dvc_chck_chckd}"\n')
        # Make sure Offline Devices checkbox is not checked in the Search page
        offln_dvc_chck_chckd = wait.until(EC.presence_of_element_located(CHCK_BX_DVC_OFFLN)).is_selected()
        print(f'Offline Devices checkbox is checked: "{offln_dvc_chck_chckd}"\n')
        # Make sure Inventory checkbox is not checked in the Search page
        inventory_chckd = wait.until(EC.presence_of_element_located(CHCK_BX_INVENTORY)).is_selected()
        print(f'Inventory checkbox is checked: "{inventory_chckd}"\n')

        # End of the above code

    def go_to_dvcs_pg(self, dvcs_url):
        # Go to the "Devices" page https://devcloud.connectedio.com/devices
        wait = WebDriverWait(self.driver, 15)
        wait.until(EC.element_to_be_clickable(DVCS_ICN)).click()
        expected_text = dvcs_url
        actual_text = self.driver.current_url
        assert expected_text in actual_text
        if expected_text == actual_text:
            print(f'Expected "{expected_text}", and got: "{actual_text}" \n')
        else:
            print(f'Expected "{expected_text}", but got: "{actual_text}" \n')

    def clck_add_nw_dvc(self):
        # Click Add new device button on the right up corner
        wait = WebDriverWait(self.driver, 15)
        wait.until(EC.element_to_be_clickable(ADD_NW_DVC_RGHT_CRNR)).click()

    def fill_emei_fld(self, emei):
        # Fill required Device IMEI field 356961071557824
        wait = WebDriverWait(self.driver, 15)
        wait.until(EC.presence_of_element_located(DVC_IMEI_FLD)).clear()
        wait.until(EC.presence_of_element_located(DVC_IMEI_FLD)).send_keys(emei)

    def fill_dvc_nm_fld(self, dvc_nm):
        # Fill Device Name field if any
        wait = WebDriverWait(self.driver, 15)
        wait.until(EC.presence_of_element_located(DVC_NAME_FLD)).clear()
        wait.until(EC.presence_of_element_located(DVC_NAME_FLD)).send_keys(dvc_nm)

    def fill_srl_nmbr_fld(self, srl_nmbr):
        # Fill required Serial Number field 1806208A0279
        wait = WebDriverWait(self.driver, 15)
        wait.until(EC.presence_of_element_located(DVC_SRL_NMBR_FLD)).clear()
        wait.until(EC.presence_of_element_located(DVC_SRL_NMBR_FLD)).send_keys(srl_nmbr)
        # Select Tags if any
        # No tags here to select

    def clck_sv_btn(self):
        # Click Save and refresh the page
        wait = WebDriverWait(self.driver, 15)
        wait.until(EC.element_to_be_clickable(DVC_ADD_SAVE_BTN)).click()
        self.driver.refresh()

    def dvc_is_on_the_pg(self):
        # Success is here - device is on the page
        wait = WebDriverWait(self.driver, 15)
        actual_text = wait.until(EC.visibility_of_element_located(IMEI_HR)).text
        print(f'IMEI: "{actual_text}"\n')
        expected_text = '356961071557824'
        assert expected_text in actual_text
        if expected_text == actual_text:
            print(f'Expected "{expected_text}", and got: "{actual_text}" \n')
        else:
            print(f'Expected "{expected_text}", but got: "{actual_text}" \n')

    def delt_dvc(self):
        # Delete device

        self.driver.refresh()

        # Go to the Devices page https://devcloud.connectedio.com/devices
        self.driver.refresh()
        wait = WebDriverWait(self.driver, 15)
        wait.until(EC.element_to_be_clickable(DVCS_ICN)).click()
        sleep(2)
        # Mark checkbox
        wait = WebDriverWait(self.driver, 15)
        wait.until(EC.element_to_be_clickable(CHCK_BX_FOR_DLT)).click()
        # Click gearbutton
        wait.until(EC.element_to_be_clickable(GEAR_BTN)).click()
        # Click remove devices button
        wait.until(EC.element_to_be_clickable(RMV_DVCS_BTN)).click()
        # Click delete button
        wait.until(EC.element_to_be_clickable(DLT_BTN_DVCS)).click()
        # Verify Success after delete is here
        actual_text = wait.until(EC.visibility_of_element_located(SCCSS_DLT_NO_DT_AVLBL)).text
        print(f'No Data Available: "{actual_text}"\n')
        expected_text = 'No Data Available'
        assert expected_text in actual_text
        if expected_text == actual_text:
            print(f'Expected "{expected_text}", and got: "{actual_text}" \n')
        else:
            print(f'Expected "{expected_text}", but got: "{actual_text}" \n')

        # End of the above code

    def add_nw_dvc_alrd_rgstrd(self):
        # Add a new device that has already registered in the system
        # Click Add new device button on the right up corner
        wait = WebDriverWait(self.driver, 15)
        self.driver.refresh()
        wait.until(EC.element_to_be_clickable(ADD_NW_DVC_RGHT_CRNR)).click()

        # Fill required Device IMEI field
        wait.until(EC.presence_of_element_located(DVC_IMEI_FLD)).clear()
        wait.until(EC.presence_of_element_located(DVC_IMEI_FLD)).send_keys('356961071557824')

        # Fill Device Name field if any
        wait.until(EC.presence_of_element_located(DVC_NAME_FLD)).clear()
        wait.until(EC.presence_of_element_located(DVC_NAME_FLD)).send_keys('TVM Test123 jjnkjn')

        # Fill required Serial Number field
        wait.until(EC.presence_of_element_located(DVC_SRL_NMBR_FLD)).clear()
        wait.until(EC.presence_of_element_located(DVC_SRL_NMBR_FLD)).send_keys('1806208A0279')

        # Select Tags if any
        # No tags here to select

        # Click Save the page
        wait.until(EC.element_to_be_clickable(DVC_ADD_SAVE_BTN)).click()

    def systm_vrfctn_dvc_alrd_exsts(self):
        # The system should check if the device has already registered a prompt should appear Device already exists
        wait = WebDriverWait(self.driver, 15)
        actual_text = wait.until(EC.element_to_be_clickable(DVC_ALRD_EXSTS)).text
        print(f'Text: {actual_text}\n')
        expected_text = 'Device already exists.'
        assert expected_text in actual_text
        if expected_text == actual_text:
            print(f'Expected "{expected_text}", and got: "{actual_text}" \n')
        else:
            print(f'Expected "{expected_text}", but got: "{actual_text}" \n')
        wait.until(EC.invisibility_of_element_located(DVC_ALRD_EXSTS))

        # Delete device
        # Close Add Device(s) pop-up-windows
        wait.until(EC.element_to_be_clickable(CROSS_TO_CLOSE)).click()
        # Mark checkbox
        wait.until(EC.element_to_be_clickable(CHCK_BX_FOR_DLT)).click()
        # Click gear button
        wait.until(EC.element_to_be_clickable(GEAR_BTN)).click()
        # Click remove devices button
        wait.until(EC.element_to_be_clickable(RMV_DVCS_BTN)).click()
        # Click delete button
        wait.until(EC.element_to_be_clickable(DLT_BTN_DVCS)).click()
        # Verify Success after delete is here
        actual_text = wait.until(EC.visibility_of_element_located(SCCSS_DLT_NO_DT_AVLBL)).text
        print(f'No Data Available: "{actual_text}"\n')
        expected_text = 'No Data Available'
        assert expected_text in actual_text
        if expected_text == actual_text:
            print(f'Expected "{expected_text}", and got: "{actual_text}" \n')
        else:
            print(f'Expected "{expected_text}", but got: "{actual_text}" \n')

        # End of the above code

    def bl_hlghtd_emei_choosen(self):
        # Choose any device with IMEI number which is highlighted in blue active IMEI number and click on an active IMEI number
        wait = WebDriverWait(self.driver, 15)
        wait.until(EC.element_to_be_clickable(EMEI_CLCK)).click()

    def dvc_dshbrd_opened(self, dvc_dshbrd_opened):
        # Verify the Device Management Portal page has opened
        wait = WebDriverWait(self.driver, 15)
        actual_text = wait.until(EC.visibility_of_element_located(DVC_MNGMNT_PRTL)).text
        print(f'Text is here: "{actual_text}"\n')
        expected_text = dvc_dshbrd_opened
        assert expected_text in actual_text
        if expected_text == actual_text:
            print(f'Expected "{expected_text}", and got: "{actual_text}" \n')
        else:
            print(f'Expected "{expected_text}", but got: "{actual_text}" \n')
        sleep(2)

        # End of the above code

    def clck_on_quick_actns_consqncs_hr(self):
        # Click on Quick Action button and verify it has consequences
        wait = WebDriverWait(self.driver, 15)
        wait.until(EC.element_to_be_clickable(QUICK_ACTION_BTN)).click()
        content = wait.until(EC.presence_of_all_elements_located(QUICK_ACTION_ID))
        for element in content:
            print(
                f'Elements names in the drop-down menu: "{element.text}", Quantity of elements in the drop-down menu: "{len(content)}"\n')

        # End of the above code

    def clck_on_sttngs_it_hs_reboot(self):
        # Click on Settings button in right up corner and verify it has Reboot item in the drop-down menu
        wait = WebDriverWait(self.driver, 15)
        wait.until(EC.element_to_be_clickable(STNGS_BTN)).click()
        actual_text = wait.until(EC.visibility_of_element_located(REBOOT_ELMNT_HR)).text
        assert 'Reboot' in actual_text
        print(f'Text is here: "{actual_text}"')

        # End of the above code

    def vrf_mdl_of_dvc(self, vrf_mdl_of_dvc):
        # Verify that model of device is ER2000T-NA-CAT1
        wait = WebDriverWait(self.driver, 15)
        actual_text = wait.until(EC.visibility_of_element_located(MODEL_TYPE)).text
        print(f'Model: "{actual_text}"\n')
        expected_text = vrf_mdl_of_dvc
        assert expected_text in actual_text
        if expected_text == actual_text:
            print(f'Expected "{expected_text}", and got: "{actual_text}" \n')
        else:
            print(f'Expected "{expected_text}", but got: "{actual_text}" \n')

    def dvc_rgth_lctn(self):
        # Device image should be present with the correct layout at the top left corner of page
        wait = WebDriverWait(self.driver, 15)
        dvc_pctr = wait.until(EC.visibility_of_element_located(DVC_PCTR))
        actual_text = str(dvc_pctr.location)
        print(f'Location of the device picture: "{actual_text}"\n')
        print(f'Got text: "{actual_text}" \n')

        # Pictures
        options = webdriver.ChromeOptions()
        options.add_argument('--ignore-certificate-errors')
        options.add_argument("--test-type")
        options.binary_location = "/usr/bin/chromium"
        images = self.driver.find_elements_by_tag_name('img')
        pics_on_page = len(images)
        for image in images:
            print((image.get_attribute('src')))
        print(f'There are: "{pics_on_page}" images on the page\n')

    def dvc_nm_crrlts_pic(self, dvc_nm_crrlts_pic):
        # The image of the device should correspond to the model in the description ER2000T1
        wait = WebDriverWait(self.driver, 15)
        actual_text = str(wait.until(EC.visibility_of_element_located(DVC_PCTR)).get_property('src'))
        print(f'Name of the src property: "{actual_text}"\n')
        expected_text = dvc_nm_crrlts_pic
        assert expected_text in actual_text
        if expected_text in actual_text:
            print(f'Expected "{expected_text}" in the: "{actual_text}" \n')
        else:
            print(f'Expected "{expected_text}", but got: "{actual_text}" \n')

        # End of the above code

    def imei_is_here(self, imei_is_here):
    # IMEI 356961071557824 is here
        wait = WebDriverWait(self.driver, 15)
        actual_text = wait.until(EC.visibility_of_element_located(IMEI_HR)).text
        print(f'IMEI: "{actual_text}"\n')
        expected_text = imei_is_here
        assert expected_text in actual_text
        if expected_text == actual_text:
            print(f'Expected "{expected_text}", and got: "{actual_text}" \n')
        else:
            print(f'Expected "{expected_text}", but got: "{actual_text}" \n')

    def mdl_is_here(self, mdl_is_here):
        # Model ER2000T-NA-CAT1 is here
        wait = WebDriverWait(self.driver, 15)
        # Choose any device with IMEI number which is highlighted in blue active IMEI number and click on an active IMEI number
        wait.until(EC.element_to_be_clickable(EMEI_CLCK)).click()
        actual_text = wait.until(EC.visibility_of_element_located(MODEL_TYPE)).text
        print(f'Model: "{actual_text}"\n')
        expected_text = mdl_is_here
        assert expected_text in actual_text
        if expected_text == actual_text:
            print(f'Expected "{expected_text}", and got: "{actual_text}" \n')
        else:
            print(f'Expected "{expected_text}", but got: "{actual_text}" \n')

    def frmwr_is_here(self, frmwr_is_here):
        # Firmware version VR2 4.0 is here
        wait = WebDriverWait(self.driver, 15)
        actual_text = wait.until(EC.visibility_of_element_located(FRM_VRSN)).text
        print(f'Firmware version: "{actual_text}"\n')
        expected_text = frmwr_is_here
        assert expected_text in actual_text
        if expected_text == actual_text:
            print(f'Expected "{expected_text}", and got: "{actual_text}" \n')
        else:
            print(f'Expected "{expected_text}", but got: "{actual_text}" \n')

    def mdm_frmwr_is_here(self, mdm_frmwr_is_here):
        # Modem firmware 20.00.524 is here
        wait = WebDriverWait(self.driver, 15)
        actual_text = wait.until(EC.visibility_of_element_located(MDM_FRM)).text
        print(f'Modem firmware: "{actual_text}"\n')
        expected_text = mdm_frmwr_is_here
        assert expected_text in actual_text
        if expected_text == actual_text:
            print(f'Expected "{expected_text}", and got: "{actual_text}" \n')
        else:
            print(f'Expected "{expected_text}", but got: "{actual_text}" \n')

    def lst_hrd_is_here(self, lst_hrd_is_here):
        # Last heard is here
        wait = WebDriverWait(self.driver, 15)
        actual_text = wait.until(EC.visibility_of_element_located(LAST_HEARD)).text
        print(f'Last heard is here: "{actual_text}"\n')
        expected_text = lst_hrd_is_here
        assert expected_text in actual_text
        if expected_text == actual_text:
            print(f'Expected "{expected_text}", and got: "{actual_text}" \n')
        else:
            print(f'Expected "{expected_text}", but got: "{actual_text}" \n')

    def uptm_is_here(self, uptm_is_here):
        # Section Uptime is here
        wait = WebDriverWait(self.driver, 15)
        actual_text = wait.until(EC.visibility_of_element_located(UPTIME)).text
        print(f'Uptime is here: "{actual_text}"\n')
        expected_text = uptm_is_here
        assert expected_text in actual_text
        if expected_text == actual_text:
            print(f'Expected "{expected_text}", and got: "{actual_text}" \n')
        else:
            print(f'Expected "{expected_text}", but got: "{actual_text}" \n')

        # End of the above code

    def ip_tx_rx_mac_pie_chrt(self):
        # Pay attention to the WAN section.
        # Verify that the following details displayed: IP address, TX data from last reboot (KB), RX data from last reboot (KB), MAC address and Pie Chart.
        # IP address
        wait = WebDriverWait(self.driver, 15)
        wait.until(EC.element_to_be_clickable(EMEI_CLCK)).click()
        actual_text = wait.until(EC.visibility_of_element_located(IP_ADDRESS)).text
        if len(actual_text) >= 0:
            print(f'IP Address: "{actual_text}"\n')
        # TX data from last reboot (KB)
        actual_text = wait.until(EC.visibility_of_element_located(TX_DATA_FRM_LST_RBT)).text
        if len(actual_text) >= 0:
            print(f'TX data from last reboot (KB): "{actual_text}"\n')
        # RX data from last reboot (KB)
        actual_text = wait.until(EC.visibility_of_element_located(RX_DATA_FRM_LST_RBT)).text
        if len(actual_text) >= 0:
            print(f'RX data from last reboot (KB): "{actual_text}"\n')
        # MAC address
        actual_text = wait.until(EC.visibility_of_element_located(MAC_ADDRESS)).text
        if len(actual_text) >= 0:
            print(f'MAC address: "{actual_text}"\n')
        # Pie Chart
        actual_text = str(wait.until(EC.visibility_of_element_located(PIE_CHART)).get_property('src'))
        if len(actual_text) >= 0:
            print(f'Pie Chart: "{actual_text}"\n')

        # End of the above code

    def sim_ip_tx_rx_mac_pie_chrt(self):
        # Pay attention to the SIM section.
        # # Verify that the following details displayed: IP address, TX data from last reboot (KB), RX data from last reboot (KB), ICC number, APN and Pie Chart.
        # # SIM IP address
        wait = WebDriverWait(self.driver, 15)
        wait.until(EC.element_to_be_clickable(EMEI_CLCK)).click()
        actual_text = wait.until(EC.visibility_of_element_located(SIM_IP_ADDRESS)).text
        if len(actual_text) >= 0:
            print(f'SIM IP Address: "{actual_text}"\n')
        # SIM TX data from last reboot (KB)
        actual_text = wait.until(EC.visibility_of_element_located(SIM_TX_DATA_FRM_LST_RBT)).text
        if len(actual_text) >= 0:
            print(f'SIM TX data from last reboot (KB): "{actual_text}"\n')
        # SIM RX data from last reboot (KB)
        actual_text = wait.until(EC.visibility_of_element_located(SIM_RX_DATA_FRM_LST_RBT)).text
        if len(actual_text) >= 0:
            print(f'SIM RX data from last reboot (KB): "{actual_text}"\n')
        # SIM ICC number
        actual_text = wait.until(EC.visibility_of_element_located(ICC_NUMBER)).text
        if len(actual_text) >= 0:
            print(f'SIM MAC address: "{actual_text}"\n')
        # SIM APN
        actual_text = wait.until(EC.visibility_of_element_located(APN)).text
        if len(actual_text) >= 0:
            print(f'SIM MAC address: "{actual_text}"\n')
        # SIM Pie Chart
        actual_text = str(wait.until(EC.visibility_of_element_located(SIM_PIE_CHART)).get_property('src'))
        if len(actual_text) >= 0:
            print(f'SIM Pie Chart: "{actual_text}"\n')

        # End of the above code

    def lan_ip_tx_rx_mac_pie_chrt(self):
        # Pay attention to the LAN section.
        # Verify that the following details displayed: IP address, TX data from last reboot KB, RX data from last reboot KB, MAC address and Pie Chart.
        # LAN IP address
        wait = WebDriverWait(self.driver, 15)
        wait.until(EC.element_to_be_clickable(EMEI_CLCK)).click()
        actual_text = wait.until(EC.visibility_of_element_located(LAN_IP_ADDRESS)).text
        if len(actual_text) >= 0:
            print(f'LAN IP Address: "{actual_text}"\n')
        # LAN TX data from last reboot (KB)
        actual_text = wait.until(EC.visibility_of_element_located(LAN_TX_DATA_FRM_LST_RBT)).text
        if len(actual_text) >= 0:
            print(f'LAN TX data from last reboot (KB): "{actual_text}"\n')
        # LAN RX data from last reboot (KB)
        actual_text = wait.until(EC.visibility_of_element_located(LAN_RX_DATA_FRM_LST_RBT)).text
        if len(actual_text) >= 0:
            print(f'LAN RX data from last reboot (KB): "{actual_text}"\n')
        # LAN Mac address
        actual_text = wait.until(EC.visibility_of_element_located(LAN_MAC_ADDRESS)).text
        if len(actual_text) >= 0:
            print(f'LAN MAC address: "{actual_text}"\n')
        # LAN Pie Chart
        actual_text = str(wait.until(EC.visibility_of_element_located(LAN_PIE_CHART)).get_property('src'))
        if len(actual_text) >= 0:
            print(f'LAN Pie Chart: "{actual_text}"\n')

        # End of the above code

    def clck_on_quick_actions_in_rght_up_crnr(self):
        # Click on Quick action button
        wait = WebDriverWait(self.driver, 15)
        wait.until(EC.element_to_be_clickable(QUICK_ACTION_BTN)).click()

    def clck_on_rfrsh_sbsctn(self):
        # Click Refresh subsection
        wait = WebDriverWait(self.driver, 15)
        wait.until(EC.element_to_be_clickable(REFRESH_BTN)).click()

    def rfrsh_sbsctn_actv(self, text):
        # Verify Refresh subsection is active and Fetching data from device... appeares
        wait = WebDriverWait(self.driver, 15)
        expected_text = text
        actual_text = wait.until(EC.presence_of_element_located((FTCHNG_DT_FRM_DVC))).text
        assert expected_text in actual_text
        print(f'Expected "{expected_text}", and got: "{actual_text}" ')

        # End of the above code

    def clck_systemlog(self):
        # Click System log subsection
        wait = WebDriverWait(self.driver, 15)
        wait.until(EC.element_to_be_clickable(SYSTEM_LOG)).click()

        # End of the above code

    def add_new_dvc_onln(self):
        # Add a new device to the Device online
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(ADD_NEW_DVC_ONLN)).click()

        # Fill required Device IMEI field
        wait.until(EC.presence_of_element_located(DVC_IMEI_FLD)).clear()
        wait.until(EC.presence_of_element_located(DVC_IMEI_FLD)).send_keys('358148062783217')

        # Fill Device Name field if any
        wait.until(EC.presence_of_element_located(DVC_NAME_FLD)).clear()
        wait.until(EC.presence_of_element_located(DVC_NAME_FLD)).send_keys('Device Name 1')

        # Fill required Serial Number field
        wait.until(EC.presence_of_element_located(DVC_SRL_NMBR_FLD)).clear()
        wait.until(EC.presence_of_element_located(DVC_SRL_NMBR_FLD)).send_keys('1933215B2356')

        # Select Tags if any
        # No tags here to select

        # Click Save the page
        wait.until(EC.element_to_be_clickable(DVC_ADD_SAVE_BTN)).click()
        self.driver.refresh()

    def system_log_txt_hr(self, text_hr):
        # Verify the device system log is displayed
        wait = WebDriverWait(self.driver, 10)
        expected_text = text_hr
        actual_text = wait.until(EC.presence_of_element_located((SYSTEM_LOG_TXT_HR))).text
        assert expected_text in actual_text
        print(f'Expected "{text_hr}", and got "{actual_text}" ')
        # End of the above code
        sleep(2)

    def clck_close_systemlog(self):
        # Click on the Close icon at the top right corner of the system log
        wait = WebDriverWait(self.driver, 15)
        wait.until(EC.element_to_be_clickable(CLOSE_SYSTEM_LOG)).click()

    # End of the above code
