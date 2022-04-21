# def solution(s):
#     length = []
#     result = ""
    
#     if len(s) == 1:
#         return 1
    
#     for cut in range(1, len(s) // 2 + 1): 
#         count = 1
#         tempStr = s[:cut] 
#         for i in range(cut, len(s), cut):
#             if s[i:i+cut] == tempStr:
#                 count += 1
#             else:
#                 if count == 1:
#                     count = ""
#                 result += str(count) + tempStr
#                 tempStr = s[i:i+cut]
#                 count = 1

#         if count == 1:
#             count = ""
#         result += str(count) + tempStr
#         length.append(len(result))
#         result = ""
    
#     return min(length)
import sys
def solution(s):
    smallest = sys.maxsize

    if len(s) == 1:
        return 1
    
    for cut in range(1, len(s) // 2 + 1):
        cnt = 1
        temp = ''
        start = s[:cut]
        for i in range(cut,len(s),cut):
            if start == s[i:i+cut] :
                cnt += 1
            else:
                if cnt == 1:
                    temp += start
                    start = s[i:i+cut]
                    cnt = 1
                else:
                    temp += str(cnt) + start
                    start = s[i:i+cut]
                    cnt = 1
        if cnt == 1:
            temp += start
        else:
            temp += str(cnt) + start
        smallest = min(smallest, len(temp))
    
    return smallest


if __name__ == '__main__':
    s = ["aabbaccc","ababcdcdababcdcd","abcabcdede","abcabcabcabcdededededede","xababcdcdababcdcd"]
    for i in s:
        print(solution(i))