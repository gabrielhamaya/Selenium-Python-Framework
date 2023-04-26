from selenium.webdriver.common.by import By


class AddProductPage:
    ################################## CONSTRUCTOR ##################################
    def __init__(self, driver) -> None:
        self.driver = driver

    #################################### LOCATORS ####################################
    name_input = (By.CSS_SELECTOR, "[data-testid='product-textbox']")

    #################################### GETTERS ####################################

    def get_name_input(self):
        return self.driver.find_element(*self.name_input)
