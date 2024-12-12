# Django

- Python 기반, 웹 프레임워크

## 시작 과정

- 프로젝트 생성
    `django-admin startproject <projectname> <dir>`  

- 현재 폴더에 생성
    `django-admin startproject <projectname> .`  

- 개발 서버 실행(폴더 안쪽 이동)
    `cd <projectname>`  
    `python manage.py runserver`  

    1. settings.py : 프로젝트 설정 관리
    2. urls.py : 어떤 요청 처리할지 결정
    3. init.py : 하나의 폴더를 하나의 파이썬 패키지로 인식하도록 하는 파일(호환성. 구버전에서도 동작하도록)
    4. wsgi.py : 웹 서버 관련 설정
    5. manage.py :  Django 프로젝트 유틸리티(조종기)
