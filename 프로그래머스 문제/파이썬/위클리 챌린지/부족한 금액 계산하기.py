def solution(price, money, count):
    answer = -1
    total_price = 0
    for i in range(1,count + 1):
        total_price += price * i
    
    if money >= total_price:
        return 0
    else:
        return abs(total_price - money)

if __name__ == "__main__":
    print(solution(3,20,4))