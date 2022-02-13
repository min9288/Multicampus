## Multicampus

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

#### RDBMS(Relational Database Management System) 이해

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

#### SQL DDL(Data Definition Language) 이해 및 실습
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
  
#### SQL DML(Data Manipulation Language) 이해 및 실습 (focusing on CRUD)
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

#### SQL DCL(Data Control Language) 이해 및 실습
  1. mysql 사용자 확인 , 추가 , 비밀번호 변경 , 삭제
    1. mysql 사용자 확인
      ```
        # mysql -u root -p
        use mysql;
        selelct + from user;
      ```
    2. 사용자 추가
      ```
        # mysql -u root -p
        use mysql;
      ```
      - 로컬에서만 접속 가능한 userid 생성
        ```
          create user 'userid' @localhost identified by '비밀번호';
        ```
      - 모든 호스트에서 접속 가능한 userid 생성
        ```
          create user 'userid'@'%' identified by '비밀번호';
        ```
    3. 사용자 비밀번호 변경
      ```
        SET PASSWORD FOR 'userid'@'%' = '신규비밀번호';
      ```  
    4. 사용자 삭제
      ```
        # mysql -u root -p
        use mysql;
        drop user 'userid'@'%';
      ```
    
  2. mysql 접속 허용 관련 설정
    - 로컬에서만 접속 허용
      ```
        GRANT ALL ON DATABASE.TABLE to 'root'@localhost identified by '비밀번호';
      ```
    - 특정 호스트에만 접속 허용
      ```
        GRANT ALL ON DATABASE.TABLE to 'root'@www.blim.co.kr identified by '비밀번호';
      ```
    - 모든 호스트에만 접속 허용
      ```
        GRANT ALL ON DATABASE.TABLE to 'root'@'%' identified by '비밀번호';
      ```
    - 옵션 상세
      1. ALL - 모든 권한 / SELECT, UPDATE - 조회, 수정 권한 등으로 권한 제한 가능
      2. DATABASE.TABLE - 특정 데이터베이스에 특정 테이블에만 권한을 줄 수 있음 / *.* - 모든 데이터베이스에 모든 테이블 권한을 가짐

#### SubQuery
  - 쿼리안의 또 다른 쿼리 - subquery
    1. SELECT col1, (SELECT....) - 스칼라 서브쿼리(Scalar Sub Query) : 하나의 컬럼처럼 사용 (표현 용도)
    2. FROM(SELECT...) - 인라인 뷰(Inline View) : 하나의 테이블처럼 사용 (테이블 대체 용도)
    3. WHERE col = (SELECT...) - 일반 서브쿼리 : 하나의 변수(상수)처럼 사용 (서브쿼리의 결과에 따라 달라지는 조건절)
  
  1. Inline View
    - 인라인 뷰는 SELECT 절의 결과를 FROM 절에서 하나의 테이블처럼 사용하고 싶을 때 사용합니다.
  
  2. Sub Query(일반 서브쿼리)
    - 일반 서브쿼리는 SELECT 절의 결과를 WHERE 절에서 하나의 변수(상수)처럼 사용하고 싶을 때 사용합니다.
    - 일반 서브쿼리는 WHERE 절에 사용하는 만큼, 조건에 필요한 단일 행 서브쿼리 / 다중 행 서브쿼리와 함께 사용됩니다.

#### 데이터수집과 분석 with Python

- 웹 스크래핑 : 파이썬으로 데이터 수집/처리 에서의 위치
  1. 데이터 수집
    - 오픈 API
    - 웹 스크래핑
  2. 데이터 가공
    - 데이터 랭글링 (Data Wrangling)
    - 데이터 클리닝
    - 데이터 분석이나 머신러닝(딥러닝)을 위한 전처리
  3. 데이터 분석
    - 통계적 분석
    - 머신러닝 (딥러닝)
  4. 데이터 저장
    - 관계형 / NoSQL 데이터베이스
    - 엑셀파일, CSV/TSV, JSON, YAML
  5. 커뮤니케이션
    - 이메일, 메신저, slack
    - 데이터 시각화

