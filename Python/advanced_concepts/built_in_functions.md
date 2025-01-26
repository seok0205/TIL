# built_in_functions

> 파이썬 모듈과 달리 import가 필요하지 않음

## abs

> 숫자를 입력받았을 때 그 숫자의 절댓값 반환

```python
print(abs(3))   # 3
print(abs(-3))  # 3
print(abs(-1.8))    # 1.8
```

## all

> 반복 가능 데이터 입력값, 요소가 모두 참이면 True, 하나라도 거짓이면 False 반환

```python
print(all([1, 2, 3]))  # True
print(all([1, 2, 0]))  # False
print(all([])) # True
```

## any

> 반복 가능 데이터 입력값, 하나라도 참이면 True, 모두 거짓일 때만 False 반환

```python
print(any([1, 2, 0, 0]))    # True
print(any([0, ""])) # False
print(any([]))  # False
```

## chr

> 유니코드 숫자 값, 코드 해당 문자 반환

```python
print(chr(97))  # 'a'
print(chr(44032))   # '가'
```

## dir

> 객체가 지닌 변수, 함수 보여줌

```python
print(dir([1, 2, 3]))   # ['append', 'count', 'extend', 'index', ...]
print(dir({'1': 'a'}))  # ['clear', 'copy', 'get', 'has_key', 'items', ...]
```

## divmod

> 2개 숫자 입력값, a를 b로 나눈 몫과 나머지를 튜플로 리턴

```python
print(divmod(9, 2)) # (4, 1)
```

## enumerate

> '열거', 순서가 있는 데이터(리스트, 튜플, 문자열) 입력값, 인덱스 값 포함하는 enumerate 객체 반환

- 보통 for문과 함께 사용

```python
for i, name in enumerate(['a', 'b', 'c']):
    print(i, name)

# 0 a
# 1 b
# 2 c
```

## eval

> 문자열로 구성된 표현식 입력값, 해당 문자열을 실행한 결괏값 반환

```python
print(eval('1+2'))  # 3
print(eval("'hi' + 'a'"))   # 'hia'
print(eval('divmod(4, 3)')) # (1, 1)
```

## filter

> 첫 번째 인수로 함수, 두 번째 인수로 함수에 들어갈 반복 가능 데이터 입력값. 반복 가능 데이터 요소 순서대로 함수 호출, 반환값이 참인 것만 묶어 반환

```python
# positive.py 
def positive(l): 
    result = [] 
    for i in l: 
        if i > 0: 
            result.append(i) 
    return result

print(positive([1,-3,2,0,-5,6]))    # [1, 2, 6]
```

```python
# filter1.py
def positive(x):
    return x > 0

print(list(filter(positive, [1, -3, 2, 0, -5, 6]))) # [1, 2, 6]
```

```python
print(list(filter(lambda x: x > 0, [1, -3, 2, 0, -5, 6])))  # [1, 2, 6]
```

## hex

> 정수 입력값, 16진수 문자열로 반환

```python
print(hex(234)) # '0xea'
print(hex(3))   # '0x3'
```

## id

> 객체 입력값, 고유 주소(레퍼런스) 반환

```python
a = 3
print(id(3))    # 2263060054320
print(id(a))    # 2263060054320
b = a
print(id(b))    # 2263060054320
```

## input

> 사용자 입력 받는 함수. 입력 인수를 문자열로 전달 > 프롬프트

```python
a = input() # hi
print(a)    # hi
b = input("입력: ") # 입력: hi
print(b)    # hi
```

## int

> 문자열 형태의 숫자, 소수점 있는 숫자를 정수로 반환

- 정수가 입력되면 그대로 반환
- 두 번째 인자에 radix 진수를 입력하고 해당 radix 진수로 표현된 문자열 입력값 x를 10진수로 변환해 반환

```python
print(int('3')) # 3
print(int(3.4)) # 3
print(int('11', 2)) # 3
print(int('1A', 16))    # 26
```

## isinstance

> 첫 번째 인수로 객체, 두 번째 인수로 클래스 입력값. 입력으로 받은 객체가 그 클래스의 인스턴스인지 판단, 참이면 True 거짓이면 False 반환

```python
class Person: pass

a = Person()
print(isinstance(a, Person)) # True
b = 3
print(isinstance(b, Person)) # False
```

## len

> 입력값의 길이(요소 전체 개수) 반환

```python
print(len("python"))    # 6
print(len([1, 2, 3]))   # 3
print(len((1, 'a')))    # 2
```

## list

