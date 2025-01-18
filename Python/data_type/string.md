# 문자열 자료형

## 문자열 만들고 사용하기

### 따옴표로 양쪽 둘러싸기

```python
"유정석"

'유정석'

"""
안녕하세요
"""

'''
반갑습니다
'''
```

- 작은 따옴표, 큰 따옴표 모두 사용할 수 있는 이유는 만들려고 하는 문자열의 내부에 구문이나 인용 대사 등이 포함되어 있을 때, 같은 따옴표가 겹치면 구문 오류가 발생하기 때문

### 역슬래시를 사용해서 작은따옴표, 큰따옴표를 문자열에 포함하기

- 역슬래시를 작은따옴표나 큰따옴표 앞, 즉 `\'` 혹은 `\"` 형태로 기입하면 그 자체로 인식해 감싸는 따옴표와 겹쳐도 오류없이 출력됨

```python
"\"안녕하세요\"라고 소년이 말했다"
```

## 여러 줄인 문자열에 변수를 대입하고 싶을 때

```python
"안녕하세요\n"  # 1
"정석입니다\n"
"반갑네요"

'''
안녕하세요
정석입니다
반갑네요
''' # 2
```

### 이스케이프 코드

|코드|설명|
|---|---|
|`\n`|문자열 안에서 줄을 바꿀 때 사용|
|`\t`|문자열 사이에 탭 간격을 줄 때 사용|
|`\\`|`\`를 그대로 표현할 때 사용|
|`\'`|작은 따옴표 그대로 표현할 때 사용|
|`\"`|큰 따옴표 그대로 표현할 때 사용|
|`\r`|캐리지 리턴(줄 바꿈 문자, 커서를 현재 줄의 가장 앞으로 이동)|
|`\f`|폼 피드(줄 바꿈 문자, 커서를 현재 줄의 다음 줄로 이동)|
|`\a`|벨 소리(출력 할때 PC 스피커에서 삑 소리가 남)|
|`\b`|백 스페이스|
|`\000`|널 문자|

## 문자열 연산하기

### 문자열 더해서 연결하기

```python
a = "se"
b = "ok"
print(a + b)    # seok
```

### 문자열 곱하기

```python
a = "seok"
print(a * 2)    # seokseok
```

## 문자열 길이 구하기

```python
a = "Seok"
len(a)  # 4
```

## 문자열 인덱싱, 슬라이싱

- indexing : 가리킨다
- slicing : 잘라낸다

### 인덱싱

```python
a = "seok"

print(a[0]) # s
print(a[3]) # k
print(a[-1])    # k
print(a[-0])    # s
print(a[-3])    # e
```

### 슬라이싱

```python
a = "seok is nice guy"

print(a[0:4])   # seok
print(a[14:])   # guy
print(a[:12])    # seok is nice
print(a[:]) # seok is nice guy
print(a[8:-1]) # nice gu
```

- 슬라이싱 `a[0:4]`의 수식은 `0 <= a < 4`

#### 슬라이싱으로 문자열 나누기

```python
a = 'seok0205male'
name = a[:4]
birth = a[4:8]
sex = a[8:]

print(name) # seok
print(birth)    # 0205
print(sex)  # male
```

#### 잘못된 문자열 바꾸기

```python
a = 'soccar'

b = a[:4] + 'e' + a[-1:]

print(b)    # soccer
```

## 문자열 포매팅

### 1. 숫자 대입

```python
a = "I ate %d pears"

print(a %3) # I ate 3 pears

num = 4
print(a %num)   # I ate 4 pears
```

### 2. 문자열 대입

```python
a = "I ate %s pears"

print(a %"six") # I ate six pears
```

### 3. 2개 이상 값 넣기

```python
a = "I ate %d pears. %s pears left."

num1 = 4
num2 = 'two'
print(a %(num1, num2))  # I ate 4 pears. two pears left.
```

### 문자열 포맷 코드

|코드|설명|
|---|---|
|`%s`|문자열(String)|
|`%c`|문자 1개(character)|
|`%d`|정수(Integer)|
|`%f`|부동소수(floating-point)|
|`%o`|8진수|
|`%x`|16진수|
|`%%`|Literal %(문자 `%`자체)|

