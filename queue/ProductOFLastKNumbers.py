"""
1352. Product of the Last K Numbers
https://www.youtube.com/watch?v=mzxkyeA7fbE&ab_channel=CrackingFAANG

Design an algorithm that accepts a stream of integers and retrieves the product of the last k integers of the stream.

Implement the ProductOfNumbers class:

ProductOfNumbers() Initializes the object with an empty stream.
void add(int num) Appends the integer num to the stream.
int getProduct(int k) Returns the product of the 
last k numbers in the current list. 
You can assume that always the current list has at least k numbers.
The test cases are generated so that, 
at any time, the product of any contiguous sequence of numbers
will fit into a single 32-bit integer without overflowing.
"""
"""
As you correctly noticed, the CPython implementation of list.clear is O(n). The code iterates over the elements in order to decrease the reference count of each one, without a way to avoid it. There is no doubt that it is an O(n) operation and, given a large enough list, you can measure the time spent in clear() as function of list size:
"""
class ProductOfNumbers:

    def __init__(self):
        self.products = [] 
        self.product = 1

    def add(self, num: int) -> None:
        if num:
            self.product*=num
            self.products.append(self.product)
        else:
            self.products=[]
            self.product = 1

    def getProduct(self, k: int) -> int:
        if len(self.products)<k:
            return 0
        elif k==len(self.products):
            return self.product #or self.products[-1]
        else:
            return int(self.products[-1] / self.products[-1-k])

# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)