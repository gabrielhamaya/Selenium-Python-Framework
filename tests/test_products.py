import pytest
from utilities.base_class import BaseClass
from pages.product_page import ProductPage


class Test_Product_Suite(BaseClass):
    ################################## FIXTURES ##################################
    @pytest.fixture
    def productPage(self):
        # Initialize Product Page POM
        productPage = ProductPage(self.driver)
        return productPage

    ################################## TEST CASES ##################################
    def test_access_productpage_KEY_XXX(self):
        # Assert you've reached the dashboard page
        assert "/" in self.driver.current_url

    def test_access_fail_productpage_KEY_XXX(self):
        # Assert you've reached the dashboard page
        assert "/failed" in self.driver.current_url
