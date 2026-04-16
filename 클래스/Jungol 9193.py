class Profile:
    def __init__(self, name, year):
        self.name = name
        self.year = year
    def intro(self):
        return f"{self.name} was born in {self.year}"

name1, year1 = input().split()
name2, year2 = input().split()

older = Profile(name1, int(year1))
younger = Profile(name2, int(year2))
print(f'{older.name} was born in {older.year}')
print(f'{younger.name} was born in {younger.year}')
print(f'{older.name} is {younger.year-older.year} years older than {younger.name}')