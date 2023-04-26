import pytest
import time
from utilities.base_class import BaseClass
from pages.navigation import Navigation


class Test_Event_Logger_Suite(BaseClass):

    ################################## FIXTURES ##################################
    @pytest.fixture
    def log(self):
        log = self.getLogger()
        return log

    @pytest.fixture
    def navigation(self):
        navigation = Navigation(self.driver)

        return navigation

    ################################## TEST CASES ##################################

    def test_event_A(self, navigation, log):
        addProductPage = navigation.go_to_add_products()
        log.info("Testing A1.1")
        addProductPage.get_name_input().send_keys("Testing")
        log.info("Testing A1.2")
        self.driver.back()
        log.info("Testing A1.3")
        # assert False

    def test_event_fail_A(self, navigation, log):
        addProductPage = navigation.go_to_add_products()
        log.info("Testing A2.1")
        addProductPage.get_name_input().send_keys("Testing")
        log.info("Testing A2.2")
        navigation.get_non_existing_element().click()
        log.info("Testing A2.3")
        self.driver.back()
        log.info("Testing A2.4")
        # assert False
