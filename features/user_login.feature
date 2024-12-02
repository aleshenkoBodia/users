Feature: User Login
  Scenario: Successful user login
    Given I am on the login page
    And a user exists with username "testuser" and password "TestPassword123"
    When I fill in "username" with "testuser"
    And I fill in "password" with "TestPassword123"
    And I press "Login"
    Then I should be redirected to the home page
    And I should see "Welcome to the site!"