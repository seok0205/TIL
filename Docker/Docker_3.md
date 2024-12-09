# Docker, CI/CD - 3

## Dockerfile로 docker image 생성

### Dockerfile

- Dockerfile은 컴퓨터에서 돌아가는 앱을 만들기 위한 레시피
- Docker image는 앱을 실행하는 데 필요한 모든 것을 담음

#### 사용하는 이유

- 앱을 컨테이너로 만들 때 이미지를 만드는 용도로 Dockerfile을 쓰면 앱이 필요로 하는 모든 것을 한 곳에 담을 수 있음
- 누구나 Dockerfile을 보고 똑같은 앱 환경을 쉽게 만들 수 있음
- Dockerfile 작성하면, 앱을 만드는 과정을 자동화할 수 있고 매번 똑같은 방식으로 앱을 만들고 배포 가능

### Dockerfile Example

- Ubuntu 최신 버전을 기반으로 Nginx를 설치, index.html 파일을 Nginx의 HTML 디렉토리에 복사하는 예시

```dockerfile
FROM ubuntu:latest
MAINTAINER Your Name <your-email@example.com>
RUN apt-get update && apt-get install -y nginx
COPY index.html /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
```

- FastAPI 앱 실행 예제

```dockerfile
FROM python:3.11

RUN pip install pipenv

WORKDIR /app

ADD . /app/

RUN pipenv --python 3.11
RUN pipenv run pip install poetry
RUN pipenv sync
RUN pipenv run pip install certifi

ARG STAGE

RUN sh -c 'echo "STAGE=$STAGE" > .env'
RUN sh -c 'echo "PYTHONPATH=." >> .env'
RUN chmod +x ./scripts/run.sh
RUN chmod +x ./scripts/run-worker.sh

CMD ["./scripts/run.sh"]
```

- nginx 이미지 생성 예제(실제로는 nginx:latest 이미지 사용)

```bash
user  nginx;
worker_processes  1;

error_log  /var/log/nginx/error.log warn;
pid        /var/run/nginx.pid;

events {
    worker_connections  1024;
}

http {
    include       /etc/nginx/mime.types;
    default_type  application/octet-stream;

    log_format  main  '$remote_addr - $remote_user [$time_local] "$request" '
                      '$status $body_bytes_sent "$http_referer" '
                      '"$http_user_agent" "$http_x_forwarded_for"';

    access_log  /var/log/nginx/access.log  main;

    sendfile        on;
    #tcp_nopush     on;

    keepalive_timeout  65;

    gzip  on;
    gzip_disable "msie6";

    include /etc/nginx/conf.d/*.conf;
}
```

1. Docker image 생성

    `docker buildx build -t my-nginx:latest .`
    `docker build -t my-nginx:latest .`

    - 현재 디렉토리에서 Dockerfile 기반으로 my-nginx:latest라는 이름의 Docker image 생성

2. Docker Container 실행

    `docker run -d -p 80:80 my-nginx:latest`

    - my-nginx:latest 이미지 기반 컨테이너 실행, 80번 포트를 호스트 머신의 80번 포트로 맵핑함.

3. Docker Container 종료 및 업데이트

    `docker stop my-nginx`

- 이렇게 생성된 Docker image는 Docker Registry를 사용하여 다른 사용자와 공유 가능. Registry는 Docker image를 저장 및 공유 가능.

### Dockerfile 명령어

1. __FROM__

    - 베이스 이미지 지정
    - ex. `FROM ubuntu:22.04`

2. __MAINTAINER__

    - Dockerfile 작성한 사람의 정보를 입력
    - ex. `MAINTAINER naebaecaem <nbcamp@spartacoding.co>`

3. __LABEL__

    - 이미지에 메타데이터를 추가
    - ex. `LABEL purpose='nginx test'`

