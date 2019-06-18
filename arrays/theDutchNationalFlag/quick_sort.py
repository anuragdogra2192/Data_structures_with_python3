#!/usr/bin/python3
import random as rnd

def partition_of_list(L, start, end):
	pivot_element = L[end]
	partition_index = start
	
	for i in range(start,end):
		if(L[i]<=pivot_element):
			L[i],L[partition_index] = L[partition_index],L[i]
			partition_index+=1
	
	L[partition_index],L[end] = L[end],L[partition_index]
	return partition_index

def quick_sort(L, start, end):
	if (start < end):
		partition_index = partition_of_list(L, start, end)
		quick_sort(L, start, partition_index-1)
		quick_sort(L, partition_index+1, end)

n = int(input('Enter the size of array/list: \n'))
given_list = rnd.sample(range(0, 100), n)

print("Unsorted List: ",given_list)

quick_sort(given_list, 0, len(given_list)-1)

print("Sorted List: ",given_list)