# class

## 클래스와 객체

```python
class seok():   # 클래스
    pass

a = seok()  # 객체
b = seok()
```

### 객체와 인스턴스의 차이

- 클래스로 만든 객체를 `인스턴스`라고도 함
- 위 코드의 a는 객체이고 a 객체는 seok의 인스턴스임
- 즉 인스턴스라는 말은 특정 객체가 어떤 클래스의 객체인지 관계 위주로 설명할 때 사용
- `a는 객체, a는 seok의 인스턴스`

## 클래스 만들기

### 사칙연산 클래스

```python
class FourCal:
    def __init__(self, first, second):
        self.first = first
        self.second = second
    def setdata(self, first, second):
        self.first = first
        self.second = second
    def add(self):
         result = self.first + self.second
        return result
    def mul(self):
        result = self.first * self.second
        return result
    def sub(self):
        result = self.first - self.second
        return result
    def div(self):
        result = self.first / self.second
        return result
```

### 메서드

- 클래스 안에 구현된 함수

#### 메서드 호출 방법

```python
a = FourCal()
FourCal.setdata(a, 4, 2)

a = FourCal()
a.setdata(4, 2)
```

### 생성자

- 생성자란 객체가 생성될 때 자동으로 호출되는 메서드를 의미
- `__init__`를 사용하면 메서드가 자동으로 생성자가 됨

### 클래스의 상속

- 상속이란 어떤 클래스를 만들 때 다른 클래스의 기능을 물려받을 수 있게 만드는 것

```python
class MoreFourCal(FourCal):
    pass
```

- `MoreFourCal`클래스는 `FourCal`클래스를 상속했으므로 `FourCal`클래스의 모든 기능을 사용할 수 있음

#### 상속 기능 쓰는 이유

- 보통 상속은 기존 클래스 변경하지 않고 기능을 추가하거나 기존 기능을 변경하려고 할 때 사용
- 기존 클래스가 라이브러리 형태로 제공되거나 수정이 허용되지 않는 상황이라면 상속을 사용해야 함

### 메서드 오버라이딩

- 부모 클래스(상속한 클래스)에 있는 메서드를 동일한 이름으로 다시 만드는 것
- 메서드를 오버라이딩하면 부모 클래스의 메서드 대신 오버라이딩한 메서드가 호출됨

### 클래스 변수

```python
class Family:
    lastname = "김"
```

- `Family` 클래스에 선언한 `lastname`이 클래스변수
- 클래스 안에 함수를 선언하는 것과 마찬가지로 클래스 안에 변수를 선언해 생성

```python
print(Family.lastname) # 김

a = Family()
print(a.lastname)   # 김

Family.lastname = '박'
print(a.lastname)   # 박
```

- 클래스변수는 객체변수와 달리 클래스로 만든 모든 객체에 공유된다는 특징이 있음

#### 클래스변수와 동일한 이름의 객체변수 생성시

```python
a.lastname = '최'

print(Family.lastname)  # '박'
```
- 객체변수는 클래스변수와 동일한 이름으로 생성될 수 있다.
- 객체 변수의 값을 변경해도 클래스 변수의 값은 변하지 않음