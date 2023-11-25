import pytest
from selenium import webdriver

from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.os_manager import ChromeType

from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.edge.options import Options as EdgeOptions
from webdriver_manager.microsoft import EdgeChromiumDriverManager

from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from webdriver_manager.firefox import GeckoDriverManager

from selenium.webdriver.ie.service import Service as IEService
from selenium.webdriver.ie.options import Options as IEOptions
from webdriver_manager.microsoft import IEDriverManager


@pytest.fixture
def arg(request):
    return request.getfixturevalue(request.param)


@pytest.fixture()
# TODO: Fix this, would be nice to have a lightest weight driver
def setup_html_unit():
    driver = webdriver.Remote(
        desired_capabilities=webdriver.DesiredCapabilities.HTMLUNIT
    )

    yield driver

    driver.close()


@pytest.fixture()
def setup_chrome():
    options = ChromeOptions()
    options_arr = [
        "--headless",
        "--disable-gpu",
        "--window-size=1920,1200",
        "--ignore-certificate-errors",
        "--disable-extensions",
        "--no-sandbox",
        "--disable-dev-shm-usage",
    ]
    for option in options_arr:
        options.add_argument(option)

    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()), options=options
    )

    yield driver

    driver.close()


@pytest.fixture()
def setup_chromium():
    options = ChromeOptions()
    options_arr = [
        "--headless",
        "--disable-gpu",
        "--window-size=1920,1200",
        "--ignore-certificate-errors",
        "--disable-extensions",
        "--no-sandbox",
        "--disable-dev-shm-usage",
    ]
    for option in options_arr:
        options.add_argument(option)

    driver = webdriver.Chrome(
        service=ChromeService(
            ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()
        ),
        options=options,
    )

    yield driver

    driver.close()


@pytest.fixture()
def setup_brave():
    options = ChromeOptions()
    options_arr = [
        "--headless",
        "--disable-gpu",
        "--window-size=1920,1200",
        "--ignore-certificate-errors",
        "--disable-extensions",
        "--no-sandbox",
        "--disable-dev-shm-usage",
    ]
    for option in options_arr:
        options.add_argument(option)

    driver = webdriver.Chrome(
        service=ChromeService(
            ChromeDriverManager(chrome_type=ChromeType.BRAVE).install()
        ),
        options=options,
    )

    yield driver

    driver.close()


@pytest.fixture()
def setup_edge():
    options = EdgeOptions()
    options_arr = [
        "--headless",
        "--disable-gpu",
        "--window-size=1920,1200",
        "--ignore-certificate-errors",
        "--disable-extensions",
        "--no-sandbox",
        "--disable-dev-shm-usage",
    ]
    for option in options_arr:
        options.add_argument(option)

    driver = webdriver.Edge(
        service=EdgeService(EdgeChromiumDriverManager().install()), options=options
    )

    yield driver

    driver.close()


@pytest.fixture()
def setup_firefox():
    options = FirefoxOptions()
    options_arr = [
        "--headless",
        "--disable-gpu",
        "--window-size=1920,1200",
        "--ignore-certificate-errors",
        "--disable-extensions",
        "--no-sandbox",
        "--disable-dev-shm-usage",
    ]
    for option in options_arr:
        options.add_argument(option)

    driver = webdriver.Firefox(
        service=FirefoxService(GeckoDriverManager().install()), options=options
    )

    yield driver

    driver.close()


@pytest.fixture()
def setup_ie():
    options = IEOptions()
    options_arr = [
        "--headless",
        "--disable-gpu",
        "--window-size=1920,1200",
        "--ignore-certificate-errors",
        "--disable-extensions",
        "--no-sandbox",
        "--disable-dev-shm-usage",
    ]
    for option in options_arr:
        options.add_argument(option)

    driver = webdriver.Ie(
        service=IEService(IEDriverManager().install()), options=options
    )

    yield driver

    driver.close()
