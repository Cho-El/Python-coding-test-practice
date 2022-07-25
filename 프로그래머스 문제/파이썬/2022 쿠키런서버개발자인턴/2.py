#
import sys

def solution(join_date, resign_date, holidays):
    day = ['']
if __name__ == '__main':
    join_date = ['2019/12/01 SUN', '2019/12/01 SUN', '2019/11/21 THU']
    resign_date = ['2019/12/31', '2020/03/02','2019/11/21']
    holidays = [['12/25'],['01/02','12/24','03/01'],['12/23']]
    for p,r,h in zip(join_date, resign_date, holidays):
        print(solution(p,r,h))