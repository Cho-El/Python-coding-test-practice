from collections import defaultdict
def solution(fees, records):
    remain = {}
    result = defaultdict(int)
    final_result = []
    for record in records:
        time, num, act = record.split(' ')
        time = 60 * int(time[:2]) + int(time[3:5])
        if act == 'IN':
            remain[num] = time
        else:
            start_time = remain[num]
            end_time = time
            dif_time = end_time - start_time
            del remain[num]
            result[num] += dif_time
    
    for key,v in remain.items():
        last_time = 23 * 60 + 59
        result[key] += last_time - v
    
    # 계산하기
    for key, v in result.items():

        if v <= fees[0]:
            final_result.append((key, fees[1])) # 차번호판과, 요금
        else:
            if (v - fees[0]) % fees[2] == 0: 
                price = fees[1] + ((v - fees[0]) // fees[2]) * fees[3]
                final_result.append((key, price))
            else:
                price = fees[1] + ((v - fees[0]) // fees[2] + 1) * fees[3]
                final_result.append((key, price))
        
    final_result.sort(key = lambda x:int(x[0]))
    result = []
    for key, v in final_result:
        result.append(v)
    
    return result

if __name__ == '__main__':
    records = [	["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"],
    ["16:00 3961 IN","16:00 0202 IN","18:00 3961 OUT","18:00 0202 OUT","23:58 3961 IN"],
    ["00:00 1234 IN"]]
    fees = [[180, 5000, 10, 600],[120, 0, 60, 591],[1, 461, 1, 10]]
    for fee, record in zip(fees,records):
        print(solution(fee, record))