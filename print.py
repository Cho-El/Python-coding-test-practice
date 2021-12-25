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