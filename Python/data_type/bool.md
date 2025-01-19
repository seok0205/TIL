# bool

- `True` or `False`를 나타내는 자료형(참, 거짓)
- 첫 글자는 무조건 대문자로 작성해야 함

## 기본 형태

```python
a = True
b = False

print(type(a))  # <class 'bool'>
print(type(b))  # <class 'bool'>

print(1 == 1)   # True
print(2 > 1)    # True
print(2 < 1)    # False
```

## 자료형의 참과 거짓

|값|참 or 거짓|
|---|---|
|"python"|참|
|""|거짓|
|[1, 2, 3]|참|
|[]|거짓|
|(1, 2, 3)|참|
|()|거짓|
|{'a': 1}|참|
|{}|거짓|
|1|참|
|0|거짓|
|None|거짓|

- 문자열, 리스트, 튜플, 딕셔너리 등의 값이 비어 있으면 거짓, 아니면 참