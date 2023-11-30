#!/usr/bin/python3
""" Finds a peak in a list of unsorted integers """


def find_peak(list_of_integers):

    if bool(list_of_integers) is False:
        return None
    list_of_integers.sort()
    return list_of_integers[-1]
