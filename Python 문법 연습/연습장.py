a=[1,2,3]
start = 1 if a else 0
print(start)
b = []
print(a[-1])
c = [1]
print(c[-1])

a = [[2],[3]]
result = []
for C in a:
    result.append([1]+C)

print(result) 

memo = {1:20, 2:30, 3:40}

if 3 in memo: # 
    print(True)
else:
    print(False)

print(list(range(4)))

key = str((1,2))
print(key)

a = [1,2,3,4,5]
a[0], a[1] = a[1], a[0]
print("a는 :", a)