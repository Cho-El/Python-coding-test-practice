#문자열 ""출력하기
print("\"성윤이\"는 밥을 먹었다.")
print('"성윤이"는 밥을 먹었다.')
print('"성윤이가 "밥을 안먹는다고""이야기 했다.')

#f string
a = 1
b = "공부하자"
c = "열심히"
d = "성윤아"
e = "EnGliSh"
dic = {'name':"csy"}
print(f"{d} {c} {b} {1} {e.upper()} {e.lower()}")
print(f"내 이름은 {dic['name']}")

#format 포맷팅
print("이름 : {}, 부사 : {}, 동사 : {}, 영어 : {}".format(d,c,b,e.upper()))

# % 포맷팅
print("이름 : %s, 숫자 : %d" % (d,a))

# while 문
a = 3
b = 5
while a and b:
    print(a,b)
    a-= 1
    b-= 1

# sep과 end 사용
print("1-1칸","1-2칸","1-3칸")
print("2-1칸","2-2칸","2-3칸")
print("1-1칸","1-2칸","1-3칸",end = "")
print("2-1칸","2-2칸","2-3칸",sep = "")
print("1-1칸","1-2칸","1-3칸",end = "**end 입니다** \n")
print("2-1칸","2-2칸","2-3칸",sep = "**sep입니다**")

# 리스트를 문자열로 합치기
# 원본 리스트
a = ['BlockDMask', 'python', 'join', 'example']
print(a)
print()
 
# 리스트를 문자열로 합치기
result1 = "_".join(a)
print(result1)
 
# 리스트를 문자열로 합치기
result2 = ".".join(a)
print(result2)