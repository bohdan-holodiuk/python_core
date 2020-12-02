"""
Задано чотирицифрове натуральне число.
- Знайти добуток цифр цього числа.
- Записати число в реверсному порядку.
- Посортувати цифри, що входять в дане число
"""

def number_digits_sum(value:str):
    # Check if input value meet the condition.
    if value.isdigit() and len(value) == 4:
        print(f'Input number = {value}')

        # Split @value string as list and convert every element to int.
        values_list = [int(digit) for digit in list(value)]

        # Calculate sum of value digits.
        value_sum = sum(values_list)

        # Get revers order.
        value_backorder = value[::-1]

        # Sorting list in direct order
        values_list.sort()

        print(f'Digits sum = {value_sum}')
        print(f'Revers order = {value_backorder}')
        print(f'Sorted digits = {str(values_list)}')
    else:
        print(f'Input value [{value}] does not meet the condition')

if __name__ == '__main__':
    input_value = input('Enter number: ')
    number_digits_sum(value=input_value)