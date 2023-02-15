import collections
from typing import List
class MinStack:

    ElementWithCachedMin = collections.namedtuple('ElementWithCachedMin', ('element', 'min'))
    def __init__(self):
        self._elements: List[MinStack.ElementWithCachedMin] = []
    def push(self, val: int) -> None:
        if not self._elements:
            self._elements.append(self.ElementWithCachedMin(val,val))
        else:
            self._elements.append(self.ElementWithCachedMin(val,min(val, self.getMin())))

    def pop(self) -> None:
        return self._elements.pop().element

    def top(self) -> int:
        return self._elements[-1].element

    def getMin(self) -> int:
        return self._elements[-1].min

"""
Each methods has Time Complexity O(1) and Space Complexity is O(n)
"""
# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()