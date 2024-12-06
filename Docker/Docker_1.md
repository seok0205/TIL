# Docker, CI/CD

## CI/CD가 무엇인가?

### CI/CD의 정의

- Continuous Integration/Continuous Deployment(Delivery)의 약자로, 지속적인 통합, 지속적인 배포(서비스 제공)을 의미한다.

1. 지속적인 통합(Continuous Integration)

    - 자동화된 빌드, 테스트 제공, 안정적 코드를 빠르게 제공할 수 있는 밑거름

2. 지속적인 서비스 제공(Continuous Delivery)

3. 지속적인 배포(Continuous Deployment)

    - 배포를 자동화하여 배포 시간을 단축하고 코드 결과물을 빠르게 지속적으로 제공

4. 과정

    - 코드 작성 : 소스 코드 리포에 업로드
    - 빌드 : 소스 코드 컴파일, 라이브러리 추가, 필요한 파일 생성하는 과정
    - 테스트 : 빌드된 결과물이 기능이 정상적으로 작동하는지, 버그를 발견하고 수정하는 과정
    - 배포 : 테스트 통과한 결과물을 서버에 업로드, 사용자에게 제공

### 과거의 배포

- 오랜 시간 동안 구현 후 테스트하여 가끔 배포. 배포하는 과정에서 같은 과정을 여러 서버에 반복을 하게 됨.

- 클러스터에서 서버 1 분리 -> 서버 1에서 톰캣 종료 -> 기존 앱 버전 제거 -> 새 앱 버전 복사(ssh 접속 or scp 복사) -> 구성 파일의 속성 업데이트 -> 톰캣 시작 -> 클러스터에 서버 1 다시 연결

- 출시 직후 테스트에서 아무도 발견치 못한 버그가 있을 경우, 롤백하거나 빠르게 수정하고 테스트하여 다시 추가 배포를 하는 등의 큰 비용이 듦.

### 현대적 개발 과정

- 스크럼으로 대표되는 애자일 개발 -> 특정 주기마다 개발, 테스트 및 프로덕션에 통합된 기능을 출시

- 테스트 및 기능 출시에 오랜 기간이 걸리고 손배포를 통해 실패 위험성을 안고 있다면 -> 빠르게 배포는 불가

- Docker를 통해 서버를 표준화하고 같은 환경에서 테스트 및 배포 테스트를 진행하고 이 과정을 자동화 -> 테스트로 자동화 배포를 사용해 실패 확률 저하

- 자동화된 과정으로 지속적으로 코드를 통합하여 지속적으로 자동 배포

- 컨테이너와 빌드/테스트 도구의 발전에 따라 Docker가 테스트, 실제 배포도 담당

## Docker 기초

### Docker 사용 이유

1. 애플리케이션 개발과 배포가 편해짐

    - Docker container 내부에서 여러 SW를 설치해도 호스트 OS에 영향이 없음
    - CI/CD에서 CI 과정의 테스트에서 Docker를 활용
    - 어떤 서버에 올리더라도 같은 환경으로 구성된 컨테이너로 동작하기 때문에 표준화된 배포를 구성 가능

2. 여러 애플리케이션의 독립성과 확장성 증가

3. Docker가 가상화에서 사실상 표준의 위치

### Docker 설치

- WSL2 설치 -> Ubuntu 설치 -> Docker, Docker Compose 버전 확인 -> Docker Desktop 설치 및 설정

## Docker Image 관리

### Docker image 이해와 구조 확인

- Docker Container 서비스를 위한 image는 Container 런타임에 필요한 바이너리, 라이브러리 및 설정 값 등을 포함하고, 변경되는 상태값을 보유하지 않고(Stateless) 변하지 않음(Immutable, Read-Only)

1. Stateless : 애플리케이션과 관련된 모든 파일과 라이브러리를 포함하고 있기 때문에, 다른 환경에서도 동일한 애플리케이션 실행 가능

2. Immutable : 이미지가 한 번 생성되면 변경할 수 없는 것

- Docker Image는 필요한 파일만 포함, 용량이 작고, 이미지의 변경이 필요한 경우 새 이미지 생성 필요

- [hub.docker.com](hub.docker.com)에서 이미지 제공 및 해당 사이트로 이미지 제공

