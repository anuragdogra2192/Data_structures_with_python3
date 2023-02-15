import numpy as np

labels = [1,2,0,5,6,0,23,14]

#print(labels)

x = np.array([[1, 1, 0], [0, 0, 0], [0, 0, 0]])
#print(np.nonzero(x))

print(x.shape)
my_array = np.array(labels)
print(x[:,0])
print(x[:,1])

#print(my_array.astype('float32'))
#print(np.nonzero(my_array))

#print(my_array.shape)

#print(np.where(my_array > 10)[0])
l = []
l2 = []

for i in range(10):
    #print(i, "  index:  ", np.where(my_array == i)[0], '\n')
    #print(type(np.where(my_array == i)[0]))
    l.append((np.where(my_array == i)[0]))
    #print(type(l))
    l2.append(len(l[i]))
    #print(l2)
#print(l)
#print(min(l2))
digit = [np.where(my_array == i)[0] for i in range(10)]
#print(type(digit))
#print(digit)
#print(digit[0][0])
#print(digit[0][1])

a = np.arange(10)
#print(a)
L = np.asarray(a==0)
#print(np.asarray(a==0))
#print(L)
#print(np.nonzero(L)) # == L.nonzero()
#
#print(np.asarray(a==0).nonzero())
#print(np.where(a < 5))

# Nested List------------------------------
n_list = ["Happy", [2, 0, 2, 0]]

# Nested indexing
#print(n_list[0][4])

#print(n_list[1][2])
#------------------------------------------

pairs = []
pairs += [[11,21]]
pairs += [[31,41]]

print(pairs[0][0])
print(pairs[0][1])
print(pairs[1][0])
print(pairs[1][1])

print(type(pairs)) 
print(len(pairs))