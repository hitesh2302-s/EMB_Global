from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    USERNAME_INPUT = (By.XPATH, "//input[@id='username']")
    PASSWORD_INPUT = (By.XPATH, "//input[@id='password']")
    LOGIN_BUTTON = (By.XPATH, "//button[@type='submit' and contains(text(),'Login')]")

    def __init__(self, browser):
        self.browser = browser

    def load(self, url):
        self.browser.get(url)

    def login(self, username, password):
        self.browser.find_element(*self.USERNAME_INPUT).send_keys(username)
        self.browser.find_element(*self.PASSWORD_INPUT).send_keys(password)
        self.browser.find_element(*self.LOGIN_BUTTON).click()

    def alert_invalidCred(self):
        try:
            # Wait for the alert to appear (timeout of 5 seconds)
            WebDriverWait(self.browser, 5).until(EC.alert_is_present())
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            assert "Invalid login" in alert_text, f"Expected 'Invalid login' in alert, but got '{alert_text}'"
            # Accept the alert (click OK)
            alert.accept()
            print("Alert handled successfully.")
        except TimeoutException:
            print("No browser alert found. Attempting to handle as a custom modal...")