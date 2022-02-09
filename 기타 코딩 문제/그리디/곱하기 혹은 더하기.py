'''
각 자리가 숫자(0~9)로만 이루어진 문자열 S가 주어졌을 떄, 왼쪽부터 오른쪽으로
하나씩 모든 숫자를 확인하며 숫자 사이에 'X' 혹은 '+' 연산자를 넣어 결과적으로 만들어
질 수 있는 가장 큰 수를 구하는 프로그램을 작성하세요. 단 모든 엿나은 왼쪽에서부터
순서대로 이루어진다고 가정합니다.
ex) 02984로 만들 수 있는 가장 큰 수는
(((((0+2) X 9)X 8) X 4) = 576
'''
# 0과 1만 아니면 모두 곱하기해주면 된다.
N = input("문자열을 입력해주세요 : ")
def big_num(N):
	result = 0
	for num in N:
		if num == '0':
			result += 0
		elif num == '1':
			result += 1
		elif result != 0:
			result *= int(num)
		else:
			result += int(num)
	
	return result


def big_num2(N):
	result = int(N[0])
	for i in range(1,len(N)):
		num = int(N[i])
		if num <=1 or result <= 1:
			result += num
		else:
			result *= num
	return result

print("결과는 : ", big_num2(N))

