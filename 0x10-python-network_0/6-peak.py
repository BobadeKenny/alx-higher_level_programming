#!/usr/bin/python3
""" function find_peak """


def get_peak(arr, low, high, n):
    '''get peak'''
    mid = (low + high) // 2
    if ((mid == 0 or arr[mid - 1] <= arr[mid])
       and (mid == n - 1 or arr[mid + 1] <= arr[mid])):
        return arr[mid]
    elif (mid > 0 and arr[mid - 1] > arr[mid]):
        return (get_peak(arr, low, mid - 1, n))
    else:
        return (get_peak(arr, mid + 1, high, n))


def find_peak(list_of_integers):
    '''find peak integer'''
    if (list_of_integers):
        n = len(list_of_integers)
        return get_peak(list_of_integers, 0, n - 1, n)
    return None
