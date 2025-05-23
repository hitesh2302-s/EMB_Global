# Patient Management Automation Framework

This project automates the testing of a Patient Management web application using **Selenium**, **Pytest**, and **Page Object Model (POM)**.

## Project Structure
├── config/
│ ├── config.py
├── pages/
│ ├── login_page.py
│ ├── dashboard_page.py
│ └── add_patient_page.py
├── tests/
│ └── test_patient_flow.py
├── utils/
│ ├── data_utils.py
│ ├── validator.py
│ └── random_util.py
  └── validator.py
├── data/
│ └── patients.json
└── README.md


---

## Features Covered

### 1. **Login Test(valid & invalid)**
- Loads the base URL from `config.py`
- Uses valid credentials to login
- Verifies successful dashboard load

### 2. **Add Patient**
- Reads patient data from `test_data/patients.json`
- Generates a **unique MRN** at runtime
- Validates:
  - Phone number (must be 8–12 digits)
  - Date of Birth (should not be in the future)
- Handles:
  - `datetime-local` inputs (Discharge Date & Time)
  - Dropdown selection for Language and Timezone
- Submits the form
- Checks for validation errors on form

### 3. **Dashboard Verification**
- Verifies table headers (including auto-added `Date Added`)
- Confirms that the newly added patient's **unique MRN** is present in the patient list rows

---

## 🔍 Sample JSON Format (`patients.json`)

```json
[
  {
    "MRN": "1003",
    "First Name": "Alex",
    "Last Name": "Joe",
    "Date of Birth": "22-05-2025",
    "Discharge Date & Time": "2025-05-22T11:34",
    "Phone Number": "+14155552671",
    "Language": "English",
    "Timezone": "EST"
  }
]

