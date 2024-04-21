from datetime import datetime


def get_days_from_today(date: str) -> int:  # get difference between the current and entered date
    try:
        now = datetime.now()  # get current date
        date = datetime.strptime(date, "%Y-%m-%d")  # convert string into datetime
        difference = now - date  # subtract user date from current date
        return difference.days  # return difference in days
    except (ValueError, TypeError):  # if ValueError or TypeError is met, print the instruction below
        print(f"Make sure date in the 'date' argument is entered in the following format: YYYY-MM-DD and try again.")


if __name__ == '__main__':
    get_days_from_today()
