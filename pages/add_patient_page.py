import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from utils.validator import is_valid_phone_number, is_valid_dob
from utils.random_util import generate_unique_mrn


class AddPatientPage:
    MRN = (By.XPATH, "//input[@id='mrn']")
    FIRST_NAME = (By.XPATH, "//input[@id='firstName']")
    LAST_NAME = (By.XPATH, "//input[@id='lastName']")
    DOB = (By.XPATH, "//input[@id='dob']")
    DISCHARGE = (By.XPATH, "//input[@id='discharge']")
    PHONE = (By.XPATH, "//input[@id='phone']")
    LANGUAGE = (By.XPATH, "//select[@id='language']")
    TIMEZONE = (By.XPATH, "//select[@id='timezone']")
    SUBMIT = (By.XPATH, "//select[@id='timezone']/following::button[@type='submit'][1]")
    ERROR_MSG = (By.CLASS_NAME, "error")
    ADD_PATIENT_BUTTON = (By.XPATH, "//button[@id='add-patient-btn']")

    def __init__(self, browser):
        self.browser = browser

    def add_Patient(self):
        self.browser.find_element(*self.ADD_PATIENT_BUTTON).click()

    def fill_form(self, patient):
        self.unique_mrn = generate_unique_mrn()
        if not is_valid_phone_number(patient["Phone Number"]):
            raise ValueError(f"Invalid phone number: {patient['Phone Number']}")
        self.browser.find_element(*self.MRN).send_keys(self.unique_mrn)
        self.browser.find_element(*self.FIRST_NAME).send_keys(patient["First Name"][:125])
        self.browser.find_element(*self.LAST_NAME).send_keys(patient["Last Name"])
        if not is_valid_dob(patient["Date of Birth"]):
            raise ValueError(f"Invalid Date of Birth: {patient['Date of Birth']}")
        self.browser.find_element(*self.DOB).send_keys(patient["Date of Birth"])
        self.browser.find_element(*self.DISCHARGE).send_keys(patient["Discharge Date & Time"])
        self.browser.find_element(*self.PHONE).send_keys(patient["Phone Number"])
        Select(self.browser.find_element(*self.LANGUAGE)).select_by_visible_text(patient["Language"])
        Select(self.browser.find_element(*self.TIMEZONE)).select_by_visible_text(patient["Timezone"])

    def submit(self):
        self.browser.find_element(*self.SUBMIT).click()
        time.sleep(3)

    def get_errors(self):
        return [e.text for e in self.browser.find_elements(*self.ERROR_MSG)]
