Feature: List of books
  In order to loan a book
  As a system user
  I want to see the list of all books in the system

  Scenario: List all books
    Given there are 20 books in the system
    When I navigate to the books list page
    Then I should see the title of the 20 books