4. __RUN__

    - 이미지를 생성하는 동안 실행할 명령어를 입력
    - 사용자를 지정하지 않은 상태라면, root로 실행
    - ex. `RUN apt update && apt upgrade -y && apt autoremove && apt autoclean`
    - ex. `RUN apt install openjdk-21-jdk`

5. __CMD__

    - 컨테이너를 생성할 때, 실행할 명령어를 입력
    - 컨테이너를 생성하 때만 실행
    - 추가적인 명령어에 따라 설정한 해당 명령어 수정 가능
    - ex. `CMD ["nginx", "-g", "daemon off;"]`

6. __ENTRYPOINT__

    - 컨테이너 시작할 때, 실행할 명령어를 입력
    - 컨테이너를 시작할 때마다 실행
    - 추가적인 명령어 존재 여부와 상관 없이 무조건 실행
    - ex. `ENTRYPOINT ["npm", "start"]`

7. __ENV__

    - 환경 변수를 설정
    - 이미지 안에 각종 환경 변수를 지정
    - ex. `ENV STAGE staging`
    - ex. `ENV JAVA_HOME /usr/lib/jvm/java-8-oracle`

8. __WORKDIR__

    - 작업 디렉터리를 지정
    - ex. `WORKDIR /app`

9. __COPY__

    - 파일을 복사
    - 호스트의 파일이나 디렉터리를 이미지 안에 복사
    - Docker Context, 즉, 빌드 작업 디렉터리 내 파일만 복사 가능
    - ex. `COPY index.html /usr/share/nginx/html`

10. __USER__

    - 사용자를 설정
    - Container의 기본 사용자는 root. root 권한이 필요 없는 application이라면 다른 사용자로 변경하여 사용해야 함

    ```dockerfile
    RUN ["useradd", "user"]
    USER user
    RUN ["/bin/bash, "-c", "ls"]
    ```

11. __EXPOSE__

    - Container에서 노출할 포트를 지정
    - ex. `EXPOSE 80`
    - ex. `EXPOSE 443`

## Docker Compose로 여러 개의 Container 관리

### Docker Compose란?

#### 사용이유

1. 편하게 설정하기 : Docker Compose는 여러 컨테이너를 한 파일에 적어서 설정 가능. 이 파일에 컨테이너가 무슨 이미지를 쓸지, 어떤 포트를 사용할지, 환경 변수는 뭐가 필요한지 등을 적어둠

2. 자동으로 배포하기 : 개발자가 명령어를 입력할 필요 없이, 설정 파일이 있으면, Docker Compose가 알아서 컨테이너들을 만들어 주고 실행함

3. 의존성 관리 : 컨테이너들이 서로 의존하는 관계가 있으면, Docker Compose가 이것을 관리해줌. 컨테이너 A가 B를 필요로 한다면, A 실행 후 B 실행.

4. 모니터링과 로깅 : 컨테이너들이 어떻게 돌아가는지 지켜보고, 로그도 모아줌. 이로 인해 문제가 생겼을 때 빨리 찾아서 고칠 수 있음.

5. 확장성 : 여러 컨테이너를 하나의 그룹으로 관리 가능. 웹 앱을 만드는 여러 컨테이너를 한꺼번에 관리하고 확장하기 쉽기 때문에 이점을 가짐.

6. 유연성 : 개발 환경, 테스트 환경, 실제 운영 환경에서도 같은 설정 파일을 써서 일관성 유지 가능.

7. 보안 강화 : 컨테이너들의 네트워크를 분리해서 외부로부터의 접근을 제한할 수도 있음. 보안이 더욱 강화.

8. 유지보수가 쉬움 : 설정 파일 하나로 컨테이너들을 관리. 수정점이 생길 시에 파일만 수정하면 알아서 변경사항 적용.

#### 사용시점

