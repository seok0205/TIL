# program_input_output

`C:\> type a.txt`  

- cmd에서 type은 바로 뒤에 적힌 파일 이름을 인수로 받아 파일의 내용을 출력해 주는 명령어

## sys 모듈 사용하기

- sys 모듈을 사용해 프로그램에 인수를 전달 가능

```python
import sys

args = sys.argv[1:]
for i in args:
    print(i)
```

```python
import sys
args = sys.argv[1:]
for i in args:
    print(i.upper(), end=' ')
```