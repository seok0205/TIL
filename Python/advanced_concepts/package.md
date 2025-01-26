# package

> 관련 있는 모듈의 집합  
> 파이썬 모듈을 계층적으로 관리할 수 있게 해줌

- 파이썬에서 모듈은 하나의 .py 파일

## 패키지 만들기

```
game/   - 루트 디렉터리
    __init__.py
    sound/  - 서브 디렉터리
        __init__.py
        echo.py
        wav.py
    graphic/
        __init__.py
        screen.py
        render.py
    play/
        __init__.py
        run.py
        test.py
```

## 패키지 안의 함수 실행

1. echo 모듈을 import
   - `import game.sound.echo`
   - `game.sound.echo.echo_test()`
2. echo 모듈이 있는 디렉터리까지 `from ... import`하여 실행
   - `from game.sound import echo`
   - `echo.echo_test()`
3. echo 모듈의 echo_test 함수 직접 import
   - `from game.sound.echo import echo_test`
   - `echo_test()`

### 주의 사항

- import game을 수행하면 game 디렉터리의 `__init__.py`에 정의한 것만 참조 가능

```python
>>> import game
>>> game.sound.echo.echo_test()
# Traceback (most recent call last): AttributeError: 'module' object has no attribute 'sound'
```

```python
import game.sound.echo.echo_test
# Traceback (most recent call last): ModuleNotFoundError: No module named 'game.sound.echo.echo_test'; 'game.sound.echo' is not a package
```

- 도트 연산자(.)를 사용해서 `import a.b.c`처럼 import할 때 가장 마지막 항목인 c는 반드시 모듈 or 패키지여야 함

## `__init__.py`의 용도

> 해당 디렉터리가 패키지의 일부임을 알려 주는 역할을 함

- 만약 패키지에 포함된 디렉터리에 `__init.py`파일이 없으면 패키지로 인식 X

- python 3.3 부터는 없어도 인식 but 하위 버전 호환 위해 생성하는 것이 안전

- 패키지와 관련된 설정이나 초기화 코드를 포함 가능

### 패키지 변수 및 함수 정의

- 패키지의 `__init__.py` 파일에 공통 변수, 함수 정의 가능

```python
# C:/seok/game/__init__.py
VERSION = 3.5

def print_version_info():
    print(f"version is {VERSION}")
```

```python
>>> import game
>>> print(game.VERSION) # 3.5
>>> game.print_version_info()   # version is 3.5
```

### 패키지 내 모듈을 미리 import

- `__init__.py` 파일에 패키지 내의 다른 모듈을 미리 import하여 패키지를 사용하는 코드에서 간편히 접근 가능

```python
# C:/seok/game/__init__.py
from .graphic.render import render_test

VERSION = 3.5

def print_version_info():
    print(f"version is {VERSION}")
```

- import 문장에서 `.graphic.render`에서 `.`은 현재 디렉터리를 의미

```python
>>> import game
>>> game.render_test()  # render
```

### 패키지 초기화

- 패키지를 처음 불러올 때 실행해야 하는 코드 작성 가능
- DB연결이나 설정 파일 로드 같은 작업

```python
# C:/seok/game/__init__.py
from .graphic.render import render_test

VERSION = 3.5

def print_version_info():
    print(f"version is {VERSION}.")

# 여기에 패키지 초기화 코드를 작성한다.
print("Initializing game ...")
```

- 패키지 처음 import할 때 초기화 코드 실행

```python
>>> import game # Initializing game ...
```

- 초기화 코드는 같은 패키지 하위 모듈의 함수를 import할 경우에도 실행

```python
>>> from game.graphic.render import render_test # Initializing game ...
```

- 단, 초기화 코드는 한 번 실행된 후에는 다시 import 해도 실행되지 않음.

```python
>>> import game # Initializing game ...
>>> from game.graphic.render import render_test
```

### `__all__`

```python
>>> from game.sound import *    # Initializing game ...
>>> echo.echo_test()    # Traceback (most recent call last): NameError: name 'echo' is not defined
```

- 특정 디렉터리의 모듈을 `*`를 활용해 import할 땐 해당 디렉터리의 `__init__.py`파일에 `__all__` 변수를 설정하고 import 할 수 있는 모듈을 정의해 줘야 함

```python
# C:/seok/game/sound/__init__.py
__all__ = ['echo']
```

- `__all__`은 sound 디렉터리에서 `*`를 사용해 import 할 때, 이곳에 정의된 echo 모듈만 import된다는 의미

- 예외로 `from game.sound.echo import *`은 `__all__`과 상관없이 import 됨

- `__all__`과 상관없이 무조건 import되는 경우는 `from a.b.c import *`에서 from의 마지막 항목인 c가 모듈인 때

```python
>>> from game.sound import *    # Initializing game ...
>>> echo.echo_test()    # echo
```

## relative 패키지

- graphic 디렉터리의 render.py 모듈에서 sound 디렉터리의 echo.py 모듈을 사용하고 싶을 때

```python
# render.py
from game.sound.echo import echo_test
def render_test():
    print("render")
    echo_test()
```

- `from game.sound.echo import echo_test` 문장 추가해 echo_test 함수 사용할 수 있게 수정

```python
# render.py
from ..sound.echo import echo_test  # ..은 부모 디렉터리 의미

def render_test():
    print("render")
    echo_test()
```

- render.py 파일의 부모 디렉터리는 game이므로 위 같은 import 가능