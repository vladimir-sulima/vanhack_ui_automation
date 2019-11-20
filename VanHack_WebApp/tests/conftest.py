import json
import pytest
import os

from selenium.webdriver import Chrome, Firefox

PATH_TO_PROJECT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
PATH_TO_WEBDRIVER = PATH_TO_PROJECT + "\\framework\\WebDrivers"
CONFIG_PATH = PATH_TO_PROJECT + "\\VanHack_WebApp\\config.json"
DEFAULT_WAIT_TIME = 10
SUPPORTED_BROWSERS = ['chrome', 'firefox']


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default=read_browser_from_config(), help="Type in BROWSER name")


def read_browser_from_config():
    with open(CONFIG_PATH) as config_file:
        data = json.load(config_file)
    return data['browser']


@pytest.fixture(scope='session')
def config():
    with open(CONFIG_PATH) as config_file:
        data = json.load(config_file)
    return data


@pytest.fixture(scope='session')
def config_browser(config, request):
    browser = request.config.getoption("--browser")
    if request.config.getoption("--browser") not in SUPPORTED_BROWSERS:
        raise Exception(f'"{browser}"is not supported browser')
    return browser


@pytest.fixture(scope='session')
def config_wait_time(config):
    return config['wait_time'] if 'wait_time' in config else DEFAULT_WAIT_TIME


@pytest.fixture(scope='session')
def config_url(config):
    return config['url']


@pytest.fixture(scope='session')
def config_failed_tests_screenshot_path(config):
    return config['failed_tests_screenshots_path']


@pytest.fixture
def browser(request, config_browser, config_wait_time, config_url):
    browser = request.config.getoption("--browser")
    if browser == 'chrome':
        browser = Chrome(executable_path=f"{PATH_TO_WEBDRIVER}\\chromedriver.exe")
    elif browser == 'firefox':
        browser = Firefox(executable_path=f"{PATH_TO_WEBDRIVER}\\geckodriver.exe")
    else:
        raise Exception(f'"Unable to find webdriver for {config_browser}" browser.')
    browser.maximize_window()
    browser.implicitly_wait(config_wait_time)
    browser.get(config_url)
    yield browser
    browser.quit()