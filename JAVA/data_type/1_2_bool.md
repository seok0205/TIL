# boolean

> 참(True) or 거짓(False)의 값을 갖는 자료형

## 불 연산

```java
public class Seok {
    public static void main(String[] args) {
        2 > 1   // 참
        1 == 2  // 거짓
        3 % 2   // 참 (1은 참)
        "3".equals("2") // 거짓

        int base = 180;
        int height = 185;
        boolean isTall = height > base;

        if (isTall) {
            System.out.println("키가 큽니다."); // 키가 큽니다
        }

        int i = 3;
        boolean isOdd = i % 2 == 1;
        System.out.println(isOdd);  // true 출력
    }
}
```

- `i % 2 == 1`은 i를 2로 나누었을 때 나머지가 1인지 묻는 조건문
- i는 3이고 2로 나누면 나머지는 1이어서 참이 됨
- 따라서 isOdd는 True값을 가짐