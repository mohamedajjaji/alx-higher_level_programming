#!/usr/bin/python3
def convert_roman(list_num):
    to_roman = 0
    max_list = max(list_num)

    for i in list_num:
        if max_list > i:
            to_roman += i

    return (max_list - to_roman)


def roman_to_int(roman_string):
    if not roman_string:
        return 0

    if not isinstance(roman_string, str):
        return 0

    roman_num = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    list_keys = list(roman_num.keys())

    num = 0
    last_roman = 0
    list_num = [0]

    for i in roman_string:
        for j in list_keys:
            if j == i:
                if roman_num.get(i) <= last_roman:
                    num += convert_roman(list_num)
                    list_num = [roman_num.get(i)]
                else:
                    list_num.append(roman_num.get(i))

                last_roman = roman_num.get(i)

    num += convert_roman(list_num)

    return (num)