- 개발환경 구성
  1. Anaconda (https://www.continuum.io/anaconda-overview)
    - 대용량 데이터 처리, 예측 분석, 과학 계산용 파이썬 배포판입니다. Anaconda아나콘다는 NumPy, SciPy, matplotlib, pandas, IPython, Jupyter Notebook, 그리고 scikit-learn을 모두 포함합니다.
    - macOS, 윈도우, 리눅스를 모두 지원하며 매우 편리한 기능을 제공하므로 파이썬 과학 패키지가 없는 사람에게 추천하는 배포판 입니다.
  
  2. Miniconda 설치 – http://conda.pydata.org/miniconda.html
    - Anaconda는 데이터 분석을 위한 오픈 소스 Python 플랫폼입니다. 단 한 번의 설치로 모든 환경 설정을 한 번에 끝내주기 때문에 사용하기에 아주 좋습니다.
    - 한편 miniconda는 Anaconda의 핵심 부분만을 추출해서 재구성한 플랫폼으로, 고유한 패키지 관리 시스템인 conda와 기본적인 Python만을 포함하고 있기 때문에 설치 소요 시간이 더 짧습니다.
  
  3. Conda 버전 업데이트 : conda update conda
  4. Python 버전 확인 : python --version
  5. Ipython 설치 : pip install ipython
  6. Jupyter Notebook 설치 : pip install jupyter
  7. Jupyter Notebook 실행방법 : jupyter notebook
    - Jupyter Notebook이 실행되면 http://localhost:8888에서 실행됨, 웹 브라우저를 실행하여 해당 URL로 접속하면, Jupyter Notebook의 GUI 화면을 확인, 상단의 New 버튼을 클릭, 맨 하단의 Python 3 메뉴를 클릭하면, 새로운 notebook을 생성하고 편집이 가능하다.

- Jupyter notebook
  1. IPython 에서 최근 Jupyter 로 이름이 변경
  2. 기본 파이썬 쉘(REPL) 에 몇 가지 강력한 기능을 추가한 것
  3. 데이터 분석 할 때 주로 많이 사용됨
  4. 노트 형식의 주석(문서화)을 추가 할 수 있는 것이 특징
  5. 웹브라우저에서 수행되어 시각화와 스크립트의 저장이 간편함
  6. http://jupyter.org

#### Web Scraping : Requests, Beautifulsoup, Selenium
  1. 웹 데이터 수집
    - 웹 데이터
      - EMC - Digital Universe (2020년에는 35ZB, 생성된 데이터의 95% 디지털화)
    - 데이터 수집의 3단계
      1. 1단계 : 대상선정
        - 목적 데이터의 위치를 파악
      2. 2단계 : 수집
        - 대상 위치에서 원하는 데이터를 수집
      3. 3단계 : 정리
        - 수집된 데이터를 정리
  
  2. 웹 데이터 수집 - 자동화
    - 웹스크래핑과 크롤러
      - 스크래핑 - 각각의 페이지에서 정보를 추출하는 행위
      - 크롤러 - 자동으로 정보추출을 반복 하는 프로그램

    - 반 자동화 프로그램
      - 수 작업의 일부를 프로그래밍 지원하는 형태
      - 1단계 : 수집할 페이지를 지정하여 프로그램 시작 —> 수동
      - 2단계 : 대상 페이지를 내려 받고 특정 데이터 추출 —> 프로그램
      - 3단계 : 수집한 데이터를 일정 형식으로 저장 —> 수동 또는 프로그램
    
    - 완전 자동화 프로그램
      - 반 자동화 프로그램의 모든 부분을 자동화 프로그램으로 작성하여 실행
      - 스케쥴링을 이용하여 순환/반복 기능을 가짐 - 크롤러
      - 변화에 취약 하다는 단점 존재
  
  3. 웹 데이터 수집 - 주의사항
    - 수집 데이터의 처리와 저작권
      - 웹 사이트의 정보는 기본적으로 저작물
      - 정보를 읽어올 수 있다고 해서, 마음대로 활용할 수 있다는 것은 아닙니다. 저작권에 유의해 주세요.
      - 2016년 재정된 저작권법 제 30조 : 정보 해석을 목적으로 저작물을 복제/번안 가능
    
    - 웹 사이트의 리소스 압박과 업무 방해
      - 웹 사이트의 자원을 독점하게 되면 다른 사람이 웹 사이트를 이용할 수 없음
      - 무한 크롤러 사용 시 업무방해 혐의 적용 가능
    
    - 크롤러와 API
      - 해당 사이트에서 API 지원 여부 확인
  
  4. 크롤링 사례
    - 구글 : 수 많은 웹 사이트를 크롤링하여 검색서비스 제공
    - 지진발생 알림 : 각종 커뮤니티에서 지진에 관련된 글을 수집하여 지진 발생시 텔레그램으로 알림
  
  5. Web 의 이해
    - 웹 페이지 Web Page
      - 웹 상의 문서
      - 우리가 보고 있는 웹 사이트들은 문서로 이루어져 있다.
      - 텍스트, 그림, 소리, 동영상 등을 표현 가능
      - 대부분 HTML 이라는 언어로 이루어져 있음
    
    - 서버와 클라이언트
      - Client : 서비스를 요청하는 프로그램
      - Server : 요청에 대해 응답을 해주는 프로그램
    
    - 웹 페이지 해석 순서
      1. 클라이언트가 서버에게 contents를 요청한다.
      2. 서버는 요청 받은 contents를 클라이언트에게 건네준다.
      3. 브라우저는 서버에게 받은 HTML을 해석하여 화면에 보여준다.
    
    - HTTP - Hyper Text Transfer Protocol
      1. 서버와 클라이언트 사이에서 정보를 주고 받기 위한 규약
      2. 시작줄, 헤더(Header), 본문(Body) 으로 이루어져 있음
      3. 9개의 메소드가 존재하지만 주로 GET과 POST만 쓰인다.
  
  6. HTTP
    - GET
      1. Body 없이 Header만으로 전송된다.
      2. 링크 / 북마크 가 가능하다.
      3. 요청에 길이 제한이 있다.
      4. URL의 ? 뒤에 쿼리 문자열이 올 수 있다.
      5. 쿼리 문자열은 key와 value를 가지고 있으며, 각 쿼리는 & 로 구분한다.
    
    - POST
      1. Body에 query data가 들어간다.
      2. 링크 / 북마크가 불가능하다.
      3. 데이터 길이에 제한이 없다.
      4. URL을 가지지 않으므로 주로 중요한 데이터를 다룰 때 사용한다.
  
  7. HTTP Client 모듈 - Python
    - urllib
      1. Python built-in module
      2. 간편하게 HTTP request를 보낼 수 있음
      3. 로그인 및 세션을 유지하기가 번거로움

    - Requests
      1. 간편하게 HTTP request를 보낼 수 있음
      2. 세션을 유지하기가 용이함
      3. python2 / python3 완벽 지원
      4. 코드가 간결하고 documentation이 잘 되어 있음
    
    - Selenium : 웹브라우저 자동화 tool
      1. javascript/css 지원, 기존 GUI 브라우저 자동화 라이브러리
      2. 사람이 웹서핑 하는 것과 동일한 환경, 대신에 리소스를 많이 사용함
      3. 웹브라우저에서 HTML에 명시된 이미지/CSS/JavaScript를 모두 자동 다운로드/적용
  
  8. requests 설치
    - pip install requests
    - 파이썬에서는 기본 라이브러리로 urllib가 제공되지만, 이보다 간결한 코드로 다양한 HTTP요청을 할 수 있는 최고의 라이브러리
    - JavaScript 처리가 필요한 경우에는 selenium을 고려할 수도 있지만 이 경우에도 requests 적용이 가능할 수도 있습니다. 크롤링 할 페이지에 대해 다각도로 검토가 필요합니다.
    - 크롤링 시에 웹 요청에 requests를 쓸 수 있다면, 가장 효율적으로 처리 가능
  
  9. requests: GET 요청
    - 단순 GET 요청
      ```
        import requests
        response = requests.get('http://news.naver.com/main/home.nhn')
      ```
    
    - GET 요청 시에 커스텀 헤더 지정
      ```
        request_headers = {
              'User-Agent': ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 '
              '(KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'),
              'Referer': 'http://news.naver.com/main/home.nhn', # 뉴스홈
        }
        response = requests.get('http://news.naver.com/main/main.nhn', headers=request_headers)

        # requests 라이브러리에서의 기본 User-Agent값은 'python-requests/버전'입니다.
        서버에 따라 User-Agent 값으로 응답 거부 여부를 결정 하기도 합니다.
      ```
    
    - GET 요청 시에 GET인자(? 뒤에 붙이는 urlencoded) 지정
      1. params 인자로 dict 지정 : 동일 Key의 인자를 다수 지정 불가
        ```
          get_params = {'mode': 'LSD', 'mid': 'shm', 'sid1': '105'}    # IT/과학 탭을 위한 GET인자
          response = requests.get('http://news.naver.com/main/main.nhn', params=get_params)
        ```
      
      2. params 인자로 (key, value) 형식의 tuple 지정 : 동일 Key의 인자를 다수 지정 가능
        ```
          get_params = [('mode', 'LSD'), ('mid', 'shm'), ('sid1', '105')]
          response = requests.get('http://news.naver.com/main/main.nhn', params=get_params)
          get_params = (('k1', 'v1'), ('k1', 'v3'), ('k2', 'v2'))
          response = requests.get('http://httpbin.org/get', params=get_params)
        ```
  10. requests: GET 응답
    - 상태코드
      ```
        >>> response.status_code #int
        >>> response.ok # status_code가 200이상 400미만의 값인지 여부 (bool)
      ```
    
    - 응답 헤더
      ```
        dict 타입이 아니라 requests.structures.CaseInsensitiveDict 타입
        Key문자열은 대소문자를 가리지 않습니다.
        각 헤더의 값은 헤더이름을 Key로 접근 하여 획득

        >>> response.headers
        >>> response.headers['Content-Type'] # Key문자열 대소문자에 상관없이 접근
        'text/html; charset=UTF-8'
        >>> response.headers['content-type']
        'text/html; charset=UTF-8'
        >>> response.encoding
        'UTF-8'
      ```
    
    - 응답 Body
      ```
        bytes_data = response.content     # 응답 Raw 데이터 (bytes)
        str_data = response.text    # response.encoding으로 디코딩하여 유니코드 변환
      ```
      - 이미지 데이터일 경우에는 .content만 사용
        ```
          with open('flower.jpg', 'wb') as f:
                    f.write(response.content)
        ```
      - 문자열 데이터일 경우에는 .text를 사용
        ```
          html = response.text
          html = response.content.decode('utf8')    # 혹은 .content 필드를 직접 디코딩
        ```
      - json 포맷의 응답일 경우
        - json.loads(응답문자열)을 통해 직접 Deserialize를 수행 혹은 .json()함수를 통해 Deserialize 수행
          ```
            import json
            obj = json.loads(response.text)
            obj = response.json()   # 위와 동일
          ```
    
    - 한글 인코딩
      - charset 정보가 없을 경우, 먼저 utf8로 디코딩을 시도하고 UnicodeDecodeError가 발생할 경우, iso-8859-1 (latin-1)로 디코딩을 수행. 이때 한글이 깨진 것처럼 보여집니다. 이때는 다음과 같이 직접 인코딩을 지정한 후에 .text에 접근해주세요.
        ```
          >>> response.encoding
          'iso-8859-1'
          >>> response.encoding = 'euc-kr'
          >>> html = response.text
        ```
      - 혹은 .content를 직접 디코딩 할 수도 있습니다.
      - " >>> html = response.content.decode('euc-kr') "
  
  11. requests: POST 요청
    - 단순 POST 요청
      ```
        response = requests.post('http://httpbin.org/post')
      ```

    - 단순 POST 요청시 커스텀 헤더, GET 인자 지정
      ```
        request_headers = {
              'User-Agent': ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 '
              '(KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'),
              'Referer': 'http://httpbin.org',
        }
        get_params = {'k1': 'v1', 'k2': 'v2'}
        response = requests.post('http://httpbin.org/post', headers=request_headers, params=get_params)
      ``` 

    - data인자로 dict지정 : 동일 Key의 인자를 다수 지정 불가
      ```
        data = {'k1': 'v1', 'k2': 'v2'}
        response = requests.post('http://httpbin.org/post', data=data)
      ```
    
    - data인자로 (key, value) 형식의 tuple 지정 : 동일 Key의 인자를 다수 지정 가능
      ```
        data = (('k1', 'v1'), ('k1', 'v3'), ('k2', 'v2'))
        response = requests.post('http://httpbin.org/post', data=data)
      ```
    
    - JSON POST 요청
      1. JSON 인코딩
        ```
          import json
          json_data = {'k1': 'v2', 'k2': [1, 2, 3], 'name': ‘Django'}
        ```
      2. json포맷 문자열로 변환한 후, data인자로 지정
        ```
          json_string = json.dumps(json_data, ensure_ascii=False)
          response = requests.post('http://httpbin.org/post', data=json_string)
        ```
      3. 객체를 json인자로 지정하면, 내부적으로 json.dumps 처리
        ```
          response = requests.post('http://httpbin.org/post', json=json_data)
        ```

    - 파일 업로드 요청
      ```
        # multipart/form-data 인코딩
        files = {
            'photo1': open('f1.jpg', 'rb'), # 데이터만 전송
            'photo2': open('f2.jpg', 'rb'),
            'photo3': ('f3.jpg', open('f3.jpg', 'rb'), 'image/jpeg', {'Expires': '0'}),
        }
        post_params = {'k1': 'v1'}
        response = requests.post('http://httpbin.org/post', files=files, data=post_params)
      ```
  
  12. 파싱 - Parsing
    - 가공되지 않은 문자열에서 필요한 부분을 추출하여 의미있는 (구조화된) 데이터로 만드는 과정
  
  13. HTML DOM
    - HTML DOM = HTML 엘레먼트(태그) 로 구성된 Tree
      ```
        <!DOCTYPE html>
        <html>
            <head>
                <title>타이틀</title>
            </head>
            <body>
                <h1>제일 큰 제목</h1>
                <div>파이썬 웹 스크래핑</div>
            </body>
        </html>
      ```
      - html > body > div > 는 앞선 엘레먼트의 자식 (child)
  
  14. 웹상에서 특정 문자열 정보를 가져 오려면?
    1. 방법1: 정규 표현식을 활용
      - 가장 빠른 처리가 가능하나, 정규 표현식 Rule을 만드는 것이 많이 번거롭고 복잡합니다.
      - 때에 따라 필요할 수도 있습니다.
    2. 방법2: HTML Parser 라이브러리를 활용
      - DOM Tree을 탐색하는 방식으로 적용이 쉽습니다.
      - ex) BeautifulSoup4, lxml
  
  15. BeautifulSoup
    1. https://www.crummy.com/software/BeautifulSoup/bs4/doc/
    2. pip install BeautifulSoup4

      - 파싱을 도와 주는 강력한 python 라이브러리
      - HTML/XML Parser : HTML/XML문자열에서 원하는 태그 정보를 추출합니다.
      - 정규식을 작성할 필요 없이 tag, id, class 등의 이름으로 쉽게 파싱 가능
      - 쉽고 간결하며, documentation이 매우 잘 되어 있음

  16. BeautifulSoup 코드
    ```
      from bs4 import BeautifulSoup
      html = '''
      <ol>
        <li>NEVER - 국민의 아들</li>
        <li>SIGNAL - TWICE</li>
        <li>LONELY - 씨스타</li>
        <li>I LUV IT - PSY</li>
        <li>New Face - PSY</li>
      </ol>
      '''
      soup = BeautifulSoup(html, 'html.parser')
      for tag in soup.select('li'):
      print(tag.text)
    ```
  
  17. BeautifuleSoup Parser
    - BeautifulSoup4 내장 파서
      ```
        soup = BeautifulSoup(파싱할문자열, 'html.parser')
      ```
    
    - lxml HTML 파서 사용 (외부 C 라이브러리)
      1. html.parser 보다 좀 더 유연하고, 빠른 처리
      2. 설치 : pip3 install lxml
      3. soup = BeautifulSoup(파싱할문자열, 'lxml')
    
    - Tag를 찾는 2가지 방법
      1. find를 통해 태그 하나씩 찾기
      2. 태그 관계를 지정하여 찾기 (CSS Selector 사용)
  
  18. BeautifuleSoup : find()
    - find() 메서드 사용
      1. find (‘tag_name’) : 태그 이름으로 엘레먼트 찾기
      2. find (‘css_class_name’) : CSS 클래스 명으로 엘레먼트 찾기
        ```
          soup.find(‘title’)
          soup.find(‘.className’)
        ```

        ```
          import requests
          url = "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp"
          html = requests.get(url).text

          # BeautifulSoup으로 분석하기
          soup = BeautifulSoup(html, 'html.parser')

          # 원하는 데이터 추출하기
          title = soup.find("title").string
          wf = soup.find("wf").string

          print(title,wf)
        ```
  
  19. BeautifuleSoup : find_all, select()
    - find_all() 메소드 사용
      1. find_all(‘tag_name’) : 태그 이름으로 엘레먼트 찾기
      2. find_all(‘css_class_name’) : CSS 클래스 명으로 엘레먼트 찾기
        ```
          soup.find_all(‘a’)
          soup.find_all(‘.className’)
        ```
    
    - select() 메소드 사용
      1. select(‘css_셀렉터’) : CSS 셀렉터 문법으로 엘레먼트 찾기 (배열로 반환)
      2. select_one(‘css_셀렉터’) : 하나의 엘레먼트만 반환
        ```
          soup.select(‘#myId > div.className > a’)
          soup.select_one(‘#myId > div.className > a’)
        ```
        - BeautifulSoup 는 CSS 셀렉터 문법 중 :nth-child 를 지원하지 않음
  
  20. BeautifulSoup : attrs()
    - attrs 속성 사용
      1. a.attrs :
      2. 해당 엘레먼트에서 속성 추출하기
      3. <a> 태그의 모든 속성을 dict 타입으로 반환
        ```
          >>> a = soup.find_all(‘a’)
          >>> type(a.attrs)
          <class ‘dict’>
          >>> a[‘href’]
          ‘a.html’
        ```
  
  21. BeautifuleSoup : find(), find_all()
    - 예시)멜론 TOP100 차트
      ```
        import requests
        from bs4 import BeautifulSoup
        headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:57.0) Gecko/20100101 Firefox/57.0',
        }
        html = requests.get('http://www.melon.com/chart/index.htm',headers=headers).text
        soup = BeautifulSoup(html, 'html.parser')
        tag_list = []
        for tr_tag in soup.find(id='tb_list').find_all('tr'):
            tag = tr_tag.find(class_='wrap_song_info')
            if tag:
                tag_sub_list = tag.find_all(href=lambda value: (value and 'playSong' in value))
                tag_list.extend(tag_sub_list)
        for idx, tag in enumerate(tag_list, 1):
            print(idx, tag.text)
      ```
  
  22. BeautifuleSoup : CSS Selector 사용
    - CSS Selector를 통한 Tag 찾기 지원1
      1. tag name : "tag_name"
      2. tag id : "#tag_id"
      3. tag class names : ".tag_class“

    - CSS Selector를 통한 Tag 찾기 지원2
      1. '*' : 모든 Tag
      2. tag : 해당 모든 Tag
      3. Tag1 > Tag2 : Tag1 의 직계인 모든 Tag2
      4. Tag1 Tag2 : Tag1 의 자손인 모든 Tag2 (직계임이 요구되지 않음)
      5. Tag1, Tag2 : Tag1이거나 Tag2인 모든 Tag
      6. tag[attr] : attr속성이 정의된 모든 Tag
      7. tag[attr="bar"] : attr속성이 "bar"문자열과 일치하는 모든 Tag
      8. tag[attr*="bar"] : attr속성이 "bar"문자열과 부분 매칭되는 모든 Tag
      9. tag[attr^="bar"] : attr속성이 "bar"문자열로 시작하는 모든 Tag
      10. tag[attr$="bar"] : attr속성이 "bar"문자열로 끝나는 모든 Tag
    
    - CSS Selector를 통한 Tag 찾기 지원3
      1. tag#tag_id : id가 tag_id인 모든 Tag
      2. tag.tag_class : 클래스명 중에 tag_class가 포함된 모든 Tag
      3. tag#tag_id.tag_cls1.tag_cls2 : id가 tag_id 이고, 클래스명 중에 tag_cls1와 tag_cls2가 모두 포함된 Tag
      4. tag.tag_cls1.tag_cls2 : 클래스명 중에 tag_cls1와 tag_cls2가 모든 포함된 모든 Tag
      5. tag.tag_cls1 .tag_cls2 : 클래스명 중에 tag_cls1이 포함된 Tag의 자식 중에 (직계가 아니어도 OK), 클래스명에 tag_cls2가 포함된 모든 Tag
    
    - CSS Selector를 지정할 때 주의사항
      - 패턴을 너무 타이트하게 지정하시면, HTML 마크업이 조금만 변경되어도 태그를 찾을 수 없게 됩니다.
      
  23. 이미지 파일 다운로드
    - res = requests.get(이미지 파일 경로)
      - res.content : 이미지파일을 바이너리로 받아옴
      - 해당 바이너리를 파일로 저장
        ```
          import requests

          res = requests.get(
          'http://www.jetbrains.com/idea/img/screenshots/idea_overview_5_1.png')

          # print(res.content)

          with open('img.png', 'wb') as f:
            f.write(res.content)
        ```
      
  24. 헤더 수정
    - user-agent 헤더 수정
      - 기본 urllib 모듈을 사용했을 때 user-agent 
      - Python-urllib/3.4
      - 브라우저에서 요청하는 것 같이 보이기!!
    
    - requests 를 사용해 헤더를 별도로 설정하여 요청
      ```
        import requests

        # 헤더 설정을 위해서 session 객체 생성
        session = requests.Session()

        # User-Agent 설정
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh . . . safari/604.1.38’
        }

        # 세션을 통해 get 요청을 시도
        res = session.get('http://www.naver.com', headers=headers)

        # 응답 받은 HTML 을 출력
        print(res.text)
      ```
    
    - 예시)네이버 웹툰
      ```
        import os
        import requests

        # URL 소스 :
        http://comic.naver.com/webtoon/detail.nhn?titleId=119874&no=1015&weekday=tue
        image_urls = [
          'http://imgcomic.naver.net/webtoon/119874/1015/20170528204207_6e9df8e618b97520233bbb35e7d4eaaf_IMAG01_1.jpg',
          'http://imgcomic.naver.net/webtoon/119874/1015/20170528204207_6e9df8e618b97520233bbb35e7d4eaaf_IMAG01_2.jpg',
          'http://imgcomic.naver.net/webtoon/119874/1015/20170528204207_6e9df8e618b97520233bbb35e7d4eaaf_IMAG01_3.jpg',
        ]
        for image_url in image_urls:
          response = requests.get(image_url)
          image_data = response.content
          filename = os.path.basename(image_url)
          with open(filename, 'wb') as f:
            print('writing to {} ({} bytes)'.format(filename, len(image_data)))
            f.write(image_data)
      ```
  
  25. 사람처럼 보이기 위한 체크리스트
    1. 기계가 웹 서핑을 하는 것 같은 패턴을 보이면 IP가 차단될 수 있습니다.
    2. 자바스크립트가 실행되기 전의 페이지는 아무 것도 없이 비어 있을 수 있습니다.
    3. 폼을 전송하거나 POST 요청을 보낼 때는 서버에서 기대하는 모든 데이터를 보내야 합니다.
      - 크롬 개발자 툴에서 network 탭을 통해 요청되는 정보를 확인
      - 폼의 hidden 필드를 확인
    4. 쿠키가 함께 전송되는 지 확인
    5. 403 Forbidden 에러를 받는 다면 IP가 차단되었을 가능성도 있습니다.
      - 새로운 IP로 요청을 시도하거나, 가까운 까페에 가서 스크래핑을 수행하세요
    6. 사이트를 너무 빨리 이동하지 마세요
      - 페이지 이동 시 지연시간을 추가
    7. 헤더를 바꾸세요
  
  26. Selenium
    1. 브라우저를 조종하여 데이터를 얻는 방법
      - Selenium
      - 브라우저를 직접 띄우기 때문에 css나 image 등 모든 데이터를 다운 받음
      - 속도가 느리다.
      - 동적 페이지도 크롤링이 가능하다. ( javascript 실행 가능)
    
    2. HTTP request를 날려서 데이터를 얻는 방법
      - requests, scrapy
      - 속도가 빠르다.
      - Javascript 실행이 불가능함 -> Web page에 대한 사전 분석이 필요
    
    3. Selenium
      - 웹 브라우저 자동화 tool
      - Java, C#, Perl , PHP, Python , Ruby 등 다양한 언어 지원
      - 직접 브라우저를 실행하여 python code로 mouse click, keyboard input 등의 event를 발생시킴
      - 실제 브라우저로 실행한 것과 동일한 값을 얻을 수 있음
      - 속도가 많이 느리다.
    
    4. Selenium 특징
      - 주로 웹앱을 테스트 하는데 이용하는 프레임워크
      - webdriver 라는 API를 통해 운영체제에 설치된 Chrome 등의 브라우저를 제어
      - 브라우저를 직접 동작 시키기 때문에 JavaScript 등 비동적으로 혹은 뒤늦게 로드 되는 컨텐츠들을 가져올 수 있음
      - 즉, 눈에 보이는 모든 컨텐츠를 다 가져올 수 있음
      - 비교) requests.text는 브라우저 소스 보기와 같이 이후에 변화된 HTML은 제어 할 수 없다.
    
    5. Selenium - webdriver
      1. Chrome WebDriver
        - 크롬 웹드라이버 설치 시 로컬에 크롬 브라우저 반드시 설치 되어 있어야 함
        - 크롬 드라이버 다운로드 (https://sites.google.com/a/chromium.org/chromedriver/downloads)
        - zip 파일을 받고 압축을 풀면 chromedriver .exe라는 파일이 저장됨
        - Selenium 객체를 지정할 때 크롬 드라이버의 위치가 필요
    
    6. Selenium - 사이트 브라우징
      1. 먼저 webdriver 를 import
        ```
          from selenium import webdriver
        ```
      2. webdriver 객체 만들기
        ```
          from selenium import webdriver

          # chromedriver 의 경로를 지정하여 웹드라이버 객체 생성
          driver = webdriver.Chrome(‘./chromedriver’) 

          # 암묵적으로 웹 자원 로드를 위해 최대 3초까지 기다린다.
          driver.implicitly_wait(3)

          # url 에 접근
          driver.get(‘http://www.naver.com')
        ```
    
    7. Selenium - 주요 메소드
      1. URL 접근
        - get(‘http://url.com')
      2. 페이지의 단일 element 에 접근하는 API
        - find_element_by_name(‘HTML_name’)
        - find_element_by_id(‘HTML_id’)
        - find_element_by_xpath(‘/html/body/some/xpath’)
      3. 페이지의 여러 elements 에 접근하는 API
        - find_elements_by_css_selector(‘#css > div.selector’)
        - find_elements_by_class_name(‘some_class_name’)
        - find_elements_by_tag_name(‘h1’)
    
    8. Selenium : find_element_by_css_selector
      - driver 를 통해 여러 방법으로 DOM을 찾을 수 있지만, CSS Selector가 더 편리
        ```
          input_id = driver.find_element_by_css_selector('#id')
          input_pw = driver.find_element_by_css_selector('#pw')
          login_button = driver.find_element_by_css_selector(
            '#frmNIDLogin > fieldset > span > input[type="submit"]'
          )
        ```
      - 폼 관련 Selector : input[type=“submit”]
        - input 태그 중 type 속성이 “submit” 인 엘레먼트
    
    9. Selenium - BeautifulSoup 과 같이 사용하기
      - driver.page_source 를 사용하여 현재 렌더링 된 페이지 소스를 모두 가져옴
        ```
          from selenium import webdriver

          driver = webdriver.Chrome(‘./chromedriver’)
          driver.implicitly_wait(3)

          # url 에 접근
          driver.get(‘http://www.naver.com')

          # 현재 페이지의 소스를 가져온다.
          html = driver.page_source

          # BeautifulSoup 객체를 생성
          soup = BeautifulSoup(html, ‘lxml')

          ...

          # 브라우저 닫기
          driver.quit()
        ```
  
    10. 크롬 - Headless 모드 사용하기
      ```
        from selenium import webdriver

        options = webdriver.ChromeOptions()
        options.add_argument(‘headless’)
        options.add_argument(‘window-size=1920x1080’)

        driver = webdriver.Chrome(‘./chromedriver’, chrome_options=options)
        driver.implicitly_wait(3)

        # url 에 접근
        driver.get(‘http://www.naver.com')

        # 현재 화면 스크린샷으로 저장
        driver.get_screenshot_as_file(‘main-page.png’)
        
        # ...이하 동일
      ```
  
  26. 웹 API
    1. 웹 API – 오픈 API 또는 API 라고 함
      - 어떤 사이트의 기능을 외부로 공개 하는 것
      - 일반적으로 HTTP 통신을 사용
      - 요청의 결과로 주로 XML 이나 JSON 형태로 데이터를 응답함
      - 최근에는 JSON 방식의 응답을 하는 API가 빠르게 늘어 나고 있음
      - 유용한 형식으로 정리된 데이터를 제공 받을 수 있음

    2. API 동작 방식
      - 브라우저나 HTTP client 툴을 사용해 요청을 보냄 (http://api.github.com/users/vega2k)
      - 응답은 JSON 형태로 반환
    
    3. JSON 포맷
      - 데이타 교환의 표준 포맷 - JSON


### 2.9 11일차(2022-02-03)

#### 깃(Git) & 깃허브(GitHub) - 깃 시작하기
  1. 깃이란 무엇인가?
    - 깃(Git) 의 탄생
      * 2005 년 리누스 토르발스가 처음 소개
      * 특징
        1. 컴퓨터 파일의 변경사항을 추적
        2. 여러 명의 사용자들 간에 해당 파일들의 작업을 조율하기 위한 분산 버전 관리 시스템
      * 개발자들은 깃을 통해 수많은 소스 코드를 효율적으로 관리
    
    - 깃의 특징 
      - 버전 관리 (Version Control) : 문서를 수정할 때마다 언제 수정했는지 , 어떤 것을 변경 했는지 편하고 구체적으로 기록하기 위한 버전 관리 시스템
        - 문서를 작성한 뒤 원본도 남겨두고 수정한 내용을 저장해야 하는 경우 '다른 이름으로 저장' 을 주로 사용
        - 깃을 사용한다면 ?
          - 파일이름은 유지하면서 문서를 수정할 때마다 언제 수정했는지 , 어떤 것이 변경되었는지 기록 가능
      - 백업 (Backup) : 현재 컴퓨터의 자료를 인터넷 상의 공간 원격 저장소에 백업
        - 백업이란?
          * 현재 내 컴퓨터에 있는 자료를 다른 곳에 복제
          * USB 디스크 , 외장하드 , 드롭박스 (Dropbox) 등
        - 깃허브 (GitHub)
          * 깃 파일을 위한 원격 저장소 또는 온라인 저장소
      - 협업 (Collaboration) : 원격 저장소를 기준으로 여러 사람이 함께 일할 수 있음
        * 깃허브와 같은 온라인 서비스를 사용하면 여러 사람이 함께 일할 수 있음
        * 깃허브(GitHub)의 장점
          1. 팀원들이 파일을 편하게 주고받으면서 일할 수 있음
          2. 누가 어느 부분을 수정했는지 기록에 남음
  
  2. 깃 프로그램의 종류
    - 깃허브 데스크톱 (GitHub Desktop)
      - 깃허브에서 제공하는 프로그램
      - 그래픽 사용자 인터페이스(GUI)로 구현
      - 사용이 쉬워 누구나 배울 수 있음
      - 기본적인 기능만 제공

    - 토터스깃 (TortoiseGit)
      - 윈도우 전용 프로그램
      - 윈도우 탐색기의 빠른 메뉴에 추가되는 프로그램
    
    - 소스트리 (Source Tree)
      - 깃의 기본 기능부터 고급 기능까지 제공
      - 사용법은 복잡하지만 익숙해지면 자유롭게 깃을 활용할 수 있음
    
    - 더 많은 깃 프로그램
      - https://git scm.com/downloads/guis
    
    - 커맨드 라인 인터페이스(CLI)
      - 터미널 창에 직접 명령을 입력해서 깃을 사용하는 방식
      - 리눅스 명령어 및 깃 명령어를 알아야 사용 가능
      - 대부분의 개발자들은 이 방식으로 깃을 사용
  
  3. 깃 설치하기
    - https://git scm.com/
    - 홈페이지에서 다운받은 설치파일로 설치 후 윈도우 검색 창에 git 입력 후 , [Git Bash] 클릭
    - 깃 설치하기 macOS
      - homebrew 설치하기
        ```
          $/bin/bash c "$(curl fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
        ```
      - 깃 설치하기
        ```
          brew install git
        ```
    - Git Bash 화면에 다음 명령어 입력
      ```
        $ git
      ```
  
  4. 깃 환경 설정
    - 사용자 정보 입력
      - 사용자 이름
        ```
          $ git config --global user.name "Minu"
        ```
      - 사용자 이메일
        ```
          $ git config --global user.email "minu@gmail.com"
        ```
  
  5. 기본 리눅스 명령어
    - 현재 디렉터리 위치 경로 : pwd
    - 현재 디렉터리에 안에 있는 파일 또는 디렉터리 확인 : ls
    - 파일과 디렉터리 상세 정보 확인 : ls -la
    - ls 명령어 옵션
        |옵션|설명|
        |:---:|:---:|
        |-a|숨김 파일과 디렉터리를 함께 표시|
        |-l|파일이나 디렉터리의 상세 정보를 함께 표시|
        |-r|파일의 정렬 순서를 거꾸로 표시|
        |-t|파일 작성 시간 순으로 내림차순 표시|
    - 화면 지우기 : clear
    - 디렉터리 이동 : cd
      - 현재 위치에서 상위 디렉터리로 이동 : cd..
      - 현재 위치에서 하위 디렉터리로 이동 : cd 하위 디렉터리 이름
      - 홈 디렉터리로 이동 : cd ~
    - cd 명령어 옵션
      |옵션|설명|
      |:---:|:---:|
      |~|현재 사용자의 홈 디렉터리(c/Users/ 계정이름)|
      |./|현재 사용자가 작업 중인 디렉터리|
      |../|현재 디렉터리의 상위 디렉터리|
    - 디렉터리 생성
      ```
        $ mkdir 생성할 디렉터리 이름
      ```
      - 홈 디렉터리 안에 있는 Documents 디렉터리 에 test 디렉터리 생성
        ```
          $ cd ~/Documents
          $ mkdir test
        ```
      - test 디렉터리 생성 확인 : ls
    - 디렉터리 삭제
      ```
        $ rm -r 삭제할 디렉터리 이름
      ```
      - 홈 디렉터리 안에 있는 Documents 디렉터리 에 test 디렉터리 삭제
        ```
          $ rm -r test
          $ ls
        ```
  
  6. 빔(Vim) 사용하기
    - 빔(Vim) 이란?
      - 터미널에서 사용할 수 있는 대표적인 문서 편집기
      - 홈디렉터리 /Documents/test 디렉터리 생성 후 이동
        ```
          $ cd ~/Documents
          $ mkdir test
          $ cd test
        ```
      - 현재 디렉터리(test)에 test.txt 파일 생성
        ```
          $ vim test.txt
        ```
    
    - 입력 모드와 ex 모드
      - ex 모드 : 저장, 종료 등 (입력 모드에서 Esc 누름)
      - 입력모드 : 텍스트 입력, 수정 (ex모드에서 A 또는 I 누름)
    - 내용 저장하기
      - 콜론(:) 을 입력하면 "INSERT"가 있던 자리에 텍스트를 입력할 수 있음
      - :wq 입력 후, Enter 키 누름
    - ex 모드 명령어
      - :w 또는 :write : 편집 중이던 문서를 저장
      - :q 또는 :quit : 편집기를 종료
      - :wq : 편집 중이던 문서를 저장하고 종료
      - :q! : 문서를 저장하지 않고 편집기를 종료
    - 텍스트 문서 내용 확인하기
      ```
        $ cat 파일이름
      ```
      - test.txt 파일 내용 확인
        ```
          $ cat test.txt
        ```

#### 깃(Git) & 깃허브(GitHub) - 깃으로 버전 관리하기
  1. 깃 저장소 만들기
    - 깃 초기화 하기
      ```
        $ git init
      ```
      - 원하는 디렉터리를 저장소로 사용할 수 있게 만들어 줌
      - 초기화 후 .git 디렉터리 숨김 폴더 가 생성

      - hello git 디렉터리 생성 후 이동
        ```
          $ mkdir hello git
          $ cd hello-git
        ```
  
  2. 버전 만들기
    - 버전이란?
      - 깃에서 문서를 수정하고 저장할 때마다 생기는 것
      - 버전마다 변경 시점과 변경 내용을 확인할 수 있음
      - 이전 버전으로 되돌아갈 수 있음

    - 작업 트리(working tree)
      - 파일 수정 , 저장 등의 작업을 하는 디렉터리
      - 작업 디렉터리 (working directory) 라고도 함
      - 우리 눈에 보이는 디렉터리를 말함
    
    - 스테이지(Stage)
      - 버전으로 만들 파일이 대기하는 곳
      - 눈에 보이지 않음
    
    - 저장소 (repository)
      - 스테이지에서 대기하고 있던 파일들을 버전으로 만들어 저장하는 곳
      - 눈에 보이지 않음
    
    - 버전 생성 과정
      1. 작업 트리에서 파일을 수정하고 저장
      2. 버전을 만들고 싶으면 스테이지에 넣음
      3. 버전을 만들기 위해 깃에게 커밋 (commit)’ 명령을 내림
      4. 스테이지에 있던 파일을 저장소에 새로운 버전으로 저장
  
    - 버전 만들기 (실습)
      1. 작업 트리에서 빔으로 문서 수정하기
        1. hello git 디렉터리로 이동 후 , 깃 상태 확인
          ```
            $ git status
          ```
        2. 새로운 파일 (hello.txt) 생성
          ```
            $ vim hello.txt
          ```
        3. 입력 모드 (A 또는 I) 로 변경 후 , 내용 입력
        4. ex 모드 (Esc) 로 변경 후 , 문서 저장 (:wq)
        5. 깃 상태 확인
          ```
            $ git status
          ```
        ** Untracked files **
          - 깃에서 아직 한번도 관리하지 않은 파일을 의미
      
      2. 수정한 파일 스테이징하기
        1. 스테이지에 수정한 파일 추가
          ```
            $ git add 파일명
          ```
        2. 깃 상태 확인
          ```
            $ git status
          ```
      
      3. 스테이지에 올라온 파일 커밋하기
        1. 파일 커밋
          ```
            $ git commit m 커밋 메시지
          ```
          - 커밋 메시지
            - 커밋할 때 해당 버전에 어떤 변경 사항이 있었는지 확인하기 위한 메시지를 기록
            - 영어로 작성하는 것이 좋음
        2. 예 ) 커밋 메시지에 “message1” 작성
          ```
            $ git commit m “message1”
          ```
        3. 깃 상태 확인
          ```
            $ git status
          ```
          - nothing to commit : 버전으로 만들 파일이 없음
          - working tree clean : 작업 트리에도 수정사항이 없음
      
      4. 커밋한 버전 확인하기
        ```
          $ git log
        ```
        - Author : 커밋을 만든 사람
        - Date : 커밋 시간 및 커밋 메시지

      5. 스테이징과 커밋 한번에 처리하기
        - 한 번 이상 커밋한 파일을 다시 커밋할 때만 사용 가능
          ```
            $ git commit -am
          ```
        - hello.txt 파일 수정 (예시)
          ```
            $ vim hello.txt
          ```

          ```
            $ git commit -am “message2”
          ```
  
  3. 커밋 내용 확인하기
    - 커밋 기록 확인하기
      ```
        $ git log
      ```
    
    - 변경 사항 확인하기
      ```
        $ git diff
      ```
      - 작업 트리에 있는 파일과 스테이지에 있는 파일을 비교
      - 스테이지에 있는 파일과 저장소에 있는 최신 커밋을 비교
  
  4. 단계마다 파일 상태 알아보기
    - tracked 파일
      - 깃이 상태를 계속 추적하고 있는 파일
    
    - untracked 파일
      - 깃이 상태를 추적하지 않는 파일
    
    - 커밋 기록 확인하기
      ```
        $ git log
      ```
    
    - 커밋 기록 자세하게 확인하기
      ```
        $ git log --stat
      ```
  
  5. 작업 되돌리기
    - 작업 트리에서 수정한 파일 되돌리기
      ```
        $ git restore 파일명
      ```
      - 파일을 수정한 후 , 소스가 정상적으로 작동하지 않는 등의 이유로 수정한 내용을 취소하고 가장 최신 버전으로 되돌려야 하는 경우에 사용
      - restore 명령어로 되돌린 내용은 다시 복구할 수 없음
    
    - 스테이징 취소하기
      ```
        $ git restore staged 파일명
      ```
      - 수정한 파일을 스테이징했을 때 , 스테이징을 취소해야 하는 경우에 사용
    
    - 최신 커밋 취소하기
      ```
        $ git reset HEAD^
      ```
      - 수정한 파일을 스테이징하고 커밋까지 했을 때 가장 마지막에 한 커밋을 취소해야 하는 경우에 사용
    
    - reset 명령어 옵션
      * --soft HEAD^
        - 최근 커밋을 하기 전 상태로 작업 트리를 되돌림
      * --mixed HEAD^ 
        - 최근 커밋과 스테이징을 하기 전 상태로 작업 트리를 되돌림
        - 옵션 없이 git reset 명령어를 사용할 경우 , 이 옵션으로 작동
      * --hard HEAD^
        - 최근 커밋과 스테이징 , 파일 수정을 하기 전 상태로 작업 트리를 되돌림
        - 이 옵션으로 되돌린 내용은 복구할 수 없음
    
    - 특정 커밋으로 되돌리기
      ```
        $ git reset hard 되돌아갈 커밋해시
      ```
        - 특정 버전의 커밋으로 되돌린 다음 그 이후 버전을 삭제하려는 경우에 사용

      ```
        $ git revert 취소할 커밋해시
      ```
        - 특정 버전의 커밋으로 되돌린 다음 그 이후 버전을 남겨두려는 경우에 사용
    
  6. 정리하기
    - git init : 현재 위치에 저장소 생성하기
    - git status : 깃 상태 확인하기
    - git add test.txt : ‘test.txt’ 파일을 스테이지에 올리기
    - git commit -m 'first commit' : 'first commit’ 메시지와 함께 커밋하기
    - git log : 커밋 정보 확인하기
    - git reset HEAD^ : 최신 커밋 취소하기
    - git reset 커밋해시 : 지정한 커밋해시로 이동 후 , 이후 커밋 취소하기
    - git revert 커밋해시 : 지정한 커밋해시의 변경 이력을 취소하기

#### 깃(Git) & 깃허브(GitHub) - 브랜치
  1. 브랜치란?
    - 브랜치 (Branch)
      - 버전 관리 시스템에서 데이터의 흐름을 의미
    
    - master 브랜치
      - 깃으로 버전 관리를 시작하면 기본적으로 생성
      - 분기(branch)와 병합(merge) 기능
  
    - 브랜치 기능
      1. 분기 (branch)
        - master 브랜치에서 새 브랜치를 생성
        - 기존에 저장한 파일을 master 브랜치에 유지하면서 기존 내용을 수정하거나 새로운 기능을 만들 수 있음
      
      2. 병합 (merge)
        - 새 브랜치에 있던 파일을 master 브랜치에 합침
  
  2. 브랜치 만들기
    - 브랜치 확인
      ```
        $ git branch
      ```
    
    - 새 브랜치 생성
      ```
        $ git branch 브랜치이름
      ```
    
    - A 사의 브랜치 생성
      ```
        $ git branch A
      ```
    
    - B 사의 브랜치 생성
      ```
        $ git branch B
      ```
    
    - 생성된 브랜치 확인
      ```
        $ git branch
      ```
    
    - 브랜치 이동하기
      ```
        $ git checkout
      ```
    
    - A 사의 브랜치로 이동하기
      ```
        $ git checkout A
      ```
  
  3. 브랜치 정보 확인하기
    - 브랜치 별 커밋 로그 확인하기
      ```
        $ git log --oneline --branches
      ```
    
    - 브랜치 사이의 차이점 확인하기
      ```
        $ git log 기준_브랜치..비교_브랜치
      ```
      - 예시> master 브랜치와 A 브랜치를 비교
        ```
          $ git log master..A
        ```
        - master 브랜치에는 없고 , A 브랜치에는 있는 커밋을 보여줌
        ```
          $ git log A..master
        ```
        - A 브랜치에는 없고 , master 브랜치에는 있는 커밋을 보여줌
  
  4. 브랜치 병합하기
    - master 브랜치로 이동하기
      ```
        $ git checkout master
      ```
    - master 브랜치에 A 브랜치 병합하기
      ```
        $ git merge A
      ```
    
    - 병합 진행 중 파일 내용 확인
      ```
        content 1
        content 2
        content 3
        <<<<<<< HEAD
        content 4    <- 현재 브랜치에서 수정한 내용
        =======
        A content 4  <- 병합할 브랜치에서 수정한 내용
        >>>>>>> A
      ```
      - 파일 내용을 원하는 대로 수정하고 저장
    
    - 파일 스테이징 및 커밋하기
      ```
        $ git commit -am “merge A branch”
      ```
    
    - 로그 확인하기
      ```
        $ git log --oneline --branches
      ```
  
  5. 정리하기
    - git branch newBranch : 새로운 브랜치 newBranch 생성
    - git checkout newBranch : 기존 브랜치에서 newBranch 로 변경
    - git log --oneline : 한 줄씩 커밋 로그 출력
    - git add . : 수정한 전체 파일을 스테이징
    - git log oneline --branches : 브랜치 별 커밋 로그 출력
    - git merge newBranch : newBranch를 master 브랜치에 병합


### 2.10 12일차(2022-02-04)


#### 깃(Git) & 깃허브(GitHub) - 오픈소스 저장소 사용하기
  1. 오픈소스 저장소 복제
    1. 오픈소스 저장소로 이동 및 포크
    2. 포크한 저장소 주소 복사
    3. 복제된 저장소를 지역 저장소로 클론하기
      `$ git clone 복사한 저장소 주소`
    4. 소스 코드 수정하기
    5. 커밋하기
      `$ git commit -am “update code”`
    6. 원격 저장소에 올리기
      `$ git push`
  
  2. 오픈소스 저장소에 합치기 요청
    1. 풀 리퀘스트 (pull request)
      - 원본 저장소의 개발자에게 수정한 내용을 반영해 달라는 요청
    2. 풀 리퀘스트 메뉴 상단 “Create pull request” 버튼 클릭
    3. 커밋에 대한 설명 추가
    4. 개발자와 소통하는 공간
      - 개발자와 질문과 답변을 주고 받으면서 수정한 내용을 원본 소스에 반영할지 여부를 결정
  
  3. 오픈소스 저장소에 합치기 수락
    - 원본 저장소에서 다른 사용자가 보낸 수정 내용 검토 후 수락 여부 결정 (pull request 메뉴)
      - 수정을 허락하려면 Merge pull request 버튼 클릭

#### 깃(Git) & 깃허브(GitHub) - 깃허브 계정 변경하기
  1. 깃허브 계정 변경하기 Windows
    1. 터미널에서 계정 변경
      - 변경을 희망하는 계정의 이름과 이메일 주소 입력
        `$ git config global user.name 계정_이름`

        `$ git config global user.email 계정_이메일`
    
    2. 제어판 - 자격증명 관리자 - GitHub 관련 자격 증명 삭제
    3. 일반 자격 증명 추가 클릭
    4. 연결할 깃허브 계정 및 사용자 이름 , 암호 입력
  
  2. 깃허브 계정 변경하기 macOS
    1. 터미널에서 계정 변경
      - 변경을 희망하는 계정의 이름과 이메일 주소 입력
        `$ git config global user.name 계정_이름`

        `$ git config global user.email 계정_이메일`

    2. '키체인 접근' 실행
    3. 검색란에 'github' 검색
    4. 변경할 계정 이름 입력 및 변경사항 저장 버튼 클릭

#### 깃(Git) & 깃허브(GitHub) - 파이참에서 깃 사용하기
  1. 환경 설정
    - GitHub 연결 방법 1> 파이참 메인 화면
      1.  GitHub 메뉴 선택 → Log in via Github 버튼 클릭
    
    - GitHub 연결 방법 2>
      1. [File] → [Settings]
      2. [GitHub] 메뉴 → Add account 클릭
      3. 권한 수락 화면 이동 버튼 클릭
      4. GitHub 로그인
      5. 권한 수락
      6. 연결 성공
      7. [VCS] → [Get from Version Control]
      8. Get from Version Control

  2. 저장소 복제
    1. 원하는 저장소 선택 → [Clone]
    2. 프로젝트 열기
      - Trust Project → This Window 또는 New Window
    3. 프로젝트에 새 파일 추가하기 - add 버튼 클릭
  
  3. 원격 저장소에 커밋
    1. 왼쪽 메뉴 [Commit] 선택
    2. 변경된 파일 → 마우스 오른쪽 클릭 → [Commit File]
    3. 커밋 메시지 입력 → Commit 버튼 클릭
  
  4. 원격 저장소에 푸시
    1. 깃허브에 올리기 <Push>
      - [Git] → [Push]
  
  5. 원격 저장소에서 풀
    1. [Git] → [Pull]
    2. 브랜치 선택 → Pull 버튼 클릭


### 2.11 13일차(2022-02-07)
  - 멜론 TOP100 차트를 활용한 웹 스크래핑
    - BeautifuleSoup, requests 사용


### 2.12 14일차(2022-02-08)

#### Pandas를 활용한 데이터 분석
  1. Pandas
    - Pandas(http://pandas.pydata.org/)는 데이터 처리와 분석을 위한 파이썬 라이브러리입니다. R의 data.frame을 본떠서 설계한 DataFrame이라는 데이터 구조를 기반으로 만들어졌습니다.
    - 간단하게 말하면 Pandas의 DataFrame은 엑셀의 스프레드시트와 비슷한 테이블 형태라고 할 수 있습니다. Pandas는 이 테이블을 수정하고 조작하는 다양한 기능을 제공합니다. 특히, SQL처럼 테이블에 쿼리나 조인을 수행할 수 있습니다.
    - 전체 배열의 원소가 동일한 타입 이어야 하는 NumPy와는 달리 Pandas는 각 열의 타입이 달라도 됩니다(예를 들면 정수, 날짜, 부동소숫점, 문자열).
    - SQL, 엑셀 파일, CSV 파일 같은 다양한 파일과 데이터베이스에서 데이터를 읽어 들일 수 있는 것이 Pandas가 제공하는 또 하나의 유용한 기능입니다.
    - 10 Minutes to pandas라는 판다스의 공식 튜토리얼을 읽어보시는 것을 추천 드립니다.
  
  2. Pandas의 고유한 자료구조 - Series
    - Series
      1. Series는 pd.Series() 함수를 사용하여 정의함.
      2. Python list와 numpy array가 이 함수의 인자로 입력됨.
      3. Series는 각 성분의 인덱스와, 이에 대응되는 값으로 구성되어 있음.
      4. Series 생성 시 인덱스는 0으로 시작하는 정수 형태의 기본 인덱스가 부여됨.
      5. 기본 인덱스 대신 Series 생성 시 각 성분에 대한 인덱스를 사용자가 직접 명시할 수도 있음.
        ```
          obj = pd.Series([4, 7, -5, 3])
          obj2 = pd.Series([4, 7, -5, 3], index=['d', 'b', 'a', 'c'])
        ```
    - Series obj의 인덱스만을 추출 : obj.index
    - Series obj의 값만을 추출 : obj.values
    - Series obj에 부여된 데이터형을 확인 : obj.dtype
    - 인덱스에 대한 이름을 지정 : obj.name과 obj.index.name에 값을 대입해 줌
  
  3. Pandas의 고유한 자료구조 - DataFrame
    - DataFrame
      1. DataFrame은 pd.DataFrame() 함수를 사용하여 정의함.
      2. Python 딕셔너리 혹은 numpy의 2차원 array가 이 함수의 인자로 입력됨.
        ```
          data = {
            "names": ["soyul", "soyul", "soyul", "Charles", "Charles"], 
            "year": [2014, 2015, 2016, 2015, 2016],
            "points": [1.5, 1.7, 3.6, 2.4, 2.9]
          }
          df = pd.DataFrame(data)
        ```
      3. DataFrame에서는 서로 다른 두 종류의 인덱스가 각각 행 방향과 열 방향에 부여되어 있으며, 교차하는 지점에 실제 값이 위치해 있음.
      4. 행 방향의 인덱스를 '인덱스', 열 방향의 인덱스를 '컬럼'이라고 부름.
        - DataFrame의 인덱스 확인 : df.index
        - DataFrame의 컬럼명 확인 : df.columns
        - DataFrame의 값 확인 : df.values
        - DataFrame의 행,열 갯수 확인 : df.shape
  
  4. Pandas DataFrame의 인덱싱
    - DataFrame의 기본 인덱싱 – 열(column) 선택하고 조작하기
      - df라는 이름의 DataFrame을 다음과 같이 정의합니다.
        ```
          data = {
            "names": ["soyul", "soyul", "soyul", "Charles", "Charles"], 
            "year": [2014, 2015, 2016, 2015, 2016], 
            "points": [1.5, 1.7, 3.6, 2.4, 2.9]
          }
          df = pd.DataFrame( data, columns=["year", "names", "points", "penalty"], index=["one", "two", "three", "four", "five"])
        ```
    
    - DataFrame의 기본 인덱싱 – 열(column) 선택하고 조작하기
      - df에서 ‘year’ 열 만을 가져올 경우, ‘year’ 열의 값들이 Series 형태로 인덱스와 함께 표시됨
        ```
          df["year"]
        ```
      - df에서 복수개의 열을 가져올 경우, 중괄호 안에 컬럼 이름으로 구성된 리스트가 들어감
        ```
          df[["year", "points"]]
        ```
      - 특정 열을 이렇게 선택한 뒤 값을 대입하면, NaN 표시된 ‘penalty’열에 값을 지정함
        ```
          df["penalty"] = [0.1, 0.2, 0.3, 0.4, 0.5]
        ```
  
  5. Pandas 데이터 그룹화 이해하기
    - 그룹화의 흐름 : split-apply-combine
      - pandas에서의 모든 그룹화의 흐름은 "split-apply-combine""이라는 키워드로 표현하기도 합니다.  그룹화하고자 하는 열의 값을 기준으로 데이터를 나누고(split), 각 그룹에 대한 통계 함수를 적용하여 (apply), 최종적인 통계량을 산출한 결과를 하나로 통합하여 표시하는(combine) 과정을 거칩니다.
    
    - 그룹화 함수 : groupby()
      - 데이터 그룹화를 하기 위해서 Series 혹은 DataFrame에 대하여 .groupby() 함수를 사용합니다. groupby()를 수행하면 결과로 SeriesGroupBy 객체가 생성되어 진다. SeriesGroupBy 객체에 mean()과 같은 함수를 적용하면 그때 그룹화된 그룹에 대하여 평균을 산출한 결과를 얻을 수 있습니다.
    
    - 그룹화 함수 : Series 객체의 groupby() 사용
      - df의 "key1" 열의 값을 기준으로 데이터를 먼저 그룹화를 진행한 뒤에, grouped 변수에 .mean() 함수를 적용하면, “key1” 열의 값을 기준으로 그룹화 된 각각의 그룹에 대하여 “data1” 열 값의 평균을 산출한 결과를 얻을 수 있습니다.
        ```
          df = pd.DataFrame({
              'key1' : ['a', 'a', 'b', 'b', 'a'],
              'key2' : ['one', 'two', 'one', 'two', 'one'],
              'data1': np.random.randn(5),
              'data2': np.random.randn(5)
          })
        grouped = df["data1"].groupby(df["key1"])
        grouped.mean()
        ```
    
    - 그룹화 함수 : DataFrame 객체의 groupby() 사용
      - Series 객체 뿐만 아니라 DataFrame 객체에서도 groupby() 함수를 제공한다.
        ```
          df = pd.DataFrame({
            'key1' : ['a', 'a', 'b', 'b', 'a'],
            'key2' : ['one', 'two', 'one', 'two', 'one'],
            'data1': np.random.randn(5),
            'data2': np.random.randn(5)
          })
          df.groupby("key1").mean()
          df.groupby("key1").count()
          df.groupby(["key1", "key2"]).mean()
          df.groupby(["key1", "key2"]).count()
        ```
    
    - 그룹에 대해 반복문 사용하기
      - 그룹에 대해 반복문을 수행하면 그룹화된 결과물에 대한 확인이 가능합니다.
      - df.groupby("key1")을 실행한 결과를 반복문에서 순회할 대상으로 명시한 뒤, name과 group 변수에서 값을 받아서 출력하면, 그룹화 기준 열의 값과 그룹화된 결과물을 확인 가능
        ```
          for name, group in df.groupby("key1"):
              print(name)
              print(group)
        ```

        ```
          for (k1, k2), group in df.groupby(["key1","key2"]):
              print(k1, k2)
              print(group)
        ```
  
  6. Pandas
    - 파일 읽어 오기
      ```
        import pandas as pd

        # train.csv 파일을 읽어옵니다. 여기서 PassengerId라는 컬럼을 인덱스(index)로 지정
        # 변수에 할당한 결과값은 데이터프레임(DataFrame)
        train = pd.read_csv("data/train.csv",  index_col="PassengerId")

        # train 변수에 할당된 데이터의 행렬 사이즈를 출력합니다. 출력은 (row, column) 으로 표시됩니다.
        print(train.shape)

        # 이후 .head()로 train 데이터프레임의 전체가 아닌 상위 5개를 띄웁니다.
        train.head()

        # 인덱스(index)를 가져옵니다. 여기서 index는 PassengerId와 동일합니다.
        train.index

        # 컬럼(columns)을 가져옵니다.
        train.columns
      ```
    
    - 행렬 : 열(column) 가져오기
      ```
        train["Survived"].head()
        train[["Sex", "Pclass", "Survived"]].head()
        columns = ["Sex", "Pclass", "Survived"]
        train[columns].head()
      ```
    
    - 행렬 : 행(row) 가져오기
      ```
        train.loc[1]
        train.loc[1:7]
        train.loc[[1, 3, 7, 13]]

        passenger_ids = [1, 3, 7, 13]
        train.loc[passenger_ids]
      ```
    
    - 행렬 동시에 가져오기
      ```
        train.loc[1, "Sex"]
        train.loc[1, ["Pclass", "Sex", "Survived"]]
        train.loc[[1, 3, 7, 13], "Sex"]
        train.loc[1:7, "Sex"]
        train.loc[[1, 3, 7, 13], ["Sex", "Pclass", "Survived"]]
      ```
    
    - Boolean Mask
      ```
        train[train["Sex"] == "male"].head()
        train[train["Fare"] > 20].head()
        train[train["Embarked"].isin(["Q", "S"])].head()
        train[train["Age"].isnull()].head()
        train[train["Age"].notnull()].head()
        train[~train["Age"].isnull()].head()
        train[(train["Age"].isnull()) | (train["Fare"].isnull())].head()
        train[(train["Age"].isnull()) & (train["Fare"].isnull())]
      ```
    
    - 기본 연산
      ```
        print(train["Fare"].mean())
        print(train["Age"].max())
        print(train["Age"].min())
      ```
    
    - 컬럼 추가 & 수정
      ```
        train["DataCategory"] = "Titanic“
        train["Id"] = range(0, 891)
        train["FamilySize"] = train["SibSp"] + train["Parch"] + 1
        train[["SibSp", "Parch", "FamilySize"]].head()
        train["Nationality_FR"] = train["Embarked"] == "C"
        train["Nationality_UK"] = train["Embarked"].isin(["S", "Q"])
      ```

      ```
        train.loc[train["Embarked"] == "C", "Nationality"] = "France"
        train.loc[train["Embarked"].isin(["S", "Q"]), "Nationality"] = "England“

        train["Fare_Cheap"] = train["Fare"] < 30
        train["Fare_Medium"] = (train["Fare"] >= 30) & (train["Fare"] < 100)
        train["Fare_Expensive"] = train["Fare"] >= 100

        train.loc[train["Fare"] < 30, "FareType"] = "Cheap"
        train.loc[(train["Fare"] >= 30) & (train["Fare"] < 100), "FareType"] = "Med"
        train.loc[train["Fare"] >= 100, "FareType"] = "Expensive“
        
        mean_age = train["Age"].mean()
        train.loc[train["Age"].isnull(), "Age"] = mean_age
      ```
  
  7. PyMySQL 모듈
    - Pymysql 이란?
      1. mysql을 python에서 사용할 수 있는 라이브러리
      2. http://pymysql.readthedocs.io/en/latest/index.html
      3. pip install pymysql
    
    - 일반적인 mysql 핸들링 코드 작성 순서
      1. PyMySql 모듈 import
      2. pymysql.connect() 메소드를 사용하여 MySQL에 연결 및 호스트명, 포트, 로그인, 암호, 접속할 DB 등을 파라미터로 지정
      3. MySQL 접속이 성공하면, Connection 객체로부터 cursor() 메서드를 호출하여 Cursor 객체를 가져옴
      4. Cursor 객체의 execute() 메서드를 사용하여 SQL 문장을 DB 서버에 전송
      5. SQL 쿼리의 경우 Cursor 객체의 fetchall(), fetchone(), fetchmany() 등의 메서드를 사용하여 서버로부터 가져온 데이터를 코드에서 활용
      6. 삽입, 갱신, 삭제 등의 DML(Data Manipulation Language) 문장을 실행하는 경우, INSERT/UPDATE/DELETE 후 Connection 객체의 commit() 메서드를 사용하여 데이터를 확정
      7. Connection 객체의 close() 메서드를 사용하여 DB 연결을 닫음

      ```
        import pymysql

        # MySQL Connection 연결
        conn = pymysql.connect(host='localhost', user='python', password='1111!', db='python_db', charset='utf8') #autocommit=True
        print('pymysql.version : ',pymysql.__version__)

        #데이터베이스 선택
        conn.select_db('python_db')

        #Cursor연결
        c = conn.cursor()
        try:
          with conn.cursor() as c:
              #데이터 삽입(개별)
              c.execute("INSERT INTO users VALUES (1 ,'kim','kim@naver.com',\ '010-0000-0000', 'kim.com', %s)", (nowDatetime,))
          conn.commit()
        finally:
          conn.close()
      ```
  
  8. SqlAlchemy (SQL Toolkit and Object Relational Mapper)
    1. SQLAlchemy는 관계형 데이터베이스에 강력하고 유연한 인터페이스를 제공하는 Python SQL Toolkit이며, Object Relation Mapper(ORM)입니다. ORM은 객체를 관계형 DB 테이블에 매핑 해주는 역할을 하는데 SQLAlchemy는 객체를 매핑하기 위해 특정 클래스를 상속받지 않아도 되기 때문에 높은 수준의 라이브러리라고 할 수 있습니다.
    2. SQLAlchemy는 데이터 매퍼 패턴을 제공하는 옵션 구성 요소 인 ORM (Object-Relational Mapper)으로 가장 유명합니다.
    3. Mike Bayer 이라는 개발자가 2005년에 발표(https://www.sqlalchemy.org/)
      ```
        공식 소스코드 저장소 :
        https://github.com/zzzeek/sqlalchemy

        설치 : 파이썬 팩키지 매니저인 pip를 이용

        쉘> pip install sqlalchemy

        쉘> pip show sqlalchemy
        Name: SQLAlchemy
        Version: 1.2.13
        Summary: Database Abstraction Library
        Home-page: http://www.sqlalchemy.org
        Author: Mike Bayer
        Author-email: mike_mp@zzzcomputing.com
        License: MIT License
        Location: c:\users\vega2k\miniconda3\lib\site-packages
        Requires:
      ```
  
  9. SQLAlchemy 모듈
    - SQLAlchemy와 PyMySQL을 사용하여 DataFrame을 Table로 저장하기
      ```
        import pandas as pd
        import pymysql

        pymysql.install_as_MySQLdb()
        from sqlalchemy import create_engine

        try:
            #엔진 생성
            engine = create_engine\
            ("mysql+mysqldb://python:"+"1111!"+"@localhost/python_db", encoding='utf-8')
            conn = engine.connect()
            df.to_sql(name='employee', con=engine,if_exists='append')
        finally:
            #모든 커넥션을 닫는다.
            conn.close()
            engine.dispose()
      ```
  
  10. Pandas DataFrame의 methods
    - read_csv() : csv file read
      ```
        df = pd.read_csv('baseballdatabank-master/core/Salaries.csv')
      ```
    - read_excel() : excel file read
      ```
        df = pd.read_excel('data\example.xlsx',sheet_name='Sheet1', index_col='park.key')
      ```
    - to_csv() : csv file write
      ```
        df = pd.to_csv(‘data/Salaries.csv‘,index=False)
      ```
    - to_excel() : excel file write
      ```
        df_name.to_excel('emp_output.xlsx', sheet_name = 'Sheet1')
      ```
    - to_sql() : table write
      ```
        df.to_sql(name='employee', con=engine, if_exists='append')
      ```

#### 데이터 시각화 라이브러리 – matplotlib, seaborn
  1. matplotlib의 개요
    - matplotlib 란?
      - matplotlib은 numpy나 pandas를 사용하여 데이터를 분석한 결과를 시각화 하는 데 사용되는 대표적인 Python 데이터 시각화 라이브러리입니다. matplotlib에서는 DataFrame 혹은 Series 형태의 데이터를 가지고 다양한 형태의 플롯을 만들어 주는 기능을 지원합니다.
      - https://matplotlib.org/
  
    - 플롯팅 옵션 지정
      - 플롯을 그리기에 앞서, %matplotlib라는 플롯팅 옵션을 먼저 지정해야 jupyter notebook에서 그래프를 그려줄 수 있다.
      - %matplotlib nbagg 설정은, 생성되는 플롯을 인터랙티브 하게 조작할 수 있음.
      - %matplotlib inline 설정은 , 플롯을 일단 생성하면 이를 조작할 수 없음.
        ```
          %matplotlib inline
        ```
    
    - 필요한 library import
      ```
        import matplotlib
        import matplotlib.pyplot as plt
        print(matplotlib.__version__)
      ```

  2. 용어 정의
    - Figure
      - Figure는 그림이 그려지는 도화지라고 생각하면 됩니다.
        1. 우선 Figure를 그린 후, plt.subplots로 도화지를 분할해 각 부분에 그래프를 그리는 방식으로 진행합니다.
        2. size를 조절하고 싶은 경우엔 fig.set_size_inches(18.5, 10.5) 또는 plt.figure(figsize=(10,5)) 또는 plt.rcParams['figure.figsize'] = (10,7)
    - Axes
      - Axes는 plot이 그려지는 공간입니다.
    - Axis
      - plot의 축입니다.
  
  3. Seaborn의 개요
    - Seaborn 이란?
      - seaborn은 matplotlib을 기반으로 다양한 색 테마, 차트 기능을 추가한 라이브러리입니다
      - matplotlib에 의존성을 가지고 있습니다
      - matplotlib에 없는 그래프(히트맵, 카운트플랏 등)을 가지고 있습니다
      - https://seaborn.pydata.org/
    - 필요한 library import
      ```
        import seaborn
        print(matplotlib.__version__)
        sns.set
      ```

### 2.13 15일차(2022-02-09)

### 2.14 16일차(2022-02-10)

#### Python Web Programming with Django
  1. Django 개요
    1. Django (Python Full stack Web Framework)
      - Django(/dʒæŋɡoʊ/ jang-goh/쟁고/장고)는 Python으로 만들어진 무료 오픈소스 웹 애플리케이션 프레임워크(web application framework)
      - 쉽고 빠르게 웹사이트를 개발할 수 있도록 돕는 구성요소로 이루어진 웹 프레임워크
      - 백엔드를 담당하는Lawrence Journal-World 신문사에서 2003년부터 개발하여, 2005년에 세상에 공개
      - 2008년에 1.0 릴리즈 (Django Roadmap)
      - 기타리스트 Django Reinhardt 이름을 따서, Django (쟁고, 장고)
      - Django 와 비슷한 웹프레임워크들
        - Flask : a micro framework for Python based on Werkzeug.
        - Pyramid : a small, fast, down-to-earth
        - Bottle : a fast and simple micro framework for small web-applications
    
    2. Django 설치 및 버전 확인
      - Pypi에서 Django 확인해 보기 (https://pypi.org/project/Django/)
      - Django 에서의 LTS(Long Term Support) 버전 대개 3년 동안 업데이트를 지원 (Django Roadmap)
      - 공식 소스코드 저장소 : http://github.com/django/django
      - 설치 : 파이썬 팩키지 매니저인 pip를 이용
      - 쉘> pip install django==3.1.13
      - 쉘> django-admin --version

    3. MTV 개발 방식
      - MTV(Model Template View) 패턴
        1. Model : 테이블을 정의한다
        2. Template : 사용자가 보게 될 화면의 모습을 정의한다.
        3. View : 애플리케이션의 제어 흐름 및 처리 로직을 정의한다.

        - 모델은 model.py파일에, 템플릿은 templates 디렉토리 하위의 *.html 파일에, 뷰는 views.py 파일에 작성하도록 처음부터 뼈대를 만들어 줍니다. 
        - 모델,템플릿,뷰 모듈 간에 독립성을 유지할 수 있고, 소프트웨어 개발의 중요한 원칙인 느슨한 결합(Loose Coupling) 설계의 원칙에도 부합된다.
        - Django에서 프로젝트를 생성하기 위해 startproject 및 startapp 명령을 실행하면 자동으로 프로젝트 뼈대(skeleton)에 해당하는 디렉토리와 파일들을 만들어 줍니다.
        - Django’s Architecture (https://djangobook.com/mdj2-django-structure/)

  2. Django 시작
    1. Django 프로젝트 생성
      - mypython 폴더 아래에 mydjango 하위 폴더를 생성한다.
        ```
          mypython> django-admin startproject mydjango
        ```
          - manage.py : 웹사이트 관리를 도와주는 역할을 하는 파일
          - settings.py : 웹사이트 설정이 있는 파일
          - urls.py : urlresolver가 사용하는 요청 패턴(URL규칙) 목록을 포함하고 있는 파일
          - wsgi.py : Web Server Gateway Interface이며 Python의 표준 Gateway Interface 입니다.
          - asgi.py : Asynchronous Server Gateway Interface WSGI와 비슷한 구조를 가지며, 비동기 통신을 지원한다.
    
    2. Django 프로젝트 설정 변경
      - settings.py의 LANGUAGE_CODE와 TIME_ZONE 변경하기
        ```
          # mydjango/settings.py  <- 파일경로

          LANGUAGE_CODE = 'ko'
          TIME_ZONE = 'Asia/Seoul
        ```
      - settings.py에 정적 파일 경로를 추가함 STATIC_URL항목 바로 아래에 STATIC_ROOT을 추가
        ```
          import os
          STATIC_URL = '/static/'
          STATIC_ROOT = os.path.join(BASE_DIR, STATIC_URL)
        ```
    
    3. Django 프로젝트 DB 생성과 Server 시작
      - 데이터베이스를 생성
        `mypython> python manage.py migrate`
          - db.sqlite3 파일이 생성됨
      - Server 시작
        `mypython> python manage.py runserver`
    
    4. Superuser 생성 및 관리자 화면
      - Superuser 계정 생성
        `mypython> python manage.py createsuperuser`
          - password를 체크 하므로 너무 짧거나 간단한 글자로 입력하면 안됩니다.
      - http://localhost:8000/admin/ 으로 접속
  
  3. Blog App 작성 : Model클래스와 테이블
    1. Django Model
      - Django 내장 ORM(Object Relational Mapping) 
      - ( https://docs.djangoproject.com/en/3.0/topics/db/models/ )
      - SQL을 직접 작성하지 않아도, Django Model을 통해 데이터베이스로의 접근가능 (조회/추가/수정/삭제)
      - <Python 클래스> 와 <데이터베이스 테이블> 을 매핑
        - Model : DB 테이블과 매핑
        - Model Instance : DB 테이블의 1 Row
        - blog앱 Post모델 : blog_post 데이터베이스 테이블과 매핑
        - blog앱 Comment모델 : blog_comment 데이터베이스 테이블과 매핑
      - 커스텀 모델 정의 (blog/models.py)
      - 데이터베이스 테이블 구조/타입을 먼저 설계를 한 다음에 모델 정의, 모델 클래스명은 단수형 (Posts가 아니라, Post)
        ```
          from django.db import models
          class Post(models.Model):
            title = models.CharField(max_length=100)
            content = models.TextField()
            created_at = models.DateTimeField(auto_now_add=True)
            updated_at = models.DateTimeField(auto_now=True)
        ```
    
    2. 지원하는 모델필드 타입 #ref
      - Field Types
        ```
          AutoField, BigInteger, BinaryField,BooleanField, CharField, DateField, DateTimeField,DecimalField, DurationField, EmailField, FileField,ImageField, IntegerField, GenericIPAddressField, PositiveIntegerField, PositiveSmallIntegerfield, SlugField, TextField, URLField, UUIDField 등
        ```
      - Relationship Types
        `ForeignKey, ManyToManyField, OneToOneField`
    
    3. 데이터 타입 매핑
      - 파이썬 데이터타입과 데이터베이스 데이터타입을 매핑
        ```
          AutoField (int), BinaryField (bytes), BooleanField (bool), NullBooleanField (None, bool), CharField/TextField/ EmailField/GenericIPAddressField/SlugField/URLField(str)
        ```
      - 같은 파이썬 데이터 타입에 매핑 되더라도, "데이터 형식" 에 따라 여러 Model Field Types 로 나뉨
    
    4. 필드 옵션
      - 자주 쓰는 필드 옵션
        - null (DB 옵션) : DB 필드에 NULL 허용 여부 (디폴트 : False)
        - unique (DB 옵션) : 유일성 여부
        - blank : 입력값 유효성(validation)검사할 때 empty값 허용여부(디폴트:False)
        - default : 디폴트 값 지정. 값이 지정되지 않았을 때 사용
        - choices (form widget 용) : select box source로 사용
        - validators : 입력 값 유효성 검사를 수행할 함수를 다수 지정, 각 필드마다 고유한 validators 들이 이미 등록되어 있기도 함 ( 이메일만 받기, 최대길이 제한, 최소길이 제한, 최대값 제한, 최소값 제한, etc)
        - verbose_name : 필드 레이블. 지정되지 않으면 필드명이 쓰여짐.
        - help_text (form widget 용) : 필드 입력 도움말
    
    5. 첫번째 앱 <blog> 앱 생성
      1. App 디렉토리 생성
        `mypython> python manage.py startapp blog`
          - django/conf/app_template 구성으로 App 디렉토리가 생성되어진다.
      2. App을 프로젝트에 등록 : 아래와 같이 mydjango/settings.py을 편집하여, INSTALLED_APPS 항목 끝에 blog App 이름을 추가한다
        ```
          INSTALLED_APPS = [
            # 생략
            'blog',
          ]
        ```
    
    6. blog앱 글(Post) Model 만들기
      1. Post(게시글)의 속성들
        - title(제목)
        - text(내용)
        - author(글쓴이)
        - created_date(작성일)
        - published_date(게시일)
      
      2. Model 객체는 blog/models.py 파일에 선언하여 모델을 만듭니다. 이 Model을 저장하면 그 내용이 데이터베이스에 저장되는 것입니다.

        ```
          from django.db import models
          from django.utils import timezone

          # Create your models here.
          class Post( models.Model):
              # 작성자
              author = models.ForeignKey ('auth.User', on_delete = models.CASCADE)
              # 제목
              title = models.CharField (max_length = 200)
              # 내용
              text = models.TextField()
              # 작성일
              created_date = models.DateTimeField ( default=timezone.now)
              # 게시일
              published_date = models.DateTimeField (blank=True , null=True)

        ```
      
    7. DB에 테이블 만들기
      1. 마이그레이션 파일(migration file) 생성하기
        ```
          mypython> python manage.py makemigrations blog

          # 정상 출력 결과
          Migrations for 'blog':
            blog\migrations\0001_initial.py
            - Create model Post
        ```
      2. 실제 데이터베이스에 Model 추가를 반영하기
        ```
          mypython> python manage.py migrate blog

          # 정상 출력 결과
          Operations to perform:
            Apply all migrations: blog
          Running migrations:
            Applying blog.0001_initial... OK
        ```

### 2.15 17일차(2022-02-11)

#### Python Web Programming with Django 지난 수업 이어서

    8. Django Admin(관리자)
      1. 관리자 페이지에서 만든 모델을 보기 위해 Post 모델을 등록
        ```
          # blog/admin.py

          from django.contrib import admin
          from .models import Post

          admin.site.register(Post)
        ```
      2. 관리자 화면에서 확인하기
        - http://localhost:8000/admin/ 으로 접속
    
    9. Migrations #ref
      1. django-south(https://south.readthedocs.io/en/latest/) 프로젝트가 킥스타터 펀딩 (£17,952, 507 Backers)을 통해, Django 1.7에 포함
        - 모델 변경내역 히스토리 관리
        - 모델의 변경내역을 Database Schema (데이터베이스 데이터 구조)로 반영시키는 효율적인 방법을 제공
      2. 관련 명령
        - 쉘> python manage.py makemigrations <app-name> # 마이그레이션 파일 생성
        - 쉘> python manage.py migrate <app-name> # 마이그레이션 적용
        - 쉘> python manage.py showmigrations <app-name> # 마이그레이션 적용 현황
        - 쉘> python manage.py sqlmigrate <app-name> <migration-name>   # 지정 마이그레이션의 SQL 내역

    10. migration 파일 생성 및 적용
      1. 마이그레이션 파일 (초안) 생성하기 : makemigrations 명령
      2. 해당 마이그레이션 파일을 DB에 반영하기 : migrate 명령
    
    11. Migrate (Forward/Backward)
      1. 쉘> python manage.py migrate <app-name>
        - 미적용 <마이그레이션 파일> 부터 <최근 마이그레이션 파일> 까지
        - "Forward 마이그레이션" 이 순차적으로 수행
      2. 쉘> python manage.py migrate <app-name> <마이그레이션 파일명>
        - <지정된 마이그레이션 파일> 이 <현재 적용된 마이그레이션> 보다 이후이면, "Forward 마이그레이션" 이 순차적으로 수행 이전이면, "Backward 마이그레이션" 이 순차적으로 수행 (롤백)
        - 전체 파일명을 지정 하지 않더라도, 유일한 1개의 파일명을 판독 가능하면, 파일명 일부로도 지정 가능
          ```
            blog/migrations/0001_initial.py
            blog/migrations/0002_create_field.py
            blog/migrations/0002_update_field.py
            python manage.py migrate blog 000 # FAIL (다수 파일에 해당)
            python manage.py migrate blog 100 # FAIL (해당되는 파일이 없음)
            python manage.py migrate blog 0001 # OK
            python manage.py migrate blog 0002 # FAIL (다수 파일에 해당)
            python manage.py migrate blog 0002_c # OK
            python manage.py migrate blog 0002_create # OK
            python manage.py migrate blog 0002_update # OK
            python manage.py migrate blog zero # blog앱의 모든 마이그레이션을 취소
          ```
    
    12. 필수 입력 필드를 추가
      - 기존 모델 클래스에 필수 필드를 추가하여 makemigrations 수행
      - 필수 입력 필드를 추가하므로, 기존 Row들에 필드를 추가할 때, 어떤 값으로 채워 넣을 지 묻습니다.
        1. 선택1> 지금 값을 입력
        2. 선택2> 모델 클래스를 수정하여 디폴트 값을 제공
  
  4. Blog App 작성 : URL Routing
    1. Django URLConf (configuration)란?
      - 프로젝트/settings.py 에 최상위 URLConf 모듈을 지정
        - URLConf는 장고에서 URL과 일치하는 view를 찾기 위한 패턴들의 집합이다.
        - 특정 URL과 View 매핑 List
        - Django 서버로 Http 요청이 들어올 때마다, URLConf 매핑 List를 처음부터 끝까지 순차적으로 찾으며 검색합니다.
          ```
            from django.conf.urls import include, url
            from django.contrib import admin

            Urlpatterns = [
                url(r'^admin/', admin.site.urls),
                url(r'', include('blog.urls')),
            ]
          ```

    2. 정규 표현식(Regex)
      1. 정규 표현식이란?
        - 문자열의 패턴, 규칙, Rule을 정의하는 방법
      2. 파이썬3 정규 표현식 라이브러리
        - https://docs.python.org/3/library/re.html
      3. 정규 표현식 예시
        - 최대 3자리 숫자 : "[0-9]{1,3}" 혹은 "\d{1,3}"
        - 휴대폰번호 : "010[1-9]\d{7}“
        - 한글이름 2글자 혹은 3글자 : "[ㄱ-힣]{2,3}"
        - 성이 "이" 인 이름 : "이[ㄱ-힣]{1,2}"
      4. 다양한 1글자 패턴
        - 숫자 1글자 : "[0123456789]" 또는 "[0-9]" 또는 "\d"
        - 알파벳 소문자 1글자 : "[abcdefghijklmnopqrstuvwxyz]" 혹은 "[a-z]"
        - 알파벳 대문자 1글자 : "[ABCDEFGHIJKLMNOPQRSTUVWXYZ]" 혹은 "[A-Z]"
        - 알파벳 대/소문자 1글자 : "[a-zA-Z]"
        - 16진수 1글자 : "[0-9a-fA-F]"
        - 문자열의 시작을 지정 : "^"
        - 문자열의 끝을 지정 : "$"
        - 한글 1글자 : "[ㄱ-힣]"
      5. 반복횟수 지정
        - "\d?" : 숫자 0회 또는 1회
        - "\d*" : 숫자 0회 이상
        - "\d+" : 숫자 1회 이상
        - "\d{m}" : 숫자 m글자
        - "\d{m,n}" : 숫자 m글자 이상, n글자 이하
        - 주의 : 정규 표현식은 띄워 쓰기 하나에도 민감합니다.
      6. 휴대폰 번호 example
        ```
          import re
          def validate_phone_number(number):
            if not re.match(r'^01[016789][1-9]\d{6,7}$', number):
                return False
            # 후에 Form Validator에서는 forms.ValidationError예외를 발생시킴
            return True
          print(validate_phone_number('01012341234')) # True
          print(validate_phone_number('010123412')) # False
          print(validate_phone_number('01012341234a')) # False
        ```
      7. url 매핑 example
        - http://www.mysite.com/post/12345/라는 요청이 있을 때 12345는 글번호 정규표현식으로 url 패턴을 만들어 숫자 값과 매칭되게 할 수 있음 
        - ^post/(\d+)/$.
          - ^post/ : url이(오른쪽부터) post/로 시작합니다
          - (\d+) : 숫자(한 개 이상)가 있습니다. 
          - / : /뒤에 문자가 있습니다.
          - $ : url 마지막이 /로 끝납니다.
    
    8. Django URLConf (configuration) 설정하기
      1. main urls.py
        - admin/로 시작하는 모든 URL을 view와 매핑하여 찾아냅니다.
        - http://127.0.0.1:8000/' 요청이 오면 views.post_list를 보여준다.
          ```
            # mydjango/urls.py

            from django.contrib import admin
            from django.urls import path
            from blog import views

            urlpatterns = [
                path('admin/', admin.site.urls),
                path('',views.post_list),
            ]
          ```
      2. blog/urls.py
        - blog/urls.py를 작성하여 blog와 관련된 url들을 따로 정의함
          ```
            # mydjango/urls.py

            from django.contrib import admin
            from django.urls import path, include

            urlpatterns = [
                path('admin/', admin.site.urls),
                path('', include('blog.urls')),
            ]
          ```
        
        - 'http://127.0.0.1:8000/' 요청이 오면 views.post_list를 보여준다.
          ```
            # blog/urls.py

            from django.urls import path
            from . import views

            urlpatterns = [
                path('', views.post_list, name='post_list'),
            ]
          ```
        
  5. Blog App 작성 : View
    1. View의 역할
      - View는 애플리케이션의 "로직"을 포함하며 모델에서 필요한 정보를 받아 와서 템플릿에 전달하는 역할을 한다.
      - View는 Model과 Template을 연결하는 역할을 한다.
      - URLConf에 매핑된 Callable Object
        - 첫번째 인자로 HttpRequest 인스턴스를 받습니다.
        - 반드시 HttpResponse 인스턴스를 리턴 해야 합니다.
        - https://docs.djangoproject.com/en/1.11/ref/request-response/
    2. blog/views.py
      - post_list라는 함수(def) 만들어 요청(request)을 받아서 직접 문자열로 HTML형식 응답(response)하기
        ```
          # blog/views.py
          
          from django.http import HttpResponse

          def post_list(request):
              name = '장고'
              return HttpResponse('''<h1>Hello Django</h1>
              <p>{name}</p>'''.format(name=name))
        ```
    3. blog/views.py 수정
      - post_list라는 함수(def) 만들어 요청(request)을 넘겨받아 render 메서드를 호출합니다
      - 함수는 호출하여 받은(return) blog/post_list.html 템플릿을 보여줍니다.
        ```
          # blog/views.py

          from django.shortcuts import render

          def post_list(request):
              return render(request,'blog/post_list.html')
        ```
  
  6. blog App 작성 : Template
    1. Template의 역할
      - Template은 정보를 일정한 형태로 표시하기 위해 재사용 가능한 파일을 말함
      - Django의 template 양식은 HTML을 사용합니다.
      - 템플릿은 blog/templates/blog 디렉토리에 저장합니다.
        ```
          # blog/templates/blog/post_list.html
          
          <html>
              <head>
                  <title>Django blog</title>
              </head>
              <body>
                  <p>Hi there!</p>
                  <p>It works!</p>
              </body>
          </html>
        ```
    2. post_list.html 템플릿 수정
      ```
        # blog/templates/blog/post_list.html

        <html>
            <head>
                <title>Django blog</title>
            </head>
            <body>
                <div>
                    <h1><a href="">Django’s Blog</a></h1>
                </div>

                <div>
                    <p>published: 14.06.2014, 12:14</p>
                    <h2><a href="">My first post</a></h2>
                    <p>Aenean eu leo quam. Pellentesque ornare sem lacinia quam venenatis vestibulum. Donec id elit non mi porta
                    gravida at eget metus. Fusce dapibus, tellus ac cursus commodo, tortor mauris condimentum nibh, ut fermentum massa justo sit
                    amet risus.</p>
                </div>

                <div>
                    <p>published: 14.06.2014, 12:14</p>
                    <h2><a href="">My second post</a></h2>
                    <p>Aenean eu leo quam. Pellentesque ornare sem lacinia quam venenatis vestibulum. Donec id elit non mi porta
                    gravida at eget metus. Fusce dapibus, tellus ac cursus commodo, tortor mauris condimentum nibh, ut f.</p>
                </div>
            </body>
        </html>
      ```
  7. blog App 작성 : ORM과 쿼리셋(QuerySets)
    1. QuerySet이란?
      - 쿼리셋(QuerySet)은 DB로부터 데이터를 읽고, 필터링을 하거나, 정렬을 할 수 있습니다.
      - 쿼리셋을 사용하기 위해 먼저 python shell을 실행한다.
      - 인터렉티브 콘솔(Interactive Console) 실행
        `mypython> python manage.py shell`
    2. 모든 객체 조회하기
      - 모든 객체를 조회하기 위해 all() 함수를 사용합니다. 
        ```
          >>> Post.objects.all()
          Traceback (most recent call last):
                File "<console>", line 1, in <module>
          NameError: name "Post" is not defined

          >>> from blog.models import Post

          >>> Post.objects.all()
          <QuerySet> [<Post: my post title>, <Post: another post title>]
        ```
    3. 객체 생성하기
      1. 객체 생성
        - 객체를 저장하기 위해 create() 함수를 사용합니다.
        - 작성자(author)로서 User(사용자) 모델의 인스턴스를 가져와 전달 해줘야 합니다
          ```
            >>> from django.contrib.auth.models import User

            >>> User.objects.all()
            <QuerySet [<User: ola>]>

            >>> me = User.objects.get(username='ola')

            >>> Post.objects.create(author=me, title = 'Sample title', text='Test')

            >>> Post.objects.all()
            <QuerySet [<Post: my post title>, <Post: another post title>]>
          ```
      2. 필터링 하기
        - 원하는 조건으로 데이터를 필터링 한다. filter() 괄호 안에 원하는 조건을 넣어 주면 됩니다.
          1. 특정 사용자가 작성한 글을 찾고자 할 때
            ```
              >>> Post.objects.filter(author=me)
              [<Post: Sample title>, <Post: Post number 2>, <Post: My 3rd post!>, <Post: 4th title of post>]
            ```
          2. 글의 제목(title)에 'title' 이라는 글자가 들어간 글을 찾고자 할 때
            ```
              >>> Post.objects.filter(title__contains='title')
              [<Post: Sample title>, <Post: 4th title of post>]
            ```
          3.  게시일(published_date)로 과거에 작성한 글을 필터링하여 목록을 가져올 때
            ```
              >>> from django.utils import timezone
              >>> Post.objects.filter(published_date__lte=timezone.now())
            ```
          4. 게시(publish)하려는 Post의 인스턴스를 가져온다.
            `>>> post = Post.objects.get(title="Sample title"`
          5. 가져온 Post 인스턴스를 publish() 메서드를 이용하여 게시한다.
            `>>> post.publish()`
          6. 게시일(published_date)로 과거에 작성한 글을 필터링하여 목록을 다시 가져온다.
            ```
              >>> Post.objects.filter(published_date__lte=timezone.now())
              [<Post: Sample title>]
            ```
      3. 정렬하기
        1. 작성일(created_date) 기준으로 오름차순으로 정렬하기
          ```
            >>> Post.objects.order_by('created_date')
            [<Post: Sample title>, <Post: Post number 2>, <Post: My 3rd post!>, <Post: 4th title of post>]
          ```
        2.  작성일(created_date) 기준으로 내림차순으로 정렬하기 : – 을 붙이면 내림차순 정렬
          ```
            >>> Post.objects.order_by('-created_date')
            [<Post: 4th title of post>, <Post: My 3rd post!>,<Post: Post number 2>, <Post: Sample title>]
          ```
        3. 쿼리셋들을 함께 연결(chaining) 하기
          `Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')`

### 2.16 18일차(2022-02-14)

#### Python Web Programming with Django 지난 수업 이어서

  8. blog App 작성 : 템플릿에서 동적 데이터 처리
    - View에서 동적(dynamic) 데이터 생성하기
      1. View의 수정
        - View는 DB에 저장되는 Model에서 정보를 가져올 때 쿼리셋(QuerySet)을 사용하며, 템플릿에 전달하는 역할을 한다.
          - 게시일(published_date) 기준으로 과거에 작성한 글을 필터링하여 정렬하여 글 목록 가져오기
            ```
              # blog/views.py

              from django.shortcuts import render
              from django.utils import timezone
              from .models import Post

              def post_list(request):
                  posts = Post.objects.filter(published_date__lte=timezone.now()).\
                  order_by('published_date')
                  return render(request, 'blog/post_list.html', {'posts': posts})
            ```
    - Template에서 동적(dynamic) 데이터 사용하기
      2. Template의 수정 1
        - Template에서는 view에서 저장한 posts 변수를 받아와서 HTML에 출력한다.
        - 변수의 값을 출력하려면 중괄호를 사용한다.
        - {% for %} 와 {% endfor %} 사이에서 목록의 모든 객체를 반복하여 출력함.
          ```
            # blog/templates/blog/post_list.html

            <div>
                <h1><a href="/">Django’s Blog</a></h1>
            </div>

            {% for post in posts %}
                {{ post }}
            {% endfor %}
          ```
      3. Template의 수정 2
        - |linebreaksbr 같이 파이프 문자(|)를 사용하여, 블로그 글 텍스트에서 행이 바뀌면 문단으로 변환하여 출력한다.
          ```
            # blog/templates/blog/post_list.html
            
            <div>
                <h1><a href="/">Django’s Blog</a></h1>
            </div>

            {% for post in posts %}
                <div>
                    <p>published: {{ post.published_date }}</p>
                    <h1><a href="">{{ post.title }}</a></h1>
                    <p>{{ post.text|linebreaksbr }}</p>
                </div>
            {% endfor %}
          ```
    - Template Engine
      - Django Template Engine : Django 기본 지원 템플릿 엔진
      - https://docs.djangoproject.com/en/3.0/topics/templates/
      - Django Template Engine Syntax
        ```
          {% extends "base.html" %}
          {% for row in rows %}
              <tr>
                  {% for name in row %}
                      <td>{{ name }}</td>
                  {% endfor %}
              </tr>
          {% endfor %}
        ```
    
    - Template Engine 문법
      1. Variables
        - {{ first_name }}
        - {{ mydict.key }} : dict의 key에 attr 처럼 접근
        - {{ myobj.attr }}
        - {{ myobj.func }} : 함수 호출도 attr 처럼 접근. 인자 있는 함수 호출 불가
        - {{ mylist.0 }} : 인덱스 접근도 attr 처럼 접근
      2. Django Template Tag
        - {% %} 1개 쓰이기도 하며, 2개 이상이 조합되기도 함.
        - 빌트인 Tag가 지원되며, 장고앱 별로 커스텀 Tag 추가 가능
          ```
            block, comment, csrf_token, extends, for, for ... empty, if, ifchanged, include, load, lorem, now, url, verbatim, with 등
          ```
      3. block tag
        - 템플릿 상속에서 사용
        - 자식 템플릿이 오버라이딩 할 block 영역을 정의
        - 자식 템플릿은 부모가 정의한 block에 한해서 재 정의만 가능. 그 외는 모두 무시됩니다/
          ```
            {% block block-name %}
                block 내에 내용을 쓰실 수 있습니다.
            {% endblock %}
          ```
      4. Comment Tag : 템플릿 주석
        ```
          {% comment "Optional note" %}
              이 부분은 렌더링 되지 않습니다.
          {% endcomment %}
        ```
      5. csrf_token tag
        - Cross Site Request Forgeries를 막기 위해 CSRF Middleware가 제공됨
        - 이는 HTML Form의 POST요청에서 CSRF토큰을 체크하며, 이때 CSRF토큰이 필요
        - csrf_token tag를 통해 CSRF토큰을 발급받을 수 있습니다
          ```
            <form method="POST" action="">
                {% csrf_token %}
                <input type="text" name="author" />
                <textarea name="message"></textarea>
                <input type="submit" />
            </form>
          ```
      6. extends tag
        - 자식 템플릿에서 부모 템플릿 상속을 명시
        - extends tag는 항상 템플릿의 처음에 위치해야 합니다
        - 상속받은 자식 템플릿은 부모 템플릿에서 정의한 block만 재정의할 수 있습니다.
          `{% extends "base.html" %}`
      7. for tag
        - 지정 객체를 순회하며 파이썬의 for문과 동일
          ```
            {% for athlete in athlete_list %}
                <li>{{ athlete.name }}</li>
            {% endfor %}
          ```
      8. for ... empty tag
        - for tag 내에서 지정 object를 찾을 수 없거나, 비었을 때 empty block이 수행
          ```
            {% for athlete in athlete_list %}
                <li>{{ athlete.name }}</li>
            {% empty %}
                <li>Sorry, no athletes in this list.</li>
            {% endfor %}
          ```
      9. if tag
        - 파이썬의 if문과 동일
          ```
            {% if athlete_list %}
                Number of athletes: {{ athlete_list|length }}
            {% elif athlete_in_locker_room_list %}
                Athletes should be out of the locker room soon!
            {% else %}
                No athletes.
            {% endif %}
          ```
      10. url tag
        - URL Reverse를 수행한 URL문자열을 출력
        - 인자 처리는 django.shortcuts.resolve_url 함수와 유사하게 처리하나, get_absolute_url 처리는 하지 않음.
          ```
            {% url "some-url-name-1" %}
            {% url "some-url-name-2" arg arg2 %}
            {% url "some-url-name-2" arg arg2 as the_url %}
          ```
  9. blog App 작성 : 템플릿에 CSS 적용하기
    - 정적(static) 파일 처리하기
      1. CSS 파일 작성
        - static 디렉토리 안에 css 디렉토리를 만들고 blog.css라는 파일을 작성.
          ```
            # blog/static/css/blog.css
            
            h1 a {
                color: #FCA205;
                font-family: 'Lobster';
            }
            body { padding-left: 15px;}
          ```

          ```
            # blog/templates/blog/post_list.html

            {% load static %}
            <html>
                <head>
                    <title>Django's blog</title>
                    <link rel="stylesheet" href="{% static 'css/blog.css' %}">
                </head>
          ```
      2. 부트스트랩(Bootstrap) 적용하기
        - Bootstrap을 설치하려면.html파일 내 <head>에 아래의 링크를 넣어야 합니다.
          ```
            # blog/templates/blog/post_list.html

            {% load static %}
            <html>
                <head>
                    <title>Django's blog</title>
                    <link rel="stylesheet"
                    href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.2/css/bootstrap.min.css">
                    <link rel="stylesheet"
                    href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.2/css/bootstrap-theme.min.css">
                    <link rel="stylesheet"
                    href="http://fonts.googleapis.com/css?family=Lobster&subset=latin,latin-ext"
                    type="text/css">
                    <link rel="stylesheet" href="{% static 'css/blog.css' %}">
                </head>
          ```
      3. 완성된 blog.css
        ```
          # blog/static/css/blog.css
          
          .page-header {
              background-color: #ff9400;
              margin-top: 0;
              padding: 20px 20px 20px 40px;
          }
          .page-header h1, .page-header h1 a, .page-header h1 a:visited, .page-header h1 a:active {
              color: #ffffff;
              font-size: 36pt;
              text-decoration: none;
          }
          .content { margin-left: 40px; }
          h1, h2, h3, h4 { font-family: 'Lobster', cursive; }
          .date { color: #828282; }
          .save { float: right; }
          .post-form textarea, .post-form input { width: 100%; }
          .top-menu, .top-menu:hover, .top-menu:visited {
              color: #ffffff;
              float: right;
              font-size: 26pt;
              margin-right: 20px;
          }
          .post { margin-bottom: 70px; }
          .post h1 a, .post h1 a:visited { color: #000000; }
        ```
      4. 완성된 post_list.html
        ```
          # blog/templates/blog/post_list.html

          <body> 
          <div class="page-header"> 
              <h1><a href="/">Django Blog</a></h1>
          </div>
          <div class="content container"> 
              <div class="row">
                  <div class="col-md-8">
                      {% for post in posts %} 
                        <div class="post"> 
                            <div class="date"> 
                                <p>published: {{ post.published_date }}</p>
                            </div>
                            <h1><a href="">{{ post.title }}</a></h1>
                            <p>{{ post.text|linebreaksbr }}</p>
                        </div>
                      {% endfor %}
                  </div>
              </div>
          </div>
          </body>
          </html>
        ```
  
  10. blog App 작성 : 템플릿 상속하기(Template Inheritance)
    1. Template 상속(Inheritance) 하기
      - Template 상속(Inheritance)이란?
        - Template 상속을 사용하면 동일한 정보/레이아웃을 사용 하고자 할 때, 모든 파일마다 같은 내용을 반복해서 입력 할 필요가 없게 됩니다.
        - 또한 수정할 부분이 생겼을 때도, 각각 모든 파일을 수정 할 필요 없이 한번만 수정하면 됩니다.
      - 기본 템플릿 html 생성하기
        - 기본 템플릿은 웹사이트 내 모든 페이지에 확장되어 사용되는 가장 기본적인 템플릿입니다.
        - blog/templates/blog/에 base.html 파일을 생성한다.
        - post_list.html에 있는 모든 내용을 base.html에 아래 내용을 복사해 붙여 넣는다.
    2. 기본 템플릿 작성하기
      - {% for post in posts %}{% endfor %} 사이에 있는 코드를 제거하고
      - {% block content %}{% endblock %} 으로 변경한다. 
        ```
          # blog/templates/blog/base.html

          <body>
              <div class="page-header">
                  <h1><a href="/">Django Blog</a></h1>
              </div>
              <div class="content container">
                  <div class="row">
                      <div class="col-md-8">
                          {% block content %}
                          {% endblock %}
                      </div>
                  </div>
              </div>
          </body>
        ```
      - post_list.html 수정하기
        - {% block content %}와 {% endblock %} 사이에 {% for post in posts %}부터 {% endfor %} 코드를 넣는다.
        - 두 템플릿을 연결하기 위해 {% extends 'blog/base.html' %} 코드를 추가한다.
          ```
            # blog/templates/blog/post_list.html

            {% extends 'blog/base.html' %}

            {% block content %}
                {% for post in posts %}
                    <div class="post">
                        <div class="date">
                            {{ post.published_date }}
                        </div>
                        <h1><a href="">{{ post.title }}</a></h1>
                        <p>{{ post.text|linebreaksbr }}</p>
                        </div>
                {% endfor %}
            {% endblock %}

          ```
  
  11. blog App 작성 : Post Detail (글 상세) 페이지 작성하기

    1. urls.py에 url 추가
      - ^은 "시작"을 뜻합니다.
      - post/란 URL이 post 문자를 포함해야 한다는 것을 말합니다
      - (?P<pk>\d+) 정규표현식은 장고가 pk 변수에 값을 넣어 view로 전송하겠다는 뜻입니다, \d은 숫자만 올 수 있다는 것을 말합니다. +는 하나 또는 그 이상의 숫자가 올 수 있습니다
      - /은 다음에 / 가 한 번 더 와야 한다는 의미입니다.
      - $는 "마지막"을 말합니다. 그 뒤로 더는 문자가 오면 안 됩니다
      - 따라서 http://127.0.0.1:8000/post/5/라고 입력하면, post_detail view를 찾아 매개변수 pk가 5인 값을 찾아 view로 전달합니다.
        ```
          # blog/urls.py

          from django.urls import path
          from . import views

          urlpatterns = [
              path('', views.post_list, name='post_list'),
              path('post/<int:pk>/', views.post_detail, name='post_detail'),
          ]

        ```

    2. post_list.html에 Post detail 페이지 링크 추가
      - {% %}는 장고 템플릿 태그이며, post_detail은 url에서 정의한 view name이다.
      - post.pk는 Post 모델의 primary key(기본키)를 의미합니다.
        ```
          # blog/templates/blog/post_list.html

          {% extends 'blog/base.html' %}

          {% block content %}
              {% for post in posts %}
                  <div class="post">
                      <div class="date">
                          {{ post.published_date }}
                      </div>
                      <h1><a href="{% url 'post_detail' pk=post.pk %}">{{ post.title }}</a></h1>
                      <p>{{ post.text|linebreaksbr }}</p>
                  </div>
              {% endfor %}
          {% endblock %}
        ```

    3. views.py에 post_detail() 함수 추가
      - def post_detail(request, pk):라고 정의하며, urls(pk)과 동일하게 이름을 사용해야 합니다.
      - 블로그 게시글 한 개만 보려면 Post.objects.get(pk=pk) 쿼리셋을 작성해야 하는데 만약 해당 primary key(pk)의 Post를 찾지 못하면 오류가 날 수 있으므로 Django에서는 이를 해결하기 위해 get_object_or_404라는 특별한 기능을 제공한다.
        ```
          # blog/views.py

          from django.shortcuts import render, get_object_or_404
          from .models import Post

          def post_detail(request, pk):
              post = get_object_or_404(Post, pk=pk)
              return render(request, 'blog/post_detail.html', {'post': post})
        ```
    
    4. post_detail.html 페이지 추가
      - base.html을 확장하고, content블록에서 블로그 글의 게시일, 제목과 내용을 보이게 한다.
      - {% if ... %} ... {% endif %}라는 템플릿 태그에서는 post의 게시일(published_date)이 있는지, 없는지를 확인합니다.
        ```
          # blog/templates/blog/post_detail.html

          {% extends 'blog/base.html' %}

          {% block content %}
              <div class="post">
                  {% if post.published_date %}
                      <div class="date">
                          {{ post.published_date }}
                      </div>
                  {% endif %}
                  <h1>{{ post.title }}</h1>
                  <p>{{ post.text|linebreaksbr }}</p>
              </div>
          {% endblock %}
        ```

  12. blog App 작성 : Django Form (글 추가)

    1. Form이란?
      - Model클래스와 유사하게 Form클래스를 정의
      - 주요 역할 : 커스텀 Form클래스를 통해
        - 입력 폼 HTML 생성 : .as_table(), .as_p(), .as_ul() 기본제공
        - 입력 폼 값 검증(validation) 및 값 변환
    
    2. Form 처리 : HTTP Method에 따라
      - 폼 처리 시에 같은 URL(즉 같은 뷰)에서 GET/POST로 나눠 처리
      - GET방식으로 요청 : 입력 폼을 보여줍니다.
      - POST방식으로 요청 : 데이터를 입력 받아 유효성 검증 과정을 거칩니다.
        - 검증 성공 시 : 해당 데이터를 저장하고 SUCCESS URL로 이동
        - 검증 실패 시 : 오류 메시지와 함께 입력 폼을 다시 보여줍니다.
    
    3. Django Form
      1. step1: Form 클래스 정의
        ```
          from django import forms

          class PostForm(forms.Form):
              title = forms.CharField()
              text = forms.CharField(widget=forms.Textarea)
        ```
      
      2. step2: 필드 유효성 검사 함수 추가 적용
        ```
          from django import forms

          def min_length_3_validator(value):
              if len(value) < 3:
                  raise forms.ValidationError('3글자 이상 입력해주세요.')


          from django import forms

          class PostForm(forms.Form):
              title = forms.CharField(validators=[min_length_3_validator])
              text = forms.CharField(widget=form.Textarea)
        ```
      
      3. step3: View 함수 내에서 Form 인스턴스 생성
        - GET요청을 통해 View 함수가 호출이 될 때, GET/POST 요청을 구분해서 Form 인스턴스 생성
          ```
            # myapp/views.py

            from .forms import PostForm

            if request.method == 'POST':
                # POST 요청일 때
                form = PostForm(request.POST, request.FILES)
            else:
                # GET 요청일 때
                form = PostForm()
          ```
      
      4. step4: POST요청에 한해 입력 값 유효성 검증
        ```
          # myapp/views.py

          if request.method == 'POST':
              # POST인자는 request.POST와 request.FILES를 제공받음.
              form = PostForm(request.POST, request.FILES)
              # 인자로 받은 값에 대해서, 유효성 검증 수행
              if form.is_valid():   # 검증이 성공하면, True 리턴
                  # 검증에 성공한 값들을 dict타입으로 제공받아서 이 값을 DB에 저장하기
                  form.cleaned_data
                  post = Post(**form.cleaned_data) # DB에 저장하기
                  post.save()
                  return redirect('/success_url/')
              else:     # 검증에 실패하면, form.errors와 form.각필드.errors 에 오류정보를 저장
                  form.errors
          else:
              form = PostForm()
          return render(request, 'myapp/form.html', {'form': form})
        ```

      5. step5: 템플릿을 통해 HTML폼 생성
        - 유효성 검증에서 실패했을 때 Form 인스턴스를 통해 HTML폼 출력하고,오류 메시지도 있다면 같이 출력
          ```
            <table>
                <form action="" method="post">
                    {% csrf_token %}
                    <table>{{ form.as_table }}</table>
                    <input type="submit" />
                </form>
            </table>
          ```

    4. Django ModelForm 클래스
      1. Model Form이란?
        - 지정된 Model로부터 필드 정보를 읽어 들여, form fields 를 세팅
          ```
            class PostForm(forms.ModelForm):
                class Meta:
                    model = Post
                    fields = '__all__'    # 전체필드지정 혹은 list로 읽어올 필드명 지정
          ```
        - 내부적으로 model instance를 유지
        - 유효성 검증에 통과한 값들로, 지정 model instance로의 저장 (save)을 지원 (Create or Update)
    
    5. Django Form vs ModelForm
      ```
        from django import forms
        from .models import Post

        class PostForm(forms.Form):
            title = forms.CharField()
            text = forms.CharField(widget=forms.Textarea)
        # 생성되는 Form Field는 PostForm과 거의 동일
        class PostModelForm(forms.ModelForm):
            class Meta:
                model = Post
                fields = ['title', 'text']
      ```
    
    6. Post New ( 글 추가 ) 페이지 작성하기
      1. forms.py 추가
        - ModelForm을 생성해 자동으로 Model에 결과물을 저장할 수 있다.
        - Form을 하나 만들어서 Post 모델에 적용한다.
        - blog 디렉토리 안에 forms.py라는 파일을 작성한다.
          - forms.ModelForm은 django에 이 폼이 ModelForm이라는 것을 알려주는 구문이다
          - class Meta 구문은 Form을 만들기 위해서 어떤 model이 쓰여야 하는지 django에 알려주는 구문, 이 폼에 필드는 title과 text만 보여지게 된다.
          - created_date는 글이 등록되는 시간이다.
            ```
              # blog/forms.py

              from django import forms
              from .models import Post

              class PostForm(forms.ModelForm):
                  class Meta:
                      model = Post
                      fields = ('title', 'text',)
            ```
      
      2. urls.py에 Post New(글 추가) url 추가
        - ^은 "시작"을 뜻합니다.
        -  post/new란 URL이 post 문자를 포함해야 한다는 것을 말합니다
        - /은 다음에 / 가 한 번 더 와야 한다는 의미입니다.
        -  $는 "마지막"을 말합니다. 그 뒤로 더는 문자가 오면 안 됩니다.
          ```
            # blog/urls.py

            from django.urls import path
            from . import views

            urlpatterns = [
                path('', views.post_list, name='post_list'),
                path('post/<int:pk>/', views.post_detail, name='post_detail'),
                path('post/new/', views.post_new, name='post_new'),
            ]
          ```
      
      3. base.html에 Post New(글 추가) 페이지 링크 추가
        - blog/templates/blog/base.html 파일을 열어서, page-header 라는 div class에 등록 폼 link를 하나 추가한다.
        - 새로운 view는 post_new입니다.
        - 부트스트랩 테마에 있는 glyphicon glyphicon-plus 클래스로 더하기 기호가 보이게 됩니다.
          ```
            # blog/templates/blog/base.html

            <div class="page-header">
                <a href="{% url 'post_new' %}" class="top-menu">
                <span class="glyphicon glyphicon-plus"></span></a>
                <h1><a href="/">Django's Blog</a></h1>
            </div>
          ```
      
      4. views.py에 post_new() 함수 추가
        - 새 Post 폼을 추가하기 위해 PostForm() 함수를 호출하도록 하여 템플릿에 넘깁니다.
          ```
            # blog/views.py

            from .forms import PostForm

            def post_new(request):
                form = PostForm()
                return render(request, 'blog/post_edit.html', {'form': form})
          ```
      
      5. post_edit.html 페이지 추가
        - {{ form.as_p }}를 HTML 태그로 폼을 감싸세요. <form method="POST">...</form>
        - <form ...>을 열어 {% csrf_token %}를 추가하세요. 이 작업은 폼 보안을 위해 중요합니다. HTML Form의 POST요청에서 CSRF 토큰을 체크하며, 이때 CSRF토큰이 필요합니다. csrf_token tag를 통해 CSRF 토큰을 발급 받을 수 있습니다.
          ```
            # blog/templates/blog/post_edit.html

            {% extends 'blog/base.html' %}

            {% block content %}
                <h1>New post</h1>
                <form method="POST" class="post-form">
                    {% csrf_token %}
                    {{ form.as_p }}
                    <button type="submit" class="save btn btn-default">Save</button>
                </form>
            {% endblock %}
          ```
      
      6. Form 저장하기 1
        - 등록 Form의 두 가지 상황
          1. 첫번째 : 처음 페이지에 접속 했을 때, 새 글을 쓸 수 있게 Form이 비어 있습니다. 이때의 Http method는 GET
          2. 두번째 : Form에 입력된 데이터를 view 페이지로 가지고 올 때입니다. 이때의 Http method는 POST
            ```
              # blog/views.py

              from .forms import PostForm

              def post_new(request):
                  if request.method == "POST":
                      form = PostForm(request.POST)
                  else:
                      form = PostForm()
                  return render(request, 'blog/post_edit.html', {'form': form})
            ```
      
      7. Form 저장하기 2
        - 폼에 들어있는 값들이 올바른 지를 확인하기 위해 form.is_valid()을 사용합니다. 작업을 두 단계로 나눈다.
          1. 첫번째 : form.save()로 폼을 저장하는 작업, commit=False란 데이터를 바로 Post 모델에 저장하지 않는다는 뜻입니다.
          2. 두번째 : author와 published_date를 추가하는 작업, post.save()는 변경사항을 유지하고 새 블로그 글이 만들어 집니다
            ```
              # blog/views.py

              if form.is_valid():
                  post = form.save(commit=False)
                  post.author = request.user
                  post.published_date = timezone.now()
                  post.save()
            ```

      8. Form 저장하기 3
        -  새 블로그 글을 작성한 다음에 post_detail 페이지로 이동 합니다.
        - post_detail은 이동 해야 할 view의 name이고, post_detail view는 pk=post.pk를 사용해서 view에게 값을 넘겨줍니다.
        - post는 새로 생성한 블로그 글입니다.
          ```
            from django.shortcuts import redirect

            return redirect('post_detail', pk=post.pk)
          ```
      
      9. 완성된 post_new 함수
        ```
          # blog/views.py

          from django.shortcuts import redirect

          def post_new(request):
              if request.method == "POST":
                  form = PostForm(request.POST)
                  if form.is_valid():
                      post = form.save(commit=False)
                      post.author = request.user
                      post.published_date = timezone.now()
                      post.save()
                      return redirect('post_detail', pk=post.pk)
              else:
                  form = PostForm()
              return render(request, 'blog/post_edit.html', {'form': form})
        ```
  
  12. blog App 작성 : Django Form (글 수정)

    1. urls.py에 Post Edit(글 수정) url 추가
      - ^은 "시작"을 뜻합니다.
      - post/1/edit란 URL이 post 문자를 포함 해야 한다는 것을 말합니다
      - /은 다음에 / 가 한 번 더 와야 한다는 의미입니다.
      - $는 "마지막"을 말합니다. 그 뒤로 더는 문자가 오면 안 됩니다.
        ```
          # blog/urls.py

          from django.urls import path
          from . import views

          urlpatterns = [
              path('', views.post_list, name='post_list'),
              path('post/<int:pk>/', views.post_detail, name='post_detail'),
              path('post/new/', views.post_new, name='post_new'),
              path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
          ]

        ```
    
    2. post_detail.html에 Post Edit(글 수정) 페이지 링크 추가
      - blog/templates/blog/post_detail.html 파일을 열어서, link를 하나 추가한다
      - 새로운 view는 post_edit입니다.
      - 부트스트랩 테마에 있는 glyphicon glyphicon-pencil 클래스로 보이게 됩니다.
        ```
          # blog/templates/blog/post_detail.html

          <div class="post">
              {% if post.published_date %}
                  <div class="date">
                      {{ post.published_date }}
                  </div>
              {% endif %}
              <a class="btn btn-default" href="{% url 'post_edit' pk=post.pk %}">
              <span class="glyphicon glyphicon-pencil"></span></a>
              <h1>{{ post.title }}</h1>
              <p>{{ post.text|linebreaksbr }}</p>
          </div>
        ```
    
    3. views.py에 post_edit() 함수 추가
      - 작업을 두 단계로 나눈다.
        1. 첫 번째: url로부터 추가로 pk 매개변수를 받아서 처리합니다.
        2. 두 번째: get_object_or_404(Post, pk=pk)를 호출하여 수정하고자 하는 글의 Post 모델 인스턴스(instance)로 가져온 데이터를 폼을 만들 때와 폼을 저장할 때 사용하게 됩니다.
          ```
            # blog/views.py

            @login_required
            def post_edit(request, pk):
                post = get_object_or_404(Post, pk=pk)
                if request.method == "POST":
                    form = PostForm(request.POST, instance=post)
                    if form.is_valid():
                        post = form.save(commit=False)
                        post.author = request.user
                        post.published_date = timezone.now()
                        post.save()
                        return redirect('post_detail', pk=post.pk)
            else:
                form = PostForm(instance=post)
            return render(request, 'blog/post_edit.html', {'form': form})
          ```

  13. blog App 작성 : Django Form (글 삭제)

    1. urls.py에 Post remove(글 삭제) url 추가
      ```
        # blog/urls.py
        
        from django.urls import path
        from . import views

        urlpatterns = [
            path('', views.post_list, name='post_list'),
            path('post/<int:pk>/', views.post_detail, name='post_detail'),
            path('post/new/', views.post_new, name='post_new'),
            path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
            path('post/<int:pk>/remove/', views.post_remove, name='post_remove'),
        ]
      ```
    
    2. post_detail.html에 Post Remove(글 삭제) 페이지 링크 추가
      - blog/templates/blog/post_detail.html 파일을 열어서, link를 하나 추가한다.
      - 새로운 view는 post_remove입니다.
      - 부트스트랩 테마에 있는 glyphicon glyphicon-remove 클래스로 보이게 됩니다.
        ```
          # blog/templates/blog/post_detail.html

          <div class="post">
              {% if post.published_date %}
                  <div class="date">
                      {{ post.published_date }}
                  </div>
              {% endif %}
              <a class="btn btn-default" href="{% url 'post_remove' pk=post.pk %}">
              <span class="glyphicon glyphicon-remove"></span></a>
              <h1>{{ post.title }}</h1>
              <p>{{ post.text|linebreaksbr }}</p>
          </div>
        ```
    
    3. views.py에 post_remove() 함수 추가
      - 작업을 두 단계로 나눈다
        1. 첫 번째: url로부터 추가로 pk 매개변수를 받아서 처리 합니다.
        2. 두 번째: get_object_or_404(Post, pk=pk)를 호출하여 삭제 하고자 하는 글의 Post 모델 인스턴스(instance)로 가져 와서 삭제 처리를 한다. 
          ```
            # blog/views.py

            @login_required
            def post_remove(request, pk):
                post = get_object_or_404(Post, pk=pk)
                post.delete()
                return redirect('post_list')
          ```

  13. blog App 작성 : 로그인/로그아웃 처리하기
    1. 로그인 처리하기
      1. @login_required 데코레이터
        - 로그인 사용자만 포스트를 접근 할 수 있도록 post_new, post_edit, post_remove의 View들을 보호하려고 한다면
        - Django에서 제공하는 django.contrib.auth.decorators 모듈 안의 login_required 데코레이터를 사용하면 된다.
        - login_required 데코레이터는 로그인 페이지로 리다이렉션(Redirection) 된다.
          - 주의: 로그인 되어 있는 admin 페이지를 로그아웃 해야 함
          - https://docs.djangoproject.com/en/3.0/topics/auth/default/#auth-web-requests

          ```
            from django.contrib.auth.decorators import login_required

            @login_required
            def post_new(request):
                [...]
          ```
      
      2. urls.py 에 login url 추가
        - blog/urls.py가 아니라 myjango/urls.py에 로그인 url 추가
          ```
            # mydjango/urls.py

            from django.contrib import admin
            from django.urls import path, include
            from django.contrib.auth import views as auth_views
            
            urlpatterns = [
                path('admin/', admin.site.urls),
                path('', include('blog.urls')),
                path('accounts/login/', auth_views.LoginView.as_view(template_name="registration/login.html"), name="login"),
            ]
          ```
      
      3. 로그인 페이지 템플릿 추가
        - blog/templates/registration 디렉토리를 생성하고, login.html 파일 작성
          ```
            # blog/templates/registration/login.html

            {% extends "blog/base.html" %}

            {% block content %}
                {% if form.errors %}
                    <p>이름과 비밀번호가 일치하지 않습니다. 다시 시도해주세요.</p>
                {% endif %}

                <form method="post" action="{% url 'login' %}">
                    {% csrf_token %}
                    <table class="table table-bordered table-hover">
                    <tr>
                        <td>{{ form.username.label_tag }}</td><td>{{ form.username }}</td>
                    </tr>
                    <tr>
                        <td>{{ form.password.label_tag }}</td><td>{{ form.password }}</td>
                    </tr>
                    </table>

                    <input type="submit" value="login" class="btn btn-primary btn-lg" />
                    <input type="hidden" name="next" value="{{ next }}" />
                </form>
            {% endblock %}
           ```
      
      4. settings.py 에 설정 추가
        - 로그인 하면 최상위 index 레벨에서 로그인이 된다.
          ```
		    # mydjango/settings.py

		    LOGIN_REDIRECT_URL = '/'	    
          ```
    
    2. 로그인 여부 체크하기
		    
      1. base.html 수정
        - 인증이 되었을 때는 추가/수정 버튼을 보여주고, 인증이 되지 않았을 때는 로그인 버튼을 보여줌
          ```
            # blog/templates/blog/base.html

            <div class="page-header">
                {% if user.is_authenticated %}
                    <a href="{% url 'post_new' %}" class="top-menu">
                    <span class="glyphicon glyphicon-plus"></span></a>
                {% else %}
                    <a href="{% url 'login' %}" class="top-menu">
                    <span class="glyphicon glyphicon-lock"></span></a>
                {% endif %}
                <h1><a href="/">Django's Blog</a></h1>
            </div>
          ```
      
      2. post_detail.html에 수정
        - 로그인 사용자만 글을 수정, 삭제 할 수 있도록 체크하기
        - {% if %} 태그를 추가해 관리자로 로그인한 사용자들 만 글 수정,삭제 링크가 보일 수 있게 만든다.
          ```
            # blog/templates/blog/post_detail.html

            {% if user.is_authenticated %}
                <a class="btn btn-default" href="{% url 'post_edit' pk=post.pk %}">
                <span class="glyphicon glyphicon-pencil"></span></a>
                <a class="btn btn-default" href="{% url 'post_remove' pk=post.pk %}">
                <span class="glyphicon glyphicon-remove"></span></a>
            {% endif %}
          ```

    3. 로그아웃 처리하기
      1. base.html 수정
        - “Hello <사용자이름>” 구문을 추가하여 인증된 사용자라는 것을 알려주고, logout link를 추가함
		    
          ```
            # blog/templates/blog/base.html

            <div class="page-header">
                {% if user.is_authenticated %}
                    <a href="{% url 'post_new' %}" class="top-menu">
                    <span class="glyphicon glyphicon-plus"></span></a>
                    <p class="top-menu">Hello {{ user.username }}<small>
                    (<a href="{% url 'logout' %}?next={{request.path}}">Log
                    out</a>)</small></p>
                {% else %}
                    <a href="{% url 'login' %}" class="top-menu">
                    <span class="glyphicon glyphicon-lock"></span></a>
                {% endif %}
                <h1><a href="/">Django's Blog</a></h1>
            </div>
          ```
      
      2. urls.py 에 logout url 추가
        - blog/urls.py가 아니라 myjango/url.py에 로그아웃 url 추가
		    
          ```
		    # mydjango/urls.py

		    from django.contrib import admin
		    from django.urls import path, include
		    from django.contrib.auth import views as auth_views

		    urlpatterns = [
			path('admin/', admin.site.urls),
			path('', include('blog.urls')),
			path('accounts/login/', auth_views.LoginView.as_view(template_name="registration/login.html"), name="login"),
			path('accounts/logout/', auth_views.LogoutView.as_view(), {'next': None}, name='logout'),
		    ]
          ```
