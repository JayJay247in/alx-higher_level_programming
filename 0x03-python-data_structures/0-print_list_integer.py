#!/usr/bin/python3
def print_list_integer(my_list=[]):
    """Print integers of a list one per line"""
    for item in my_list:
        print("{:d}".format(item))
