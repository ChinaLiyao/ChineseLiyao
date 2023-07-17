class Xiaoming:
    def __init__(self):
        self.kg = 102
    def eat(self):
        self.kg += 1
        print(f"小明吃饭,体重加1斤。当前小明重{self.kg}斤")
    def run(self):
        self.kg -= 0.5
        print(f"小明跑步,体重减少0.5斤。当前小明重{self.kg}斤")
xiaoming = Xiaoming()
for i in range(3):
    xiaoming.eat()
for i in range(6):
    xiaoming.run()