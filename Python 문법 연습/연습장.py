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

for i in range(1,0,-1):
    print("메롱")

for i in range(0,2):
    print(i)

print(8//2)
nums = [1,2,3,4,5]
for i in range(len(nums)-1):
    print("는",i)

print(3//2)

a = [1,2,3,4,5,6]

a[0] = a[3] = a[5] = 12
print(a)

g = [[' ' for _ in range(3)] for _ in range(3)]
print(g)
print(g[0][:3])
print(g[0])
g[1] = ['*', ' ', '*']
g[0] = g[2] = ['*']*3
for i in range(3):
    print(g[i][:3])

print(g)

abc = [['1','2','3'],['4','5','6'],['7','8','9']]
print(abc[1])
print(abc[1][2] )
print(''.join(abc[1]))

a = [1,2,3,4,5,6]
for i in a:
    if i == 1 or i == 2 or i == 3:
        print(i)

a = []
a.append('L')
a.append('R')
print(a)

N = 17
a = 5

N /= a

print(N)

print(a)
print()
for i in range(0,2):
    print(i)