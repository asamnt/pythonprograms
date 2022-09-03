def equilibrium(arr):
    print('this calculates the equilibrium point')

    leftsum = 0
    rightsum = 0

    n = len(arr)
    print(n)

    for i in range(n):
        leftsum=0
        rightsum=0

        for j in range(i):
            leftsum += arr[j]
        for j in range(i+1, n):
            rightsum += arr[j]
        
        if leftsum==rightsum:
            return i
    
    return -1

def equilibrium2(arr):
    total_sum = sum(arr)
    leftsum = 0
    


arr = [-7, 1, 5, 4, -2, 3, 0]
print(equilibrium(arr))