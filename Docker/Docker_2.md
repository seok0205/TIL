# Docker, CI/CD - 2

## Github Actions

### Github Actions란?

- Github에 내장된 CI/CD 도구
- Github와 통하ㅏㅂ이 쉽고, CI/CD 서버 내장되어 있어 따로 구축할 필요 없음. 일정 수준까지 가격 무료.(500MB, 월 2000분)

#### 동작 방법

- repository의 ".github/workflows" 디렉토리에 필요한 Actions 파일들을 yaml 형식으로 작성(필수)
- 작성된 actions 파일들을 github에서 자동으로 실행

### Github Actions에서의 CI

- test를 통과한 코드만 ```develop``` 브랜치와 ```main``` 브랜치에 merge되도록 하여 오류를 방지하고 안정적인 코드가 배포되고 버그를 빠르게 발견

### Github Actions에서의 CD

- 배포를 자동화하는 작업을 기술해서 빠르고 간편하게 배포
- ```main``` 브랜치에 코드가 통합된 경우 운영 환경에 빠르게 배포할 수 있게 함

### Github Actions Details

1. __Workflow__

    - 최상위 개념
    - 여러 Job으로 구성, Event에 의해 트리거될 수 있는 자동화된 프로세스
    - Workflow 파일은 YAML로 작성되고, Github Repository의 .github/workflows 폴더 아래에 저장됨

2. __event__

    - Github Repository에서 발생하는 push, pull request open, issue open, 특정 시간대 반복(cron) 등의 특정한 규칙
    - workflow를 실행(trigger)함

3. __runner__

    - Github Action Runner app이 설치된 가상머신(VM)
    - Workflow가 실행될 instance, 각각의 Job들은 개별적 runner에서 실행

4. __job__

    - 하나의 runner에서 실행될 여러 step의 모음을 의미

5. __step__

    - 실행 가능한 하나의 'shell script' or 'action'

6. __Actions__

    - Workflow의 가장 작은 단위로 재사용 가능
    - Job을 만들기 위해 Step들을 연결

### Workflow Details

1. name

    - github actions의 이름을 정하는 부분

2. on

    - 이 action이 언제 실행되는지에 대한 부분

3. jobs

    - 실제 실행할 내용에 대한 부분
        - runs-on : 어떤 환경에서 실행하는지 기술
        - steps : 실제 실행할 단계들을 기술
            - name : 실행에 표시될 이름
            - uses : 여러가지 plugin 사용
                - 다양한 action들 사용
            - with : plugin에서 사용할 파라미터들
            - run : 실제로 실행할 스크립트