import random


def get_numbers_ticket():
    # the function generates a sorted list of unique integers where
    # the range (min and max values) and quantity are provided by a user
    min_value = input(f"Please enter a minimum number: ")  # getting a minimum value
    while True:  # making sure min_value is an integer
        try:
            min_value = int(min_value)
            break
        except ValueError:
            print("Make sure you enter an integer!")
            min_value = input(f"Please enter a minimum number: ")

    max_value = input(f"Please enter a maximum number: ")  # getting a maximum value
    while True:  # making sure max_value is an integer
        try:
            max_value = int(max_value)
            break
        except ValueError:
            print("Make sure you enter an integer!")
            max_value = input(f"Please enter a maximum number: ")

    quantity = input(f"Please enter how many unique numbers you would like to get: ")  # getting a quantity
    while True:  # making sure quantity is an integer
        try:
            quantity = int(quantity)
            break
        except ValueError:
            print("Make sure you enter an integer!")
            quantity = input(f"Please enter quantity: ")

    try:
        # main function logic, creating a sorted list with unique values
        unique_number_list = sorted(random.sample(range(min_value, max_value), quantity))
        return unique_number_list
    except ValueError:
        # making sure the max number is bigger than the min one 
        # and the quantity can fit the difference between them
        print("Try again ang make sure the maximum number is larger than the minimum "
              "one and the quantity can fit in their difference.")


if __name__ == '__main__':
    print(get_numbers_ticket())
