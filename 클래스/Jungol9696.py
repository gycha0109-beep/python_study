class info:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def rated(self):
        if self.age >= 18:
            return "adult"
        else:
            return "child"

    def __str__(self):
        return f"{self.name}({self.age}) : {self.rated()}"

for _ in range(2):
    a, b = input().split()
    p = info(a, int(b))
    print(p)
