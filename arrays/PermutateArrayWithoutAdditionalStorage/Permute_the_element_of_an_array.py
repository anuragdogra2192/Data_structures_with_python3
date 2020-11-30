"""
Permutate an array without additional storage
Given:
A = [a,b,c,d]

Mapping
a - 0
b - 1
c - 2
d - 3

c - 0
a - 2

perm = [2,0,1,3]  == perm = [0,1,2,3] 
        0 1 2 3              b c a d
                             0 1 2 3

map  1  2  0  3      
A = [b, c, a, d]
     0  1  2  3

a b c d e     
4 3 2 0 1
d e c b a

Dry run:
While: A -> ['e', 'b', 'c', 'd', 'a']
While: A -> ['b', 'e', 'c', 'd', 'a']
While: A -> ['d', 'e', 'c', 'b', 'a']
for loop: A -> ['d', 'e', 'c', 'b', 'a']  iteration i ->  0
for loop: A -> ['d', 'e', 'c', 'b', 'a']  iteration i ->  1
for loop: A -> ['d', 'e', 'c', 'b', 'a']  iteration i ->  2
for loop: A -> ['d', 'e', 'c', 'b', 'a']  iteration i ->  3
for loop: A -> ['d', 'e', 'c', 'b', 'a']  iteration i ->  4
perm: [0, 1, 2, 3, 4]
['d', 'e', 'c', 'b', 'a']

"""
def apply_permutation(A, perm):
    for i in range(len(A)):
        while perm[i] != i: 
            A[perm[i]], A[i] = A[i], A[perm[i]]                                                          
            perm[perm[i]], perm[i] = perm[i], perm[perm[i]]
            print ("While: A -> ", A)
        print("for loop: A -> ", A, " iteration i -> ", i)                        
    print("perm:",perm)
    return A

print("Provide an array of characters to permutate: \n")
A = [x for x in input().split()]

print("Provide permutate sequence of samelength as the previous given array: \n")
perm = [int(x) for x in input().split()]

print(apply_permutation(A, perm))