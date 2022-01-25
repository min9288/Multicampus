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