## one way
def middle(lst):
    # TODO
    lst.pop(-1)
    return lst[1:]

## second way
def middle2(lst):
    return lst[1:-1]