```python
# %s는 문자열뿐만 아니라 어느 형태든 대입이 가능. 단, 문자열 형태로 변환해서 대입함.
print("%s pears left." %5)  # 5 pears left.
print("rate is %s" %3.234)  # rate is 3.234

print("download %d%%" %90)  # download 90%
```

## 포맷 코드와 숫자 함께 사용하기

### 1. 정렬과 공백

```python
print("%10s" % "hi")    # '        hi'
print("%-10ssoek" % "hi")   # 'hi        seok'
```

### 2. 소수점 표현하기

```python
print("%0.4f" %3.123456) # 3.1234
print("%.4f" %3.12345)  # 3.1234
```

## 포맷 함수를 사용한 포매팅

### 1. 숫자 바로 대입

```python
print("I ate {0} pears".format(3))  # I ate 3 pears
```

### 2. 문자열 바로 대입

```python
print("I ate {0} pears".format("four")) # I ate four pears
```

### 3. 숫자 값을 가진 변수로 대입

```python
num = 6
print("I ate {0} pears".format(num))
```

### 4. 두 개 이상 값 넣기

```python
num1 = 2
num2 = 'three'
print("I ate {0} pears. {1} pears left".format(num1, num2)) # I ate 2 pears. three pears left
```

### 5. 이름으로 넣기

```python
print("I ate {num1} pears. {num2} pears left".format(num1=2, num2='three')) # I ate 2 pears. three pears left
```

### 6. 인덱스, 이름 혼용해서 넣기

```python
print("I ate {0} pears. {num} pears left".format(4, num='two')) # I ate 4 pears. two pears left
```

### 7. 왼쪽, 오른쪽, 가운데 정렬

```python
print("{0:<10}".format("hi"))   # 'hi        '
print("{0:>10}".format("hi"))   # '        hi'
print("{0:^10}".format("hi"))   # '    hi    '
```

### 8. 공백 채우기

```python
print("{0:=^10}".format("hi"))  # '====hi===='
print("{0:!<10}".format("hi"))  # 'hi!!!!!!!!'
```

### 9. 소수점 표현하기

```python
y = 3.12345678
print("{0.0.4f}".format(y)) # '3.1234'
print("{0:10.4f}".format(y))    # '    3.1234'
```

### 10. { 또는 } 문자 표현

```python
print("{{ and }}".format()) # '{ and }'
```

### 11. f 문자열 포매팅

```python
name = 'seok'
age = 27
print(f"my name is {name}. age is {age}")   # my name is seok. age is 27
print(f"my age will be {age + 2} after 2 years") # my age will be 29 after 2 years

dic = {'sport' : 'soccer', 'num' : 11}
print(f"{dic['sport']} can play with {dic['num']} players") # soccer can play with 11 players

print(f'{"hi":<10}')    # 'hi        '
print(f'{"hi":=^10}')   # '====hi===='

y = 3.12345678
print(f'{y:0.4f}')  # 3.1234
print(f'{y:10.4f}') # '    3.1234'

print(f'{{ and }}') # { and }
```

## 문자열 관련 함수

### count

```python
a = 'arsenal'
print(a.count('a')) # 2
```

### find

```python
a = 'tottenham is the greatest team'
print(a.find('g'))  # 17
print(a.find('z'))  # -1
```

- 함수에 대입한 문자 'g'가 처음 등장하는 위치 반환
- 만약 존재하지 않는다면 -1 반환
  
### index

```python
a = "don't look back in anger"
print(a.index('c')) # 13
```

- 함수에 대입한 문자 'c'가 처음 등장하는 위치 반환
- 존재하지 않는다면 오류 발생

### join

```python
print(",".join("jude")) # j,u,d,e
print(",".join(['j', 'u', 'd', 'e']))   # j,u,d,e
```

### upper

```python
a = "hi"
print(a.upper())    # HI
```

- 대문자로 변경

### lower

```python
a = "HI"
print(a.lower())    # hi
```

- 소문자로 변경

### lstrip, rstrip, strip

```python
a = ' seok '
print(a.lstrip())   # 'seok '
print(a.rstrip())   # ' seok'
print(a.strip())    # 'seok'
```

- 선택한 방향의 공백을 지움

### replace, split

```python
a = "It's my life"

print(a.replace("my life", "your life"))    # It's your life

print(a.split())    # ["It's", 'my', 'life']
print(a.split("'")) # ['It', 's my life']
```