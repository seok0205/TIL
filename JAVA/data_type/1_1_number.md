# number

## data type

> 데이터의 종류와 크기를 결정하는 기본 구성 요소

- 숫자, 문자열처럼 자료 형태로 사용하는 모든 것
- 프로그램에서 가장 기본적, 핵심 단위

## 정수

- **int**
  - -2147483648 ~ 2147483647이 표현 범위
- **long**
  - -9223372036854775808 ~ 9223372036854775807
- **byte**(-128~127), **short**(-32768~32767)도 있지만 잘 사용 X
- 특정 상황에서 효율적 메모리 사용이 필요할 경우 사용
- long 자료형 변수에 값을 대입할 때 int 자료형의 최댓값보다 크면 접미사로 `L`이나 `I`를 붙여줘야 함. 그렇지 않으면 컴파일 오류 발생

## 실수

- **float**
  - -3.4 * 10\**38 ~ 3.4 * 10**38
- **double**
  - -1.7 * 10\**308 ~ 1.7 * 10**308
- 실수형은 기본값이 double이므로 float 변수에 값을 대입할 땐 `3.14F`처럼 접미사로 `F`, `f`를 붙여줘야 함. 마찬가지로 컴파일 오류 발생

```java
double a = 123.4;
double b = 1.234e2; // 1.234 * 10**2
```

## 8진수, 16진수

- int 자료형을 사용
- 0으로 시작하면 8진수, 0x로 시작하면 16진수

```java
int octal = 023;    // 19
int hex = 0xC3; // 195
```

## 숫자 연산

```java
public class Computer {
    public static void main(String[] args) {
        int a = 12;
        int b = 4;
        int c = 5;
        System.out.println(a+b);    // 16
        System.out.println(a-b);    // 8
        System.out.println(a*b);    // 48
        System.out.println(a/b);    // 3
        System.out.println(a%c);    // 2
        System.out.println(c%a);    // 5
    }
}
```

## 증감 연산

- `++`, `--` : 증감 연산자

```java
public class Computer {
    public static void main(String[] args) {
        int i = 0;
        int j = 10;
        i++;
        j--;

        System.out.println(i);  // 1
        System.out.println(j);  // 9
        System.out.println(i++);    // 1
        System.out.println(i);  // 2
        System.out.println(++i);    // 3
    }
}