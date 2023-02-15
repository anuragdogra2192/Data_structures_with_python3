#Implement a stack with Max API.
"""
Design a stack that includes a max operation, in addition to push and pop. 
The max method should return the maximum value stored in the stack. Use the additional space to track the maximum.
"""
import collections
from typing import List

class Stack:
    ElementWithCachedMax = collections.namedtuple('ElementWithCachedMax', ('element', 'max'))
    
    def __init__(self) -> None:
        self._element_with_cached_max: List[Stack.ElementWithCachedMax] = []
    
    def empty(self) -> int:
        return len(self._element_with_cached_max) == 0
    
    def max(self) -> int:
        return self._element_with_cached_max[-1].max
    
    def pop(self) -> int:
        return self._element_with_cached_max.pop().element
    
    def push(self, x: int) -> None:
        if self.empty():
            self._element_with_cached_max.append(self.ElementWithCachedMax(x, x))
        else:
            self._element_with_cached_max.append(self.ElementWithCachedMax(x, max(x, self.max())))


"""
Each methods has Time Complexity O(1) and Space Complexity is O(n)
"""

if __name__ == '__main__':
    S = Stack()
    S.push(1)
    S.push(2)
    S.push(3)
    S.push(4)
    S.push(5)
    S.push(1)
    S.push(1)
#
    print("Max is: ", S.max())
#
    S.pop()
    S.pop()
    S.pop()
#
    print("Max is: ", S.max())

    Point = collections.namedtuple('Point', ['x','y'])
    Line:List[Point] = []
    p = Point(11, y=22)
    Line.append(p)
    Line.append(Point(x=38, y=22))
    Line.append(Point(x=29, y=33))

    print(Line)

    S1 = "Anurag"
    S2 = "Shaleen"

    print(min(S1, S2))
    print(max(S1, S2))

    A = [10,3,1,4,5]
    s = lambda y , x : x - y
#             y=5        x=4
    print(s(A.pop(), A.pop()))
#           y=1        x=3 
    print(s(A.pop(), A.pop()))
