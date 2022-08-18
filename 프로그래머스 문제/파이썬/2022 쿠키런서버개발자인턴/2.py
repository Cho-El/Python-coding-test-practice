#
import sys
from collections import deque

def check_leap_year(year):
    if year % 400 == 0:
        return 1
    if year % 4 == 0 and year % 100 != 0:
        return 1
    return 0
        
        
    
def solution(join_date, resign_date, holidays):
    check_year = [365,366]
    leap_year = [31,29,31,30,31,30,31,31,30,31,30,31]
    com_year = [31,28,31,30,31,30,31,31,30,31,30,31]
    result = 0
    
    date = deque(['MON', 'TUE', 'WED','THU','FRI','SAT','SUN'])
    temp = deque([])
    
    join_date_day, join_date_date = map(str, join_date.split())
    join_date_day = list(map(int, join_date_day.split('/')))
    resign_date_day = list(map(int,resign_date.split('/')))
    
    while join_date_date != date[0]:
        temp_date = date.popleft()
        temp.append(temp_date)
    
    while temp:
        temp_date = temp.popleft()
        date.append(temp_date)
    
    days = 0
    for year in range(join_date_day[0], resign_date_day[0]):
        if check_leap_year(year): # 윤년인 경우
            days += leap_year[join_date_day[1]] - join_date_day[2] + 1
            for month in range(join_date_day[1] + 1, 13):
                days += leap_year[month-1]
                
            
    
    
    
if __name__ == '__main__':
    join_date = ['2019/12/01 SUN', '2019/12/01 SUN', '2019/11/21 THU']
    resign_date = ['2019/12/31', '2020/03/02','2019/11/21']
    holidays = [['12/25'],['01/02','12/24','03/01'],['12/23']]
    for p,r,h in zip(join_date, resign_date, holidays):
        print(solution(p,r,h))