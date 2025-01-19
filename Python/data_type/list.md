# 리스트

- 리스트는 `[]`(대괄호)로 감싸져 있고 담긴 자료들은 ,(콤마)로 이루어져 있음

```python
a = [1, 2, 3]
b = ['my', 'life']
c = [1, 'my', ['your', 'life']]
d = list()  # 비어 있는 리스트 []

print(a[1]) # 2
print(a[0] + a[2])  # 4
print(a[-1])    # 3
print(c[2][0])  # your
print(c[-1][-1])    # life

print(a[:]) # [1, 2, 3]
print(c[2][:1]) # ['life']
```

## 리스트 연산하기

### 리스트 더하기

```python
a = [9, 5]
b = [2, 6]
print(a+b)  # [9, 5, 2, 6]
```

### 리스트 반복

```python
a = [1, 3]
print(a * 4)    # [1, 3, 1, 3, 1, 3, 1, 3]
```

### 리스트 길이 구하기

```python
a = [1, 2, 3, 4]
print(len(a))   # 4
```

### 잦은 리스트 연산 실수

```python
a = [1, 2]
b = "hi"

print(a[0]+b)   # error
print(str(a[0])+b)  # 1hi
```

- 정수 형태와 문자 형태는 합치려면 정수를 문자의 형태로 변환해야 함

## 리스트 수정과 삭제

### 리스트 값 수정

```python
a = [1, 2, 3, 4]
a[0] = 4
print(a)    # [4, 2, 3, 4]
```

### 리스트 요소 삭제

```python
a = [1, 2, 3, 4]

del a[3]
print(a)    # [1, 2, 3]

del a[1:]
print(a)    # [1]
```

## 리스트 관련 함수

### append

```python
a = [1, 2]

a.append(5)
print(a)    # [1, 2, 5]

a.append([6, 7])
print(a)    # [1, 2, 5, [6, 7]]
```

### sort

```python
a = [8, 2, 5, 7]
b = ['z', 'a', 'h']

a.sort()
print(a)    # [2, 5, 7, 8]

b.sort()
print(b)    # ['a', 'h', 'z']
```

### reverse

```python
a = ['z', 'b', 'w', 'h']
a.reverse()
print(a)    # ['h', 'w', 'b', 'z']
```

- 정렬 후 역순으로 정렬이 아니라, 현재 리스트를 그대로 거꾸로 뒤집음

### index

```python
a = [1, 2, 5, 3]
print(a.index(3))   # 3
print(a.index(5))   # 2
```

- 존재하지 않는 값을 찾으려고 하면 오류 발생

### insert

```python
a = [5, 2, 6]
a. insert(0, 9)
print(a)    # [9, 5, 2, 6]

a. insert(3, 1)
print(a)    # [9, 5, 2, 1, 6]
```

- 그 자리에 값을 대체하는 것이 아니라 원래 있던 값은 위치가 하나 뒤로 밀려남

### remove

```python
a = [9, 5, 2, 6, 9]
a.remove(9)
print(a)    # [5, 2, 6, 9]

a.remove(9)
print(a)    # [5, 2, 6]
```

- x를 대입했을 때, 리스트에서 첫 번째로 나오는 x를 삭제

### pop

```python
a = [9, 5, 2, 6]

print(a.pop())  # 6
print(a)    # [9, 5, 2]

print(a.pop(9)) # 9
print(a)    # [5, 2]
```

- x를 입력했을 때, x를 반환하고 리스트에서는 삭제
- x를 입력하지 않고 빈칸일 때는 마지막 인덱스가 리턴 및 삭제

### count

```python
a = [1, 1, 1, 2, 2, 3]
print(a.count(1))   # 3
```

- 리스트 안에 입력한 x가 몇 개 있는지 조사해 반환

### extend

```python
a = [1, 2, 3]

a.extend([6, 7])
print(a)    # [1, 2, 3, 6, 7]

b = [1, 2]

a.extend(b)
print(a)    # [1, 2, 3, 6, 7, 1, 2]
```

- `a.extend([6, 7])`는 `a += [6, 7]`과 동일