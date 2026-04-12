class House:
    def __init__(self, location, bedroom, bathroom):
        self.location = location
        self.bedroom = bedroom
        self.bathroom = bathroom

    def __str__(self):
        return f"location: {self.location}\nbedrooms: {self.bedroom}\nbathrooms: {self.bathroom}"

a, b, c = input().split()
h = House(a, b, c)
print(h)
