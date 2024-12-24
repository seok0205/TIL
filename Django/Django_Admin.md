# Django Admin

## 관리자 페이지(Admin Site)

- 실제 서비스 운영 시 서비스 관리 페이지가 필요. 모든 관리자에게 DB를 열어주거나, 매번 SQL을 입력해서 보거나 수정할 수는 없기 때문.

### Django의 Admin Site

- Django는 기본적으로 관리자 사이트 제공. 강력한 장점 중 하나.
- 직접 record를 조회, 생성, 수정, 삭제할 수 있는 모든 기능 제공.
- 이외에도 각종 권한 부여를 해서 제한하거나, 페이지 자체를 커스텀 하는 것도 가능.

### 직접 사용

- admin 계정 생성 : `python manage.py createsuperuser`(최소 `is_staff`)권한이 필요.

- admin에서 관리할 모델 등록 : 관리자 페이지에서 사용할 모델은 직접 등록해주는 것이 필요. 각 앱의 admin.py에서 설정 가능.

#### articles

- 기본 등록

```python
# articles/admin.py
from django.contrib import admin
from .models import Article

admin.site.register(Article)
```

- 등록 후 살펴 보면 조금 전 등록한 모델이 보임.

- 모델 추가. 게시글이 많아지면 원하는 게시물만 보고 싶음. 작성일 기준으로 정렬해 볼수 있게 하려면

```python
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title", "created_at")
    search_fields = ("title", "content")
    list_filter = ("created_at",)
    date_hierarchy = "created_at"
    ordering = ("-created_at",)
```

- 이 밖에도 CSS, 자바스크립트를 사용하여 원하는 대로 커스텀 사용도 가능.
