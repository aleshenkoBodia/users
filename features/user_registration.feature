Feature: User Registration
  Scenario: Successful user registration
    Given I am on the registration page
    When I fill in "username" with "testuser21"
    And I fill in "password1" with "12345678@"
    And I fill in "password2" with "12345678@"
    And I press "Register"
    Then I should be redirected to the login page
