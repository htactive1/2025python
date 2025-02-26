class Person:
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height

    def run(self):
        pass

    def eat(self):
        pass


p1 = Person("Alice", 20, 170)


class Dog:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def do(self, object):
        if object == "生人":
            print(f"狗狗看见{object}汪汪叫")
        elif object == "熟人":
            print(f"狗狗看见{object}摇尾巴")


dog1 = Dog("旺财", "白色")
dog1.do("生人")

if __name__ == '__main__':
    pass