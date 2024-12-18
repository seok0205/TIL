# Django ORM

- Object-Relational-Mapping(객체, 관계형, 매핑)

## ORM

- 파이썬으로 SQL을 쓰지 않고 데이터베이스를 조작할 수 있게 해줌
- 객체 지향 언어에서는 클래스를 이용한 객체로 데이터와 기능을 캡슐화해서 다루고 DB는 테이블과 행으로 데이터를 저장하고 관리하는데 이 두가지 사이 개념적 간극을 줄인 것.

### 장점

- SQL 몰라도 DB 조작 가능
- SQL 알아도 기존 복잡한 쿼리문 작성 없이 객체 지향적 접근 가능
- SQL 사용 못한다면 ORM이 변환해주는 게 더 빠름
- 생산성 높음

### 단점

- ORM에서 지원하지 않는 쿼리는 직접 작성
- 서비스 커질수록 ORM으로는 한계 존재
- 매우 효율적인 SQL을 작성하고 싶다면 ORM이 불편할 수 있음

## DB API

- database-abstraction API, ORM으로 DB API를 사용해 데이터베이스 조작하는 것.

### Manager

- 모델 클래스 생성 시 쟝고는 자동적으로 CRUD 할 수 있는 DB API 제공
- 그리고 Magnager를 붙여줌. 작성한 모델 클래스를 이용해 DB 쿼리작업을 도와줌
- Manager 활용해 ORM, QuerysetAPI 사용할 것. Queryset은 ORM을 사용해서 DB로부터 전달받은 객체이다.
- 이 매니저의 기본명은 `objects`

### 기본 형태

- MyModel . objects . all()

- Model Class . Manager . QuerysetAPI

## CRUD with Shell

### Shell

- Django가 제공하는 여러가지 기능을 명령어로 입력해 실행해볼 수 있는 shell 환경

- `python manage.py shell`로 현재 프로젝트 환경을 shell로 접근할 수 있음

- `pip install django-extensions`의 설치로 기본 shell보다 더많은 기능이 있는 shell_plus 사용 가능.

- shell_plus를 사용하기 위해서는 `settings.py`에서 INSTALLED_APPS에 설치한 django_extensions를 등록해줘야 함

### CRUD

- Create, Read, Update, Delete(작성하고 조회하고 수정하고 삭제하는 것)

1. 전체 Article 조회 : `Article.objects.all()`

2. Article 생성 다른 방법
    - `article = Article(title='second_title', content='my_content')`
    - `article.save()`

3. Article 생성 또 다른 방법
    - `Article.objects.create(title='third title', content='마지막 방법임')`
    - save()가 필요하지 않음

```bash
article = Article()
article.title = 'first_title'
article.content = 'my_content'

# 여기에서 전체 Article을 조회해보면
Article.objects.all() # 비어있다

# save()하기전에는 저장되지 않음
article.save()

# 다시 전체 Article을 조회해보면 하나의 아티클이 있음
Article.objects.all()


# 속성 하나씩 접근하기
# 제목 
article.title

# 내용
article.content

# 생성일시
article.create_at

# pk(id)
article.id
```

- __str__매직 메서드 활용해서 문자열 취급 시 처리 로직을 작성 가능.

- 모두 조회하기 : `Article.objects.all()`

- 하나만 조회하기 : `Article.objects.get(id=n)`

- 하나만 조회하려 했는데 조건이 맞아 두개가 반환되면 에러 발생

- 조건으로 조회 : `Article.objects.filter(content='my_content')`

- 조건에 사용되는 매개변수를 `lookup`이라고 함.

- `id__gt` : n보다 큰 id

- `id__in` : 주어진 수에 속하는 id

- `contnet__contains` : content에 어떤 문자열이 포함된

- 수정하기 : 수정 객체 조회 `article = Article.objects.get(id=1)`, 내용 입력 `article.title = 'updated title`, 저장 `article.save()`

- 삭제하기 : 삭제 객체 조회 `article = Article.objects.get(id=2)`, 삭제 `article.delete()`
