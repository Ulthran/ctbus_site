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


# TODO: Fix this, would be nice to have a lightest weight driver
@pytest.fixture()
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
def setup_chrome_mobile():
    options = ChromeOptions()
    options_arr = [
        "--headless",
        "--disable-gpu",
        "--window-size=1080,1920",
        "--ignore-certificate-errors",
        "--disable-extensions",
        "--no-sandbox",
        "--disable-dev-shm-usage",
        "--user-agent=Mozilla/5.0 (Linux; Android 11; Pixel 4 XL) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Mobile Safari/537.36",
    ]
    for option in options_arr:
        options.add_argument(option)

    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()), options=options
    )

    yield driver

    driver.close()


# TODO: The version of ChromeDriver needs to be held consistent with chromium-browser (currently installed via apt in CI workflow)
# Try just uncommenting and it might work again once the apt repo is up to date with the latest version of chromium-browser
# Maybe try to get the current version of chromium-browser in the CI workflow and install the corresponding version of ChromeDriver
# It should be installed by this point, so if we could interact with apt to get the version...
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


# TODO: Get Brave working
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


# TODO: Setup Windows runner in GHA to test IE (same with macOS for Safari)
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
