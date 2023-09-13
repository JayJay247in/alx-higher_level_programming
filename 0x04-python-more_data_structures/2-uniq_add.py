#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniq = []
    sum = 0
    for n in my_list:
        if n not in uniq:
            uniq.append(n)
            sum += n
    return sum
