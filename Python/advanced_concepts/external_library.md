# external library

- 외부 라이브러리는 파이썬 표준 라이브러리가 아니므로 사용하려면 pip 도구를 사용해 설치

## pip

> 파이썬 모듈이나 패키지를 쉽게 설치할 수 있도록 도와주는 도구

- pip로 파이썬 프로그램 설치 시 의존성 있는 모듈이나 패키지를 함께 설치해주어 편리함

### pip install

- `pip install numpy`와 같은 형식으로 PyPI에서 설치
- numpy는 패키지의 이름(pandas, pytorch 등)

### pip uninstall

- 설치한 패키지 삭제
- `pip uninstall numpy` 형태

### 특정 버전 설치

- 버전을 지정해 설치도 가능
- `pip install numpy==1.0.0` 형태
- 버전을 입력하지 않으면 자동으로 최신 버전 설치

### 최신 버전 업그레이드

- `pip install --upgrade numpy` 형태

### 설치된 패키지 확인

- `pip list`로 설치한 패키지 목록 출력 가능

## Faker

> 테스트용 가짜 데이터를 생성할 때 사용

- `pip install Faker`로 설치

### Faker 사용

```python
from faker import Faker
fake = Faker()
print(fake.name())  # Sara Ramirez

fake = Faker('ko-KR')
print(fake.name())  # 조지아
print(fake.address())   # 강원도 포천시 논현7거리 145 (상훈허면)

test_data = [(fake.name(), fake.address()) for i in range(30)]
print(test_data)    # 30개의 가짜 데이터가 담긴 리스트 출력
```

### Faker 활용

|항목|설명|
|---|---|
|`fake.postcode()`|우편 번호|
|`fake.country()`|국가명|
|`fake.company()`|회사명|
|`fake.job()`|직업명|
|`fake.phone_number()`|휴대폰 번호|
|`fake.email()`|이메일 주소|
|`fake.user_name()`|사용자명|
|`fake.pyint(min_value=0, max_value=100)`|0부터 100 사이 임의 숫자|
|`fake.ipv4_private()`|IP 주소|
|`fake.text()`|임의의 문장(한글 임의 문장은 `fake.catch_phrase()` 사용)|
|`fake.color_name()`|색상명|

## sympy

> 방정식 기호(symbol)를 사용하게 해주는 라이브러리

- `pip install sympy`로 설치
  
### sympy 사용

- 여러 개의 기호를 사용하고 싶다면 `x, y = sympy.symbols('x y')`으로 표현

- `sympy.Eq(a, b)`는 a와 b가 같다는 방정식

- fractions.Fraction으로 유리수 계산 가능. `Fractions(x, y)는 y분의 x라는 뜻

```python
# sympy_test.py
from fractions import Fraction
import sympy

# 가지고 있던 돈을 x라고 하자.
x = sympy.symbols("x")

# 가지고 있던 돈의 2/5가 1760원이므로 방정식은 x * (2/5) = 1760 이다.
f = sympy.Eq(x*Fraction('2/5'), 1760)

# 방정식을 만족하는 값(result)을 구한다.
result = sympy.solve(f)  # 결괏값은 리스트

# 남은 돈은 다음과 같이 가지고 있던 돈에서 1760원을 빼면 된다.
remains = result[0] - 1760

print('남은 돈은 {}원 입니다.'.format(remains))
# 남은 돈은 2640원 입니다.
```

### sympy 활용

- `x ** 2 = 1`같은 2차 방정식 해 구하기

```python
import sympy
x = sympy.symbols("x")
f = sympy.Eq(x**2, 1)
print(sympy.solve(f))   # [-1, 1]
```

- `x+y=10`, `x-y=4` 연립방정식의 해 구하기

```python
import sympy
x, y = sympy.symbols('x y')
f1 = sympy.Eq(x+y, 10)
f2 = sympy.Eq(x-y, 4)
sympy.solve([f1, f2])   # {x: 7, y: 3}
```

- 미지수가 2개 이상이면 결괏값이 리스트가 아닌 딕셔너리