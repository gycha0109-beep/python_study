a = True
b = True
c = False

# 1. not a
# a가 True이므로 not True는 False
print(not a) 

# 2. a and b
# True and True는 True
print(a and b) 

# 3. a or b
# True or True는 True
print(a or b) 

# 4. a and (b or c)
# b or c는 (True or False)이므로 True
# a and True는 (True and True)이므로 True
print(a and (b or c)) 

# 5. a or (b and c)
# b and c는 (True and False)이므로 False
# a or False는 (True or False)이므로 True
print(a or (b and c)) 

# 6. not a or (b and not c)
# not a는 False
# not c는 True
# b and True는 (True and True)이므로 True
# False or True는 True
print(not a or (b and not c))