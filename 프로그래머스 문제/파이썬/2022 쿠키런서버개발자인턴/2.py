#
from calendar import month
import sys
from collections import deque
from bisect import bisect_left
from bisect import bisect_right
def check_leap_year(year):
    if year % 400 == 0:
        return 1
    if year % 4 == 0 and year % 100 != 0:
        return 1
    return 0
        
def cal_days(start_day, end_day):
    
    year = [[365,31,28,31,30,31,30,31,31,30,31,30,31],[366,31,29,31,30,31,30,31,31,30,31,30,31]]
    days = 0
    
    start_year, start_month, start_days = start_day
    end_year, end_month, end_days = end_day
    
    
    if start_year == end_year:# 근무 년도와 퇴직 연도가 같을 때
        month_temp = year[check_leap_year(start_year)]
        if start_month == end_month: # 달이 같은 경우
            days += end_days - start_days + 1
            return days
        
        days += month_temp[start_month] - start_days + 1
        for m in range(start_month + 1, end_month):
            days += month_temp[m]
        days += end_days
        
    else:# 근무 년도와 퇴직 연도가 다를 때
        # 근무 시작 해 계산
        month_temp = year[check_leap_year(start_year)]
        days += month_temp[start_month] - start_days + 1
        for m in range(start_month + 1, 13):
            days += month_temp[m]
        
        # 중간 해 계산
        for y in range(start_year + 1, end_year):
            days += year[check_leap_year(y)][0]
        
        # 근무 마지막 해 계산
        month_temp = year[check_leap_year(end_year)]
        for m in range(1, end_month):
            days += month_temp[m]
        days += end_days
        
    return days

def not_weekend_hol(holidays, start_day, end_day, date):
    holidays.sort()
    result = 0
    s_idx = bisect_left(holidays, start_day)
    e_idx = bisect_right(holidays, end_day)

    holidays = holidays[s_idx:e_idx]
            
    for h in holidays:
        days = cal_days(start_day, h)
        if date[(days - 1) % 7] == 'SAT' or date[(days - 1) % 7] == 'SUN':
            continue
        else:
            result += 1
            
    return result

def solution(join_date, resign_date, holidays):

    result = 0
    holidays_list = []
    
    date = deque(['MON','TUE', 'WED','THU','FRI','SAT','SUN'])
    temp = deque([])
    
    join_date_day, join_date_date = map(str, join_date.split())
    join_date_day = list(map(int, join_date_day.split('/')))
    resign_date_day = list(map(int,resign_date.split('/')))

    # 공휴일
    for y in range(join_date_day[0], resign_date_day[0] + 1):
        for h in holidays:
            h_month, h_day = map(int, h.split('/'))
            holidays_list.append([y,h_month,h_day])
    
    # 요일
    while join_date_date != date[0]:
        temp_date = date.popleft()
        temp.append(temp_date)
    
    while temp:
        temp_date = temp.popleft()
        date.append(temp_date)
    date = list(date)
    
    total_days = cal_days(join_date_day,resign_date_day)

    sun_or_sat_days = (total_days-1) // 7 * 2
    cnt = 0
    if 'SAT' in date[:(total_days - 1) % 7 + 1]:
        cnt += 1
    if 'SUN' in date[:(total_days - 1) % 7 + 1]:
        cnt += 1
        
    total_holidays = not_weekend_hol(holidays_list, join_date_day, resign_date_day,date)
    
    return total_days - sun_or_sat_days - total_holidays - cnt
    
    
if __name__ == '__main__':
    join_date = ['2020/1/5 TUE','2019/12/01 SUN', '2019/12/01 SUN', '2019/11/21 THU']
    resign_date = ['2024/03/20','2019/12/31', '2020/03/02','2019/11/21']
    holidays = [['5/5', '12/25', '3/1'],['12/25'],['01/02','12/24','03/01'],['12/23']]
    for p,r,h in zip(join_date, resign_date, holidays):
        print(solution(p,r,h))