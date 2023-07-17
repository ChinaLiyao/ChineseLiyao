import sys
class Student:
    def __init__(self, name, b:int):
        self.name = name
        self.b = b
        if type(self.b) == int or type(self.b) == float:
            pass
        else:
            print("成绩不可为字符串,请检查传入的参数")
            sys.exit()
    def get(self):
        if self.b > 90:
            print(f"{self.name}成绩优秀!")
        elif self.b > 80:
            print(f"{self.name}成绩良好!")
        elif self.b > 70:
            print(f"{self.name}成绩中等!")
        elif self.b > 60:
            print(f"{self.name}成绩及格!")
        else:
            print(f"{self.name}成绩太差，要补考!")
a = Student('a', 100)
a.get()
b = Student('b', 85)
b.get()
c = Student('c', 75)
c.get()
d = Student('d', 65)
d.get()
e = Student('e', 50)
e.get()
f = Student('f', '100')
f.get()