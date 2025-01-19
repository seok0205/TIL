# if문

## 기본 구조

```python
if 조건문:
    수행_문장1
else:
    수행_문장2
```

- if의 조건을 만족하면 수행_문장1, 아니라면 수행_문장2를 실행함
- 조건문 다음의 `:`과 들여쓰기가 중요

## 조건문

- 참과 거짓을 판단하는 문장

### 비교 연산자

|비교연산자|설명|
|---|---|
|`x<y`|x가 y보다 작다|
|`x>y`|x가 y보다 크다|
|`x==y`|x, y가 같다|
|`x!=y`|x, y가 같지 않다|
|`x>=y`|x가 y보다 크거나 같다|
|`x<=y`|x가 y보다 작거나 같다|

### and, or, not

|연산자|설명|
|---|---|
|`x or y`|x와 y 둘 중 하나만 참이어도 참이다|
|`x and y`|x와 y 모두 참이어야 참이다|
|`not x`|x가 거짓이면 참이다|

### in, not in

|in|not in|
|---|---|
|`x in 'list'`|`x not in 'list'`|
|`x in 'tuple'`|`x not in 'tuple'`|
|`x in 'string'`|`x not in 'string'`|

```python
print('a' in ('a', 'b', 'c'))   # True
print('z' not in 'seok')    # True
print(1 not in [1, 2])  # False
```

### 조건문에서 아무 일도 하지 않게 설정

```python
bag = ['paper', 'pencil', 'book']
if 'paper' in bag:
    pass    # 조건문이 True라서 pass가 실행되면 아무런 결과도 보여주지 않음
else:
    print("종이 꺼내")
```

## 다양한 조건 판단하는 elif

- if, else만으로는 다양한 조건 판단이 어려움
- elif의 삽입으로 다양한 조건문 삽입이 가능
- 개수 제한이 없음

## 조건부 표현식

```python
if money >= 1000:
    message = "rich"
else:
    message = "poverty"
```

```python
message = "rich" if money >= 1000 else "poverty"
```