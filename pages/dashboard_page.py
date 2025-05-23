from selenium.webdriver.common.by import By


class DashboardPage:
    TABLE_ROWS = (By.XPATH, "//tbody/tr")
    LOGOUT_BUTTON = (By.ID, "logoutBtn")
    LOGIN_TEXT = (By.XPATH,"//h2[normalize-space()='Login']")

    def __init__(self, browser):
        self.browser = browser

    def is_loaded(self):
        return "Provider Platform Mock" in self.browser.title

    def get_patient_list(self):
        rows = self.browser.find_elements(*self.TABLE_ROWS)
        return [row.text for row in rows]

    def logout(self):
        self.browser.find_element(*self.LOGOUT_BUTTON).click()
        return self.browser.find_element(*self.LOGIN_TEXT).text