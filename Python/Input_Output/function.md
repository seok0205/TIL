# function

## 함수 사용 이유

- 똑같은 내용을 반복해서 작성할 때 함수 필요
- 자신이 작성한 프로그램을 기능 단위 함수로 분리하면 흐름을 일목요연하게 볼 수 있음

## 함수 구조

```python
def add(a, b):  # a, b : 매개변수(parameter)
    return a + b

c = add(1, 2)   # 1, 2 : 인수(arguments)
print(c)    # 3
```

## 입력값과 리턴값에 다른 함수 형태

```python
def add(a, b):  # 입력값, 리턴값이 있는 함수
    return a + b

def eat():  # 입력값이 없는 함수
    return "먹다"

def make(a):    # 리턴값이 없는 함수
    print("%s 제작 완료!" %a)

n = '상자'
a = make(n) # 상자 제작 완료!
print(a)    # None

def sleep():    # 입력값, 리턴값 없는 함수
    print("잘자~")

sleep() # 잘자~
```

## 매개변수 지정해 호출

```python
def add(a, b):
    return a + b

result = add(b=10, a=2)
print(result)   # 12
```

## 입력값이 몇 개가 될지 모를 때

### 여러 개 입력값 받는 함수

```python
def add(*args): # *args는 고정 이름이 아님. *뒤에 아무 이름을 써도 됨
    result = 0
    for i in args:
        result += i # *args에 입력받은 모든 값 더함
    
    return result

n = add(4, 5, 6)
print(n)    # 15
```

```python
def song(genre, *args):
    song = list()
    if genre == 'rock':
        for i in args:
            song.append(i)
    elif genre == 'kpop':
        for i in args:
            song.append(i)
    else:
        return print("장르를 제대로 입력하세요")
    return song

genre = 'rock'
song1 = 'smells like a teen spirit'
song2 = 'sk8er boy'
song3 = 'numb'
playlist = song(genre, song1, song2, song3)

print(playlist)
# ['smells like a teen spirit', 'sk8er boy', 'numb']
```

### 키워드 매개변수, kwargs

```python
def print_kwargs(**kwargs):
    print(kwargs)

print_kwargs(a=1, name='seok')   # {'a': 1, 'name': 'seok'}
```

- 매개변수 이름 앞에 `**`를 붙이면 그 매개변수는 `key=value` 형태의 입력값으로 입력이 되야 하고 딕셔너리에 저장됨

## 함수의 리턴값은 언제나 하나

```python
def add(a, b):
    return a+b, a*b

print(add(4,6)) # (10, 24)
```

```python
def add(a, b):
    return a+b
    return a*b  # 리턴값은 하나라 뒷부분은 무시됨

print(add(4,6)) # 10
```

- 위 코드가 첫 return값만 나오는 이유는 return을 만나는 순간 함수를 빠져나가기 때문

### return의 다른 쓰임새

- 특별한 상황일 때 함수를 빠져나가고 싶을 때 return을 단독으로 사용해 빠져나갈 수 있음

```python
def sex_seok(seok):
    if seok == "여자":
        return
    print("저는 %s 입니다" %seok)

sex_seok('남자')    # 저는 남자입니다
sex_seok('여자')    # 
```

## 매개변수에 초깃값 미리 설정

```python
def introduce(name, age, man=True):
    print("저는 이름이 %s입니다" %name)
    print("저는 %d살입니다" %age)
    if man:
        print("성별은 남자입니다")
    else:
        print("성별은 여자입니다")

introduce("유정석", 27)
# 저는 이름이 유정석입니다
# 저는 27살입니다
# 성별은 남자입니다
```

- 매개변수를 (name, man=True, age)와 같이 초깃값을 설정해 놓은 매개변수를 그렇지 않은 변수들과 섞이게 해놓으면 설정해놓은 매개변수의 자리에 그 뒤의 매개변수의 인수를 입력하게 되어 오류가 발생. 초깃값 설정해놓으면 뒤에 놓는 것이 바람직함

## 함수 안에서 선언한 변수의 효력 범위

```python
a = 1
def add(a):
    a += 1

print(add(a))   # 2
print(a)    # 1
```

- 함수 안에서 사용하는 매개변수는 함수 안에서만 사용될 뿐, 함수 밖의 변수 이름과는 전혀 상관이 없음

## 함수 안에서 함수 밖의 변수를 변경

### return

```python
a = 1
def add(a):
    a += 1
    return a

a = add(a)  # 2
print(a)    # 2
```

### global

```python
a = 1
def add():
    global a
    a += 1

add()
print(a)    # 2
```

## lambda 예약어

- lambda는 함수 생성 시 사용하는 예약어, def와 동일한 역할
- 비교적 def 사용할 정도로 복잡하지 않거나 사용할 수 없는 곳에 lambda 사용

```python
multi = lambda a, b: a*b
result = multi(6, 8)
print(result)   # 48
```