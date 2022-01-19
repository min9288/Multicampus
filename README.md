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
