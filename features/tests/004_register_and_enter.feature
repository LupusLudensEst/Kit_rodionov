# Created by rapid at 12/18/2020
Feature: # Enter the main page as a new user and verify Подтверждение доступа is here

  Scenario: # Enter the main page as a new user and verify Подтверждение доступа is here
    Given Loginpage
    Then Click on Ekaterinburg/Moscow
    And Register as a new user
    Then Verify text: "Подтверждение доступа" is here
