from selenium.webdriver.common.by import By


class ProductPage:
    ################################## CONSTRUCTOR ##################################
    def __init__(self, driver) -> None:
        self.driver = driver

    #################################### LOCATORS ####################################
    filter_textbox = (By.CLASS_NAME, "filter-textbox")
    filter_button = (By.CSS_SELECTOR, "[data-testid='filter-button']")

    #################################### GETTERS ####################################

    def get_filter_textbox(self):
        return self.driver.find_element(*self.filter_textbox)
