'''
    본 프로그램은 섭씨를 화씨로 변환해주는 프로그램 입니다.
    변환하고 싶은 섭씨온도를 입력하면 화씨를 출력해준다.
'''

# def transTem(temp):
#     return ((9/5) * temp) + 32
# print(transTem(32.2))
#
#
temperature = float(input())

fah = ((9/5) * temperature) + 32
print('섭씨온도 '. temperature)
print('화씨온도 '. fah)
print('화씨온도 {:.2f} '.format(fah))
print(f'화씨온도 {fah:.2f}')