1. 개발 환경에서

    - 앱을 개발할 때, 앱을 따로 떼어 놓고 실행하고 테스트할 수 있는 환경이 필요. Docker Compose를 쓰면 이런 환경 쉽게 만들고 관리 가능.
    - 앱이 필요로 하는 모든 서비스(DB, Queue, cache, web api 등)를 정리해주고, `docker compose up` 명령어로 한 번에 시작 가능.
    - 새 프로젝트 시작 시 시간 절약. 설명서 대신 Compose 파일로 모든 설정.

2. 자동화된 테스트 환경에서

    - 자동화된 테스트는 앱이 잘 돌아가는지 확인하는 데 중요. 이런 테스트를 위한 별도의 환경을 쉽게 만들고 없앨 수 있음.
    - Compose 파일에 테스트 환경 정의해두고, 간단한 명령어 몇 개로 테스트 환경을 만들고 테스트를 실행한 다음, 다시 환경을 없앨 수 있음.

    ```bash
    docker compose up -d
    ./run_tests
    docker compose down
    ```

3. 단일 호스트 배포에서

    - 주로 개발과 테스트에 많이 쓰이지만, 실제로 앱을 운영하는 환경(프로덕션)에도 쓸 수 있음. 매번 새 버전이 나올 때마다 이런 용도로도 쓰기 좋게 상시 개선 중

#### 특징과 장점

1. 한 번에 여러 컨테이너 설정하기

    - Docker Compose는 여러 컨테이너의 설정을 하나의 YAML 파일에 넣어서 관리. 이 파일 하나로 여러 컨테이너의 모든 환경을 설정, 그걸로 여러 컨테이너를 한 번에 실행 가능.

2. 빠른 서비스 실행

    - 설정 값들을 저장해 두고 다시 쓸 수 있음. 만약 설정이 바뀌지 않았다면, Docker Compose는 이전에 저장해둔 정보를 다시 사용해서 서비스를 더 빨리 시작할 수 있음.

3. 같은 네트워크에서 쉽게 연결

    - `docker-compose.yaml` 파일에 있는 애플리케이션들은 모두 같은 네트워크에 자동으로 연결. 복잡한 네트워크 설정 없이도 여러 컨테이너가 서로 쉽게 통신할 수 있음.

#### 실행하기

1. 각 애플리케이션의 Dockerfile 작성 : 보통 내가 만든 애플리케이션을 실행하기 위한 Dockerfile만 작성

2. docker-compose.yaml 파일 작성 : 내가 만든 애플리케이션을 실행하기 위해 필요한 database라든지 redis라든지 다른 서비스들을 한꺼번에 정의하는 파일을 작성

3. `docker compose up`으로 실행

### YAML file

- YAML file은 컴퓨터가 읽을 수 있는 설정 파일. 사람이 읽기에도 쉬운 텍스트 형식. 'YAML Ain't Markup Language'

- 일반 텍스트. 목록이나 키-값 쌍 같은 것들처럼 설정이나 데이터를 쉽게 알아볼 수 있는 형식으로 나열함.

- YAML file은 설정을 정리하고 관리하기에도 좋다. docker compose에서는 yaml 파일을 사용해서 여러 컨테이너의 설정을 한 곳에 쉽게 정리가 가능하다.

- yaml은 읽기 쉽고, 쓰기도 간단해서 많은 프로그램과 도구에서 선호하는 설정 파일 형식.

- YAML file은 구조가 명확하고 간단해서 사람이 보기에도 이해하기 쉽다. 들여쓰기를 사용해서 가가 설정의 관계를 나타냄.

#### YAML의 문법

1. 키-값 쌍 : 키와 값으로 이루어진 쌍으로 구성. 키와 값은 콜론(:)으로 구분

2. 리스트 : 쉽표(,)로 구분된 값들의 리스트로 구성됨

3. 딕셔너리 : 중괄호({})로 둘러싸인 키-값 쌍의 리스트로 구성됨

4. 불린 값 : true, flase, yes, no 등의 값으로 표현

5. 문자열 : 큰 따옴표("")나 작은 따옴표('')로 둘러싸인 문자열로 표현

