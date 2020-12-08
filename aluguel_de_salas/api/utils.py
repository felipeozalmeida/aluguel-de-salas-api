import re

def validate_cpf(cpf: str) -> bool:
    """
    Function for brazilian CPF validation.
    """

    # Checks CPF formatting
    if not re.search(r'^\d{11}$', cpf):
        return False

    # Get CPF numbers only
    numbers = [int(digit) for digit in cpf]

    # Check if CPF numbers are equal:
    if len(set(numbers)) == 1:
        return False

    # Validates first digit:
    sum_of_products = sum(a*b for a, b in zip(numbers[0:9], range(10, 1, -1)))
    expected_digit = (sum_of_products * 10 % 11) % 10
    if numbers[9] != expected_digit:
        return False

    # Validates second digit:
    sum_of_products = sum(a*b for a, b in zip(numbers[0:10], range(11, 1, -1)))
    expected_digit = (sum_of_products * 10 % 11) % 10
    if numbers[10] != expected_digit:
        return False

    return True
