# 학생별 과목의 평균점수 구하기

kor_score = [49,79,20,100,80]
math_score = [43,59,85,30,90]
eng_score = [49,79,48,60,100]

midterm_score=[kor_score, math_score, eng_score]

# 학생별 과목의 합계를 저장할 리스트 선언
student_score = [0,0,0,0,0]
# 과목이 바뀌면 학생을 구분하는 index를 초기화
# 학생을 구분하기 위한 index 변수 선언
index = 0
for subject_score in midterm_score:
    # print(subject_score)
    for score in subject_score:
        # 각 학생 개별로 과목점수를 누적
        student_score[index] += score
        # print(student_score)
        index += 1
    print('--------------------------')
    # 과목이 바뀌면 학생 index 변수를 초기화
    index = 0
else:
    print(f'학생별 누적 점수 {student_score}')
    a, b, c, d, e = student_score
    student_avg_score = [int(a/3), int(b/3), int(c/3), int(d/3), int(e/3)]
    print(f'학생별 평균 점수 = {student_avg_score}')