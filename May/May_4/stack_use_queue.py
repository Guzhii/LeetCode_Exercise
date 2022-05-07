import queue

class MyStack:

    def __init__(self):
        self.q_1 = queue.Queue()
        self.q_2 = queue.Queue()
        self.fir = None

    def push(self, x: int) -> None:
        self.q_1.put(x)
        self.fir = x

    def pop(self) -> int:
        while self.q_1.qsize() > 1:
            self.fir = self.q_1.get()
            self.q_2.put(self.fir)
        
        tmp = self.q_1.get()
        self.q_1 = self.q_2
        self.q_2 = queue.Queue()
        return tmp

    def top(self) -> int:
        return self.fir

    def empty(self) -> bool:
        return self.q_1.empty()


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
