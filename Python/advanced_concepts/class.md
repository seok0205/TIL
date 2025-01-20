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