from datetime import datetime


def get_days_from_today() -> int:  # get difference between the current and entered date
    try:
        now = datetime.now()  # get current date
        user_input = input("Please enter the date in the following format: YYYY-MM-DD\n")
        date = datetime.strptime(user_input, "%Y-%m-%d")
        difference = now - date  # subtract user date from current date
        print(f"Difference between the entered date and today is {difference.days} days.")
        return difference.days  # return difference in days
    except ValueError or TypeError:  # if ValueError or TypeError is met, print the instruction below
        print(f"Make sure the date is entered in the following format: YYYY-MM-DD and try again.")


if __name__ == '__main__':
    get_days_from_today()
