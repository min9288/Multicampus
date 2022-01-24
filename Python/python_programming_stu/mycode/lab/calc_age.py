'''
    태어난 년도를 입력받아서 나이를 계산하기
    나이 = 현재년도 - 태어난 년도 + 1
'''
from datetime import datetime as dt
# 현재년도
print(dt.now())
print(dt.today())
current_year = dt.today().year
print(f'현재년도 {current_year}')

input_year = int(input('태어난 년도를 입력하세요 :'))
print(type(input_year), input_year)

age = current_year - input_year + 1
print(f'나이 {age}')

if 17 <= age < 20:
    print('고등학생입니다.')
elif age >= 20 and age <= 27:
    print('대학생입니다.')
else:
    print('학생이 아닙니다.')