def solution(number, k):
    stack = []
    
    for num in number:
        if not stack:
            stack.append(num)
            continue
        
        while k != 0 and stack[-1] < num:
            stack.pop()
            k -= 1
            if not stack:
                break

        if k == 0:
            stack.append(num)
            continue

        stack.append(num)

    stack = stack[:-k] if k > 0 else stack
    return ''.join(stack)

# def solution(number, k):
#     i=0
#     while i<len(number)-1 and k>0:
#         if number[i]<number[i+1]:
#             number = number[:i]+number[i+1:]
#             if i!=0:
#                 i-=1
#             k-=1
#         else:
#             i+=1
#     if k>0:
#         return number[:-k]
#     return number

print(solution("4177252841", 4))
        