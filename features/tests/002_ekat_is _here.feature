# Created by rapid at 12/17/2020
Feature: # Enter the main page, click on Ekaterinburg/Yes and verify "https://ekaterinburg.gtdel.com/" is here

  Scenario: # Enter the main page, click on Ekaterinburg/Yes and verify "https://ekaterinburg.gtdel.com/" is here
    Given Loginpage
    Then Click on Ekaterinburg/Yes
    And Verify "https://ekaterinburg.gtdel.com/" is here