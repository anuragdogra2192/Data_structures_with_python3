"""
Permutate an array without additional storage
and without altering the permutation array
Given:
A =    [a,b,c,d,e]
perm = [4,3,2,0,1]
Rearranged A = [e, d, c, b, a] 
"""
def apply_permutation(A, perm):
    i = 0
    while(perm[i]!=0):
        A[i], A[perm[i]] = A[perm[i]], A[i]
        i = perm[i]
        print(A)
        #if perm[i] == 0:
            #exit
    print("Anurag")
    return A

print("Provide an array of characters to permutate: \n")
A = [x for x in input().split()]

print("Provide permutate sequence of samelength as the previous given array: \n")
perm = [int(x) for x in input().split()]
print(apply_permutation(A, perm))