from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class AddPatientPage:
    MRN = (By.ID, "mrn")
    FIRST_NAME = (By.ID, "firstName")
    LAST_NAME = (By.ID, "lastName")
    DOB = (By.ID, "dob")
    DISCHARGE = (By.ID, "dischargeDateTime")
    PHONE = (By.ID, "phone")
    LANGUAGE = (By.ID, "language")
    TIMEZONE = (By.ID, "timezone")
    SUBMIT = (By.ID, "submitBtn")
    ERROR_MSG = (By.CLASS_NAME, "error")

    def __init__(self, driver):
        self.driver = driver

    def fill_form(self, patient):
        self.driver.find_element(*self.MRN).send_keys(patient["MRN"])
        self.driver.find_element(*self.FIRST_NAME).send_keys(patient["First Name"])
        self.driver.find_element(*self.LAST_NAME).send_keys(patient["Last Name"])
        self.driver.find_element(*self.DOB).send_keys(patient["Date of Birth"])
        self.driver.find_element(*self.DISCHARGE).send_keys(patient["Discharge Date & Time"])
        self.driver.find_element(*self.PHONE).send_keys(patient["Phone Number"])
        Select(self.driver.find_element(*self.LANGUAGE)).select_by_visible_text(patient["Language"])
        Select(self.driver.find_element(*self.TIMEZONE)).select_by_visible_text(patient["Timezone"])

    def submit(self):
        self.driver.find_element(*self.SUBMIT).click()

    def get_errors(self):
        return [e.text for e in self.driver.find_elements(*self.ERROR_MSG)]
