def fib_recursive(n):
    if n <= 1:
        return n
    return fib_recursive(n-1) + fib_recursive(n-2)

print([fib_recursive(i) for i in range(7)])


def flatten_list(lst):
    ls=[]
    for l in lst:
        if isinstance(l,list):
            ls.extend(flatten_list(l))
        else:
            ls.append(l)
    return ls


flatten_list([1,2,3,[2,4,[5,6]]])