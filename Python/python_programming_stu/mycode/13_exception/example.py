for i in range(10):
    try:
        print(i, 10 // i)
    except ZeroDivisionError:
        print("Not divided by 0")


for i in range(10):
    try:
        result = 10 // i
    except Exception as exp:
        print(exp)
    else:
        print(result)
    finally:
        print('에러여부 상관없이 출력')