

def even_odd(A):
    next_even, next_odd = 0, len(A) -1
    while next_even < next_odd:
        if A[next_even] % 2 == 0:# that is next_even is even, the move to next index
            next_even += 1
            print(A)
        else:
            A[next_even], A[next_odd] = A[next_odd],A[next_even] 
            next_odd -= 1
        print(A)
    return A.sort()


print(even_odd([7,3,2,4,6]))
