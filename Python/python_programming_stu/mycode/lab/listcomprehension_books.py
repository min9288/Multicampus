books = list() # 책 목록 선언
# 책 목록 만들기
books.append({'제목': '개발자의 코드', '출판연도': '2013.02.28', '출판사': 'A출판', '쪽수': 200, '추천유무': False})
books.append({'제목': '클린 코드', '출판연도': '2013.03.04', '출판사': 'B출판 ', '쪽수': 584, '추천유무': True})
books.append({'제목': '빅데이터 마케팅', '출판연도': '2014.07.02', '출판사': 'A출판 ', '쪽수': 296, '추천유무': True})
books.append({'제목': '구글드', '출판연도': '2010.02.10', '출판사': 'B출판', '쪽수': 526, '추천유무': False})
books.append({'제목': '강의력', '출판연도': '2013.12.12', '출판사': 'C출판', '쪽수': 248, '추천유무': True})

# 1. 250쪽 넘는 책 목록 만들기
# 2. 추천유무가 True인 책 목록 만들기
# 3. 출판사 목록 만들기 ( 중복되는 이름은 제거합니다.)

# 책제목 List 선언
title_list = list()
# 출판사 List 선언
publisher_list = set()
# 페이지가 250 초과 List 선언
many_page_list = []
# 추천유무가 True 인 List 선언
recommend_list = list()
# 모든 책들의 쪽수의 합
all_pages_sum = int()

# [{},{},{}]
for book in books:
    #print(type(book), book)
    title_list.append(book['제목'])
    publisher_list.add(book['출판사'].strip())
    if book['쪽수'] > 250:
        many_page_list.append({'제목': book['제목'],'쪽수':book['쪽수']})
    if book['추천유무']:
        recommend_list.append(book['제목'])

    all_pages_sum += book['쪽수']

print(title_list)
print(publisher_list)
print(many_page_list)
print(recommend_list)
print(all_pages_sum)

# List Comprehension Style
title_list = [book['제목'] for book in books]
publisher_list = set([book['출판사'].strip() for book in books])
many_page_list = [{'제목': book['제목'],'쪽수':book['쪽수']} for book in books if book['쪽수'] > 250]
recommend_list = [book['제목'] for book in books if book['추천유무']]
all_pages_sum = sum([book['쪽수'] for book in books])

print(title_list)
print(publisher_list)
print(many_page_list)
print(recommend_list)
print(all_pages_sum)