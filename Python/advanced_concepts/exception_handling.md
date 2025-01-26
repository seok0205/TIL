# exception_handling

## 오류는 언제 발생하는가?

1. 존재하지 않는 파일 사용하려고 시도했을 때
   - `FilNotFoundError` 발생
2. 0으로 다른 숫자 나누었을 때
   - `ZeroDivisionError` 발생
3. 인덱싱 진행 시 잘못된 요솟값 가리킬 때
   - `IndexError` 발생

## 오류 예외 처리 기법

### try-except

```python
try:
    ...
except [발생오류[as 오류변수]]: # [] 안의 내용은 생략할 수 있음
    ...
```

1. try-except
    ```python
    try:
        ...
    except:
        ...
    ```
    - 오류의 종류 상관 X, 오류 발생시 except 수행

2. 발생 오류만 포함 except
    ```python
    try:
        ...
    except 발생오류:
        ...
    ```
    - 오류 발생 시 except 문에 미리 정해 놓은 오류와 동일한 오류만 except 수행
  
3. 발생 오류, 오류 변수 포함 except
    ```python
    try:
        ...
    except 발생오류 as 오류변수:
        ...
    ```
    - 오류의 내용까지 알고 싶을 때 사용

### try_finally

- finally 절은 try 문 수행 도중 예외 발생 여부에 상관없이 항상 수행
- 보통 finally 절은 사용한 리소스를 close해야 할 때 많이 사용

```python
# try_finally.py
try:
    f = open('foo.txt', 'w')
    # 무언가를 수행한다.

    (... 생략 ...)

finally:
    f.close()  # 중간에 오류가 발생하더라도 무조건 실행된다.
```

### 여러 개의 오류 처리

```python
try:
    ...
except 발생오류1:
   ... 
except 발생오류2:
   ...
```

```python
try:
    a = [1,2]
    print(a[3])
    4/0
except (ZeroDivisionError, IndexError) as e:
    print(e)
```

- 2개 이상의 오류를 동일하게 처리하기 위해서 위와 같이 함께 묶음

### try-else

```python
try:
    ...
except [발생오류 [as 오류변수]]:
    ...
else:  # 오류가 없을 경우에만 수행
    ...
```

- try문 수행 중 오류 발생 시, except절, 발생하지 않으면 else절이 수행

## 오류 회피하기

```python
# error_pass.py
try:
    f = open("나없는파일", 'r')
except FileNotFoundError:
    pass
```

- try문에서 `FileNotFoundError` 발생 시, pass 사용해 오류 회피

## 오류 고의 발생

- 상속받는 자식 클래스에 반드시 특정 기능을 가진 함수를 구현해야할 때(메서드 오버라이딩를 활용해 구현하지 않았을 때 `NotImplementedError` 이용)

- `raise`를 활용하여 오류를 발생시킬 수 있음

## 예외 만들기

```python
# error_make.py
class MyError(Exception):
    def __str__(self):
        return "허용되지 않는 별명입니다."
```

```python
def say_nick(nick):
    if nick == '바보':
        raise MyError()
    print(nick)
```

```python
try:
    say_nick("천사")
    say_nick("바보")
except MyError:
    print("허용되지 않는 별명입니다.")
    # 오류 메시지를 사용하고 싶다면
# except MyError as e:
#     print(e)
```

- `print(e)`로 오류메시지가 출력되는 건 오류 메시지를 print문으로 출력할 경우에 호출할 `__str__` 메서드 구현 때문