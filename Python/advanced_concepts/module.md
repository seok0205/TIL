# module

> 함수나 변수 또는 클래스를 모아놓은 파이썬 파일

## 모듈 만들기

```python
# mod1.py
def add(a, b):
    return a+b

def sub(a, b):
    return a-b
```

- mod1.py 파일이 저장된 디렉터리에서 진행해야 모듈을 인터프리터에서 읽을 수 있음

```python
import mod1 # 모듈 불러오는 법

print(mod1.add(3, 4))   # 7
print(mod1.sub(5, 1))   # 4
```

```python
from mod1 import add, sub

print(add(1, 3))    # 4
print(sub(4, 4))    # 0
```

## `if __name__ == "__main__":`의 의미

- mod1 모듈을 import하는 순간 mod1.py 파일이 실행되어 결괏값을 출력
- 아래 코드처럼 수행해야 위 문제 방지

```python
# mod1.py
def add(a, b):
    return a+b

def sub(a, b):
    return a-b

if __name__ == "__main__":
    print(add(1, 4))
    print(sub(4, 2))
```

- 직접 파일을 실행했을 때는 `__name__ == "__main__"`이 참이 되어 if 문장 다음이 실행
- 다른 파일에서 import할 때에는 거짓이되어 if문 다음 문장 실행 안함

### `__name__` 변수란?

> 파이썬이 내부적으로 사용하는 특별한 변수 이름

- mod1.py를 직접 실행할 경우, mod1.py의 `__name__` 변수에는 `__main__` 값이 저장

- 하지만 파이썬 셸이나 다른 파이썬 모듈에서 mod1을 import하면 mod1.py의 `__name__` 변수에 mod1.py의 모듈 이름인 mod1이 저장

```python
>>> import mod1
>>> mod1.__name__
'mod1'
```

## 클래스나 변수 등을 포함한 모듈

```python
# mod2.py
PI = 3.141592

class Math:
    def solv(self, r):
        return PI * (r ** 2)

def add(a, b):
    return a+b
```

```python
>>> import mod2
>>> print(mod2.PI)  # 3.141592
>>> a = mod2.Math()
>>> print(a.solv(2))    # 12.566368
>>> print(mod2.add(mod2.PI, 4.4))   # 7.541592
```

## 다른 파일에서 모듈 불러오기

```python
# modtest.py
import mod2
result = mod2.add(3, 4)
print(result)   # 7
```

- modtest.py, mod2.py 파일이 동일한 디렉터리에 있어야함

## 다른 디렉터리에 있는 모듈 불러오기

- `mod2.py` 파일이 `C:\seok\mymod`있다는 가정

### sys.path.append 사용

```python
>>> import sys
>>> sys.path    # 파이썬 라이브러리가 설치되어 있는 디렉터리 목록보여줌. 이 디렉토리에 저장된 모듈은 이동 필요없이 호출 가능
>>> sys.path.append("C:/seok/mymod")
>>> import mod2
>>> print(mod2.add(3, 4))   # 7
```

## PYTHONPATH 환경 변수 사용하기

```
C:\seok>set PYTHONPATH=C:\seok\mymod
C:\doit>python
```

```python
>>> import mod2
>>> print(mod2.add(3, 4))   # 7
```

- mac or unix는 export 명령 사용