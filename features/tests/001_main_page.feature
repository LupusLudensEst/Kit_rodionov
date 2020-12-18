# Created by rapid at 12/17/2020
Feature: # Enter the main page and verify "GTD - доступно, выгодно, надежно." is here

  Scenario: # Enter the main page and verify "GTD - доступно, выгодно, надежно." is here
    Given Loginpage
    Then Verify text "GTD - доступно, выгодно, надежно." is here
