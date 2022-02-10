'''
알파벳 대문자와 숫자0~9로만 구성된 문자열이 입력으로 주어집니다. 이때 모든 알파벳을 오름차순으로 정렬하여
이어서 출력한 뒤에, 그 뒤에 모든 숫자를 더한 값을 이어서 출력합니다.
예를 들어 K1KA5CB7이라는 값이 들어오며 ABCKK13을 출력합니다.
'''

s = input("문자열을 입력해주세요 : ")
def re_sort(s):
    new_alp = []
    result = ''
    sum = 0
    for i in s:
        if 'A'<=i and 'Z'>=i :
            new_alp.append(ord(i))
        else:
            sum += int(i)
    new_alp.sort()
    for i in range(len(new_alp)):
        result += chr(new_alp[i])

    return result + str(sum)

print(re_sort(s))