'''
in given list place the zero's value at end.
'''

lst=[2,1,0,6,0,7,0,0,8]

pos=0

for i in range(len(lst)):
    if lst[i] !=0:
        lst[pos],lst[i]=lst[i],lst[pos]
        pos+=1
        
print(lst)



