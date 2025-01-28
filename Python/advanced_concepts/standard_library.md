# standard library

> 유능한 파이썬 사용자들이 만든 유용한 프로그램을 모아 놓은 곳

## datetime.date

> 연, 월, 일로 날짜를 표현할 때 사용

```python
import datetime
day1 = datetime.date(1999, 2, 5)
day2 = datetime.date(2025, 1, 28)

diff = day2 - day1
print(diff.days)    # 9489
print(day2.weekday())   # 1
print(day2.isweekday()) # 2
```

- weekday() : 해당 날짜의 요일에 따라 결과값이 0~6으로 출력
- isweekday() : 결과값이 1~7로 출력

## time

### time.time

- UTC(세계 표준시) 기준으로 시간을 실수 형태로 반환

```python
import time
print(time.time()) # 1738040982.5787454
```

### time.localtime

- time.time()이 반환한 실숫값을 사용해 연, 월, 일, 시, 분, 초, ...의 형태로 바꿈

```python
import time
print(time.localtime(time.time()))  # time.struct_time(tm_year=2025, tm_mon=1, tm_mday=28, tm_hour=14, tm_min=11, tm_sec=16, tm_wday=1, tm_yday=28, tm_isdst=0)
```

### time.asctime

- time.localtime()이 반환한 튜플 형태의 값을 인수로 받아 날짜와 시간을 알아보기 쉬운 형태로 반환

```python
import time
a = time.asctime(time.localtime(time.time()))
print(a)    # Tue Jan 28 14:13:28 2025
```

### time.ctime

- 위에서 작성한 `time.asctime(time.localtime(time.time()))`을 간단히 표시 가능

```python
import time
print(time.ctime()) # Tue Jan 28 14:15:03 2025
```

### time.strftime

- 시간에 관계된 것을 세밀하게 표현하는 여러 포맷 코드 제공

|포맷코드|설명|예|
|---|---|---|
|`%a`|요일의 줄임말|Mon|
|`%A`|요일|Monday|
|`%b`|달의 줄임말|Jan|
|`%B`|달|January|
|`%c`|날짜와 시간 출력|Thu May 25 10:13:52 2024|
|`%d`|일(day)|[01, 31]|
|`%H`|시간(24)|[00, 23]|
|`%I`|시간(12)|[01, 12]|
|`%j`|1년 중 누적 날짜|[001, 366]|
|`%m`|달|[01, 12]|
|`%M`|분|[01, 59]|
|`%p`|AM or PM|AM|
|`%S`|초|[00, 59]|
|`%U`|1년 중 누적 주(일요일 시작)|[00, 53]|
|`%w`|숫자로 된 요일|[0(일), 6(토)]|
|`%W`|1년 중 누적 주(월요일 시작)|[00, 53]|
|`%x`|현재 설정된 지역에 기반한 날짜|01/28/25|
|`%X`|현재 설정된 지역에 기반한 시간|14:41:23|
|`%Y`|연도 출력|2025|
|`%Z`|시간대 출력|대한민국 표준시|
|`%%`|문자 %|%|
|`%y`|세기 부분을 제외한 연도 출력|25|

### time.sleep

- 루프안에서 주로 사용
- 일정한 시간 간격을 두고 루프 실행 가능

```python
# sleep1.py
import time
for i in range(10):
    print(i)
    time.sleep(1)   # 1초 간격으로 0부터 9까지 출력
```

## math.gcd

- 최대 공약수 쉽게 구할 수 있음

```python
import math

print(math.gcd(60, 100, 80))   # 20
```

## math.lcm

- 최소 공배수 쉽게 구할 수 있음

```python
import math

print(math.lcm(10,15))  # 30
```

## random

- 난수를 발생시키는 모듈

```python
import random
print(random.random())  # 0.0~1.0 사이의 실수 중 난수 반환
print(random.randint(1, 10))    # 1, 10 사이 정수 주 난수 반환
```

### random.choice

```python
import random
a = [1, 2, 3, 4, 5]
print(random.choice(a)) # 리스트 a의 무작위 요소 출력
```

### random.sample

```python
import random
a = [1, 2, 3, 4, 5]
print(random.sample(a, len(a))) # 리스트 a에서 len(a)만큼 무작위로 추출해서 반환
```

## itertools.zip_longest

```python
# itertools_zip.py
import itertools

bands = ['nirvana', 'linkinpark', 'queen', 'greenday', 'sum41']
genre = ['grunge', 'nu-metal', 'hard-rock']

result = itertools.zip_longest(bands, genre, fillvalue='punk')
print(list(result))
'''
[('nirvana', 'grunge'), ('linkinpark', 'nu-metal'), ('queen', 'hard-rock'), ('greenday', 'punk'), ('sum41', 'punk')]
'''
```

