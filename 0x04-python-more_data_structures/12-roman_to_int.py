#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is not None or type(roman_string) == str:
        roman_num = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000
            }
        num = 0
        num_arr = [roman_num[i] for i in roman_string] + [0]
        for i in range(len(num_arr) - 1):
            if num_arr[i] >= num_arr[i+1]:
                num += num_arr[i]
            else:
                num -= num_arr[i]
        return(num)
    else:
        return(0)
