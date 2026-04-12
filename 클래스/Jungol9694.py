class introduce():
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def hello(self):
        print(f"My name is {self.name}.")
        print(f"I am {self.age} years old.")

a, b = input().split()
introduce(a, b).hello()