## itertools.permutation

```python
import itertools
list(itertools.permutations(['1', '2', '3'], 2))
for a, b in itertools.permutations(['1', '2', '3'], 2):
    print(a+b)

'''
1, 2, 3 카드 중 2장의 카드를 꺼내 만들 수 있는 2자리 숫자의 경우의 수 구하기
12
13
21
23
31
32
'''
```

## itertools.combinations

- 3장의 카드에서 순서에 상관없이 2장을 고르는 조합의 경우
- 45개 숫자중 숫자 6개 선택하는 경우의 수

```python
import itertools
a = list(itertools.combinations(['1', '2', '3'], 2))
print(a)    # [('1', '2'), ('1', '3'), ('2', '3')]

b = itertools.combinations(range(1, 46), 6)
len(list(b))    # 경우의 수 개수
```

- 숫자에 중복을 허용하고 싶다면 `itertools.combinations_with_replacement()` 활용

## functools.reduce

- arguments = (function, iterable)
- 함수를 반복 가능한 객체의 요소에 차례대로 누적 적용해 하나의 값으로 줄이는 함수

```python
def add(data):
    result = 0
    for i in data:
        result += i
    return result

data = [1, 2, 3, 4, 5]
result = add(data)
print(result)   # 15
```

```python
import functools

data = [1, 2, 3, 4, 5]
result = functools.reduce(lambda x, y: x + y, data)
print(result)   # 15
```

```python
# 최댓값 구하기
num_list = [3, 2, 9, 4, 1, 6]
max_num = functools.reduce(lambda x, y: x if x > y else y, num_list)
print(max_num)  # 9
```

## operator.itemgetter

- 주로 sorted같은 함수의 key 매개변수에 적용해 다양한 기준으로 정렬할 수 있도록 도와주는 모듈

```python
from operator import itemgetter

students = [
    ('seok', 27, 'A'),
    ('yoon', 25, 'B'),
    ('sin', 33, 'B'),
]

result = sorted(students, key=itemgetter(1))
print(reslt)    # [('yoon', 25, 'B'), ('seok', 27, 'A'), ('sin', 33, 'B')]
```

```python
from operator import itemgetter

students = [
    {"name": "seok", "age": 27, "grade": 'A'},
    {"name": "yoon", "age": 25, "grade": 'B'},
    {"name": "sin", "age": 33, "grade": 'B'},
]

result = sorted(students, key=itemgetter('age'))
print(result)   # [{'name': 'yoon', 'age': 25, 'grade': 'B'}, {'name': 'seok', 'age': 27, 'grade': 'A'}, {'name': 'sin', 'age': 33, 'grade': 'B'}]
```

## operator.attrgetter

- students 리스트의 요소가 튜플이 아닌 Student 클래스의 객체라면 이 함수를 적용해 정렬해야 함

```python
from operator import attrgetter

class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

students = [
    Student('seok', 27, 'A'),
    Student('yoon', 25, 'B'),
    Student('sin', 33, 'B'),
]

result = sorted(students, key=attrgetter('age'))
```

## shutil

- 파일을 복사(copy)하거나 이동(move)할 때 사용하는 모듈
- 아래 코드는 백업용으로 `c:\doit\a.txt`를 백업용 디렉터리 temp에 `c:\temp\a.txt.bak`이라는 이름으로 복사하는 코드

```python
# shutil_copy.py
import shutil

shutil.copy("c:/doit/a.txt", "c:/temp/a.txt.bak")
```

### shutil.move

- 휴지통으로 삭제하는 기능
- `c:\doit\a.txt`파일을 `c:\temp\a.txt`로 이동

```python
# shutil_move.py
import shutil

shutil.move("c:/doit/a.txt", "c:/temp/a.txt")
```

## glob

### 디렉터리에 있는 파일들을 리스트로 만들기 - glob(pathname)

- `C:\seok` 디렉터리에 있는 파일 중 이름이 yu로 시작하는 파일을 모두 찾아서 읽는 코드

```python
import glob
print(glob.glob("c:\seok\yu*"))
# ['c:/seok\\yu1.py', ...]
```

## pickle

- 객체의 형태를 그대로 유지하면서 파일에 저장하고 불러올 수 있게 하는 모듈
- pickle 모듈의 dump 함수 활용해 딕셔너리 객체인 data를 그대로 파일에 저장하는 법

