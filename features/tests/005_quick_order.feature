# Created by rapid at 12/28/2020
Feature: # Fill the form of "Quick order"

  Scenario: # Fill the form of "Quick order"
    Given Loginpage
    Then Click on "ЗАКАЗАТЬ"
    And Click on "от терминала"
    Then Click on "до терминала"
    And Send "999" to "кг"
    Then Send "3.500" to "м3"
    And Send "3" to "мест"
    Then Send "30000" to "₽"
    And Click on "рассчитать"
    Then Verify "4 дня" is here as text
    And Verify "8 941 ₽/8&nbsp;941 ₽" is here as text