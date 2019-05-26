#!/usr/bin/python3
import random as rnd

def even_odd(given_array):
	"This rearrange the even elements of the given sequence first, later comes the odds"
	print("Given state of sequence: ",given_array)

	next_even = 0;
	next_odd = len(given_array) -1
	while next_even < next_odd:
		if given_array[next_even] % 2 == 0:
			next_even += 1
		else:
			given_array[next_even], given_array[next_odd] = given_array[next_odd], given_array[next_even]
			next_odd -= 1
	return given_array

n = int(input('Enter the size of array/list: \n'))

given_array = rnd.sample(range(0, 100), n)
print("Rarranged array/list with first evens and later odds: \n", even_odd(given_array))


