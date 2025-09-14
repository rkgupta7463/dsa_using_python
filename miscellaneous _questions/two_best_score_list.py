'''
Best Score

Given a list, write a function to get first, second best scores from the list.

List may contain duplicates.

Example

    myList = [84,85,86,87,85,90,85,83,23,45,84,1,2,0]
    first_second(myList) # 90 87
'''

def first_second(my_list):
    # TODO
    m1,m2=0,0
    for i in my_list:
        if i >  m1:
            m2=m1
            m1=i
        elif i > m2 and i != m1:
            m2=i
    return m1,m2

myList = [84,85,86,87,85,90,85,83,23,45,84,1,2,0]
result=first_second(myList) # 90 87
print("Result:- ",result)