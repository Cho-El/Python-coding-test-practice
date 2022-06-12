import sys

def vip_check(pe, pa): # vip 여부 확인

    if 24 <= pe < 60:
        if sum(pa) >= 900000:
            return 1
        else:
            return 0

    elif pe >= 60:
        if sum(pa) >= 600000:
            return 1
        else:
            return 0

    else:
        return 0
            
def solution(periods, payments, estimates):
    answer = [0,0]
    check = 1
    this_month_customer_vip = []
    next_month_customer_vip = []

    # 이번 달 vip 여부
    for pe, pa in zip(periods, payments):
        this_month_customer_vip.append(vip_check(pe, pa))

    # 다음 달 vip 여부
    for pe, pa, es in zip(periods, payments, estimates):
        temp = pa[1:len(pa)] + [es]
        next_month_customer_vip.append(vip_check(pe + 1, temp))
    
    for tv, nv in zip(this_month_customer_vip, next_month_customer_vip):
        if tv == 0 and nv == 1:
            answer[0] += 1
        elif tv == 1 and nv == 0:
            answer[1] += 1
        
    return answer

if __name__ == '__main__':
    periods = [[20,23,24],[24, 59, 59, 60]]
    payments = [[[100000,100000,100000,100000,100000,100000,100000,100000,100000,100000,100000,100000],
    [100000,100000,100000,100000,100000,100000,100000,100000,100000,100000,100000,100000],
    [350000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000]],
    [[50000,50000,50000,50000,50000,50000,50000,50000,50000,50000,50000,50000],
    [50000,50000,50000,50000,50000,50000,50000,50000,50000,50000,50000,50000],
    [350000,50000,50000,50000,50000,50000,50000,50000,50000,50000,50000,50000],
    [50000,50000,50000,50000,50000,50000,50000,50000,50000,50000,50000,50000]]]
    estimates = [[100000, 100000, 100000], [350000, 50000, 40000, 50000]]

    for pe, pa, es in zip(periods, payments, estimates):
        print(solution(pe, pa, es))