> 반복 가능 데이터 입력. 리스트로 만들어 반환

- list 함수에 리스트 입력 시 똑같은 리스트로 복사하여 리턴

```python
print(list('python'))   # ['p', 'y', 't', 'h', 'o', 'n']
print(list((1,2,3)))    # [1, 2, 3]

a = [1, 2, 3]
b = list(a)
print(b)    # [1, 2, 3]
```

## map

> (함수, 반복 가능 데이터)  
> 입력받은 데이터의 각 요소에 함수를 적용한 결과 반환

```python
def two_times(x): 
    return x*2
print(list(map(two_times, [1, 2, 3, 4])))   # [2, 4, 6, 8]
```

```python
print(list(map(lambda a: a*2, [1, 2, 3, 4])))   # [2, 4, 6, 8]
```

## max

> (반복 가능 데이터)
> 요소 중 최댓값 반환

```python
print(max([1, 2, 3]))   # 3
print(max('python'))    # 'y'
```

## min

> (반복 가능 데이터)
> 요소 중 최솟값 반환

```python
print(min([1, 2, 3]))   # 1
print(min('seok'))  # 'e'
```

## oct

> (정수)
> 8진수 문자열로 변환 후 반환

```python
print(oct(34))  # '0o42'
print(oct(12345))   # '0o30071'
```

## open

> ('파일 이름', '읽기 방법': 'r', 'w', 'a'(추가), 'b'(바이너리 모드))  
> 파일 객체 반환

```python
f = open("file", "rb")  # 바이너리 읽기 모드
```

## ord

> (문자)  
> 유니코드 숫자 값 반환

```python
print(ord('a')) # 97
print(ord('가'))    # 44032
```

## pow

> (x, y)  
> x를 y제곱한 결괏값 반환

```python
print(pow(2, 4))    # 16
print(pow(3, 3))    # 27
```

## range

> (시작 숫자, 끝 숫자, step)  
> 입력받은 숫자에 해당하는 범위 값을 반복 가능 객체로 만들어 반환

```python
# 인수 한개
print(list(range(5)))   # [0, 1, 2, 3, 4]

# 인수 두개
print(list(range(1, 5)))    # [1, 2, 3, 4]

# 인수 세개
print(list(range(1, 10, 3)))    # [1, 4, 7]
print(list(range(5, 1, -1)))    # [5, 4, 3, 2]
```

## round

> (`숫자`, `[,ndigits]`)
> 숫자 입력받아 반올림 후 반환

```python
print(round(4.6))   # 5
print(round(3.1))   # 3
print(round(2.1234, 2)) # 2.12
```

## sorted

> (iterable(가변))  
> 정렬 후 리스트 반환

```python
print(sorted([3, 1, 2]))   # [1, 2, 3]
print(sorted(['a', 'c', 'b'])) # ['a', 'b', 'c']
print(sorted("zero"))  # ['e', 'o', 'r', 'z']
print(sorted((3, 2, 1)))   # [1, 2, 3]
```

## str

> (객체)  
> 문자열 형태로 객체 변환 후 반환

```python
print(str(3))   # '3'
print(str('hi'))    # 'hi'
```

## sum

> (iterable(가변))  
> 입력 데이터 합 반환

```python
print(sum([1, 2, 3]))   # 6
print(sum([4, 5, 6]))   # 15
```

## tuple

> (iterable(가변))
> 반복 가능 데이터를 튜플로 변환 후 리턴, 입력 값 튜플인 경우 그대로 반환

```python
print(tuple("abc")) # ('a', 'b', 'c')
print(tuple([1, 2, 3])) # (1, 2, 3)
print(tuple((1, 2, 3))) # (1, 2, 3)
```

## type

> (객체)  
> 입력값의 자료형이 무엇인지 알려줌

```python
type("abc") # <class 'str'>
type([])    # <class 'list'>
type(open("test", 'w')) # <class '_io.TextIOWrapper'>
```

## zip

> (*iterable)
> 동일한 개수로 이루어진 데이터들 묶어서 반환

- `*iterable`은 반복 가능 데이터를 여러 개 입력할 수 있다는 의미

```python
list(zip([1, 2, 3], [4, 5, 6])) # [(1, 4), (2, 5), (3, 6)]
list(zip([1, 2, 3], [4, 5, 6], [7, 8, 9]))  # [(1, 4, 7), (2, 5, 8), (3, 6, 9)]
list(zip("abc", "def")) # [('a', 'd'), ('b', 'e'), ('c', 'f')]
```