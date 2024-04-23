import re


# the function removes all symbols from the provided phone number except digits 
# and adds a Ukrainian country code or a plus sign if missing
def normalize_phone(phone_number: str) -> str:
    pattern = r"[\D]"
    phone_number = ''.join(re.split(pattern, phone_number))
    if phone_number.startswith('380') and len(phone_number) == 12:
        phone_number = "+" + phone_number
    elif phone_number.startswith('0') and len(phone_number) == 10:
        phone_number = "+38" + phone_number
    return phone_number


if __name__ == '__main__':
    normalize_phone()
    