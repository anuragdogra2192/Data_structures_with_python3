class MyCircularQueue:
    def __init__(self, k: int):
        self.q = [0]*k    
        self.rear = -1
        self.front = -1
        self.capacity = k 

    def enQueue(self, value: int) -> bool:
        if self.isEmpty():
            self.front=self.rear=0
            self.q[self.rear]=value
            return True
        if self.isFull():
            return False
        self.rear = (self.rear+1)%self.capacity
        self.q[self.rear] = value
        return True
        

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        if(self.front == self.rear):
            self.rear = -1
            self.front = -1
            return True
        self.front = (self.front+1)%self.capacity
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.q[self.front]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.q[self.rear]
        

    def isEmpty(self) -> bool:
        if self.front == -1 and self.rear == -1:
            return True
        return False

    def isFull(self) -> bool:
        if (self.rear+1)%self.capacity == self.front:
            return True
        else:
            return False
    def display(self):
        i = self.Front()
        rear = self.Rear()
        
        if not self.isEmpty():
            print("Queue : ")
            while i<=rear+1:
                print(self.q[i])
                i = (i+1)%self.capacity

# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()

