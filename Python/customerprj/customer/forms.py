from django import forms

def min_length_2_validator(value):
    if len(value) < 2:
        # ValidataionError 예외를 강제로 발생시킨다
        raise forms.ValidationError('text은 2글자 이상 입력해 주세요!')

class CustomerForm(forms.Form):
    name = forms.CharField(validators=[min_length_2_validator])
    email = forms.EmailField()
    birthdate = forms.DateField()
    CHOICES = [('1', '남자'), ('0', '여자')]
    gender = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES)