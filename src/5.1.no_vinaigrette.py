"""Choose a random date between two dates entered by the user."""

import datetime
import random

MONDAY = 0


def no_vinaigrette(start_date, end_date):
    """Return a random date between the given dates, including both endpoints."""
    if start_date > end_date:
        raise ValueError("Start date must not be after end date.")

    days_between = (end_date - start_date).days
    random_days = random.randint(0, days_between)

    return start_date + datetime.timedelta(days=random_days)


def main():
    """Read two dates, choose a random date, and display the result."""
    try:
        start_date = datetime.date.fromisoformat(
            input("Enter start date (YYYY-MM-DD): ")
        )
        end_date = datetime.date.fromisoformat(
            input("Enter end date (YYYY-MM-DD): ")
        )
        chosen_date = no_vinaigrette(start_date, end_date)
    except ValueError as error:
        print(f"Invalid input: {error}")
        return

    print(chosen_date)

    if chosen_date.weekday() == MONDAY:
        print("אין לי ויניגרט!")


if __name__ == "__main__":
    main()
