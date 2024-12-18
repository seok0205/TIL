# Django Model

## Model

- 저장할 데이터에 대한 필드와 동작들을 포함한 DB 구조
- Django는 Model을 이용해서 데이터를 조작
- 일반적으로 하나의 Model은 하나의 DB 테이블을 의미

## DataBase(DB)

- 잘 정리된 데이터가 모여있는 것

## 쿼리(query)

- DB를 조작할 수 있는 언어

## 스키마(Schma)

- DB의 구조, 관계 등을 정의한 것(전반적인 명세서)

## 테이블(Table)

- 열(Column) - 속성 / 필드(Field)
- 행(Row) - 데이터 / 레코드(Record) / 튜플(Tuple)
- 조직화된 데이터 요소들의 집합

## DB 기본 구조

- 테이블(table)
- 기본키(primary key)
- 열(column)
- 행(row)

## 모델 작성해보기

1. `models.py`
    - `models.Model`을 사아속받아 사용하고자하는 데이터 스키마 정의
    - 모든 모델은 `models.Model`의 서브 클래스로 표현

2. 필드 추가
    - 각 필드는 테이블의 컬럼
    - 필드의 타입에 따라 사용, 각 필드 별로 필요한 옵션들이 존재

```python
from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
```

## 마이그레이션(Migration)

- Django는 마이그레이션을 만들고 이 단위로 DB에 변경사항을 반영

### 마이그레이션 관련 명령어

```python
# 마이그레이션 생성
python manage.py showmigration

# 반영되지 않은 마이그레이션 반영
python manage.py migrate

# 마이그레이션 목록, 적용여부 보여주는 명령어
python manage.py showmigration

# 해당 마이그레이션이 어떤 sql문을 작성했는지 보여주는 명령어
python manage.py sqlmigrate <app_name> <maigration_no>
```

### 마이그레이션 적용 순서

1. Model 변경사항 마이그레이션으로 생성

2. 마이레이션 반영

3. 데이터베이스 확인(쟝고는 기본적으로 sqlite DB 내장해 사용)

## 많이 쓰는 필드

- 어떤 테이블이던 생성일, 수정일은 많이 씀.

- `auto_now_add=True`, `auto_now=True` 사용

- 하지만 이미 기존에 있는 데이터들의 시간값들은 어떻게 해야하는지 마이그레이션 생성시 메세지가 뜸. 엔터 누르면 현재 시간으로 모든 값 처리.
