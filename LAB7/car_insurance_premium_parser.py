
import re
from datetime import datetime


def normalize_registration(plate):
    """
    Removes spaces and dashes from a registration number
    and converts it to uppercase.
    """
    if not isinstance(plate, str):
        return ""

    plate = plate.strip().upper()

    for ch in [" ", "-", "."]:
        plate = plate.replace(ch, "")

    return plate


def total_claim_amount(text):
    """
    Adds valid whole-number claim amounts separated by semicolons.
    Invalid and empty entries are ignored.
    """
    if not isinstance(text, str):
        return 0

    total = 0

    for amount in text.split(";"):
        amount = amount.strip()

        try:
            if amount and re.fullmatch(r"[0-9]+", amount):
                total += int(amount)
        except (ValueError, OverflowError):
            continue

    return total


def driver_age(dob, current_year=2026):
    """
    Calculates the driver's age from a DD/MM/YYYY date of birth.
    Returns None for invalid inputs.
    """
    if not isinstance(dob, str):
        return None

    if (
        isinstance(current_year, bool)
        or not isinstance(current_year, int)
        or not 1 <= current_year <= 9999
    ):
        return None

    if not re.fullmatch(r"\d{2}/\d{2}/\d{4}", dob):
        return None

    try:
        birth_date = datetime.strptime(dob, "%d/%m/%Y")

        if birth_date.year > current_year:
            return None

        return current_year - birth_date.year

    except (ValueError, TypeError, OverflowError):
        return None


def main():
    print("==== Running normalize_registration ====")
    value = input("Enter a registration number (e.g. ka 01 ab 1234): ")
    print("Normalized registration:", normalize_registration(value))

    print("\n==== Running total_claim_amount ====")
    value = input("Enter past claim amounts separated by ; (e.g. 12000;4500;800): ")
    print("Total claimed:", total_claim_amount(value))

    print("\n==== Running driver_age ====")
    value = input("Enter the driver's date of birth as DD/MM/YYYY (e.g. 14/08/1999): ")
    print("Driver age in 2026:", driver_age(value))


if __name__ == "__main__":
    main()
