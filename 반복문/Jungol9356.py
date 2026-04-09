lst = [1, 2, 3, 4, 5]
print(f"last: {len(lst)}")
del lst[4]
print(lst)
print(f"len: {len(lst)}")

print(f"second: {lst[1]}")
del lst[1]
print(lst)
print(f"len: {len(lst)}")