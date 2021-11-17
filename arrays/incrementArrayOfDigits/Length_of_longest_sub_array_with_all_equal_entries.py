#!/usr/bin/python3

"""
Write a program that takes an array of integers 
and finds the length of the longest subarray with
all of whose entries are equal
"""
A = [1,2,3,7,5,1,7,8,1,2,3,5,6,7,8,2,1,4,4,5,1,1,1]

def length_of_the_longest_subarray(A):
    A.sort()
    print("Sorted array", A)
    
    max_occurence_so_far = 1 
    current_occurence = 1

    for i in range(1, len(A)):
        if A[i-1] != A[i]:
            max_occurence_so_far = max(max_occurence_so_far, current_occurence)
            current_occurence = 1
        else:
            current_occurence += 1

    return max_occurence_so_far

print("Length of the longest subarray: ", length_of_the_longest_subarray(A))