```python
>>> import pickle
>>> f = open("test.txt", 'wb')
>>> data = {1: 'python', 2: 'you need'}
>>> pickle.dump(data, f)
>>> f.close()
```

- pickle.dump로 저장한 파일을 pickle.loda 사용해 원래 있던 딕셔너리 객체(data) 상태 그대로 불러오는 코드

```python
>>> import pickle
>>> f = open("test.txt", 'rb')
>>> data = pickle.load(f)
>>> print(data)
{2:'you need', 1:'python'}
```

## os

- 환경 변수나 디렉터리, 파일 등의 OS 자원을 제어할 수 있게 해 주는 모듈

### 내 시스템의 환경 변숫값을 알고 싶을 때, os.environ

```python
import os
print(os.environ)   # environ({...})
print(os.environ['CONFIGSETROOT'])  # 'C:\\WINDOWS\\ConfigSetRoot'
```

### 디렉터리 위치 변경하기 - os.chdir

- 현재 디렉터리 위치 변경

```python
import os
os.chdir("C:\Users")
```

### 디렉터리 위치 돌려받기 - os.getcwd

- 현재 자신 디렉터리 위치 반환

```python
import os
os.getcwd() # 'C:\Users'
```

### 시스템 명령어 호출하기 - os.system

- 시스템 자체 프로그램이나 기타 명령어를 파이썬에서도 호출 가능
- `os.system('명령어')` 형태

```python
import os
os.system('dir')    # 현재 디렉터리에서 시슽메 명령어 dir 실행
```

### 실행한 시스템 명령어의 결괏값 돌려받기 - os.popen

- 시스템 명령어를 실행한 결괏값을 읽기 모드 형태의 파일 객체로 반환

```python
import os
f = os.popen("dir")
print(f.read()) # 읽어 들인 파일 객체 내용
```

### 기타 os 관련 함수

|함수|설명|
|---|---|
|`os.mkder(디렉터리)`|디렉터리 생성|
|`os.rmdir(디렉터리)`|디렉터리 삭제, 단 디렉터리가 비어 있어야 삭제 가능|
|`os.remove(파일)`|파일 지움|
|`osrename(src, dst)`|src라는 이름의 파일을 dst로 바꿈|

## zipfile

- 여러 개의 파일을 zip 형식으로 합치거나 해제할 때 사용

```python
# zipfile_test.py
import zipfile

# 파일 합치기
with zipfile.ZipFile('mytext.zip', 'w') as myzip:
    myzip.write('a.txt')
    myzip.write('b.txt')
    myzip.write('c.txt')

# 해제하기
with zipfile.ZipFile('mytext.zip') as myzip:
    myzip.extractall()

# 특정 파일만 해제하기
with zipfile.ZipFile('mytext.zip') as myzip:
    myzip.extract('a.txt')

# 압축하여 묶기
with zipfile.ZipFile('mytext.zip', 'w', compression=zipfile.ZIP_LZMA, compresslevel=9) as myzip:
    (... 생략 ...)
```

- compression에는 4가지 종류가 있음
  - ZIP_STORED : 압축하지 않고 파일을 zip으로만 묶는다. 속도 빠름
  - ZIP_DEFLATED : 일반적인 zip 압축으로 속도가 빠르고 압축률은 낮다(호환성 좋음)
  - ZIP_BZIP2 : bzip2 압축으로 압축률 높고 속도 느림
  - ZIP_LZMA : lzma 압축으로 압축률 높고 속도 느림(7zip과 동일한 알고리즘)

- compressionlevel은 압축 수준 숫자값, 1~9사용, 1은 속도 빠르지만 압축률 낮고 9는 속도 느리지만 압축률 높음

## threading

- 컴퓨터에서 동작하고 있는 프로그램을 프로세스라 함
- 1개의 프로세스는 하나의 일을 하지만 thread를 사용하면 한 프로세스 안에서 2가지 혹은 그 이상을 동시 수행 가능

```python
# thread_test.py
import time
import threading

def long_task():
    for i in range(5):
        time.sleep(1)
        print("working:%s\n" % i)

print("Start")

threads = []
for i in range(5):
    t = threading.Thread(target=long_task)
    threads.append(t)

for t in threads:
    t.start()

for t in threads:
    t.join()  # join으로 스레드가 종료될때까지 기다린다.

print("End")
```

## tempfile

- 파일을 임시로 만들어서 사용 시 유용한 모듈

### tempfile.mkstemp

- 중복되지 않는 임시 파일의 이름을 무작위로 만들어 반환

