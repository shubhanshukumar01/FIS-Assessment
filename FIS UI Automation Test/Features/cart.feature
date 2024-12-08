Feature: eBay Cart Functionality
  As a user
  I want to add an item to the cart
  So that I can proceed with purchasing

  Scenario: Verify item can be added to Cart
    Given I open the browser
    And I navigate to ebay.com
    When I search for 'book'
    And I select the first book in the list
    And I click 'Add to cart'
    Then the cart should display the number of items added