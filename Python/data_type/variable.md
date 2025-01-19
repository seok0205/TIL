# variable

## 변수란?

- 객체. 자료형의 데이터(값)와 같은 것을 의미

```python
a = [9, 5, 2, 6]
print(id(a))    # 1817239436224
```

- 위의 같이 변수가 가리키는 메모리의 주소를 확인 가능

## 리스트 복사

```python
a = [9, 5, 2, 6]
b = a

print(id(a))    # 1817239436224
print(id(b))    # 1817239436224

print(a is b)   # True

a[0] = 1

print(a)    # [1, 5, 2, 6]
print(b)    # [1, 5, 2, 6]
```

- 위 코드를 통해 a와 b가 가리키는 객체가 동일함을 알 수 있음

### `[:]` 이용하기

```python
a = [9, 5, 2, 6]
b = a[:]
a[1] = 4

print(a)    # [9, 4, 2, 6]
print(b)    # [9, 5, 2, 6]
```

### copy 모듈 이용

```python
from copy import copy
a = [1, 2, 3]
b = copy(a) # or 'a.copy()' (리스트 자료형 자체 함수. copy 모듈이 필요 없음)

print(b is a)   # False
```

### 변수를 만드는 여러 가지 방법

```python
a, b = ('seok', 'man')  # (a, b) = 'seok', 'man'
[c, d] = ['yu', 'jung']
e = f = 'world'

a, b = b, a
print(a)    # man
print(b)    # seok
```