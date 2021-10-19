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

import re
# Starts with The and ends with Spain
txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)
print(x)
#Start position and end position 
print(list(x.span()))

#Print a list of all matches:
txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)

txt = "The rain in Spain"
x = re.search("\s", txt)
print("The first white-space character is located in position:", x.start())

txt = "The rain in Spain"
x = re.split("\s", txt)
print(x)

#Replace every white-space character with the number 9:
txt = "The rain in Spain"
x = re.sub("\s", "9", txt)
print(x)

#Replace the first 2 occurrences:
txt = "The rain in Spain"
x = re.sub("\s", "9", txt, 2)
print(x)

#Do a search that will return a Match Object:
txt = "The rain in Spain"
x = re.search("ai", txt)
print(x) #this will print an object
print(x.span())
print(x.group())

#Print the position (start- and end-position) of the first match occurrence.
#The regular expression looks for any words that starts with an upper case "S"
txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.span())

#Print the string passed into the function:
txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.string)

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.group())

#reverse
txt = "Hello World"[::-1]
print(txt)
#reversve a List
L = [1,2,3,54,5]
print(L[::-1])
