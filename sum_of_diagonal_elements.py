### 1st way of solving this problem, for left to right diagonal elements  
def diagonal_sum(matrix):
    # TODO
    s=0
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if i == j:
                s+=matrix[i][j]
    return s

### 2nd way of solving this problem, for left to right diagonal elements 
def diagonal_sum(matrix):
    # TODO
    s=0
    for i in range(len(matrix)):    
        s+=matrix[i][i]
    return s

### 1st way of solving this problem, for right to left diagonal elements 
def diagonal_sum(matrix):
    # TODO
    s=0
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if i + j == 2:
                s+=matrix[i][j]
    return s
