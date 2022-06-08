#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or type(roman_string) != str:
        return 0
    roman_num = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000
        }
    num_arr = [roman_num[j] for j in roman_string] + [0]
    num = 0
    for i in range(len(num_arr) - 1):
        if num_arr[i] >= num_arr[i+1]:
            num += num_arr[i]
        else:
            num -= num_arr[i]
    return num
