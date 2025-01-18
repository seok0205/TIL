# Docker 심화

- Docker compose 활용해 Django 애플리케이션과 Postres DB 연결.
- 로컬 환경에서 컨테이너 간 네트워크 설정 및 DB 연동 실습

## Docker Compose

- 여러 컨테이너를 정의하고 실행할 수 있는 도구

### 장점

- 복잡한 다중 컨테이너 애플리케이션 쉽게 관리
- 코드 기반 환경 설정(yml 파일)
- 컨테이너 간 네트워크 자동 구성

### 명령어

- `docker-compose up` : 컨테이너 실행
- `docker-compose down` : 컨테이너 종료 및 삭제
- `docker-compose logs` : 로그 확인