- Private Registry 서버를 통해서도 이미지를 제공받거나 제공 가능

- ```docker pull``` : Docker Image 내려받기

- ```docker image inspect``` : Docker 이미지 구조 확인

- ```docker image inspect --format="{{info_name}}" nginx:latest``` : 이미지 내부 구조 정보를 json 형태로 제공

- ```docker image history``` : Dockerfile에 대한 정보(여러 개의 계층 구조로 구성된 것 확인 가능)

## Docker Container와 Container를 다루는 CLI

### Docker Image와 Docker Container의 관계

- Image : Container에 대한 OS, Application, Library 등의 정보 담음

- Container : Image를 실행한 상태, 1개의 Image로부터 N개의 Container를 생성할 수 있는 1 대 다의 관계

### Docker Container 수동 생성

1. ```docker pull [imagename]``` : 이미지 다운
2. ```docker images``` : pull된 것 확인
3. ```docker create -ti --name [Containername] [imagename]``` : 생성
4. ```docker ps -a``` : 생성 확인
5. ```docker start [Containername]``` : 컨테이너 시작
6. ```docker attach [Containername]``` : 현재 터미널 세션이 컨테이너 터미널과 연결

- ```docker run -ti --name=[Containername] [imagename] /bin/bash``` : run = create/start/attach 과정

### Docker run 자주 사용하는 옵션

1. ```-d``` :  detached mode; 백그라운드 모드
2. ```-p``` : 호스트와 컨테이너의 포트 연결(포워딩)
3. ```-v``` : 호스트와 컨테이너의 디렉토리 연결(마운트)
4. ```-e``` : 컨테이너 내에서 사용할 환경변수 설정
5. ```-name``` : 컨테이너 이름 설정
6. ```-rm``` : 프로세스 종료 시 컨테이너 자동 삭제
7. ```-ti``` : -i, -t를 동시에 사용한 것, 터미널 입력을 위한 옵션

### 실행중인 Container에 대한 정보

- ```docker top [containername]``` : 컨테이너에서 실행 중인 프로세스 조회
- ```docker port [containername]``` : 컨테이너에서 매핑된 포트 조회
- ```docker stats [containername] --no-steram``` : 컨테이너 리소스 통계 출력(1회)
- ```docker stats [containername]``` : 컨테이너 리소스 통계 출력(스트림)

### Docker logs

- ```docker logs [containername]``` : 표준 출력(stdout), 표준 에러(strerr) 출력
- ```docker logs -f [containername]``` : 로그 계속 출력
- ```docker info | grep -i log``` : 출력된 로그는 파일로 관리, HostOS의 disk 사용

### CLI(Command Line Interface)

- ```docker inspect [containername]``` : 컨테이너 내부 확인

- ```docker stats``` : 도커 상태 확인

- ```docker events``` : 도커 프로세스 이벤트 확인

- ```docker stop [containername]``` : 컨테이너 중지
- ```docker start [containername]``` : 컨테이너 시작
- ```docker pause [containername]``` : 컨테이너 일시정지
- ```docker unpause [containername]``` : 컨테이너 이어서 시작

- ```docker ps``` : 실행중인 컨테이너 목록

### docker exit code

- 0 : Docker Process가 수행해야 할 모든 Command or Shell을 실행하고 정상 종료
- 255 : Docker Image에 정의된 EntryPoint or CMD가 수행이 완료되었을 경우 발생
- 125 : Docker run 명령어의 실패로 실제 docker process가 기동되지 않음
- 126 : Docker Container 내부에서 Command를 실행하지 못할 경우 발생
- 127 : Docker Container 내부에서 Command를 발견하지 못했을 경우 발생
- 137 : kill -9로 인해 종료
- 141 : 잘못된 메모리 참조하여 종료
- 143 : Linux Signal로 정상 종료
- 147 : 터미널에서 입력된 정지 시그널로 종료
- 149 : 자식 프로세스가 종료되어 종료

### Docker Container 정리 방법

- ```docker container prune``` : 실행 중이 아닌 모든 컨테이너 삭제
- ```docker image prune``` : 태그가 붙지 않은 모든 이미지 삭제
- ```docker system prune``` : 사용하지 않는 도커 이미지, 컨테이너, 볼륨, 네트워크 등 모든 도커 리소스 일괄적으로 삭제
