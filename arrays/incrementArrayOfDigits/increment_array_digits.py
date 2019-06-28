#!usr/bin/python3

def increment_by_one(L):
	L[-1] += 1; #increment the last(unit) digit by 1
	for i in reversed(range(1, len(L))):
		if L[i]!=10:
			break
		L[i] = 0
		L[i-1] += 1

	if L[0] == 10:
		L[0] = 1
		L.append(0)

	return L


print("Enter the array or Lists of digits: \n")

given_list = [int(x) for x in input().split()]

print("The given array: ",given_list)
L = increment_by_one(given_list)

print("\n Incremented array: ", L)
