class MyQueue:

    def __init__(self):
        self.enq = []
        self.deq = []
        
    def push(self, x: int) -> None:
        self.enq.append(x)

    def pop(self) -> int:
        if not self.deq:
            while self.enq:
                self.deq.append(self.enq.pop())
        return self.deq.pop()

    def peek(self) -> int:
        if not self.deq:
            return self.enq[0]
        else:
            return self.deq[-1]

    def empty(self) -> bool:
        if not self.enq and not self.deq:
            return True
        return False


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()