'''
Middle Function

Write a function called middle that takes a list and returns a new list that contains all but the first and last elements.

    myList = [1, 2, 3, 4]
    middle(myList)  # [2,3]
'''

## one way
def middle(lst):
    # TODO
    lst.pop(-1)
    return lst[1:]

## second way
def middle2(lst):
    return lst[1:-1]