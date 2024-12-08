from behave import given, when, then
from selenium import webdriver
from pages.ebay_pages import EbayHomePage, SearchResultsPage, ItemPage

@given('I open the browser')
def step_open_browser(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()



@given('I navigate to ebay.com')
def step_navigate_to_ebay(context):
    context.driver.get('https://www.ebay.com')

@when('I search for \'book\'')
def step_search_for_book(context):
    home_page = EbayHomePage(context.driver)
    home_page.search_item('book')

@when('I select the first book in the list')
def step_select_first_book(context):
    results_page = SearchResultsPage(context.driver)
    results_page.select_first_item()

@when('I click \'Add to cart\'')
def step_add_to_cart(context):
    item_page = ItemPage(context.driver)
    item_page.add_to_cart()

@then('the cart should display the number of items added')
def step_verify_cart_items(context):
    item_page = ItemPage(context.driver)
    cart_count = item_page.get_cart_items_count()
    assert cart_count == '1', f"Expected cart count to be 1, but got {cart_count}"
    context.driver.quit()