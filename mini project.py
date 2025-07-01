from datetime import date

def ageCalculator(birth_date):
    today = date.today()

    # Calculate initial age difference
    age_year = today.year - birth_date.year
    age_month = today.month - birth_date.month
    age_day = today.day - birth_date.day

    # Adjust for negative day difference
    if age_day < 0:
        age_month -= 1
        previous_month = today.month - 1 or 12
        previous_year = today.year if today.month != 1 else today.year - 1
        days_in_prev_month = (date(today.year, today.month, 1) - date(previous_year, previous_month, 1)).days
        age_day += days_in_prev_month

    # Adjust for negative month difference
    if age_month < 0:
        age_month += 12
        age_year -= 1

    print(f"\nYour age is: {age_year} years, {age_month} months, and {age_day} days.")

# Main code
try:
    birth_input = input("Enter your birth date in YYYY-MM-DD format: ")
    year, month, day = map(int, birth_input.split('-'))
    birth_date = date(year, month, day)

    if birth_date > date.today():
        print("Invalid birth date: Date is in the future.")
    else:
        print(f"Your birth date is: {birth_date}")
        ageCalculator(birth_date)
except ValueError:
    print("Invalid date format or values. Please enter the date as YYYY-MM-DD.")