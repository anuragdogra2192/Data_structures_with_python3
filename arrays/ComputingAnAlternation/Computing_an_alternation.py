"""
Computing an alternation

Write a program that takes an array A of n numbers, and 
rearranges A's elements to get a new array B having the
property that

B[0]<=B[1]>=B[2]<=B[3]>=B[4]<=B[5]>=...

For example
A = [1,2,3,4,5,6,7]
id   0 1 2 3 4 5 6
B = [1,3,2,5,4,7,6]
"""

def rearrange(A):
    for i in range(len(A)):
        A[i:i+2] = sorted(A[i:i+2], reverse=bool(i % 2))
    return A

print("Input the array to rearrange: ")
A = [int(x) for x in input().split()]
print("The rearranged array A: ", rearrange(A))

