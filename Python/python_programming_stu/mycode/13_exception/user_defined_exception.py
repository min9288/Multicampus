# 사용자정의 Exception  클래스 선언하기
# Exception 클래스를 상속받아야 한다.
# 음수 값이 입력되었을때 강제로 예외를 발생시키기
class NegativePriceException(Exception):
    # 생성자(클래스로 부터 객체가 생성이 될때 호출되는 함수) 선언하기
    def __init__(self):
        print('Price는 can\'t be Negative')
        # AttributeError
        raise AttributeError

def calc_price(value):
    price = value * 1000
    if price < 0:
        raise NegativePriceException
    return price

print(calc_price(200))
print(calc_price(-100))
