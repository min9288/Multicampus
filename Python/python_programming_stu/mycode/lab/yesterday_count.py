'''
    yesterday.txt 파일을 읽어서
    'YESTERDAY', 'yesterday', 'Yesterday'
    단어가 몇 번 나오는지 Counting 해보기
'''
# file, mode = 'r', buffering=None, encoding=None, errors=None, newline=Nene, closefd=True
# mode : r(read), w(write), a(write append), rb,wb (binary fule r/w)

lyrics_text = ''
file = open('yesterday.txt', 'r')

# while 1:
#     text = file.readline()
#     if not text:
#         break
#     lyrics_text += text
#     # lyrics_text = lyrics_text + text
#
# file.close()

with open('yesterday.txt', 'r') as file:
    # while 1:
    #     text = file.readline()
    #     if not text:
    #         break
    #     lyrics_text += text
    #     # lyrics_text = lyrics_text + text

    lyrics_text = file.read()

# print(len(lyrics_text))
# print(lyrics_text)

n_of_YESTERDAY = lyrics_text.upper().count('YESTERDAY')
print(f'Number of a word YESTERDAY {n_of_YESTERDAY}')

n_of_yesterday = lyrics_text.lower().count('yesterday')
print(f'Number of a word yesterday {n_of_yesterday}')

n_of_Yesterday = lyrics_text.count('Yesterday')
print(f'Number of a word Yesterday {n_of_Yesterday}')