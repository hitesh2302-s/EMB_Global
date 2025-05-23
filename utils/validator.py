from datetime import datetime


def is_valid_phone_number(phone: str) -> bool:
    digits_only = ''.join(filter(str.isdigit, phone))
    return 8 <= len(digits_only) <= 12


def is_valid_dob(dob_str: str) -> bool:
    try:
        dob = datetime.strptime(dob_str, "%d-%m-%Y")
        return dob <= datetime.today()
    except ValueError:
        return False