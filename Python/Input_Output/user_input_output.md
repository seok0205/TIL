# user_input_output

## 사용자 입력 활용하기

### input 사용

```python
a = input() # my name is seok
print(a)    # my name is seok
```

### 프롬프트 띄워 사용자 입력받기

```python
age = input("나이를 입력하세요: ")
# 이름을 입력하세요: 27
print(age)
# 27
type(age)
# <class 'str'>
```

## print 자세히 알기

### 큰따옴표로 둘러싸인 문자열은 + 연산과 동일

```python
print("you" "are" "my precious")
# youaremy precious
print("you" + "are" + "my precious")
# youaremy precious
```

### 문자열 띄어쓰기는 쉼표로

```python
print("you", "are", "my precious")
# you are my precious
```

### 한 줄에 결괏값 출력하기

```python
for i in range(10):
    print(i, end=" ")   # end의 매개변수 초깃값은 '\n'

# 0 1 2 3 4 5 6 7 8 9
```