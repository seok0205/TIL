# Django URL pattern 및 사용 방법

## URLs 구성

1. 각 App의 urls.py 생성 후 `app_name` 변수 및 값을 작성.
2. `app_name`, `url의 name`을 통해 실제 url로 접근하는 방법이 권장.
    - ex: `posts:detail`, `posts:category_list`

```python
# project/urls.py
from django.urls import path, include

urlpatterns = [
    path('posts/', include('posts.urls')),
]

# posts App 생성함
# posts/urls.py
from django.urls import path
from . import views

app_name = 'posts'  # URL namespace 설정 

# name 파라미터를 통해 url의 이름 설정
urlpatterns = [ 
 path('', views.post_list, name='list'),  # /posts/
    path('detail/<int:pk>/', views.post_detail, name='detail'),  # ex) /posts/detail/1/
    path('create/', views.post_create, name='create'),  # /posts/create/
    path('category/<str:category>/', views.category_list, name='category'),  # ex) /posts/category/news/
]
```

## Redirect 방법

```python
from django.shortcuts import redirect

def post_create(request):
    if request.method == 'POST': (권장되는 방법)
        # 1. 기본 URL 이름으로 redirect
        return redirect('posts:list') 
        
        # 2. URL 이름 + 파라미터 (권장되는 방법)
        return redirect('posts:detail', pk=post.id) 
        
        # 3. 절대 경로 URL (권장하지 않음)
        return redirect('/posts/')
        
        # 4. 상대 경로 URL (권장하지 않음)
        return redirect('../')  # 현재 URL 기준 상위 경로로
        return redirect('./detail/')  # 현재 URL 기준 하위 경로로
        return redirect('detail/')  # 현재 URL 기준 하위 경로로(위와 같음)
```

## template에서 url 사용

```html
<!-- 기본 URL -->
<a href="{% url 'posts:list' %}">목록</a>

<!-- 파라미터가 있는 URL -->
<a href="{% url 'posts:detail' pk=post.id %}">상세보기</a>

<!-- 파라미터 여러 개 전달 -->
{% url 'posts:filter' category=category_name tag=tag_name %}

<!-- 쿼리스트링 추가 -->
<a href="{% url 'posts:list' %}?page={{ page }}">페이지</a>

<!-- 절대 경로 (내부 서버 URL접근에서 권장하지 않음, 다른 외부 URL일 경우에만 권장) -->
<a href="/posts/">목록</a>
<a href="/posts/{{ post.id }}/">상세보기</a>

<!-- 상대 경로 (일반적으로 권장하지 않고 특수한 경우에만 사용) -->
<a href="../">상위로</a>
<a href="./edit/">수정</a>
```
