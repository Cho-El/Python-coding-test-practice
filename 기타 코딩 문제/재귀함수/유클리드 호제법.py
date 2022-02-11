'''
두 개의 자연수에 대한 최대공약수를 구하는 대표적인 알고리즘으로 유클리드 호제법이 있다.
A B에 대하여 A를 B로 나눈 나머지를 R이라고 하자.
A와 B의 최대공약수는 B왜 R의 최대공약수와 같다.
ex)
192 162
162 30
30 12
12 6
'''
A, B = map(int, input("숫자 두개를 입력해주세요 :").split())
# if A<B :
# 	A,B = B,A 

def GCD(A, B):
	if A%B == 0:
		return B
	a = GCD(B,A%B)
	
print(GCD(A, B))