# for문

## 기본 구조

```python
lst = [1, 2, 3]
for i in lst:
    print(i)
# 1
# 2
# 3
```

- 리스트나 튜플, 문자열의 첫 요소부터 마지막까지 순서대로 변수에 대입되어 문장이 실행

## 다양한 for문 사용

```python
lst = [(2, 3), (5, 6), (1, 9)]
for (a, b) in lst:
    print(a+b)
# 5
# 11
# 10
```

```python
score = [30, 50, 20, 15]

number = 0
for i in score:
    number += 1
    if i >= 30:
        print("%d번 학생은 합격" %number)
    else:
        print("%d번 학생은 불합격" %number)
# 1번 학생은 합격
# 2번 학생은 합격
# 3번 학생은 불힙격
# 4번 학생은 불합격
```

## for, continue

```python
score = [30, 50, 20, 15]

number = 0
for i in score:
    number += 1
    if i < 30:
        continue
    print("%d번 학생 합격" %number)
# 1번 학생 합격
# 2번 학생 합격
```

## range

```python
a = range(10)
print(a)    # range(0, 10)

b = range(1, 20)
print(b)    # range(1, 20)
```

### 예시

```python
a = 0
for i in range(1, 11):
    a += i

print(a)    # 55
```

## 리스트 컴프리헨션

```python
# 리스트의 숫자 3씩 곱하기
a = [9, 5, 2 ,6]
result = [n * 3 for n in a]
print(result)   # [27, 15, 6, 18]
```

```python
# 짝수만 3만 곱하기
a = [1, 2, 3, 4]
result = [n * 3 for n in a if n % 2 == 0]
print(result)   # [6, 12]
```

```python
# 구구단
gugu = [i*j for i in range(2, 10)
            for j in range(1, 10)]
print(gugu) # 2단부터 9단까지 출력
```