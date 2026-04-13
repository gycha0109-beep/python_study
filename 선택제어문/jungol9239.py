A, B, C = map(int, input().split())
minone = (A if A<B else B)
mintwo = (B if B<C else C)
print(minone if minone<mintwo else mintwo)