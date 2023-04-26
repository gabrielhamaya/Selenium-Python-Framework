import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.events import EventFiringWebDriver
from utilities.event_logger import EventLogger
import logging

driver = None

# Setup config


@pytest.fixture(scope="class")
def setup(request):
    global driver

    # Install the Browser Driver
    chromeManager = ChromeDriverManager().install()

    # Invoke Chrome Driver
    service_obj = ChromeService(chromeManager)
    driver_browser = webdriver.Chrome(service=service_obj)

    # Setup the event lister for the logger
    driver = EventFiringWebDriver(driver_browser, EventLogger())

    # Go to page / Local
    driver.get("https://commitquality.com/")
    driver.maximize_window()

    # Extend implicit wait to 10 seconds
    driver.implicitly_wait(10)

    # Store webdriver instance
    request.cls.driver = driver

    # Close the browser once done
    yield
    driver.close()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):

    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            path = file_name.replace("tests", "reports")
            html_image_src = file_name.replace("tests", ".")
            driver.get_screenshot_as_file(path)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                    'onclick="window.open(this.src)" align="right"/></div>' % html_image_src
                extra.append(pytest_html.extras.html(html))
        report.extra = extra
