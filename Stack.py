class Stack:
    def __init__(self, size):
        self.size = size
        self.stack = []
        if type(self.size) == int:
            pass
        else:
            print("数据类型出错,栈容量必须为整型")
    def add(self, a):
        if len(self.stack) == self.size:
            print("失败,栈满")
        else:
            self.stack.append(a)
            print(f"数据{a}入栈")
    def take(self):
        if len(self.stack) < 1:
            print("失败,空栈")
        else:
            self.s = self.stack.pop()
            print(f"数据{self.s}出栈")
        return self.s
z = Stack(2)
z.add(1234)
z.add(2234)
z.add(3234)
z.take()
z.add(3234)
z.take()
z.take()
z.take()