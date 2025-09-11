import array as arr

def find_number(arr,n):
    for i in range(len(arr)):
        if arr[i] == n:
            return f"Number present at {i} index"

print(find_number(arr.array('i',[1,2,4,5,7,8,9,12]),4) )
