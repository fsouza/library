Feature: List of books
  In order to loan a book
  As a system user
  I want to see the list of all books in the system

  Scenario: List all books
    Given there are 20 books in the system
    When I navigate to the listing page
    Then I should see the 20 books titles
