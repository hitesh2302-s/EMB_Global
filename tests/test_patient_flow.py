import pytest
from config.config import CONFIG
from conftest import browser
from pages.add_patient_page import AddPatientPage
from pages.dashboard_page import DashboardPage
from pages.login_page import LoginPage
from utils.data_utils import load_patient_data

expected_headers = [
    "First Name",
    "Last Name",
    "Date of Birth",
    "Discharge Date & Time",
    "Phone Number",
    "Date Added",
    "Language",
    "Timezone"
]


def test_invalidLogin(browser):
    base_url = CONFIG["base_url"]
    creds = CONFIG["invalidCredentials"]
    login_page = LoginPage(browser)
    login_page.load(base_url)
    login_page.login(creds["username"], creds["password"])
    login_page.alert_invalidCred()


def test_login(browser):
    creds = CONFIG["credentials"]
    login_page = LoginPage(browser)
    dashboard_page = DashboardPage(browser)
    browser.refresh()
    login_page.login(creds["username"], creds["password"])
    assert dashboard_page.is_loaded(), "Login failed or dashboard not loaded"


@pytest.mark.parametrize("patient", load_patient_data())
def test_add_and_verify_patient(browser, patient):
    add_patient_page = AddPatientPage(browser)
    dashboard_page = DashboardPage(browser)

    """Navigate to add patient screen and fill the form"""
    add_patient_page.add_Patient()
    add_patient_page.fill_form(patient)
    add_patient_page.submit()

    """Get the generated unique MRN"""
    unique_mrn = add_patient_page.unique_mrn

    """Verify validation errors"""
    errors = add_patient_page.get_errors()
    assert not errors, f"Validation errors: {errors}"

    """Verify patient is present in dashboard"""
    patient_list = dashboard_page.get_patient_list()
    print(patient_list)
    found = any(unique_mrn in row for row in patient_list)
    assert found, f"Patient with MRN {unique_mrn} not found in dashboard"


def test_logout(browser):
    dashboard_page = DashboardPage(browser)
    assert dashboard_page.logout() == "Login", "Logout failed"
