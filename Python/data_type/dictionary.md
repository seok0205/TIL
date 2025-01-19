# dictionary

- 리스트나 튜플처럼 인덱스가 아닌 `key`를 통해 `value` 얻음
- 대응 관계를 나타내는 자료형
- `연관 배열(associative array)` or `해시(hash)`라고 함
- 딕셔너리 a일 때, a[x]로 표현 시, x에 인덱스가 아닌 key 값을 입력해야 함

## 기본 형태

```python
a = {'name': 'seok', 'age': 27, 'birth': [1999, 2, 5]}
```

## 쌍 추가, 삭제

### 추가

```python
a = {'name': 'seok'}
a['age'] = 27
print(a)    # {'name': 'seok', 'age': 27}
```

### 삭제

```python
a = {'name': 'seok', 'age': 27}

del a['age']
print(a)    # {'name': 'seok'}
```

## dictionary 사용법

### dictionary 주의 사항

- 중복된 key 값을 설정해 놓으면 하나를 제외한 모든 것들이 무시됨

- key에는 list를 사용할 수 없음. value에만 list 사용 가능. 하지만 튜플은 key에 사용 가능.

- 이유는 `mutable`, `immutable`에 따라 쓸 수 있냐 없느냐 정하기 때문(value에는 둘 다 가능)

## dictionary 관련 함수

### keys

```python
a = {'name': 'seok', 'age': 27}
print(a.keys()) # dict_keys(['name', 'age'])
print(list(a.keys()))    # ['name', 'age']

for i in a.keys():
    print(i)
# name
# age
```

### values

```python
a = {'name': 'seok', 'age': 27}
print(a.values())   # dict_values(['seok', 27])
```

### items

```python
a = {'name': 'seok', 'age': 27}
print(a.items())    # dict_items(['name', 'seok'], ['age', 27])
```

### clear

```python
a = {'name': 'seok', 'age': 27}
a.clear()
print(a)    # {}
```

### get

```python
a = {'name': 'seok', 'age': 27}
print(a.get('name'))    # seok
```

- 딕셔너리에 존재하지 않는 키를 get에 사용하면 'None'이 반환됨
- 하지만 a[x] 형식으로 입력 시, x가 a라는 딕셔너리에 존재하지 않으면 오류가 발생함
- 'None'을 반환받고 싶지 않다면 디폴트 값을 정해주면 됨

```python
a = {'name': 'seok'}
print(a.get('height', 'unknown')) # unknown
```

### in

```python
a = {'name': 'seok', 'age': 27, 'height': 183}
print('name' in a)  # True
print('birth' in a) # False
```