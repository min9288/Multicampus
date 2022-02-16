from django.db import models
from django.utils import timezone
from django import forms


# title 필드의 length가 2보다 작으면 검증오류 발생시키는 함수 선언하기
def min_length_2_validator(value):
    if len(value) < 2:
        # ValidataionError 예외를 강제로 발생시킨다
        raise forms.ValidationError('title은 2글자 이상 입력해 주세요!')


class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200, validators=[min_length_2_validator])
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    # 삭제할 예정 마이그레이션 테스트 하기 위함
    # test = models.TextField()

    # Model클래스에 정의된 __str__ 함수를 재정의 (title 필드값을 리턴함)
    def __str__(self):
        return self.title + '(' + str(self.id) + ')'

    # published_date 필드에 현재날짜를 저장하는 메서드
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    # Post가 참조하는 Comment 중에서 승인된 Comment만 필터링하기
    def approved_comments(self):
        return self.comments.filter(approved_comment=True)


# 댓글(Comment) Model 클래스 선언
class Comment(models.Model):
    # 참조하는 Post 객체
    post = models.ForeignKey('blog.Post', on_delete=models.CASCADE, related_name='comments')
    # 작성자
    author = models.CharField(max_length=200)
    # 내용
    text = models.TextField()
    # 작성일
    created_date = models.DateTimeField(default=timezone.now)
    # 승인여부
    approved_comment = models.BooleanField(default=False)

    # 댓글승인
    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text + '(' + str(self.id) + ')'