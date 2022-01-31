# Multicampus

## 0. 목차
**[1. 개요](#1-개요)**  
**[2. 교육 일정](#2-교육-일정)**  

<details>
<summary>교육 일정 상세보기</summary>
<div markdown="1">
	
| 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |  
| :-----: | :-----: | :-----: | :-----: | :-----: | :-----: | :-----: | :-----: | :-----: | :-----: |  
| [2.1](#21-1일차2022-01-17) | [2.2](#22-2일차2022-01-18) | [2.3](#23-3일차2022-01-19) |

</div>
</details>  

<details>
<summary>교육 내용 시작점 상세보기</summary>
<div markdown="1">

**[1. PYTHON](#22-2일차2022-01-18)**  

</div>
</details>  

## 1. 개요
- 이 문서는 멀티캠퍼스 교육 중 만들어지는 문서들을 저장하기 위한 Repository입니다.

## 2. 교육 일정

### 2.1 2일차(2022-01-17)
- 교육 오리엔테이션(학원 소개, 제한 사항, 등)

### 2.2 2일차(2022-01-18)
- 파이썬의 특징
 1. 문법이 다른 언어에 비해 쉽다.
 2. 특정한 기술을 미리 만들어서 모듈 = 패키지 = 라이브러리로 제공한다.
 3. 다양한 분야에 사용가능하다, 특히 데이터분석 & 인공지능과 관련된 모듈을 다양하게 제공한다.
 4. 객체지향적인 언어
  - 실행순서가 아닌 단위모듈(객체) 중심으로 프로그램을 작성
  - 하나의 객체는 어떤 목적을 달성하기 위한 행동(method)과 속성(attribute)를 가지고 있다.
 5. 동적 타이핑 언어
  - 프로그램이 실행하는 시점에 데이터에 대한 타입을 결정한다.

- 파이썬과 관련된 모듈 메뉴얼 확인법 : filetype:pdf metplotlib
- 파이썬은 프로젝트 형식으로 완성된 코드가 많이 웹상에서 공유되기 때문에 메뉴얼과 병행하여서 프로젝트성의 완성코드를 공부하는것도 좋음
  => 캐글, 데이콘 등
- 파이썬 관련 코드는 git을 통해 공유하는 경우도 많음.

- 파이썬 주의점 : 파이썬은 작업하는 프로젝트에 따라서 사용하는 모듈이 다를 수 있음.
                  텐서플로우는 인공지능 모듈이 주 목적임.
                  텐서플로는 버전에 따라서 넘파이 등의 하위 모듈을 갖고 있음.
                  나는 넘파이가 3.4고, 텐서플로우는 넘파이를 3.0으로 사용해야 할때도 있음.
                  나의 넘파이 3.4를 지우고 텐서에 맞는 3.0으로 다운해야함.
                  이러면 기존의 3.4가 필요한 다른 모듈이 문제가 됨
 -> 해결책 : 각 프로젝트별로 가상환경을 세팅하여 작업
            envs라는 폴더아래 - 각 가상환경 폴더가 생성 - 그 안에 라이브러리가 생성됨
         
### 2.3 3일차(2022-01-19) 

 - 1단계 (반복문 없이 작업)
 ```
  folderName='./picture/'
  fileName='pic1.jpg' ; print(folderName+fileName)
  fileName='pic2.jpg' ; print(folderName+fileName)
 ```
 - 2단계 (fileName을 리스트화해서 인덱싱)
 ```
  folderName='./picture/'
  fileName=['pic1.jpg', 'pic2.jpg', 'pic3.jpg']
  print(folderName+fileName[0])
  print(folderName+fileName[1])
 ```
 - 3단계 (fileName 리스트 인덱싱 값 변수추가)
 ```
  folderName='./picture/'
  fileName=['pic1.jpg', 'pic2.jpg', 'pic3.jpg']
  i=0 ; print(folderName+fileName[i])
  i=1 ; print(folderName+fileName[i])
 ```
 - 4단계 (for를 이용한 반복문 & i값 갯수)
 ```
  folderName='./picture/'
  fileName=['pic1.jpg', 'pic2.jpg', 'pic3.jpg']
  cnt=len(fileName)
  for i in range(cnt):  
  print(folderName+fileName[i])
 ```
 - 5단계(fileName 리스트추가 자동화)
 ```
  import os
  folderName='./picture/'
  fileName=os.listdir(folderName)

  cnt=len(fileName)
  for i in range(cnt):  
   print(folderName+fileName[i])
 ```
 - 6단계(fileName중 확장자(.을 기준으로 나누는 뒷글자임)가 'jpg'인 자료만)
 ```
  import os
  folderName='./picture/'
  fileName=os.listdir(folderName)

  for i in range(cnt): # 
      tmp=fileName[i].split('.')[1]
      if tmp=='jpg':
          print(folderName + fileName[i])
```

**제어문**
- 결과값이 true(참)이거나 false(거짓)이 나오는 경우에 사용
- true(조건에 대한 결과가 일치함) / false(조건에 대한 결과가 불일치)
- 구문구성 (if 조건 true 일때 할 작업 false 일때 할 작업)
- 단, 파이썬,자바,C 등의 언어에 따라 구문구성의 문법이 다를 뿐

<pre><code class="python">if 조건문:
    수행할 문장1
    수행할 문장2
    ...
else:
    수행할 문장A
    수행할 문장B
    ...
</code></pre>

**반복문(for)**
- 프로그램 언어에 따라 for 구문은 다름
- 파이썬에서는 숫자값이 생성되면서 할당 할때는 <br>
     for 변수 in range(숫자) :    # 파이썬 2 와 3 버전에서 해당 구문이 다름
- 리스트 자료에 있는 값을 직접 할당 할 때는 <br>
    for 변수 in zip (자료1, 자료2)


### 2.4 6일차(2022-01-24) 
- 파이썬의 특징 (정규과정 시작)
 1. 문법이 다른 언어에 비해 쉽다.
 2. 특정한 기술을 미리 만들어서 모듈 = 패키지 = 라이브러리로 제공한다.
 3. 다양한 분야에 사용가능하다, 특히 데이터분석 & 인공지능과 관련된 모듈을 다양하게 제공한다.
 4. 객체지향적인 언어
  - 실행순서가 아닌 단위모듈(객체) 중심으로 프로그램을 작성
  - 하나의 객체는 어떤 목적을 달성하기 위한 행동(method)과 속성(attribute)를 가지고 있다.
 5. 동적 타이핑 언어
  - 프로그램이 실행하는 시점에 데이터에 대한 타입을 결정한다.
 6. 가독성 - 문법이 간결하고 들여쓰기를 기반으로 가독성이 좋음
 7. 풍부한 라이브러리를 바탕으로 무궁한 확장성
 8. 유니코드 – 문자열이 모두 유니코드로 나타남

- 파이썬 인터프리터 설치  - www.python.org
 - 설치경로 (유닉스 계열) - /usr/local/bin/python3.5
 - 윈도우 – c:\Python37 ( set path=%path%;c:\python37 )

- PyCharm 설치
 - https://www.jetbrains.com/pycharm/download
 - 유료인 프로페셔널 에디션과 무료인 커뮤니티 에디션이 있음

## 자료형과 연산자 - 숫자타입
- 숫자형 타입 (Numbers)
    ```
    # 변수를 선언하고 값을 할당 my_int = 7 my_float = 1.23
    >>>30.5
    ```
  1. 변수를 만들고 값을 할당
  2. 소수점이 없는 정수는 int 타입으로 인식 – 파이썬3 에서 long 타입이 없어지고 모두 int 타입
  3. 소수점이 있는 숫자는 float 타입
  4. type() 함수로 확인

  - 변수명과 타입 정리
    - 변수명
	  1. 변수의 타입을 지정하지 않음
	  2. 문자, 숫자, 밑줄( _ )을 포함 가능. 숫자는 처음에 올 수 없음
	  3. 예약어는 변수명으로 사용할 수 없음
  ```
    PEP 8 스타일 가이드를 따르자
    •파이썬 개선 제안서 (Python Enhancement Proposal) #8
    •https://www.python.org/dev/peps/pep-0008
  ```

- 싱글 라인 주석
  ```
    # 샵 문자 이후의 모든 내용은 주석처리 되어 인터프리터에 의해 읽혀지지 않음! 
    my_varibale = 7
  ```
  1. 주석은 코드의 문서화의 의미로 코드 가독성을 향상시키고 품질과 생산성을 향상시킴
  2. 주석에 대한 표준을 전체 프로젝트 표준으로 설정 필요
 
- 멀티 라인 주석 – docstring 이라고 함
 ```
  """
    Hello, how are you?
    작성일 : 2016.01.01
    작성자 : Jerry Kim
  """
  ```
 1. 싱글 라인 주석에 비해 여러 줄의 주석을 사용할 때 사용
 2. 세개의 따옴표 사이에 들어가는 모든 문자(숫자 포함, 공백 포함)는 주석처리 됨
 3. 모든 모듈, 클래스, 함수에 docstring 포함(PEP8 스타일가이드) - http://pep8.org

- Data Type Casting : 정수형 <-> 실수형
 - float()와 int() 함수를 사용하여 데이터의 타입 변환 가능

- CLI(Command Line Interface) : input() 함수
 - CLI 란?
  1. Graphic User Interface(GUI)와 달리 Text를 사용하여 컴퓨터에 명령을 입력하는 인터페이스 체계
  2. Windows : CMD window
  3. Mac, Linux : Terminal
 - 콘솔(Console) 창 입출력
  1. input() 함수는 콘솔 창에서 문자열을 입력 받는 함수

- 문자열
 - 문자를 다루는 방법 – string
	  ``` 
	    mystring = “hello world”
	    my_string2 = ‘hello world’

	  ```
 - 문자열 결합 : +
  ``` 
    first_name='Monty'
    last_name= 'Python'
    full_name= full_name+last_name
    full_name
    -> 'MontyPython'
  ```
 - 문자열 복제 : *
  ``` 
    >>> greet = ‘Hello ‘ * 4 + ‘\n’
    >>> end = ‘Goodbye.’
    >>> print(greet + greet + end)
  ```
 - 이스케이프 문자
    ``` 
	>>> print(‘\tabc’)
	abc
	>>> print(‘a\tbc’)
	a bc
	>>> print(‘ab\tc’)
	ab c
	>>> print(‘I love back slash \\’)

	\n 개행(줄바꿈)
	\t 탭
	\r 캐리지 리턴
	\0 널(null)
	\\ 문자 \
	\’ 단일 인용부호
	\” 다중 인용부호
    ```
- 데이터 타입 변환 : str()
 1. str() 함수를 사용하여 데이터 타입을 문자열로 변환 가능
  - int(), float() 는 마찬가지로 각각 int와 float 로 변환한다.
  
  ``` 
   >>> str(98.6)
    ‘98.6’
    >>> str(1.0e4)
    ‘10000.0’
    >>> str(True)
    ‘True’ 
  ```

- 문자열 자르기 : 음수 인덱스 사용
    >>> letters[-3:]
    >>> letters[18:-3]
    >>> letters[-6:-3]

- 문자열 길이 : len()
 1. 문자열의 길이를 잰다.
 2. 다른 시퀀스 타입에서도 사용 가능하다.

 ``` 
	 >>> letters = ‘abcdefghijklmnopqrstuvwxyz’ 
	 >>> len(letters) 26 
	 >>> empty = ‘’ 
	 >>> len(empty) 
	 0
 ```

 - 문자열 함수
  1. len(a) - 문자열의 문자 개수를 반환
  2. a.upper() - 대문자로 변환
  3. a.lower() - 소문자로 변환
  4. a.capitalize() - 첫 문자를 대문자로 변환
  5. a.title() - 제목형태로 변환, 띄어쓰기 후 첫 글자만 대문자
  6. a.count('abc') - 뮨자열 a에 'abc'가 들어간 위치 (오프셋) 반환
  7. a.find('abc') / a.rfind('abc') - 문자열 a에 'abc'가 들어간 위치(오프셋) 반환
  8. a.starswith(ab'c) - 문자열 a는 'abc'로 시작하는 문자열 여부 반환
  9. a.endswith('abc') - 문자열 a는 'abc'로 끝나는 문자열 여부 반환
  10. a.strip() - 좌우 공백을 없앰
  11. a.rstrip() - 오른쪽 공백을 없앰
  12. a.lstrip() - 왼쪽 공백을 없앰
  13. a.split() - 공백을 기준으로 나눠 리스트로 반환
  14. a.split('abc') - abc를 기준으로 나눠 리스트로 반환
  15. a.isdigit() - 문자열이 숫자인지 여부 반환
  16. a.islower() - 문자열이 소문자인지 여부 반환
  17. a.isupper() - 문자열이 대문자인지 여부 반환

- 리스트 
 - 파이썬에서 리스트는 원하는 모든 데이터를 담는 컨테이너
  1. Read-Only 리스트 – 튜플(Tuples)
  2. 위 두가지 모두 시퀀스 구조의 컨테이너 이다.
  ``` 
  # anemptylist
  empty =[]
  ```

  ``` 
  #listofnumbers
  nums= [10,20,30,40.5]
  ```

  ``` 
  #listofstrings
  words=['cheerio','cheers','watcha','hiya']
  ```

  ``` 
  # listofmixeditems
  anything=[10,'hello','ahoy',123.45]
  ```

 - 리스트의 아이템은 0부터 시작하는 인덱스(또는 오프셋이라고 함)로 순서를 가진다.
  1. 오프셋으로 데이터를 추출 또는 변경이 가능
  2. insert(offset, data) 함수를 통해 데이터 변경도 가능
  3. append(data) 함수로 데이터를 마지막에 추가

 - 오프셋으로 아이템 얻기
 ```
    >>> address = [‘seoul’, ‘seocho’, ‘woomyun’]
    >>> address[0]
    ‘seoul’
    >>> address[2]
    ‘woomyun’
    >>> address[-2]
    ‘seocho’
 ```

 - 오프셋으로 아이템 바꾸기
 ```
    >>> phone_number = [‘010’, ‘1234’, ‘4567’]
    >>> phone_number[1] = ‘2346’
    >>> phone_number
    [‘010’, ‘2346’, ‘4567’]
 ```

 - 슬라이싱(slicing)으로 아이템 추출
  - Slicing으로 리스트의 서브시퀀스를 추출할 수 있다.
  ``` 
    >>> address = [‘seoul’, ‘seocho’, ‘woomyun’]
    >>> address[0:2]
    [‘seoul’, ‘seocho’]

    >>> cities = [‘서울’,’부산’,’인천’,’대구’,’대전’,’광주’,’울산’,’수원’]
    >>> print(cities[0:6],” AND “, a[6:]) # 0 부터 5까지, 6부터 끝까지
    [‘서울’,’부산’,’인천’,’대구’,’대전’,’광주’] AND [’울산’,’수원’]
    >>> print([:]) # 처음부터 끝까지
    [‘서울’,’부산’,’인천’,’대구’,’대전’,’광주’,’울산’,’수원’]
    >>> print(cities[::2]) #2칸 단위로
    [‘서울’,’인천’,’대전’,’울산’]
    >>> print[::-1] #역으로 슬라이싱
    [‘수원’,’울산’,’광주’,’대전’,’대구’,’인천’,’부산’,’서울’]

  ```

 - 리스트의 연산
  ``` 
    >>> color = [‘red’,’blue’,’green’]
    >>> color2 = [‘orange’,’black’,’white’]
    >>> print(color + color2) # 두 리스트 합치기
    >>> color[0] = ‘yellow’ # 0번째 리스트의 값을 변경
    >>> print(color * 2) # color 리스트 2회 반복
    >>> ‘blue’ in color2 # 문자열 ‘blue’가 color2 존재 여부 반환

  ```

 - 아이템 추가와 삭제 append,extend,insert,remove,del
  ``` 
    >>> color.append(“white”) # 리스트에 “white” 추가
    >>> color.extend([“black”,”purple”]) # 리스트에 새로운 리스트 추가
    >>> color.insert(0,”orange”) # 0번째 주소에 “orange” 추가
    >>> print(color)
    [‘orange’,’yellow’,’blue’,’green’,’white’,’black’,’purple’]
    >>> color.remove(“white”)
    >>> del color[0]
    >>> print(color)
    [’yellow’,’blue’,’green’,’black’,’purple’]

  ```

 - 다른 데이터 타입을 리스트로 변환 : list()
  ``` 
    >>> list(‘cat’)
    [‘c’, ‘a’, ‘t’]

  ```

 - 문자열을 구분자로 나누어서 리스트로 변환 : split()
  ``` 
    >>> birthday = ‘1985/2/5’
    >>> birthday.split(‘/’)
    [‘1985’, ‘2’, ‘5’]

  ```

 - 값으로 오프셋 찾기 : index()
  ``` 
    >>> address = [‘seoul’, ‘seocho’, ‘woomyun’, ‘123-4’]
    >>> address.index(‘seocho’)
    1

  ```

 - 멤버쉽 확인 : in
  - 리스트의 멤버(아이템) 인지 확인하려면 in 을 사용
  ``` 
    >>> address = [‘seoul’, ‘seocho’, ‘woomyun’, ‘123-4’]
    >>> ‘seocho’ in address
    True
    >>> ‘gangnam’ in address
    False

  ```

 - 값 세기 : count()
  - 리스트에 특정 값이 얼마나 있는지 세기 위해서 count() 함수 사용
  ``` 
    >>> address.count(‘seocho’)
    1
    >>> address.count(‘gangnam’)
    0

  ```

 - 패킹과 언패킹
  - 패킹 : 한 변수에 여러 개의 데이터를 넣는 것
  - 언패킹 : 한 변수의 데이터를 각각의 변수로 반환
  ``` 
    >>> t = [1,2,3]     # 1,2,3을 변수 t에 패킹
    >>> a,b,c = t       # t에 있는 값 1,2,3을 변수 a,b,c에 언패킹
    >>> print(t,a,b,c)  # [1,2,3] 1 2 3

  ```

### 2.5 7일차(2022-01-25) 

  ## 제어문
  - 코드구조
    - 흐름 제어 : Flow Control
      1. 구조적 프로그래밍 : 순차구조, 선택구조, 반복구조로 이루어짐
    
    - bool 타입
      1. True 참
      2. False 거짓

  - 비교 연산자
    - 파이썬에서의 6개의 비교 연산자
      1. '<' : less than
      2. '<=' : less than equal to
      3. '==' : equal to
      4. '>=' : greater than equal to
      5. '>' : greater than
      6. '!=' : not equal to

  - flow - if
    - if - 조건문 (Conditional)
      1. if 는 조건문으로 if 문에 따라오는 문장이 True 이면 특정한 문장이 수행된다.
      2. 점수가 90점 이상이면 A학점을 받는다
        ``` 
          score = 92
          if score >= 90:
          print(‘grade A’)
        ```
      3. 조건문에는 if 라는 키워드를 사용한다
      4. if 다음에는 ‘조건＇이 존재하는데 이 ‘조건‘ 이 참 (True)이면 들여쓰기 한 문장이 실행된다
      5. if 문장 끝에는 콜론 ( : ) 을 입력한다
      6. if 문의 ‘조건‘ 이 참 (True)일 때 실행되는 문장은 들여쓰기를 해야 한다
  
    - if ~ elif ~ else 다중 구문
      1. 점수가 60점 이상이면 합격이고 이하이면 불합격 이다
        ```
          score = 59 
          if score >= 60: 
            print(‘합격’) 
          else: 
            print(‘불합격‘)
        ```
    
    - True 와 False
      1. 확인할 요소가 bool 형이 아니면 True와 False 를 어떻게 구별할까?
      2. False 값을 명시적으로 False 값이라고 할 필요없다.
      3. 다음 값은 모두 False 이다.
        ```
          null -> None
          int 타입 0 -> 0
          float 타입 0 -> 0.0
          빈 문자열 -> ''
          빈 리스트 -> []
          빈 튜플 -> ()
          빈 딕셔너리 -> {}
        ```
  - for 루프 – Dictionary
    - for 문
      1. 0부터 10까지 출력하기
        ```
          for i in [0,1,2,3,4,5,6,7,8,9,10]: 
              print(i)

          for i in range(0, 11): 
              print(i)
        ```
      
      2. for 와 list (list는 tuple로도 가능, 속도가 더 빠름)
        ```
          favorite_hobby = [‘reading’,’fishing’,’shopping’]
          for hobby in favorite_hobby:
          print(‘%s is my favorite hobby’ % hobby)
        ```

      3. for 와 dictionary
        ```
          wish_travel_city = {‘bangkok’:’Thai’, ’Los Angeles’:’USA’,      ’Manila’:’Philiphines’} 
          
          for city, country in wish_travel_city.items(): 
              print(‘%s in %s’ % (city, country))
        ```
      
    - for 루프 – 리스트의 각 아이템을 순환
      ```
        prices = [2.50, 3.50, 4.50]
        for price in prices:
        print('Price is', price)
      ```

      ```
        import random

        for i in range(10):
            ticket = random.randint(1, 1000)
            print(ticket)
      ```

      ```
        import random
        r1 = random.random()
        print(r1)
      ```

      ```
        import random

        r2 = random.choice([1,2,3,4,5])
        print(r2)
      ```

      ```
        r3 = random.randint(1,1000)
        print(r3)
      ```

  - for 루프 - range() 함수
    - range() 사용하기
      ```
        for looper in [1,2,3,4,5]:
            print('hello')
        for looper in range(0,5):
            print 'hello'
      ```

    - 간격을 두고 세기
      ```
        for i in range(1,10,2):
            # 1부터 10까지 2씩 증가시키면서 반복문 수행
            print(i)
      ```
    
    - 역순으로 반복문 수행
      ```
        for i in range(10,1,-1):
        # 10부터 1까지 -1씩 감소시키면서 반복문 수행
        print(i)
      ```
  - While 루프
    - while 문 – 조건이 만족하는 동안 반복 명령문을 수행
      ``` 
        i = 1
        while i < 10:
            print(i)
            i += 1
      ```

  - 반복의 제어 – break, continue , else
    - break 특정 조건에서 반복 종료
      ```
        for i in range(10):
            if i == 5: break    # i가 5가 되면 반복 종료
            print(i)
        print("EOP")      # 반복 종료 후 "EOP" 출력

        ** break로 종료된 반복문은 else block이 수행되지 않음
      ```

    - continue 특정 조건에서 남은 반복 명령 skip
      ```
        for i in range(10):
            if i == 5: continue    # i가 5가 되면 i를 출력하지 않음
            print(i)
        print("EOP")      # 반복 종료 후 "EOP" 출력
      ```

    - 반복 조건이 만족하지 않을 경우 반복 종료 시 1회 수행
      ```
        for i in range(10):
            print(i)
        else:
            print("EOP")
      ```
      ```
        i = 0
        while i < 10:
            print(i)
            i += 1
        else:
            print("EOP") 
      ```

### 2.6 8일차(2022-01-26)
  ## Data Structure
  - 자료구조(Data Structure) 란?
    1. 메모리상에서 데이터를 효율적으로 관리하는 방법
    2. 검색,저장 등의 작업에서 효율성을 고려하여 메모리 사용량과 실행시간 등을 최소화 해준다.
    3. 파이썬에서 List, Tuple, Set, Dictionary 등의 기본 데이터 구조를 제공한다.
    4. 스택과 큐 ( Stack & Queue )
    5. 튜플과 집합 ( Tuple & Set )
    6. 사전 ( Dictionary )
  
  - 스택 ( Stack )
    1. 나중에 넣은 데이터를 먼저 반환 하도록 설계된 메모리 구조로 Last In First Out ( LIFO ) 구현됨
    2. Data의 입력을 Push, 출력을 Pop 이라고 함
    3. 파이썬은 List를 사용하여 스택 구조를 활용
    4. push를 append() / pop을 pop() 사용

  - 큐 ( Queue )
    1. 처음에 넣은 데이터를 먼저 반환 하도록 설계된 메모리 구조로 FIFO ( First In First Out) 구현됨
    2. Stack 과 반대 되는 개념
    3. 파이썬은 List를 사용하여 큐 구조를 활용
    4. put을 append(), get을 pop(0) 사용
  
  - 튜플 (Tuples) – Read Only
    1. 값의 변경이 불가능한 리스트
    2. 선언 시 “[ ]” 가 아닌 “( )” 를 사용
    3. 리스트의 연산, 인덱싱, 슬라이싱 등을 동일하게 사용함
      ```
        t = (1)   # 일반정수로 인식
        1

        t = (1,)    # 값이 하나인 Tuple은 반드시 "," 를 붙여야 함
        (1,)
      ```
  
  - 튜플과 리스트
    1. 튜플은 더 적은 공간을 사용한다.
    2. 실수로 튜플의 항목이 손상될 염려가 없다.
    3. 함수의 파라미터들은 튜플로 전달된다.
    4. 튜플을 사용하는 이유는 프로그램을 작동하는 동안 변경되지 않는 데이터의 저장
    5. 예) 학번, 이름, 우편번호 등
  
  - 집합(Set) – 중복 허용 안함
    1. 값을 순서 없이 저장, 중복을 허용하지 않는 자료형
    2. set 객체 선언을 이용하여 객체 생성
      ```
        >>> s = set([1,2,3,1,2,3])    # set 함수를 사용 1,2,3을 집합 객체 생성
        >>> s
        {1,2,3}

        >>> s.add(1)    # 한 원소 1만 추가 -> 중복 불허로 추가 되지 않음
        >>> s
        {1,2,3}

        >>> s.remove(1)   # 1 삭제
        >>> s
        {2,3}

        >>> s.update([1,4,5,6,7])   # [1,4,5,6,7] 추가
        >>> s
        {1,2,3,4,5,6,7}

        >>> s.discard(3)    # 3삭제
        >>> s
        {1,2,4,5,6,7}

        >>> s.clear()   # 모든 원소 삭제
      ```
  
  - 집합(Set) 의 연산
    - 수학에서 활용하는 다양한 집합 연산 가능
    ```
      >>> s1 = set([1,2,3,4,5])
      >>> s2 = set([3,4,5,6,7])

      >>> s1.union(s2)    # s1 과 s2의 합집합
      {1,2,3,4,5,6,7}
      >>> s1 | s2     s1.union(s2)
      {1,2,3,4,5,6,7}

      >>> s1.intersection(s2)     # s1 과 s2의 교집합
      {3,4,5}
      >>> s1 & s2     # s1.intersection(s2)
      {3,4,5}

      >>> s1.difference(s2)     # s1 과 s2의 차집합
      {1,2}
      >>> s1 - s2     # s1.difference(s2)
      {1,2}
    ```
  
  - Dictionary – 키/값 쌍으로 데이터를 관리
    1. 리스트와 유사하지만 인덱스 대신에 키를 통해 값을 찾는다.
      - key와 value를 매칭하여 key로 value를 검색한다. 다른 언어에서는 Hash Table 이라는 용어를 사용한다.
        ```
          slang = {'cheerio' : 'goodbye', 'knackered' : 'tired', 'yonks' : 'ages'}
        ```
      
    2. 딕셔너리 생성
      ```
        - 빈 딕셔너리 만들기
        slang = {}

        - 딕셔너리 아이템 추가
        slang['cheerio']  = 'goodbye'
        slang['smashing'] = 'terrific'        # 딕셔너리에 키/값 쌍으로 된 아이템을 추가
        slang['knackered'] = 'tired'
        print(slang)
      ```
    
    3. 아이템 업데이트
      ```
        slang['smashing'] = 'awesome'
        print(slang['smashing'])
      ```
    
    4. Dictionary – 아이템 삭제
      ```
        slang = {'cheerio' : 'goodbye', 'knackered' : 'tired', 'smashing' : 'terrific'}
        del slang['cheerio']      # del 키워드 사용해서 삭제
        print(slang)
      ```
    
    5. 모든 항목 삭제 : clear()
      ```
        slang.clear()
      ```
    
    6. 딕셔너리로 변환 : dict()
      ```
        >>> lol = [[‘a’, ‘b’], [‘c’, ‘d’], [‘e’, ‘f’]]
        >>> dict(lol)
        {‘c’: ‘d’, ‘a’: ‘b’, ‘e’: ‘f’}

        >>> los = [ ‘ab’, ‘cd’, ‘ef’]
        >>> dict(los)
        {‘c’: ‘d’, ‘a’: ‘b’, ‘e’: ‘f’}

        >>> tos = (‘ab’, ‘cd’, ’ef’)
        >>> dict(tos)
        {‘c’: ‘d’, ‘a’: ‘b’, ‘e’: ‘f’}
      ```
    
    7. 멤버쉽 테스트 : in
      - 딕셔너리에 키가 있는지 테스트
        ```
          >>> pythons = {‘Chapman’: ‘Graham’, ‘Cleese’: ‘John’, ’Johns’: ‘Terry’, ‘Palin’: ‘Michael’}
          >>> ‘Chapman’ in pythons
          True
          >>> ’Palin’ in pythons
          True
          >>> ‘Michael’ in pythons
          False
        ```
    
    8. 모든 키 가져오기 : key()
      ```
        >>> signals = {‘green’: ‘go’, ‘yellow’: ‘go faster’, ‘red’: ‘stop’}
        >>> signals.keys()
        dict_keys(['green', 'yellow', 'red'])
      ```
    
    9. 모든 값 가져오기 : values()
      ```
        >>> signals.values()
        dict_values(['go', 'go faster', 'stop'])
      ```
    
    10. 모든 키-값 쌍 가져오기 : items()
      ```
        >>> signals.items()
        dict_items([('green', 'go'), ('yellow', 'go faster'), ('red', 'stop')])
      ```
  - 여러 시퀀스 순회하기 : zip()
    1. zip() 함수를 사용하여 여러 시퀀스 병렬로 순회하기
      - 여러 시퀀스 중 가장 짧은 시퀀스가 완료되면 zip()은 멈춘다.
        ```
          >>> days = [‘Monday’, ‘Tuesday’, ‘Wednesday’]
          >>> fruits = [‘banana’, ‘orange’, ‘peach’]
          >>> drinks = [‘coffee’, ‘tea’, ‘beer’]
          >>> desserts = [‘tiramisu’, ‘ice cream’, ‘pie’, ‘pudding’]
          >>> for day, fruit, drink, dessert in zip(days, fruits, drinks, desserts):
          ... print(day, “: drink”, drink, “- eat”, fruit, “- enjoy”, dessert)
          ...
          Monday : drink coffee – eat banana – enjoy tiramisu
          Tuesday : drink tea – eat orange – enjoy ice cream
          Wednesday : drink beer – eat peach – enjoy pie
        ```

        ```
          >>> engilsh = ‘Monday’, ‘Tuesday’, ‘Wednesday’
          >>> french = ‘Lundi’, ‘Mardi’, ‘Mercredi’
          >>>
          >>> list(zip(english, french))
          [(‘Monday’, ‘Lundi’), (‘Tuesday’, ‘Mardi’), (‘Wednesday’, ‘Mercredi’)]
          >>> dict(zip(english, french))
          {‘Monday’: ‘Lundi’, ‘Tuesday’: ‘Mardi’, ‘Wednesday’: ‘Mercredi’}
        ```

  - 숫자 시퀀스 생성하기 : range()
    1. 리스트나 튜플을 사용하여 저장하지 않더라도 특정 범위의 숫자 시퀀스를 생성한다.
      - 컴퓨터 메모리를 전부 사용하지 않고 아주 큰 범위를 생성할 수 있게 해줌
      - range(start, stop, step)
        ```
          >>> for x in range(0,3): 
          ... print(x) 
          ... 
          0 
          1 
          2 
          >>> list[range(0,3)] 
          [0, 1, 2]
        ```
    2. zip(), range() 와 같은 함수는 순회 가능한 (iterable) 객체를 반환한다.
      - for .. in 형태로 값을 순회할 수 있다.
      - 객체를 리스트와 같은 시퀀스로 변환할 수 있다.
        ```
          >>> for x in range(2, -1, -1):
          ... print(x)

          >>> for x in range(0, 11, 2):
          ... print(x)

          >>> list(range(2000, 2016, 2)
        ```
  
  - setdefault() 함수
    1. 딕셔너리에 값을 추가하려고 할 때 해당 키가 없으면 추가하는 코드
      ```
        spam = {'name': 'Pooka', 'age': 5}
        if 'color' not in spam:
            spam['color'] = 'black'
      ```
    
    2. setdefault() 는 해당 키가 없으면 추가
      ```
        >>> spam = {'name': 'Pooka', 'age': 5}
        >>> spam.setdefault('color', 'black')
        'black'

        >>> spam
        {'color': 'black', 'age': 5, 'name': 'Pooka'}

        >>> spam.setdefault('color', 'white')
        'black'

        >>> spam
        {'color': 'black', 'age': 5, 'name': 'Pooka'}
      ```
    
    3. Exercise : 문장 속에 나타나는 문자 갯수를 카운팅해서 딕셔너리 형태로 표현
      ```
        문장 : message = 'It was a bright cold day in April, and the clocks were striking thirteen.’

        결과 :
        {' ': 13, ',': 1, '.': 1, 'A': 1, 'I': 1, 'a': 4, 'c': 3, 'b': 1, 'e': 5, 'd': 3, 'g': 2, 'i': 6, 'h': 3, 'k': 2, 'l': 3, 'o': 2, 'n': 4, 'p': 1, 's': 3, 'r': 5, 't': 6, 'w': 2, 'y': 1}
      ```
  
  ## Coding Convention
  - 사람의 이해를 돕기 위한 규칙이 필요함
  - 그 규칙을 코딩 컨벤션 ( Coding Convention ) 이라고 함

  - 파이썬 Coding Convention ( https://spoqa.github.io/2012/08/03/about-python-coding-convention.html )
    1. 명확한 규칙은 없음
    2. 때로는 팀마다, 프로젝트 마다 따로
    3. 중요한 건 일관성 지키는 것임
    4. 읽기 좋은 코드가 좋은 코드
  
  - 파이썬 코딩 컨벤션의 예시
    1. 들여쓰기는 Tab or 4 Space 논쟁!
    2. 일반적으로 4 Space를 권장함
    3. 중요한 건 혼합하지 않으면 된다.
  
  - PEP8 – 파이썬 Coding Convention의 기준 ( https://www.python.org/dev/peps/pep-0008/ )
    1. PEP ( Python Enhance Proposal )
    2. 파이썬 코드 개선을 위한 제안서이며 코딩 기준을 제시함
    3. PEP8 파이썬 코딩 컨벤션에서 제시하는 기준들
      ```
        : 들여쓰기 공백 4칸을 권장
        : 한 줄은 최대 79자 까지
        : 불필요한 공백은 피함
        : = 연산자는 1칸 이상 띄우지 않음
        : 주석은 항상 갱신, 불필요한 주석은 삭제함.
        : 소문자 l(엘), 대문자 O, 대문자 I (아이) 금지
        : 함수명은 소문자로 구성하고, 두 단어는 밑줄로 연결함
      ```
  
  - PEP8 – 파이썬 Coding Convention의 기준
    1. “flake8” 모듈로 체크 : flake8 <파일명>
    2. pip install flake8

## 함수
- 함수란?
  * 어떤 일을 수행하는 코드의 덩어리
  * 코드를 논리적인 단위로 분리
  * 캡슐화 : 인터페이스만 알면 타인의 코드를 사용할 수 있다.

- 함수의 정의
  1. 함수 선언은 def 로 시작
  2. 함수의 시작과 끝은 들여쓰기(indentation)로 구분
  3. 시작과 끝을 명시하지 않음
  4. 함수 이름 뒤에 오는 ( ) 안에 함수로 전달하는 인자(파라미터)를 적음

- 함수 선언 문법
  * 함수이름, Parameter, Return Value(optional)
    ```
      def 함수 이름 (parmaeter #1 ....):
          수행문 #1(statements)
          수행문 #2(statements)
          return <반환값>
    ```

- Parameter vs Argument
  - Parameter : 함수의 입력 값 인터페이스
  - Argument : 실제 Parameter에 대입된 값

- 함수의 파라미터
  * 위치 파라미터
  * 키워드 파라미터
    ```
      def connect_URI(server, port):
          str = ‘http://’ + server + ‘:’ + port
          return str

      connect_URI(‘test.com’, ‘8080’)
      connect_URI(port=‘8080’, server=‘test.com’)

      connect_URI(‘test.com’, port=‘8080’)
      connect_URI(port=‘8080’, ‘test.com’)
    ```

- 기본 파라미터 값 지정
  1. 파라미터에 기본값을 지정할 수 있다.
  2. 함수를 호출할 때 파라미터를 제공하지 않으면 기본값을 사용한다.
    ```
      def times(a=10, b=20): 
          return a * b 

      x = times() 
      y = times(5) 
      
      print(x) 
      print(y)
    ```
  
- 함수 파라미터 : 가변 파라미터
- *p : tuple type parameter
- **p : dict type parameter

- 리턴 값 return
  1. 함수를 종료하고 해당 함수를 호출한 곳으로 돌아감
  2. 함수를 실행할 때 모든 함수 관련 리소스(변수 포함)를 스택에 저장 return 시 스택에서 제거
  3. 파이썬은 다중값을 리턴값 으로 전달 가능 (실제 튜플에 저장되어 리턴 됨)
  4. return 을 사용하지 않거나, return 만 적었을 때도 함수가 종료 (None 객체를 돌려줌)

- 함수 작성 가이드 라인
  1. 함수는 가능하면 짧게 작성할 것 (줄 수를 줄일 것)
  2. 함수 이름에 함수의 역할, 의도가 명확히 들어낼 것
    ```
      def print_hello_world():
          print("Hello, World")
      
      def get_hello_world():
          return "Hello, World"
    ```
  3. 하나의 함수에는 유사한 역할을 하는 코드만 포함
    ```
      def add_variables(x, y):
          return x + y
      
      def add_variables(x, y):
          print(x, y)
          return x + y
    ```
  4. 인자로 받은 값 자체를 바꾸진 말 것 (임시변수 선언)

- 함수는 언제 만드는가?
  1. 공통적으로 사용되는 코드는 함수로 변환
  2. 복잡한 수식 -> 식별 가능한 이름의 함수의 변환
  3. 복잡한 조건 -> 식별 가능한 이름의 함수로 변환

- 함수 – 변수의 범위
  - 변수의 범위 ( Scoping Rule )
    - 변수가 사용되는 범위
    - 지역변수( local variable) : 함수 내부에서만 사용
    - 전역변수(Global variable) : 프로그램 전체에서 사용, 함수 내부에서도 사용 가능, 하지만 함수 내에 전역변수와 같은 이름의 변수를 선언하면 새로운 지역변수가 생긴다.
    - 함수 내에서 전역변수 사용 시 global 키워드 사용

- Split 함수
  * String type의 값을 나눠서 List 형태로 변환
    ```
      >>> items = 'zero one two three'.split()'   # 빈칸을 기준으로 문자열 나누기
      >>> print(items)
        ['zero', 'one', 'two', 'three']
      >>> langs = 'python, java, javascript'
      >>> a,b,c = langs.split(",")    # ","를 기준으로 문자열 나누어 각 값을 a,b,c에 언패킹

      >>> url = 'mail.naver.com'
      >>> subdomain,domain,type = url.split(".")    # "."를 기준으로 문자열 나누기
    ```

- Join 함수
  * String List를 합쳐 하나의 String으로 반환할 때 사용
    ```
      >>> colors = ['red', 'blue', 'green', 'yellow']
      >>> result = ''.join(colors)
      >>> result
      'redbluegreenyellow'

      >>> result = ' '.join(colors)   # 연결 시 빈칸 1칸으로 연결
      >>> result
      'red blue green yellow'

      >>> result = ', '.join(colors)  # 연결 시 ", "으로 연결
      >>> result
      'red, blue, green, yellow'

      >>> result = "-".join(colors)   # 연결 시 "-"으로 연결
      >>> result
      'red-blue-green-yellow' 
    ```

- List Comprehensions
  1. 기존 List 사용하여 간단히 다른 List를 만드는 기법
  2. 포괄적인 List, 포함되는 리스트라는 의미로 사용됨
  3. 파이썬에서 가장 많이 사용되는 기법 중 하나
  4. 일반적으로 for + append 보다 속도가 빠름

- Enumerate
  * List의 element를 추출할 때 번호를 붙여서 추출

- Zip
  * 두 개의 list의 값을 병렬적으로 추출함

## 람다와 Map/Reduce
- 람다함수란?
  - 함수의 이름 없이 쓸 수 있는 익명함수
  - 수학의 람다 대수에서 유래함

  ``` 
    # 일반함수
    def f(x, y):
        return x + y
    
    print(f(1,4))

    # 람다함수
    f = lambda x, y: x + y

    print(f(1, 4))
  ```

- Map 함수
  1. Sequence 자료형 각 element에 동일한 function을 적용함
    - map(function_name, list_data)
  2. 두 개 이상의 list에도 적용 가능함, if filter도 사용가능
  3. python3 는 iteration을 생성 à list을 붙여줘야 list 사용가능
  4. 실행시점의 값을 생성, 메모리 효율적

- Reduce 함수
  1. map function과 달리 list에 똑같은 함수를 적용해서 통합

## 객체와 클래스
- Class Naming 규칙
  1. 변수와 Class 명 , function 명은 Naming을 작성하는 규칙이 존재함
  2. Snake_Case : 띄워 쓰기 부분에 “_” 를 추가한다. 뱀 처럼 늘여 쓰기, 파이썬 함수명 / 변수명에 사용함
  3. CamelCase : 띄워 쓰기 부분에 대문자 낙타의 등 모양, 파이썬 클래스명에 사용함

- Class 구현하기 in Python - Attribute
  1. Attribute 추가는 __init__, self 와 함께
  2. __init__ 은 객체 초기화 예약 함수 ( 즉, 생성자 )
  3. __는 특수한 예약 함수나 private 변수에 사용됨

- Class 구현하기 in Python - Function
  1. Function 추가는 기존의 함수와 같지만, 반드시 self 를 추가해야 class에 속한 함수로 인정됨

- 상속 ( Inheritance ) – Person 클래스
  1. 부모클래스로 부터 속성과 메서드를 상속 받은 자식 클래스를 생성하는 것
  2. 부모 클래스 : Person
  3. 자식 클래스 : Employee

- 다형성 ( Polymorphism ) ( https://goo.gl/lBy9uf )
  1. 메서드의 Signature는 동일하고, 내부 로직은 다르게 작성한다.
  2. Dynamic Typing 특성으로 인해 파이썬에서는 같은 부모 클래스의 상속에서 주로 발생함

- 캡슐화 ( Encapsulation, Visibility )
  1. 캡슐화 또는 정보 은닉 ( Information Hiding)
  2. 객체의 정보를 볼 수 있는 레벨을 조절하는 것
  3. 클래스를 설계할 때, 클래스 간 간섭 / 정보 공유의 최소화

## 모듈과 패키지 pip
- 모듈이란?
  1. 프로그램에서는 작은 프로그램 조각들, 모듈들을 모아서 하나의 큰 프로그램을 개발한다.
  2. 프로그램을 모듈화 시키면 다른 프로그램에서 사용하기 쉽다.
  3. 파이썬 모듈로 분리해서 프로그램 좀 더 구조화 할 수 있음
  4. 파이썬의 Module == py 파일을 의미한다.
  5. import 문을 사용해서 Module을 호출한다.

- 모듈을 import 하는 4 가지 방법
  1. 모듈명을 import 하기
    ```
      import fah_converter
      print(fah_converter.convert_c_to_f(41.6))
    ```
  2. 모듈명을 Alias 설정하기
    ```
      import fah_converter as fah
      print(fah.convert_c_to_f(41.6))
    ```
  3. 모듈에서 특정 함수 또는 클래스만 import 하기
    ```
      from fah_converter import convert_c_to_f
      print(convert_c_to_f(41.6))
    ```
  4. 모듈에서 모든 함수 또는 클래스를 import 하기
    ```
      from fah_converter import *
      print(convert_c_to_f(41.6))
    ```

- 빌트인 모듈 : 파이썬 설치 시 제공되는 내장 모듈
  ```
    >>> import sys
    >>> sys.path # 모듈이 설치된 경로를 확인할 수 있음
    >>> import random
    >>> print(random.randint(0,100) # 0~100 사이의 정수 난수를 발생시킴
  ```

- 써드파티 모듈 : 외부 모듈로써 별도로 설치가 필요함
  * 파이썬 커뮤니티에 의해 지금도 계속 개발되고 배포되고 있음

- 써드파티 모듈 설치 관리자 : pypi
  1. 파이썬 모듈 중앙 저장소
  2. https://pypi.python.org/pypi
  3. 비교해 보기 : 자바 Maven Repository, 자바스크립트 NPM(node pakage manager) 저장소

- pip 을 사용해 모듈 설치
  - requests 모듈은 파이썬에 내장되어 있지 않다. pip 을 사용해서 설치해야 한다.
    ```
      pip install 모듈명
    ```

- 패키지, package
  1. 모듈 : 함수와 클래스를 정리해서 파일로 분리시키는 방법
  2. 패키지 : 다양한 모듈들의 합, 폴더로 연결됨
    - __init__.py 파일이 디렉토리에 위치하면 파이썬은 패키지로 인식
    - 다양한 오픈 소스들이 모두 패키지로 관리됨

- Package 내에서 다른 폴더의 모듈을 부를 때 호출하는 방법
  1. 절대참조
    - from game.graphic.render import render_test
  2. 현재 디렉토리 기준
    - from .render import render_test
  3. 부모 디렉토리 기준
    - from ..sound.echo import echo_test

### 2.7 9일차(2022-01-27) 

## 예외처리와 로깅
- Exception 유형
  1. 예상 가능한 예외
    - 발생 여부를 사전에 인지할 수 있는 예외
    - 사용자의 잘못된 입력, 파일 호출 시에 파일 없음
    - 개발자가 반드시 명시적으로 정의해야 함
  2. 예상이 불가능한 예외
    - 인터프리터 과정에서 발생하는 예외, 개발자 실수
    - 리스트의 범위를 넘어 가는 값 호출, 정수 0으로 나눔
    - 수행 불가시 인터프리터가 자동 호출

- Exception Handling
  - 예외가 발생한 경우 후속 조치 등 대처 필요가 필요함

- 프로그램의 비정상 적인 종료를 막는 방법
  - 에러가 발생 할 가능성이 있는 코드를 사전에 처리해 주는 방법
  - 예) 파일을 다룰 때 파일이 없거나 쓰기 금지로 설정 된 경우
  - 데이터베이스 연결 시 DB쪽 이슈
  - 네트웍 관련 코드에서 네트웍 이슈

- try ~ except 를 이용한 에러로 부터의 복구
  ```
    try:
        예외 발생 가능 코드
    except <Exception Type>:
        예외 발생시 대응하는 코드
  ```

- Built-in Exception : 기본적으로 제공되는 예외. ( https://docs.python.org/3/library/exceptions.html )
  ```
    IndexError -> List의 Index 범위를 넘어갈 때
    NameError -> 존재하지 않은 변수를 호출 할 때
    ZeroDivisionError -> 0으로 숫자를 나눌 때
    ValueError -> 변환할 수 없는 문자 / 숫자를 변환할 때
    FileNotFoundError -> 존재하지 않는 파일을 호출할 때
  ```

  ```
    price = input("Enter the price: ")
    try:
        price = float(price)
        print('Price =', price)
    except ValueError:
        print('Not a number!')
  ```

  ```
    price = input("Enter the price: ")
    try:
        price = float(price)
        print('Price =', price)
    except ValueError as err:
        print(err)
  ```

- try ~ except ~ else 를 이용한 에러로 부터의 복구
  ```
    try:
        예외 발생 가능 코드
    except <Exception Type>:
        예외 발생시 대응하는 코드
    else:
        예외가 발생하지 않을 때 동작하는 코드
  ```

- try ~ except ~ finally 를 이용한 에러로 부터의 복구
  ```
    try:
        예외 발생 가능 코드
    except <Exception Type>:
        예외 발생시 대응하는 코드
    finally:
        예외 발생 여부와 상관없이 실행됨
  ```

- raise 구문 : 필요에 따라 강제로 Exception을 발생
  ```
    raise <Exception Type>(예외정보)
  ```

- 사용자 정의 예외 만들기
  - 새로운 예외 타입을 만들기 위해서는 class 객체 타입을 정의해야 한다.
    ```
      class BizException(Exception): 
          pass
    ```

- 예외 발생 : raise
  - 특정한 상황에서 예외를 발생 시킬 수 있다.
    - raise BizException
      ```
        try:
            raise BizException(‘error occurred’)
        except BizException as e:
            print(e)
      ```

- 로그 남기기 - Logging
  - 로그 메세지를 디스플레이 하고자 할 때 사용
    1. 프로그램이 실행되는 동안 일어나는 정보를 기록을 남기기
    2. 유저의 접근, 프로그램의 Exception, 특정 함수의 사용
    3. Console 화면에 출력, 파일에 남기기, DB에 남기기 등등
    4. 기록된 로그를 분석하여 의미 있는 결과를 도출 할 수 있음
    5. 실행시점에서 남겨야 하는 기록, 개발시점에서 남겨야 하는 기록
  
  - Print vs Logging
    1. 기록을 print로 남기는 것도 가능함
    2. 그러나 Console 창에만 남기는 기록은 분석 시 사용불가
    3. 때로는 레벨 별(개발, 운영)로 기록을 남길 필요도 있음
    4. 모듈별로 별도의 logging을 남길 필요도 있음
    5. 이러한 기능을 체계적으로 지원하는 모듈이 필요함

- Logging Level ( https://stackoverflow.com/questions/2031163/when-to-use-the-different-log-levels )
  1. 프로그램 진행 상황에 따라 다른 Level의 Log를 출력함
  2. 개발 시점, 운영 시점 마다 다른 Log가 남을 수 있도록 지원함
  3. DEBUG > INFO > WARNING > ERROR > Critical

- logging 모듈
  - 로그 메세지를 콘솔에 출력
    1. 코드 제일 위쪽에 로깅 설정 코드를 추가
      ```
        import logging

        logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
      ```
    2. 팩토리얼 코드 로깅 예제 (디버깅을 위해 print() 사용 권장하지 않음)
      ```
        import logging
        logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s') logging.debug('Start of program')

        def factorial(n):
            logging.debug('Start of factorial(%s)' % (n))
            total = 1
            for i in range(n + 1):
                total *= i
                logging.debug('i is ' + str(i) + ', total is ' + str(total))
            logging.debug('End of factorial(%s)' % (n))
            return total

        print(factorial(5))
        logging.debug('End of program')
      ```
  
  - 로그 메세지를 파일로 저장
    1. 로깅 설정 코드 부분을 수정
      ```
        import logging

        logging.basicConfig(filename='myProgramLog.txt', level=logging.DEBUG,
        format=' %(asctime)s - %(levelname)s - %(message)s')
      ```
    
    2. 팩토리얼 코드 로깅 예제
      ```
        import logging logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s') logging.debug('Start of program')

        def factorial(n): 
            logging.debug('Start of factorial(%s)' % (n)) 
            total = 1 
            for i in range(n + 1): 
              total *= i 
              logging.debug('i is ' + str(i) + ', total is ' + str(total)) 
            logging.debug('End of factorial(%s)' % (n)) 
            return total

        print(factorial(5)) 
        logging.debug('End of program')
      ```

## 파일 다루기
- 파일 읽기
  - 파일 처리를 위해 open 키워드를 사용함
    ```
      # 접근모드
      r -> 읽기모드 : 파일을 읽기만 할 때 사용
      w -> 쓰기모드 : 파일에 내용을 쓸 때 사용
      a -> 추가모드 : 파일의 마지막에 새로운 내용을 추가 시킬 때 사용
    ```

    ```
      f = open("<파일이름>", "접근모드")
      f.close()
    ```
  
  - open() / close() 로 파일 읽기
    ```
      f = open("i_have_a_dream.txt", "r")
      contents = f.read()
      print(contents)
      f.close()
    ```
  
  - with 구문으로 파일 읽기
    ```
      with open("i_have_a_dream.txt", "r") as my_file:
          content = my_file.read()
          print(type(contents), contents)
    ```
  
  - 한 줄씩 읽어 List Type으로 반환함
    ```
      with open("i_have_a_dream.txt", "r") as my_file:
          content_list = my_file.readlines()    # 파일 전체를 list로 반환
          print(type(content_list))   # Type 확인
          print(content_list)     # 리스트 값 출력
    ```
  
  - with 구문과 함께 사용하기
    ```
      with open("i_have_a_dream.txt", "r") as my_file:
          contents = my_file.read()
          print(type(contents), contents)
    ```

- 파일 쓰기
  - mode는 “w”, encoding=“utf8”
    ```
      f = open("count_log.txt", "w", encoding = "utf-8")
      for i in range(1, 11):
          data = "%d번째 줄입니다.\n" % i
          f.write(data)
      f.close()
    ```
  
  - mode는 “a”는 추가 모드
    ```
      with open("count_log.txt", "a", encoding = "utf-8") as f:
          for i in range(1, 11):
            data = "%d번째 줄입니다.\n" % i
            f.write(data)
    ```

- 디렉토리 생성
  - os 모듈을 사용하여 디렉토리 만들기
    ```
      import os
      os.mkdir("log")
    ```

  - 디렉토리가 있는지 확인하기
    ```
      if not os.path.isdir("log"):
          os.mkdir("log")
    ```

- 파일 – pickle
  - Pickle 이란?
    1. 파이썬의 객체를 영속화(pesistence) 하는 build-in 객체
    2. 데이터, object 등 실행 중 정보를 저장한 후에 불러와서 사용가능하다.
    3. 저장해야 하는 정보, 계산 결과 ( 모델 ) 등 활용이 많음

- 파일과 파일경로
  - 리눅스와 맥에서는 ( / )를 사용, 윈도우에서는 ( \ ) 사용
    ```
      >>> import os
      >>> os.path.join('usr', 'bin', 'spam')
      'usr\\bin\\spam’

      >>> myFiles = ['accounts.txt', 'details.csv', 'invite.docx']
      >>> for filename in myFiles:
              print(os.path.join('C:\\Users\\python', filename)) 
              
      C:\Users\python\accounts.txt
      C:\Users\python\details.csv
      C:\Users\python\invite.docx
    ```
  
  - 윈도우의 dir 과 리눅스의 ls 명령과 유사한
    - glob 모듈
    - glob.glob(‘*’) : 현재 디렉토리의 모든 파일을 리스트로 반환

- 디렉토리 관리
  - 현재 작업 디렉토리 : Current Working Directory
    1. os.getcwd() : 현재 작업디렉토리를 보여줌
    2. os.chdir() : 디렉토리 변경
      ```
        >>> import os
        >>> os.getcwd()
        'C:\\Python34'
        >>> os.chdir('C:\\Windows\\System32')
        >>> os.getcwd()
        'C:\\Windows\\System32'
      ```
  
  - Dir name 과 base name
    ```
      >>> path = 'C:\\Windows\\System32\\calc.exe' 
      >>> os.path.basename(path) 
      'calc.exe' 
      >>> os.path.dirname(path) 
      'C:\\Windows\\System32'
    ```

## XML과 JSON
- XML이란?
  - 정보의 구조에 대한 정보인 스키마와 DTD 등으로 정보에 대한 정보(메타정보)가 표현되며, 용도에 따라 다양한 형태로 변경가능
  - XML은 컴퓨터(예: PC <-> 스마트폰)간에 정보를 주고받기 매우 유용한 저장 방식으로 쓰이고 있음

- XML Parsing in Python
  - XML도 HTML과 같이 구조적 MarkUp 언어
  - 정규표현식으로 Parsing이 가능함
  - 그러나 좀 더 손쉬운 도구들이 개발되어 있음
  - 가장 많이 쓰이는 parser인 beautifulsoup으로 파싱

- BeautifulSoup
  - HTML, XML 등 Markup 언어 Scraping을 위한 대표적인 도구
  - https://www.crummy.com/software/BeautifulSoup/
  - lxml 과 html5lib 과 같은 Parser를 사용함
  - 속도는 상대적으로 느리나 간편히 사용할 수 있음

- BeautifulSoup 설치
  - pip install lxml
  - pip install beautifulsoup4

- BeautifulSoup 모듈 사용
  - 모듈 호출
    - from bs4 import BeautifulSoup
  
  - 객체 생성
    - soup = BeautifulSoup(books_xml, "lxml")
  
  - Tag 찾는 함수 find_all 생성
    - soup.find_all("author")
  
  - find_all : 정규식과 마찬가지로 해당 패턴을 모두 반환
  - find('invention-title')
  - get_text() : 반환된 패턴의 값 반환 (태그와 태그 사이)
    - <tag>값<tag>

- JSON
  - JavaScript Object Notation
  - 원래 웹 언어인 Java Script의 데이터 객체 표현 방식
  - 간결성으로 기계 / 인간이 모두 이해하기 편함
  - 데이터 용량이 적고, Code로의 전환이 쉬움
  - 이로 인해 XML의 대체제로 많이 활용되고 있음

- JSON in 파이썬
  - JSON 모듈을 사용하여 손 쉽게 파싱 및 저장 가능
  - 데이터 저장 및 읽기는 dict type과 상호 호환 가능
  - 웹에서 제공하는 API는 대부분 정보 교환 시 JSON 활용
  - 페이스북, 트위터, Github 등 거의 모든 사이트
  - 각 사이트 마다 Developer API의 활용법을 찾아 사용

### 2.8 10일차(2022-01-28)

## RDBMS(Relational Database Management System) 이해

  1. 데이터베이스란?
  
    - 체계화된 데이터의 모임
    - 여러 응용 시스템들의 통합된 정보를 저장하여 , 운영할 수 있는 공용 데이터의 묶음
    - 논리적으로 연관된 하나 이상의 자료 모음으로 , 데이터를 고도로 구조화함으로써 검색 갱신등의 데이터 관리를 효율화함
    - DBMS: 데이터베이스를 관리하는 시스템

    - 데이터베이스 장점
      1. 데이터 중복 최소화
      2. 데이터 공유
      3. 일관성 , 무결성 , 보안성 유지
      4. 최신의 데이터 유지
      5. 데이터의 표준화 가능
      6. 데이터의 논리적 , 물리적 독립성
      7. 용이한 데이터 접근
      8. 데이터 저장 공간 절약
    
    - 데이터베이스 단점
      1. 데이터베이스 전문가 필요
      2. 많은 비용 부담
      3. 시스템의 복잡함

  2. RDBMS(Relational Database Management System, 관계형 데이터베이스 관리 시스템)

    1. 데이터베이스의 한 종류로, 가장 많이 사용됨
    2. 역사가 오래되어, 가장 신뢰성이 높고, 데이터 분류, 정렬, 탐색 속도가 빠름
    3. 관계형 데이터베이스 = 테이블!
    4. 2차원 테이블(Table) 형식을 이용하여 데이터를 정의하고 설명하는 데이터 모델
    5. 관계형 데이터베이스에서는 데이터를 속성(Attribute)과 데이터 값(Attribute Value)으로 구조화(2차원 Table 형태로 만들어짐)
    6. 데이터를 구조화한다는 것은 속성(Attribute)과 데이터 값(Attribute Value) 사이에서 관계(Relation)을 찾아내고 이를 테이블 모양의 구조로 도식화함의 의미함

    - Primary Key and Foreign Key
      1. Primary Key(기본키): Primary Key는 한 테이블(Table)의 각 로우(Row)를 유일하게 식별해주는 컬럼(Column)으로, 각 테이블마다 Primary Key가 존재해야 하며, NULL 값을 허용하지 않고, 각 로우(Row)마다 유일한 값이어야 한다.
      2. Foreign Key(외래키 또는 외부키): Foreign Key는 한 테이블의 필드(Attribute) 중 다른 테이블의 행(Row)을 식별 할 수 있는 키
  
  3. 데이터베이스 스키마(Schema)
    - 데이터베이스의 테이블 구조 및 형식, 관계 등의 정보를 형식 언어(formal language)로 기술한 것

    1. 관계형 데이터베이스를 사용하여 데이터를 저장할 때 가장 먼저 할 일은 데이터의 공통 속성을 식별하여 컬럼(Column)으로 정의하고, 테이블(Table)을 만드는 것
    2. 통상적으로 하나의 테이블이 아닌 여러 개의 테이블로 만들고, 각 테이블 구조, 형식, 관계를 정의함
    3. 이를 스키마라고 하며, 일종의 데이터베이스 설계도로 이해하면 됨
    4. 데이터베이스마다 스키마를 만드는 언어가 존재하며, 해당 스키마만 있으면 동일한 구조의 데이터베이스를 만들 수 있음 (데이터베이스 백업과는 달리 데이터 구조만 동일하게 만들 수 있음)

  4. SQL(Structured Query Language)
    - 관계형 데이터베이스 관리 시스템에서 데이터를 관리하기 위해 사용되는 표준 프로그래밍 언어
    - 데이터베이스 스키마 생성 및 수정 , 테이블 관리 , 데이터 추가 , 수정 , 삭제 , 조회 등 데이터베이스와 관련된 거의 모든 작업을 위해 사용되는 언어
    - 데이터베이스마다 문법에 약간의 차이가 있지만 , 표준 SQL 을 기본으로 하므로 , 관계형 데이터베이스를 다루기 위해서는 필수적으로 알아야 함
    - SQL 은 크게 세 가지 종류로 나뉨
      1. 데이터 정의 언어 (DDL, Data Definition Language)
      2. 데이터 처리 언어 (DML, Data Manipulation Language)
      3. 데이터 제어 언어 (DCL, Data Control Language)
    
  5. 데이터 정의 언어 (DDL, Data Definition Language): 데이터 구조 정의
    - 테이블 (TABLE), 인덱스 (INDEX) 등의 개체를 만들고 관리하는데 사용되는 명령
    - CREATE, ALTER, DROP 등이 있음
  
  6. 데이터 조작 언어 (DML, Data Manipulation Language): 데이터 CRUD [Create(생성), Read(읽기), Update(갱신), Delete(삭제)]
    - INSERT 테이블 (Table) 에 하나 이상의 데이터 추가
    - UPDATE 테이블 (Table) 에 저장된 하나 이상의 데이터 수정
    - DELETE 테이블 (Table) 의 데이터 삭제
    - SELECT 테이블 (Table) 에 저장된 데이터 조회
  
  7. 데이터 제어 언어 (DCL, Data Control Language): 데이터 핸들링 권한 설정 , 데이터 무결성 처리 등 수행
    - GRANT 데이터베이스 개체 (테이블 , 인덱스 등) 에 대한 사용 권한 설정
    - BEGIN 트랜잭션 (Transaction) 시작
    - COMMIT 트랜잭션 (Transaction) 내의 실행 결과 적용
    - ROLLBACK 트랜잭션 (Transaction) 의 실행 취소
    ```
      # 실습 일반 사용자 계정 생성하기

      C:\> mysql –u root –p 
      MariaDB [(none)]> show databases; 
      MariaDB [mysql]> use mysql 
      MariaDB [mysql]> create user python@localhost identified by 'python'; 
      MariaDB [mysql]> grant all on *.* to spring@localhost; MariaDB [mysql]> flush privileges; 
      MariaDB [mysql]> exit;
    ```

## SQL DDL(Data Definition Language) 이해 및 실습
  1. 데이터베이스
    - 데이터베이스 안에는 여러 개의 데이터베이스 이름이 존재한다.
    - 각 데이터베이스 이름 안에는 여러 개의 테이블이 존 재한다.
      ```
        # 실습 데이터베이스 생성 , 목록 보기 , 사용

          C:\> mysql –u python –p 
        1. 데이터베이스 생성
          CREATE DATABASE 데이터베이스명; 
        2. 데이터베이스 목록 보기
          SHOW DATABASES; 
        3. 데이터베이스 사용 시
          USE 데이터베이스명;
        4. 데이터베이스 삭제
          DROP DATABASE [IF EXISTS] 데이터베이스명;
      ```
  
  2. 테이블
    1. 테이블 생성
      ```
        CREATE TABLE 테이블명 (
          컬럼명 데이터형,
          컬럼명 데이터형,
          ...
          Primary key 가 될 필드 지정
        )
      ```
    
    2. 숫자 타입의 컬럼 정의 문법
      ```
        CREATE TABLE minu_table(
          id INT [UNSIGNED] [NOT NULL] [AUTO_INCREMENT]
        );
      ```
      - id : 컬럼명 - 가능한 영어 소문자 중심으로 명명
      - INT : 컬럼에 대한 데이터 타입 선언
      - [UNSIGNED] : 옵션 사항 (0 ~ 255)
      - [NOT NULL] : NOT NULL 명시하면 데이터 입력시, 해당 컬럼 데이터에 값이 할당되지 않는 경우를 허락하지 않겠다는 의미
      - [AUTO_INCREMENT] : AUTO_INCREMENT 명시하면, 해당 테이블에 데이터 등록시 해당 컬럼은 자동으로 숫자가 1씩 증가하며 저장됨

      * 숫자형 데이터 타입
        데이터 유형|정의|
        |------|---|
        |TINYINT|정수형 데이터 타입(1byte) -128 ~ +128 또는 0 ~ 255 수 표현 가능|
        |SMALLINT|정수형 데이터 타입(2byte) -32768 ~ +32767 또는 0 ~ 65536 수 표현 가능|
        |MEDIUMINT|정수형 데이터 타입(3byte) -8388608 ~ +8388607 또는 0 ~ 16777215 수 표현 가능|
        |INT|정수형 데이터 타입(4byte) -2147483648 ~ +2147483647 또는 0 ~ 4294967295 수 표현 가능|
        |BIGINT|정수형 데이터 타입(8byte) 무제한 수 표현 가능|
        |FLOAT(정수부 길이, 소수부 자릿수)|부동 소수형 데이터 타입(4byte)|
        |DECIMAL(정수부 길이, 소수부 자릿수)|고정 소수형 데이터 타입고정(길이 + 1byte)|
        |DOUBLE(정수부 길이, 소수부 자릿수)|부동 소수형 데이터 타입(8byte)|
    
    3. 문자 타입의 컬럼 정의 문법
      ```
        CREATE TABLE minu_table(
          name VARCHAR(50),
          ....
        );
      ```
      - name : 컬럼명, 가능한 영어 소문자 중심으로 명명
      - VARCHAR(n) : 컬럼에 대한 문자형 데이터 타입 선언

      - 문자형 데이터 타입
        1. CHAR(n) : 고정 길이 데이터 타입, 정확히 (n <= 255)
        2. VARCHAR(n) : 가변 길이 데이터 타입 (n <= 65535)
        3. TINYTEXT(n) : 문자열 데이터 (n <= 255)
        4. TEXT(n) : 문자열 데이터(n <= 65535)
        5. MEDIUMTEXT(n) : 문자열 데이터(n <= 16777215)
        6. LONGTEXT(n) : 문자열 데이터(n <= 4294967295)

    4. 시간 타입의 컬럼 정의 문법
      ```
        CREATE TABLE minu_table(
          ts DATE,
          ....
        );
      ```
      - ts : 컬럼명, 가능한 영어 소문자 중심으로 명명
      - DATE : 컬럼에 대한 시간 타입 선언

      - 시간형 데이터 타입
        1. DATE : 날짜(YYYY-MM-DD) 형태의 기간 표현 데이터 타입(3byte)
        2. TIME : 시간(hh:mm:ss) 형태의 기간 표현 데이터 타입 (3byte)
        3. DATETIME : 날짜와 시간(YYYY-MM-DD hh:mm:ss) 형태 '1001-01-01 00:00:00' 부터 '9999-12-31 23:59:59' 까지의 값 표현
        4. TIMESTAMP : 1970-01-01 00:00:00 이후부터 시스템 현재 시간까지의 지난 시간을 초로 환산하여 숫자로 표현
        5. YEAR(n)과 같은 형식으로 사용
          - n은 2와 4 지정 가능
          - 2인 경우는 70 에서 69 까지
          - 4인 경우는 1970 에서 2069 까지 표시
    
    5. Primary Key 가 될 필드 지정 문법
      ```
        CREATE TABLE minu_table(
          컬럼명 데이터형,
          ....
          PRIMARY KEY(컬럼명1, 컬럼명2, .....)
        );
      ```
      - 컬럼명1, 컬럼명2, .... : PRIMARY KEY 로 지정할 컬럼명을 넣음 (한 개 이상을 지정할 수 있음, 보통은 한 개를 지정함) PRIMARY KEY 로 지정할 컬럼은 NULL 값을 등록할 수 없어야 하고, 컬럼 안에서 같은 값이 없도록 각 값이 유일해야 함 따라서, 해당 컬럼은 보통 NOT NULL(NULL 값 방지) AUTO_INCREMENT(유일함) 선언이 되어 있는 경우가 많음

        ```
          CREATE TABLE mytable(
            id INT UNSIGNED NOT NULL AUTO_INCREMENT,
            name VARCHAR(50) NOT NULL,
            modelnumber VARCHAR(15) NOT NULL,
            series VARCHAR(30) NOT NULL,
            PRIMARY KEY(id)
          );
        ```

        ```
          # 실습 테이블 생성 , 조회
            C:\> mysql –u python –p 
            MariaDB [(none)]> SHOW DATABASES; 
            MariaDB [(python_db)]> USE python_db; 
            MariaDB [(python_db)]> CREATE TABLE mytable ( 
              id INT UNSIGNED NOT NULL AUTO_INCREMENT, 
              name VARCHAR(50) NOT NULL, 
              modelnumber VARCHAR(15) NOT NULL, 
              series VARCHAR(30) NOT NULL, 
              PRIMARY KEY(id) 
              ); 
              MariaDB [(python_db)]> SHOW TABLES; 
              MariaDB [(python_db)]> desc mytable;
        ```

    6. 테이블 삭제
      - 기본 문법
        ```
          DROP TABLE [IF EXISTS] 테이블명;

          # IF EXISTS 옵션은 해당 데이터베이스 이름이 없더라도 오류를 발생시키지 말라는 의미
        ```

    7. 테이블 구조 수정
      - 테이블에 새로운 컬럼 추가
        ```
          ALTER TABLE [테이블명] ADD COLUMN [추가할 컬럼명][추가할 컬럼 데이터형]
          
          ALTER TABLE mytable ADD COLUMN model_type varchar(10) NOT NULL;
        ```
      
      - 테이블 컬럼 타입 변경
        ```
          ALTER TABLE [테이블명] MODIFY COLUMN [변경할 컬럼명][변경할 컬럼 타입]
          
          ALTER TABLE mytable MODIFY COLUMN model_type varchar(20) NOT NULL;
        ```
      
      - 테이블 컬럼 이름 변경
        ```
          ALTER TABLE [테이블명] CHANGE COLUMN [기존 컬럼명][변경할 컬럼명][변경할 컬럼 타입]
          
          ALTER TABLE mytable CHANGE COLUMN model_type rename_type varchar(20) NOT NULL;
        ```
      
      - 테이블 컬럼 삭제
        ```
          ALTER TABLE [테이블명] DROP COLUMN [삭제할 컬럼명]
          
          ALTER TABLE mytable DROP COLUMN model_type;
        ```
  
## SQL DML(Data Manipulation Language) 이해 및 실습 (focusing on CRUD)
  1. 4.1. CRUD [Create(생성), Read(읽기), Update(갱신), Delete(삭제)
    - 데이터 관리는 결국 데이터 생성 , 읽기(검색), 수정(갱신), 삭제를 한다는 의미
  
  2. 데이터 생성
    - 테이블에 컬럼에 맞추어 데이터를 넣는 작업
    - 기본 문법 (INSERT)
      1. 테이블 전체 컬럼에 대응하는 값을 모두 넣기
        ```
          INSERT INTO 테이블명 VALUES(값1, 값2, ...);
        ```
      2. 테이블 특정 컬럼에 대응하는 값만 넣기 (지정되지 않은 컬럼은 디폴트값 또는 NULL값이 들어감)
        ```
          INSERT INTO 테이블명(col1, col2, ...) VALUES(값1, 값2, ...);
        ```
      
      ```
        # 실습 - 데이터 생성

        MariaDB [(python_db)]> INSERT INTO mytable VALUES(1, 'i7', '7700', 'Kaby Lake'); 
        MariaDB [(python_db)]> INSERT INTO mytable (name, model_num, model_type) VALUES('i7', '7500', 'Kaby Lake'); 
        MariaDB [(python_db)]> INSERT INTO mytable VALUES('i7', 'G4600', 'Kaby Lake'); 
        MariaDB [(python_db)]> INSERT INTO mytable VALUES('i7', '7600', 'Kaby Lake');
      ```
  
  3. 데이터 읽기
    - 테이블에 저장된 데이터를 읽는 작업
    - 기본 문법 (SELECT)
      1. 테이블 전체 컬럼의 데이터 모두 읽기
        ```
          SELECT * FROM 테이블명;
        ```
      2. 테이블 특정 컬럼의 데이터만 읽기
        ```
          SELECT 컬럼1, 컬럼2, ... FROM 테이블명;
        ```
      3. 테이블 특정 컬럼의 데이터를 검색하되, 표시할 컬럼명도 다르게 하기
        ```
          SELECT 컬럼1 AS 바꿀컬럼이름, 컬럼2 AS 바꿀컬럼이름 FROM 테이블명;
        ```
      4. 데이터 정렬해서 읽기
        - ORDER BY 정렬할 기준 컬럼명 DESC / ASC
        - DESC는 내림차순 ASC 오름차순
          ```
            SELECT * FROM 테이블명 ORDER BY 정렬할 기준 컬럼명 DESC; 
          ```

          ```
            SELECT 컬럼1, 컬럼2 FROM 테이블명 ORDER BY 정렬할기준컬럼명 ASC;
          ```
      5. 조건에 맞는 데이터만 검색하기 (비교)
        - WHERE 조건문으로 조건 검색
        - 예) WHERE 컬럼명 < 값
        - 예) WHERE 컬럼명 > 값
        - 예) WHERE 컬럼명 = 값
          ```
            SELECT * FROM 테이블명 WHERE 필드명 = '값'
          ```
      6. 조건에 맞는 데이터만 검색하기 (논리 연산자)
        - WHERE 조건문으로 조건 검색
        - 논리 연산자 활용
        - 예) WHERE 컬럼명 < 값 OR 컬럼명 > 값
        - 예) WHERE 컬럼명 > 값 AND 컬럼명 < 값
          ```
            SELECT * FROM 테이블명 WHERE (필드명='값') OR (필드명 = '값');
          ```

          ```
            SELECT * FROM 테이블명 WHERE (필드명='값') AND (필드명 = '값');
          ```
      7. 조건에 맞는 데이터만 검색하기 (LIKE 를 활용한 부분 일치)
        - WHERE 조건문으로 조건 검색
        - LIKE 활용
        - 예) 홍으로 시작되는 값을 모두 찾을 경우
          ```
            SELECT * FROM 테이블명 WHERE 필드명 LIKE '홍%';
          ```
        - 예) 홍이 들어간 값을 모두 찾을 경우
          ```
            SELECT * FROM 테이블명 WHERE 필드명 LIKE '%홍%';
          ```
        - 예) 홍으로 시작되고 뒤에 2글자가 붙을 경우
          ```
            SELECT * FROM 테이블명 WHERE 필드명 LIKE '홍__';
          ```
      8. 결과 중 일부만 데이터 가져오기 (LIMIT 을 활용)
        - LIMIT 활용
        - 예) 결과중 처음부터 10개만 가져오기
          ```
            SELECT * FROM 필드명 LIMIT 10;
          ```
        - 예) 결과중 100번째 부터, 10개만 가져오기
          ```
            SELECT * FROM 필드명 LIMIT 100, 10;
          ```
      9. 조건 조합
        - 위에서 나열한 조건을 조합해서 다양한 Query를 작성할 수 있음
        - 조합 순서 SELECT FROM WHERE ORDER BY LIMIT
          ```
            SELECT id, name FROM mytable
            WHERE id < 4 AND name LIKE '%i%'
            ORDER BY name DESC
            LIMIT 2;
          ```

        ```
          # 실습 - 데이터 조회
          SELECT * FROM mytable WHERE model_num LIKE '7700%' SELECT * FROM mytable WHERE name LIKE '%i7%' 
          SELECT * FROM mytable WHERE model_type LIKE '%Kaby Lake%' LIMIT 1
        ```
    
    4. 데이터 수정
      - 테이블에 저장된 데이터를 수정하는 작업
      - 기본 문법(UPDATE)
        1. 보통 WHERE 조건문과 함께 쓰여서, 특정한 조건에 맞는 데이터만 수정하는 경우가 많음
          ```
            UPDATE 테이블명 SET 수정하고 싶은 컬럼명 = '수정하고 싶은 값' WHERE 특정 컬럼 = '값';
          ```
        2. 다수의 컬럼 값을 수정할 수도 있음
          ```
            UPDATE 테이블명 SET 수정하고 싶은 컬럼명1 = '수정하고 싶은 값', 수정하고 싶은 컬럼명2 = '수정하고 싶은 값', 수정하고 싶은 컬럼명3 = '수정하고 싶은 값'
            WHERE 특정 컬럼 < '값';
          ```
    
    5. 데이터 삭제
      - 테이블에 저장된 데이터를 삭제하는 작업
      - 기본 문법(DELETE)
        1. 보통 WHERE 조건문과 함께 쓰여서, 특정한 조건에 맞는 데이터만 삭제하는 경우가 많음
          ```
            DELETE FROM 테이블명 WHERE 특정 컬럼 = '값'
          ```
        2. 테이블에 저장된 모든 데이터를 삭제할 수도 있음
          ```
            DELETE FROM 테이블명;
          ```


