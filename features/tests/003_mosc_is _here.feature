# Created by rapid at 12/17/2020
Feature: # Enter the main page, click on Ekaterinburg/Moscow and https://moscow.gtdel.com/ is here

  Scenario: # Enter the main page, click on Ekaterinburg/Moscow and https://moscow.gtdel.com/ is here
    Given Loginpage
    Then Click on Ekaterinburg/Moscow
    And Verify "https://moscow.gtdel.com/" is here