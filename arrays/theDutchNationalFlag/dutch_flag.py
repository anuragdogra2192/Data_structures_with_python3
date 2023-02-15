#!/usr/bin/python3

def dutch_flag_partition(L):
	pivot_element = 1 #randmly choosen
	# Value's index in comparision with pivot element  
	smaller = 0
	equal = 0
	larger = len(L) - 1	

	while equal <= larger:
		if L[equal] < pivot_element:
			L[smaller], L[equal] = L[equal], L[smaller]
			smaller += 1
			equal += 1
		elif L[equal] == pivot_element:
			equal += 1
		else:
			L[equal], L[larger] = L[larger], L[equal]
			larger -= 1
	return L

print("Enter the random Dutch Flag sequence, where RED:0, WHITE:1, BLUE:2 \n")
given_flag = [int(x) for x in input().split()]

print("The given flag sequence: ",given_flag)
L = dutch_flag_partition(given_flag)
print("\n The Dutch Flag: ", L)