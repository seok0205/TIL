# while문

## 기본 구조

```python
num = 0
a = 0
while num < 10:
    num += 1
    a += 2

print(a)    # 20
```

- 조건문이 참인 동안 수행문장들이 반복해서 수행

## while문 강제로 빠져나가기

```python
song = 1
playlist = 10
while True:
    print("노래 재생")
    playlist -= song
    print("남은 노래: %d." %playlist)
    if playlist == 0:
        print("플레이리스트 재생 완료")
        break
```

## while문 맨 처음으로 돌아가기

```python
num = 0
while num < 10:
    num += 1
    if num % 3 == 0: continue
    print(num)

# 1
# 2
# 4
# 5
# 7
# 8
# 10
```

## 무한 루프

```python
a = 0
while True:
    a += 1
    print("Ctrl+C 입력 시 while문 탈출")
```