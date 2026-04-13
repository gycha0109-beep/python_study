class Player:
    def __init__(self, name, AB, H):
        self.name = name
        self.AB = int(AB)
        self.H = int(H)
    
    def get_avg(self):
        # 타율 = 안타(H) / 타수(AB)
        # 소수점 셋째 자리까지 고정 출력 (.3f 포맷 사용)
        return f"{self.H / self.AB:.3f}"
    
    def display(self):
        print(f"name:{self.name}, AVG:{self.get_avg()}, AB:{self.AB}, H:{self.H}")

for _ in range(2):
    name, ab, h = input().split()
    player = Player(name, ab, h)
    player.display()