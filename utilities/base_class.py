import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
import logging


@pytest.mark.usefixtures("setup")
class BaseClass:

    def waitForLink(self, text):
        wait = WebDriverWait(self.driver, 15)
        wait.until(expected_conditions.presence_of_element_located((
            By.LINK_TEXT, text)))

    def waitForPage(self, page):
        wait = WebDriverWait(self.driver, 15)
        wait.until(expected_conditions.url_contains(
            (page)))

    def getLogger(self) -> logging:
        """This method is used to create logs for debug purposes

        Returns:
            logging: returns an object that will be used to log the events
        """

        # Set up name of the logger, in this case we're using the name of the test case that triggered it (In theory)
        logger = logging.getLogger(__name__)

        # Set level, will only print the specified levels, since we are selecting debug that will be all the levels (debug > info > warning > error > critical)
        logger.setLevel(logging.DEBUG)

        # We add a file handler to save the path we want to store the log in
        fileHandler = logging.FileHandler('debug.log')

        # Format the log
        format = logging.Formatter(
            "%(asctime)s : %(levelname)s : %(name)s : %(message)s")
        fileHandler.setFormatter(format)

        # Add the handler configurations to the logger
        logger.addHandler(fileHandler)

        return logger
