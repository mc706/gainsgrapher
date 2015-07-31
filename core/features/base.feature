Feature: The Basic Login Functions
  
  Scenario: Admin Page
    Given I am on the page with relative url "/admin/"
    Then I should be on the page with relative url "/admin/login/?next=/admin/"