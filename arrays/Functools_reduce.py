myList = [10, 25, 17, 9, 30, -5]
# Double the value of each element
myList2 = map(lambda n : n*2, myList)
print(list(myList2))

square = lambda n : n*n
num = square(5)
print(num)

sub = lambda x, y : x-y
print(sub(5, 3))

L1 = [10, 25, 17, 9, 30, -5]
# Filters the elements which are not multiples of 5
L2 = filter(lambda n : n%5 == 0, L1)
print(list(L2))


import functools
# reduce
#At first step, first two elements of sequence are picked and the result is obtained.
#Next step is to apply the same function to the previously attained result 
#and the number just succeeding the second element 
#and the result is again stored.
#This process continues till no more elements are left in the container.
#The final returned result is returned and printed on console.

lis = [1, 3, 5, 6, 2, ] 
# using reduce to compute sum of list
print("The sum of the list elements is : ", end="")
print(functools.reduce(lambda a, b: a+b, lis))
 
# using reduce to compute maximum element from list
print("The maximum element of the list is : ", end="")
print(functools.reduce(lambda a, b: a if a > b else b, lis))