import pytest
from selenium import webdriver

from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.os_manager import ChromeType

from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.edge.options import Options as EdgeOptions
from webdriver_manager.microsoft import EdgeChromiumDriverManager


@pytest.fixture()
def setup(setup_chrome, setup_chromium, setup_brave, setup_edge):
    yield {
        "chrome": setup_chrome,
        "chromium": setup_chromium,
        "brave": setup_brave,
        "edge": setup_edge,
    }


@pytest.fixture
def arg(request):
    return request.getfuncargvalue(request.param)


@pytest.fixture()
def setup_chrome(request):
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
def setup_chromium(request):
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
def setup_brave(request):
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
def setup_edge(request):
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
