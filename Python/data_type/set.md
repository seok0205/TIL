# set(집합)

## 기본 형태

```python
a = set([1, 2, 3])
print(a)    # {1, 2, 3}

b = set("seok")
print(b)    # {'e', 'k', 'o', 's'}
```

- 비어 있는 집합 자료형 `a = set()`

## 특징

- 중복을 허용하지 않음
- 순서가 없음(Unordered)
- 따라서 데이터의 중복을 제거하기 위한 필터로 종종 사용되고 인덱싱이 불가하여 요솟값 얻을 수 없음
- 하지만 `list()`, `tuple()`의 활용으로 인덱싱으로 접근 가능

## 교, 합, 차집합 구하기

```python
a = set([1, 2, 3, 4, 5, 6])
b = set([2, 5, 6, 8, 9, 10])

print(a & b)    # {2, 5, 6}
print(a.intersection(b))    # {2, 5, 6}

print(a | b)    # {1, 2, 3, 4, 5, 6, 8, 9, 10}
print(a.union(b))   # {1, 2, 3, 4, 5, 6, 8, 9, 10}

print(a - b)    # {1, 3, 4}
print(b - a)    # {8, 9, 10}
print(a.difference(b))  # {1, 3, 4}
print(b.difference(a))  # {8, 9, 10}
```

## 집합 자료형 관련 함수

### add

```python
a = set([1, 2, 3])
a.add(5)
print(a)    # {1, 2, 3, 5}
```

### update

```python
a = set([1, 2, 3])
a.update([4, 5, 6])
print(a)    # {1, 2, 3, 4, 5, 6}
```

### remove

```python
a = set([1, 2, 3])
a.remove(3)
print(a)    # {1, 2}
```