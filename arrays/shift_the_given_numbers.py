#Shift the given number of values to the end of an array
#def shift_values(L, shifts):
#    for i  in range(0, len(L)-shifts):
#        temp = i + shifts
    #     L[temp], L[i] = L[i], L[temp]
    #     L[temp], L[temp - 1] = L[temp - 1], L[temp]

    # L[len(L)-shifts], L[len(L) - shifts+1] = L[len(L)-shifts + 1], L[len(L) - shifts]

    # print("Array after the shift: ", L)

def shift_values(A, shifts):
    i = shifts
    j = 0
    while i < len(A) and j < shifts:
        print("i: ",i)
        print("j: ",j)
        if i < (len(A) - shifts):
            A[i], A[j] = A[j], A[i]
            A[len(A)-shifts + j], A[i] = A[i], A[len(A)-shifts + j]
            A[i + shifts], A[i] = A[i], A[i + shifts]
        print("Swap1 A: ",A)
        if i >= (len(A)-shifts):
            A[len(A)-shifts + j], A[j] = A[j], A[len(A)-shifts + j]
            A[i-j], A[j] = A[j], A[i-j]
            print("Swap1 B: ",A)
        i +=1
        j +=1
    print("Array after the shift: ", A)
    
print("Provide the array of integers and the shifting value: \n")
A = [int(x) for x in input().split()]

print("Input the shifting value: ")
shifts = int(input())

shift_values(A, shifts)
