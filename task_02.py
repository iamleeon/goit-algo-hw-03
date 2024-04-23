import random


def get_numbers_ticket(min: int, max: int, quantity: int) -> list:
    # the function generates a sorted list of unique integers where
    # the range (min and max values) and quantity are provided by a user.
    # Requirements: min >= 1 and max <= 1000 and quantity in range(1, 1000). All should be integers.
    unique_numbers_list = []
    try:
        if min >= 1 and max <= 1000 and quantity in range(1, 1000):  # verify requirements
            # main function logic, creating a sorted list with unique values
            unique_numbers_list = sorted(random.sample(range(min, max), int(quantity)))
            return unique_numbers_list
        else:  # provide instructions if requirements are not met
            print("Requirements are not met: min value >=1, max value <= 1000, quantity is in range between min and max values. All should be integers.")
            return unique_numbers_list

    except (TypeError, ValueError):
        # making sure the max number is bigger than the min one 
        # and the quantity can fit the difference between them
        print("Exception caught. Requirements: min value >=1, max value <= 1000, quantity is in range "
              "between min and max values. All should be integers.")
        return unique_numbers_list


if __name__ == '__main__':
    get_numbers_ticket()
