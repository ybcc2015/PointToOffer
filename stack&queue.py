# 1.用两个栈实现一个队列
class MyQueue(object):
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    # 入队
    def append_tail(self, value):
        self.stack1.append(value)

    # 出队
    def delete_head(self):
        if len(self.stack2) == 0:
            if len(self.stack1) != 0:
                while len(self.stack1) != 0:
                    value = self.stack1.pop()
                    self.stack2.append(value)
            else:
                raise Exception("queue is empty")
        head = self.stack2.pop()
        return head

    def __len__(self):
        return len(self.stack1) + len(self.stack2)


# 两个队列实现一个栈
class MyStack(object):
    def __init__(self):
        self.que1 = MyQueue()
        self.que2 = MyQueue()

    # 入栈
    def push(self, value):
        self.que1.append_tail(value)

    # 出栈
    def pop(self):
        if len(self.que1) == 0:
            raise Exception("stack is empty")
        elif len(self.que1) == 1:
            value = self.que1.delete_head()
        else:
            while len(self.que1) != 1:
                self.que2.append_tail(self.que1.delete_head())
            value = self.que1.delete_head()
            while len(self.que2) != 0:
                self.que1.append_tail(self.que2.delete_head())
        return value


if __name__ == '__main__':
    stack = MyStack()
