from selenium.webdriver.support.events import AbstractEventListener
from utilities.base_class import BaseClass


class EventLogger(AbstractEventListener, BaseClass):

    def __init__(self):
        self.logger = self.getLogger()

    def before_navigate_to(self, url: str, driver) -> None:
        self.logger.debug(f"going to {url} ...")

    def after_navigate_to(self, url: str, driver) -> None:
        self.logger.debug(f"reached {url}")

    def before_navigate_back(self, driver) -> None:
        self.logger.debug("navigating back ...")

    def after_navigate_back(self, driver) -> None:
        self.logger.debug("navigated back")

    def before_navigate_forward(self, driver) -> None:
        self.logger.debug("navigating forward ...")

    def after_navigate_forward(self, driver) -> None:
        self.logger.debug("navigated forward")

    def before_find(self, by, value, driver) -> None:
        self.logger.debug(f"finding {by} with value {value} ...")

    def after_find(self, by, value, driver) -> None:
        self.logger.debug(f"found {by} with value {value}")

    def before_click(self, element, driver) -> None:
        self.logger.debug("clicking element ... ")

    def after_click(self, element, driver) -> None:
        self.logger.debug("clicked element")

    def before_change_value_of(self, element, driver) -> None:
        self.logger.debug("changing value in element ...")

    def after_change_value_of(self, element, driver) -> None:
        self.logger.debug("changed value in element")

    def before_execute_script(self, script, driver) -> None:
        self.logger.debug(f"executing {script} ...")

    def after_execute_script(self, script, driver) -> None:
        self.logger.debug(f"executed {script}")

    def before_close(self, driver) -> None:
        self.logger.debug("closing ...")

    def after_close(self, driver) -> None:
        self.logger.debug("closed")

    def before_quit(self, driver) -> None:
        self.logger.debug("quitting ...")

    def after_quit(self, driver) -> None:
        self.logger.debug("quit ...")

    def on_exception(self, exception, driver) -> None:
        self.logger.debug(f"exception: {exception}")
