# from 패키지명 import 모듈명(.py)
# 1. 모듈명을 import 하기
# from mycode.lab import fah_converter

# 2. 모듈명을 import 하면서 alias name (별명) 설정하기
# from mycode.lab import fah_converter as conv

# 3. 모듈에 속한 convert_c_to_f 함수만 import 하기
# from mycode.lab.fah_converter import convert_c_to_f

# 4. 모듈에 속한 모든 함수를 import 하기
from mycode.lab.fah_converter import *

def main():
    print('변환하고 싶은 섭씨온도를 입력하세요!!')
    # float() : str -> float 타입으로 변환해주는 함수
    temperature = float(input())

    # fah_converter 모듈의 convert_c_to_f() 함수호출
    # result = conv.convert_c_to_f(temperature)

    # result = conv.convert_c_to_f(temperature)

    result = convert_c_to_f(temperature)

    print('섭씨온도 ', temperature)
    print(f'화씨온도 = {result:.2f}')

    print(say_hello('python'))

# main()

# 직접실행 아니?
if __name__ == "__main__":
    main()
    print('직접실행됨 ', __name__)
# 직접실행이 아니라 임포트되는 경우
else:
    print('import되어 실행됨', __name__)
