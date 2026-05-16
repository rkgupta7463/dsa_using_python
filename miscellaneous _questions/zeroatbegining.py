'''
in given list place the zero's value at begining.
'''

lst=[2,1,0,6,0,7,0,0,8]

pos=len(lst)-1

for i in range(len(lst)-1,-1,-1):
    if lst[i] !=0:
        lst[pos]=lst[i]
        pos-=1

print("list:- ",lst)        
while pos>=0:
    lst[pos]=0
    pos-=1
        
print(lst)



