import pytest
from config.config import CONFIG
from conftest import browser
from pages.add_patient_page import AddPatientPage
from pages.dashboard_page import DashboardPage
from pages.login_page import LoginPage
from utils.data_utils import load_patient_data

add_patient_page = AddPatientPage(browser)


def test_login(browser):
    base_url = CONFIG["base_url"]
    creds = CONFIG["credentials"]
    login_page = LoginPage(browser)
    dashboard_page = DashboardPage(browser)

    login_page.load(base_url)
    login_page.login(creds["username"], creds["password"])
    assert dashboard_page.is_loaded(), "Login failed or dashboard not loaded"

#
# @pytest.mark.parametrize("patient", load_patient_data())
# def test_add_patient(browser, patient):
#     add_patient_page.fill_form(patient)
#     add_patient_page.submit()
#
#     # Check for errors
#     errors = add_patient_page.get_errors()
#     assert not errors, f"Validation errors: {errors}"
#
#     # Verify in Dashboard
#     patient_list = dashboard_page.get_patient_list()
#     found = any(patient["MRN"] in row for row in patient_list)
#     assert found, f"Patient with MRN {patient['MRN']} not found in dashboard"
#
#
# def test_logout(browser):
#     dashboard_page.logout()
#     assert "login" in browser.current_url.lower(), "Logout failed"
