#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    """Print ints of list in reverse order per line""" 
    if my_list:
        my_list.reverse()
        for item in my_list:
            print("{:d}".format(item))
