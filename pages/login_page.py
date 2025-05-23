from selenium.webdriver.common.by import By


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
