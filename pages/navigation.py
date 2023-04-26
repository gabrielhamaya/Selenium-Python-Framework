from selenium.webdriver.common.by import By

from pages.product_page import ProductPage
from pages.add_product_page import AddProductPage


class Navigation:
    ################################## CONSTRUCTOR ##################################
    def __init__(self, driver):
        self.driver = driver

    ################################## LOCATORS ##################################
    products_tab = (By.CSS_SELECTOR, "[data-testid='navbar-products']")
    add_products_tab = (By.CSS_SELECTOR, "[data-testid='navbar-addproduct']")
    practice_tab = (By.CSS_SELECTOR, "[data-testid='navbar-practice']")
    learn_tab = (By.CSS_SELECTOR, "[data-testid='navbar-learn']")
    login_tab = (By.CSS_SELECTOR, "[data-testid='navbar-login']")

    # Test
    non_existing_element = (By.CLASS_NAME, ".non-existing-class")

    ################################## GETTER ##################################

    def get_non_existing_element(self):
        self.driver.find_element(*self.non_existing_element)

    ################################## CUSTOM METHODS ##################################
    def go_to_products(self):
        self.driver.find_element(*self.products_tab).click()
        productPage = ProductPage(self.driver)
        return productPage

    def go_to_add_products(self):
        self.driver.find_element(*self.add_products_tab).click()
        addProductPage = AddProductPage(self.driver)
        return addProductPage
