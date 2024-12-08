from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class EbayHomePage:
    SEARCH_INPUT = (By.ID, 'gh-ac')
    SEARCH_BUTTON = (By.ID, 'gh-btn')

    def __init__(self, driver):
        self.driver = driver

    def search_item(self, item):
        search_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.SEARCH_INPUT)
        )
        search_input.clear()
        search_input.send_keys(item)
        
        search_button = self.driver.find_element(*self.SEARCH_BUTTON)
        search_button.click()

class SearchResultsPage:
    FIRST_ITEM = (By.XPATH, '(((//li[contains(@class, "s-item")])[3])//a)[1]')

    def __init__(self, driver):
        self.driver = driver

    def select_first_item(self):
        first_item = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.FIRST_ITEM)
        )
        self.driver.execute_script("arguments[0].click();", first_item)
        self.driver.switch_to.window(self.driver.window_handles[1])

class ItemPage:
    ADD_TO_CART_BUTTON = (By.ID, 'atcBtn_btn_1')
    CART_ITEMS_COUNT = (By.ID, 'gh-cart-n')

    def __init__(self, driver):
        self.driver = driver

    def add_to_cart(self):
        add_to_cart = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.ADD_TO_CART_BUTTON)
        )
        add_to_cart.click()

    def get_cart_items_count(self):
        cart_count = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.CART_ITEMS_COUNT)
        )
        assert int(cart_count.text) == 1
        return cart_count.text