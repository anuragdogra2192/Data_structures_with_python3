"""
if v1 = [1,2] and v2 = [3,4,5,6]
output v3 = [1,3,2,4,5,6]
"""
from typing import List
from collections import deque
class ZigZagIterator:
    def __init__(self, v1: List[int], v2: List[int]):
        self.v1 = v1
        self.v2 = v2
        self.q = deque({})
        if v1:
            pair = {0:0}
            self.q.append(pair)
        if v2:
            pair = {1:0}
            self.q.append(pair)
        #print("A: ", self.q)
        #print("A: ", self.q[0])

    def next(self):
        temp = self.q[0]
        self.q.popleft()

        ret = 0
        #print(temp)

        k = list(temp.keys())[0]
        #print(k)
        if  k == 1:
            ret = self.v2[temp[1]]
            temp[1] += 1
            if(temp[1] < len(self.v2)):
                self.q.append(temp)
                #print("1: ", self.q)

        else:
            ret = self.v1[temp[0]]
            temp[0] += 1
            if(temp[0] < len(self.v1)):
                self.q.append(temp)
                #print("0:", self.q)

        return ret

    def hasNext(self):
        if self.q:
            return True
        else:
            return False


z = ZigZagIterator([1, 2],[3, 4, 5, 6])
print(z.next())
print(z.next())
print(z.hasNext())

print(z.next())
print(z.next())
print(z.next())
print(z.hasNext())

print(z.hasNext())
print(z.next())
print(z.hasNext())








