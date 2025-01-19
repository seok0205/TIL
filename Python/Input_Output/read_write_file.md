# read_write_file

## create file

```python
new = open("file.txt", 'w')
new.close()

new2 = open("C:/user/file.txt", 'w')
# "C:\\user\\file.txt"
# r"C:\user\file.txt"(r은 raw string)
new2.close()
```

|파일 열기 모드|설명|
|---|---|
|`r`|읽기 모드: 파일을 읽기만 할 때 사용|
|`w`|쓰기 모드: 파일을 내용을 쓸 때 사용|
|`a`|추가 모드: 파일의 마지막에 새로운 내용 추가할 때 사용|

## write a data in file

```python
new = open("C:/user/file.txt", 'w')
for i in range(1, 11):
    data = "%d번째 줄.\n" %i
    f.write(data)
f.close()
```

- 위와 같이 쓰면 텍스트 파일에 1부터 10번째 줄까지 작성되있는 것을 확인 가능

## 파일을 읽는 여러 가지 방법

### readline 함수

```python
new = open("C:/user/file.txt", 'r')
line = new.readline()
print(line) # 한 줄 출력
```

```python
new = open("C:/user/file.txt", 'r')
while True: # 모든 줄 출력. 읽을 것 없으면 break.
    line = new.readline()
    if not line: break
    print(line)
new.close()
```

### readlines 함수

```python
new = open("C:/user/file.txt", 'r')
lines = f.readlines()
for line in lines:
    print(line)
new.close()
```

- 파일의 모든 줄을 읽어 각각의 줄을 요소로 가지는 리스트를 반환

#### 줄 바꿈 문자 제거

- strip()을 활용해 제거

```python
new = open("C:/user/file.txt", 'r')
lines = new.readlines()
for line in lines:
    line = line.strip()
    print(line)
new.close()
```

### read 함수

```python
new = open("C:/user/file.txt", 'r')
data = new.read()   # 파일 내용 전체 문자열로 반환
print(data)
new.close()
```

### 파일 객체를 for문과 함께 사용

```python
new = open("C:/user/file.txt", 'r')
for line in new:
    print(line)
new.close()
```

- 파일 객체(new)는 기본적으로 위 코드처럼 for문과 함께 사용해 파일을 줄 단위로 읽을 수 있음

## 파일에 새로운 내용 추가

- 쓰기 모드(`w`)로 파일을 열 때, 이미 존재하는 파일을 열면 그 파일의 내용이 모두 사라짐
- 새 내용을 추가하려면 추가 모드(`a`)로 열어야 함

```python
new = open("C:/user/file.txt", 'a')
for i in range(11, 20):
    data = "%d번째 줄입니다.\n" %i
    new.write(data)
new.close()
```

## with문과 함께 사용

```python
new = open('file.txt', 'w')
new.write("you are my precious")
new.close()

with open('file.txt', 'w') as new:
    new.write("you are my precious")
```

- with문을 사용하면 with블록을 벗어나는 순간, 열린 파일 객체가 자동으로 닫힘