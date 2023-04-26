from selenium.webdriver.support.events import AbstractEventListener
import logging


# This logging instance is used specifically to log events that happen in the tests
logger = logging.getLogger(__name__)

logger.setLevel(logging.DEBUG)

fileHandler = logging.FileHandler('event.log')
formatter = logging.Formatter(
    "%(asctime)s : %(levelname)s : %(name)s : %(message)s")

fileHandler.setFormatter(formatter)
logger.addHandler(fileHandler)


class EventLogger(AbstractEventListener):

    logger = logger

    def before_navigate_to(self, url: str, driver) -> None:
        logger.debug(f"going to {url} ...")

    def after_navigate_to(self, url: str, driver) -> None:
        logger.debug(f"reached {url}")

    def before_navigate_back(self, driver) -> None:
        logger.debug("navigating back ...")

    def after_navigate_back(self, driver) -> None:
        logger.debug("navigated back")

    def before_navigate_forward(self, driver) -> None:
        logger.debug("navigating forward ...")

    def after_navigate_forward(self, driver) -> None:
        logger.debug("navigated forward")

    def before_find(self, by, value, driver) -> None:
        logger.debug(f"finding {by} with value {value} ...")

    def after_find(self, by, value, driver) -> None:
        logger.debug(f"found {by} with value {value}")

    def before_click(self, element, driver) -> None:
        logger.debug("clicking element ... ")

    def after_click(self, element, driver) -> None:
        logger.debug("clicked element")

    def before_change_value_of(self, element, driver) -> None:
        logger.debug("changing value in element ...")

    def after_change_value_of(self, element, driver) -> None:
        logger.debug("changed value in element")

    def before_execute_script(self, script, driver) -> None:
        logger.debug(f"executing {script} ...")

    def after_execute_script(self, script, driver) -> None:
        logger.debug(f"executed {script}")

    def before_close(self, driver) -> None:
        logger.debug("closing ...")

    def after_close(self, driver) -> None:
        logger.debug("closed")

    def before_quit(self, driver) -> None:
        logger.debug("quitting ...")

    def after_quit(self, driver) -> None:
        logger.debug("quit ...")

    def on_exception(self, exception, driver) -> None:
        logger.debug(f"exception: {exception}")