- 들여쓰기가 잘못된 경우 의도와 다르게 해석하게 됨.
- [yaml lint](https://www.yamllint.com/)에서 들여쓰기 검사 가능함.

### Docker Compose file example

#### Docker Compose file example - 1

```yaml
version: '3'    # docker engine의 버전
services:   # 컨테이너 대신 서비스 개념으로 간주
  web:
    image: nginx:latest
    ports:
      - 80:80
    volumes:
      - ./web:/usr/share/nginx/html
    depends_on:
      - api
    links:
      - api:api
  api:
    image: java:latest
    volumes:
      - ./api:/app
    ports:
      - 8080:8080
    environment:
      - REDIS_HOST=redis
      - MYSQL_HOST=mysql
      - MYSQL_USER=root
      - MYSQL_PASSWORD=password
      - MYSQL_DATABASE=test
    depends_on:
      - mysql
      - redis
    links:
      - mysql:mysql
      - redis:redis
  redis:
    image: redis:latest
    ports:
      - 6379:6379
  mysql:
    image: mysql:latest
    ports:
      - 3306:3306
    volumes:
      - ./mysql:/var/lib/mysql
    environment:
      - MYSQL_ROOT_PASSWORD=password
      - MYSQL_DATABASE=test
      - MYSQL_USER=root
      - MYSQL_PASSWORD=password
```

1. `version` : Docker Compose의 버전 정의
2. `services` : 네 개의 서비스 정의
    - `web` 서비스는 Nginx image 사용, 포트 80번을 호스트 머신에 노출.
    - `api` 서비스는 Java image 사용, 포트 8080번을 호스트 머신에 노출.
    - `redis` 서비스는 Redis image 사용, 포트 6379번을 호스트 머신에 노출.
    - `mysql` 서비스는 MySQL image 사용, 포트 3306번을 호스트 머신에 노출.
3. `voulumes`
    - `web` 서비스는 현재 디렉토리 내 `web` 디렉토리를 컨테이너에 연결함
    - `api` 서비스는 현재 디렉토리 내 `api` 디렉토리를 컨테이너에 연결함
    - `mysql` 서비스는 현재 디렉토리 내 `mysql` 디렉토리를 사용하여 MySQL 데이터를 영구적으로 저장하게 함
4. `depends_on` : 각 서비스 간의 의존성을 정의. `web` 서비스는 `api` 서비스에 의존. `api` 서비스는 `mysql`, `redis` 서비스에 의존
5. `links` : 각 서비스 간의 링크를 정의. `web` 서비스는 `api` 서비스에 링크됨. `api` 서비스는 `mysql`, `redis` 서비스에 링크됨

- 위 예제에서는 `web` 서비스와 `api` 서비스가 각각 독립적인 컨테이너로 실행. `web` 서비스는 `api` 서비스에 의존하며, `api` 서비스는 `mysql`, `redis` 서비스에 의존. `redis`, `mysql` 서비스는 각각 독립적인 컨테이너로 실행.

#### Docker Compose file example - 2

```yaml
services:
  web:
    build:
      context: .    # Dockerfile 의 위치
      dockerfile: Dockerfile    # Dockerfile 파일명
    container_name: testapp_web_1    # 생략하는 경우 
    # 자동으로 부여 docker run 의 --name 옵션과 동일
    ports: "8080:8080"  # docker run 의 -p 옵션과 동일
    expose: "8080"    # 호스트머신과 연결이 아니라 
    # 링크로 연결된 서비스 간 통신이 필요할 때 사용
    networks: testnetwork    # networks 를 최상위에 정의한다면 해당 이름을 사용
    # docker run의 --net 옵션과 동일
    volumes: .:/var/lib/nginx/html    # docker run 의 -v 옵션과 동일
    environment:
      - APPENV=TEST    # docker run 의 -e옵션과 동일
    command: npm start   # docker run 의 가장 마지막
    restart: always    # docker run 의 --restart 옵션과 동일
    depends_on: db    # 이 옵션에 지정된 서비스가 시작된 이후에 `web`서비스가 실행
    links: db # Docker가 네트워크를 통해 컨테이너를 연결하도록 정의합니다. 
    # 컨테이너를 연결할 때 Docker는 환경 변수를 만들고 
    # 컨테이너를 알려진 호스트 목록에 추가하여 서로를 검색할 수 있도록 합니다.
    deploy:    # 서비스의 복제본 개수 등 지정
      replicas: 3
      mode: replicated
```

#### Docker Compose file example - 3

- `volumes` : 도커 볼륨 혹은 호스트 볼륨을 마운트하여 사용. 도커 볼륨의 경우 `docker-compose` 파일에 선언된 볼륨만 `docker-compose.yml`에서 사용 가능.

```yaml
version: "3.9"
services:
  web:
    # ...
    volumes:
      - README.md:/docs/README.md # 호스트의 README.md 파일을 컨테이너 내부 /docs/README.md에 마운트   
      - logvolume01:/var/log # 선언된 도커 볼륨 logvolume01을 컨테이너 내부 /var/log에 마운트
# ...
volumes:
  logvolume01: {} # 도커볼륨 logvolume01 선언
```

- `network` : 서비스(컨테이너)가 소속된 네트워크. 따로 지정하지 않을 시 default_${project}와 같이 지정. 기본적으로 컨테이너는 같은 네트워크에 있어야 서로 통신이 가능.

- `healthcheck` : 서비스 컨테이너가 'healthy'한지 계속 체크. Dockerfile에 정의된 것을 먼저 따르지만 docker-compose 파일에서 재지정 가능

```yaml
healthcheck:
  test: ["CMD", "curl", "-f", "http://localhost"]
  interval: 1m30s
  timeout: 10s
  retries: 3
  start_period: 40s
  start_interval: 5s
```

#### Docker Compose CLI

- `docker-compose [COMMAND] [SERVICES...]`의 형태로 지정된 서비스(컨테이너)만 제어가 가능함. 예를 들어 web, redis 중 web만 기동하고 싶을 경우 `docker-compose up -d web`와 같이 실행함.

1. `docker-compose up`

    - `docker-compose up` 실행 시 다음 순서로 진행. 이미 생성된 경우 해당 단계를 건너 뜀.
    1. 서비스를 띄울 네트워크 생성
    2. 필요한 볼륨 생성(or 이미 존재하는 볼륨과 연결)
    3. 필요한 이미지 풀(pull)
    4. 필요한 이미지 빌드(build)
    5. 서비스 실행(depends_on 옵션 사용 시 서비스 의존성 순서대로 실행)

2. `--build` : 이미 빌드가 되었더라도 강제로 빌드를 진행

3. `-d` : 백그라운드로 실행

4. `--force-recreate` : docker-compose.yml 파일의 변경점이 없더라도 강제로 컨테이너를 재생성. 즉, 컨테이너가 종료되었다가 다시 생성.

5. `docker-compose down` : 서비스 멈추고 삭제. 컨테이너와 네트워크 삭제.

6. `--volume` : 선언된 도커 볼륨도 삭제.

7. `docker-compose stop`, `docker-compose start` : 서비스 멈춤, 멈춘 서비스 시작.

8. `docker-compose ps` : 현재 환경에서 실행 중인 각 서비스의 상태 표시.

9. `docker-compose logs` : 컨테이너 로그 확인.

10. `-f` : tail -f와 유사하게 컨테이너 로그를 실시간으로 확인.

- `docker-compose exec` : 실행 중인 컨테이너에 해당 명령어를 실행.

```bash
docker-compose exec django ./manage.py makemigrations
docker-compose exec db psql postgres postgres
```

- `docker-compose run` : 특정 명령어를 일회성으로 실행하지만 컨테이너를 batch성 작업으로 사용하는 경우에 해당. 이미 기동하고 있는 컨테이너에 명령어를 실행하고자 하면 docker-compose exec를 사용하는 반면에 docker-compose run을 사용할 경우 컨테이너를 기동시키고 특정 명령어를 실행이 완료된 후에 컨테이너를 종료.

```bash
docker-compose exec web echo "hello world" # 이미 실행된 web 컨테이너에서 echo "hello world"를 실행
docker-compose run web echo "hello world" # web 컨테이너에서 echo "hello world"를 실행하고 컨테이너 종료
```

### Docker Compose file 실전 예제

- fastai app

```dockerfile
FROM python:3.10

RUN pip install pipenv

WORKDIR /app

ADD . /app/

RUN pipenv --python 3.10
RUN pipenv run pip install poetry
RUN pipenv sync
RUN pipenv run pip install certifi


ARG STAGE

RUN sh -c 'echo "STAGE=$STAGE" > .env'
RUN sh -c 'echo "PYTHONPATH=." >> .env'
# ENV PYTHONPATH=/app
RUN chmod +x ./scripts/run.sh
RUN chmod +x ./scripts/run-worker.sh

# ENV PYTHONPATH=/app
CMD ["./scripts/run.sh"]
```

- docker_compoe.yaml

```yaml
version: "3"
services:
  channel-api:
    image: xxxx.dkr.ecr.ap-northeast-2.amazonaws.com/reaction-channel:${AWS_ENV_STAGE:-dev}-${TAG:-latest}
    build:
      context: .
      dockerfile: dockerfile
      args:
        STAGE: ${STAGE:-develop}
    ports:
      - "8000:8000"
    environment:
      - NEW_RELIC_CONFIG_FILE=newrelic.ini
      - NEW_RELIC_ENVIRONMENT=ecs-${STAGE:-develop}
    logging:
      driver: awslogs
      options:
        awslogs-stream-prefix: channel
        awslogs-group: /ecs/reaction/${AWS_ENV_STAGE:-dev}/channel-api
        awslogs-region: ap-northeast-2

  reverseproxy:
    image: xxxxx.dkr.ecr.ap-northeast-2.amazonaws.com/reverseproxy:prod-channel-latest
    ports:
    - "80:80"
    - "81:81"
    logging:
      driver: awslogs
      options:
        awslogs-stream-prefix: reverseproxy
        awslogs-group: /ecs/reaction/${AWS_ENV_STAGE:-dev}/reverseproxy
        awslogs-region: ap-northeast-2
```

- 코드를 clone

```bash
cd ~
git clone https://github.com/...
```

- docker-compose로 실행

```bash
cd ~/filepath
docker-compose up -d
docker-compose logs -f
```

## Docker Monitoring, logging

### Docker Monitoring

- Docker Monitoring은 컨테이너가 어떻게 돌아가고 있는지 지켜보는 것. 컨테이너의 성능, 사용 중인 자원(cpu memory), 네트워크 사용량 등 확인 가능.
- 도커에는 모니터링을 위한 기본 도구들이 있음. 외부 모니터링 도구를 사용해 더 자세한 정보를 얻거나, 여러 컨테이너의 데이터를 한번에 볼 수도 있음.
- 모니터링을 통해 문제를 빨리 발견하고 해결 가능. 컨테이너를 효율적으로 관리하고 최적화할 수 있음.

### Container resource monitoring

- 내가 실행하는 앱이 어떤 상태인지 Docker Monitoring을 통해 알아봄

#### Docker stats

- 컨테이너 모니터링의 시작점, Docker에서 제공하는 간단하고 실용적인 모니터링 도구. 명령어를 사용하면 현재 실행 중인 Docker Container들이 얼마나 많은 자원을 사용하고 있는지 실시간으로 볼 수 있음.

- 자원을 얼마나 사용하고 있는지 알면, 성능 문제를 빨리 찾아내고 해결 가능.

- `docker stats` 입력하면 실행 중인 컨테이너들의 상태가 나옴. cpu 사용률, 메모리 사용량, 네트워크 입출력, 디스크 입출력 등.

- 특정 컨테이너만 보고싶다면 `docker stats [container]` 입력.

#### htop

- 리눅스 시스템을 모니터링하는데 사용되는 강력한 도구. 일반적 시스템 모니터와 비슷, 사용하기 편하고 여러 유용한 기능 제공.

- CPU, memory 사용량 같은 중요한 정보를 실시간으로 볼 수 있음.

- 실시간 모니터링, 프로세스 관리, 사용자 친화적 인터페이스가 주요 기능.

```bash
docker run --name test-tools -ti -d ubuntu:22.04

docker exec -ti test-tools /bin/bash
apt update; apt upgrade -y; apt install htop -y;
htop
exit
```

- 키보드 화살표 사용으로 프로세스 목록을 넘길 수 있고, `F9`로 프로세스 종료 가능.

#### df

- disk free의 약자. 리눅스 시스템 전체의 디스크 사용량 확인 가능.

```bash
docker exec -ti test-tools /bin/bash
df -h
exit
```

#### du

- 디렉토리 별로 사용 공간을 나타냄.

```bash
docker exec -ti test-tools /bin/bash
du -sh # 현재 디렉토리의 총 디스크 사용량을 GB 단위로 보여줌
du -h --max-depth=1 # 현재 디렉토리 한 단계 아래 디렉토리 까지만 사용량을 보여줌
exit
```

### Container logging

- 만든 앱의 실행 과정을 기록한 로깅. Docker는 모든 컨테이너의 표준 출력(stdout) or 표준 에러(stderr)를 캡쳐하여 `json-file` 로깅 드라이버를 사용해 json 형식으로 파일에 기록함.

- Ubuntu에서는 `/var/lib/docker/containers/[컨테이너ID]/[컨테이너ID]-json.log`에 로그가 기록.

- 특정 컨테이너의 로그 보는 법

```bash
docker run --name logs-test --rm -d ubuntu:22.04 /bin/bash -c 'while true; do date; sleep 1; done'

# logs-test 컨테이너의 로그를 전체 출력하기
docker logs logs-test

# logs-test 컨테이너의 로그를 tailing하기
docker logs -f logs-test

# 마지막 10줄부터 로그를 계속 보기
docker logs -f --tail 10 logs-test
```

- log 파일 설정 확인

```bash
docker inspect logs-test --format "{{.LogPath}}"
```

- 로그 로테이션 설정 : 실제 운영 시 로그 파일의 크기가 계속 커질 수 있기 때문에 로그 파일의 최대 크기와 최대 파일 개수를 지정함.

- Container별 로깅 드라이버 구성

```bash
docker run -d \
--log-driver json-file \
--log-opt max-size=10m \
--log-opt max-file=10 \
--name nginxtest \
--restart always \
-p 80:80 \
-p 443:443 \
nginx:latest
```

#### 실습

nginx를 Container로 실행시키고 log file 크기와 개수를 제한 확인  

- Container의 log file 크기, 개수 제한

```bash
docker run -d \
--log-driver json-file \
--log-opt max-size=1m \
--log-opt max-file=5 \
--name nginxtest \
--restart always \
-p 80:80 \
-p 443:443 \
nginx:latest
```

- log 보기

```bash
docker logs -f nginxtest
```

- log를 임의로 많이 생성하기

```bash
sudo apt update && sudo apt install -y wrk

wrk -t10 -c100 -d30s http://localhost:80/
```

- docker compose 파일에서 설정 : app Container는 10mb 이하의 log file을 최대 10개까지 생성.

```bash
services:
  app:
    ...
    logging:
      driver: 'json-file'
      options:
        max-size: '10m'
        max-file: '10'
```

- 사용한 Container 정리

```bash
docker stop nginxtest
docker container rm nginxtest
```
