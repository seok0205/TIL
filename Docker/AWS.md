# AWS

- Github actions를 활용하여 AWS의 EC2에 배포하고, Docker compose로 실행.

[실습에 활용했던 코드 및 리포](https://github.com/seok0205/cicd-aws.git)  

## 실습 순서

1. AWS 가입 및 로그인

2. 인스턴스 생성(이미지, 인스턴스 유형 설정)

3. 키페어 생성, RSA 암호 방식 및 (.pem) 파일 형식 설정

4. 네트워크 설정(`보안 그룹 생성`, `Allow SSH traffic from`:'위치 무관', `인터넷에서 HTTPS`, `HTTP 트래픽 허용` 둘 다 선택)

5. ec2에 jdk와 docker, docker-compose 설치하여 서버 설정.

6. 깃 리포를 생성하고 앞서 받은 키페어와 호스트 주소를 `Action Secret`의 키로 등록.

    - 리포 메뉴 -> `Settings` -> `Secrets and variables` -> `Actions` 선택

7. 코드 확인 후 JDK 설정, gradlew 실행, jar 파일 전송, 실행.

8. `.github/workflows/deploy.yml` 파일을 커밋.

9. 오픈되어 있는 포트를 통해 서버 접속하여 웹 상태 확인

    - 서버 접속이 안 되면, 해당 인스턴스에 연결된 보안 그룹에서 포트가 개방되어 있는지 확인.
    - 배포하는 동안 scp로 copy할 때 서버 접속이 안 되면, DNS, IP가 변경되지 않았는지 확인.