```python
import tempfile
filename = tempfile.mkstemp()
print(filename)
# 'C:\WINDOWS\TEMP\~-275151-0'
```

### tempfile.TemporaryFile

- 임시 저장 공간으로 사용할 파일 객체 반환
- 기본적으로 바이너리 쓰기(wb) 모드를 가짐
- `f.close()` 호출 시 자동 삭제

```python
import tempfile
f = tempfile.TemporaryFile()
f.close()
```

## traceback

- 프로그램 실행 중 발생한 오류를 추적하고자 할 때 사용하는 모듈

```python
# traceback_test.py
import traceback

def a():
    return 1/0

def b():
    a()

def main():
    try:
        b()
    except:
        print("오류가 발생했습니다.")
        print(traceback.format_exc())   # 오류 추적 결과를 문자열로 반환하는 함수

main()

'''
오류가 발생했습니다.
Traceback (most recent call last):
  File "c:\doit\traceback_sample.py", line 14, in main
    b()
  File "c:\doit\traceback_sample.py", line 9, in b
    a()
  File "c:\doit\traceback_sample.py", line 5, in a
    return 1/0
ZeroDivisionError: division by zero
'''
```

## json

- JSON 데이터를 쉽게 처리하고자 사용하는 모듈
- 아래 파일은 `seok.json`

```json
{
    "name": "seok",
    "birth": "0205",
    "age": 27
}
```

- json 파일 읽어 딕셔너리로 변환

```python
import json
with open('seok.json') as f:
    data = json.load(f)

print(type(data))   # <class 'dict'>
print(data) # {'name': 'seok', 'birth': '0205', 'age': 27}
```

- 딕셔너리 자료형을 JSON 파일로 생성

```python
import json
data = {'name': 'seok', 'birth': '0205', 'age': 27}
with open('seok.json', 'w') as f:
    json.dump(data, f)
```

- 파이썬 자료형을 JSON 문자열로 만드는 방법
- JSON 데이터로 변경하면 한글 문자열은 코드 형태로 표시
- dump(), dumps() 함수는 기본적으로 데이터를 아스키 형태로 저장하기 때문
- JSON 문자열을 다시 딕셔너리로 역변환해 사용하는 것도 문제가 없음(json.loads() 함수 사용)
- 출력 JSON 문자열을 보기 좋게 정렬하려면 indent 옵션을 추가
- 딕셔너리 외에 다른 자료형도 JSON 문자열로 변경 가능

```python
import json
d = {'name': '석', 'birth': '0205', 'age': 27}
json_data = json.dumps(d)
print(json_data)    # {'name': '\\ud...', 'birth': '0205', 'age': 27}

json_data = json.dumps(d, ensure_ascii=False)   # 데이터를 저장할 때 아스키 형태로 변환하지 않겠다는 옵션
print(json_data)    # {'name': '석', 'birth': '0205', 'age': 27}

json_data = json.dumps(d, ident=2, ensure_ascii=False)
print(json_data)

'''
{
    'name': '석',
    'birth': '0205',
    'age': 27,
}
'''
```

## urllib

- URL을 읽고 분석할 때 사용하는 모듈
- URL을 호출해 원하는 리소스를 얻으려면 urllib 모듈 사용

```python
# urllib_test.py
import urllib.request

def get_wikidocs(page):
    resource = 'https://wikidocs.net/{}'.format(page)
    with urllib.request.urlopen(resource) as s:
        with open('wikidocs_%s.html' % page, 'wb') as f:
            f.write(s.read())
```

### SSL 오류 발생 시

- 파이썬이 서버의 SSL 인증서를 신뢰할 수 있는지 확인하는 과정에서, 로컬 시스템에 필요한 CA 인증서가 없거나 찾을 수 없어 발생하는 문제(macOS에서 자주 발생)

```python
import urllib.request

# SSL 인증서 검증을 비활성화하는 Context 생성
import ssl
context = ssl._create_unverified_context()

def get_wikidocs(page):
    resource = f'https://wikidocs.net/{page}'
    with urllib.request.urlopen(resource, context=context) as s:  # 생성한 Context 전달
        with open(f'wikidocs_{page}.html', 'wb') as f:
            f.write(s.read())

get_wikidocs(12)
```

## webbrowser

- 시스템 브라우저를 호출할 때 사용하는 모듈
- 파이썬으로 웹 페이지를 새 창으로 열려면 webbrowser 모듈의 open_new() 함수를 사용

```python
import webbrowser

webbrowser.open_new("http://...")

webbrowser.oepn("http://...")   # 이미 열린 브라우저로 원하는 사이트 열고 싶다면
```