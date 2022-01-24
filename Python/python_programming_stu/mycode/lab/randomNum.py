import random
inputNum = int(input())
while True:
    guess_number = random.randint(1, 100)
    print(guess_number)
    if guess_number == inputNum:
        print('값이 동일합니다, 프로그램을 종료합니다.')
        break
    elif guess_number > inputNum:
        print('입력 값이 랜덤 값보다 작습니다.')
    else:
        print('입력 값이 랜덤 값보다 큽니다.')