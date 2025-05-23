import os
from datetime import datetime
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import allure
import json

@pytest.fixture(scope="session")
def browser(request):
    # Get the browser name from the command-line argument
    browser_name = request.config.getoption("--browser").lower()

    # Initialize browser options based on the selected browser
    if browser_name == "chrome":
        options = webdriver.ChromeOptions()
        options.add_argument('log-level=3')
        options.add_argument("--window-size=1920,1080")
        options.add_argument("--disable-extensions")
        options.add_argument("--start-maximized")
        options.add_argument('--disable-gpu')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--no-sandbox')
        options.add_argument("--disable-3d-apis")
        options.add_argument("--disable-webgl")
        options.add_argument("--use-gl=swiftshader")
        options.add_argument("disable-infobars")
        options.add_argument("--ignore-certificate-errors")
        options.add_argument("--disable-software-rasterizer")
        options.add_argument("--enable-unsafe-swiftshader")
        options.add_argument("--disable-devtools")
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
        driver.implicitly_wait(20)

    elif browser_name == "firefox":
        options = webdriver.FirefoxOptions()
        options.add_argument("--width=1920")
        options.add_argument("--height=1080")
        options.add_argument("--disable-extensions")
        options.add_argument("--start-maximized")
        options.add_argument("--disable-gpu")
        options.add_argument("--ignore-certificate-errors")
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=options)
        driver.implicitly_wait(20)

    else:
        raise ValueError(f"Unsupported browser: {browser_name}. Please choose 'chrome' or 'firefox'.")

    # Maximize window and return driver
    driver.maximize_window()
    yield driver
    driver.quit()


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Browser to run tests: chrome or firefox")


@pytest.fixture(scope="function")
def patient_data():
    file_path = "data/patient_data.json"  # adjust the path if needed

    with open(file_path, "r") as f:
        data = json.load(f)

    unique_mrn = datetime.now().strftime("%Y%m%d%H%M%S")
    data[0]["MRN"] = unique_mrn

    with open(file_path, "w") as f:
        json.dump(data, f, indent=2)

    return data[0]

"""allure report"""
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # Execute all other hooks to get the test result
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        # Get the browser instance from the fixture
        driver = item.funcargs.get('browser', None)
        if driver:
            screenshot_dir = "screenshots"
            if not os.path.exists(screenshot_dir):
                os.makedirs(screenshot_dir)
            screenshot_path = os.path.join(
                screenshot_dir,
                f"{item.name}_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.png"
            )
            driver.save_screenshot(screenshot_path)

            # Attach the screenshot to the Allure report
            allure.attach.file(
                screenshot_path,
                name=f"Screenshot_{item.name}",
                attachment_type=allure.attachment_type.PNG
            )
