# Model Relationship (1:N)

## Many to one relationships

1. 1:N 관계 예시
    - 만약 `Article`에 `Author`라는 개념을 둔다면
        - 하나의 Article은 한 명의 Author를 가질 수 있다.
        - 한 명의 Author는 여러개의 Article을 가질 수 있다.
    - 만약 `Article`에 `comment`라는 개념을 둔다면
        - 하나의 `Article`은 여러 개의 `Comment`를 가질 수 있다.
        - 하나의 `Comment`는 하나의 `Article`을 가질 수 있다.

2. Foreign Key
    - 외래키를 의미함
    - 관계형 DB에서 한 테이블ㅇ의 필드 중 다른 테이블의 행을 유잃게 식별이 가능한 키

### 실습 : 댓글 구현하기

```python
# articles/models.py
class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    content = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content
```

> on_delete 옵션

1. CASCADE : 부모가 삭제되면 이를 참조하는 객체도 삭제
2. PROTECT : 참조하는 객체가 있을 경우 예외 발생시켜 삭제 방지
3. SET_NULL : 참조하는 객체가 삭제될 경우 NULL 값으로 지정

> `<filename>_id`

1. 참조 테이블의 이름 뒤에 `_id`를 붙여 컬럼을 자동으로 생성.

> ORM 사용해보기

- 터미널에서 shell_plus 이용하기

```bash
python manage.py shell_plus

comment = Comment()

comment.content = “first comment”

comment.save()
```

1. Comment 생성 : `Comment.objects.create(content="")` (article_id 값을 지정해야함.)

2. 오류 발생시 `article_id` 값을 지정해줌.

3. `comment.article_id = article.pk`로 명시하지 않아도 됨.

```bash
article = Article.objects.get(pk=1)

comment = Comment()

comment.article = article

comment.content = "first comment"

comment.save()
```

- 두번째 댓글 생성 : `Comment.objects.create(content="", article=article)`

- `comment.article`로 어떤 article인지 접근 가능.

- `comment.article.title`, `comment.article.content`로 제목, 내용 알 수 있음.

- 정참조 : Comment(N) -> Article(1) 참조

- Model Class에서 Field가 정의되어 있으므로 `comment.article`로 쉽게 접근 가능.

#### article -> comments 접근

- Article 모델 클래스에는 Comment에 대한 어떤 정보도 X.

- 역참조 : Article(1) -> Comment(N) 참조

- Django는 역참조의 경우 참조하는 클래스명에 `_set`을 붙인 manager를 생성

- `article = Article.objects.get(pk=1)`

- `article. comment_set.all()`

- manager 이름이 마음에 들지않아 변형시킨다면 변형시킨 뒤 migration 필요

### 실습 : 댓글 생성

```python
# forms.py
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = "__all__"
        exclude = ("article",)
```

```python
# articles/views.py
def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    comment_form = CommentForm()
    context = {
        "article" : article,
        "comment_form" : comment_form,
    }
    return render(request, "articles/article_detail.html", context)
```

- `articles/templates/articles/article_detail.html`

```html
...
<hr>
<h3>댓글</h3>
<form action="#" method="POST">
    {% csrf_token %}
    {{ comment_form.as_p }}
    <input type="submit" value="댓글작성">
</form>
```

### 로직 구현

- `articles/url.py`

```python
path("<int:pk>/comments/", views.comments_create, name="comments_create"),
```

- `articles/views.py`

```python
@require_POST
def comment_create(request, pk):
    article = get_object_or_404(Article, pk=pk)
    form = CommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.article = article
        comment.save()
    return redirect("articles:article_detail", article.pk)
```

- save(commit=False) : 실제 DB에 처리되지 않은 상태의 인스턴스를 반환합니다. 저장 전 로직이 필요한 경우 사용.

- `articles/templates/articles/article_detail.html`

```html
<hr>
<h3>댓글</h3>
<form action="{% url 'articles:comment_create' article.pk' %} method="POST">
    {% csrf_token %}
    {{ comment_form.as_p }}
    <input type="submit" value="댓글작성">
</form>
```

### 실습 : 댓글 읽기

```python
# articles/views.py
def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    comment_form = CommentForm()
    context = {
        'article': article,
        'comment_form': comment_form,
        'comments': comments,
    }
    return render(request, 'articles/article_detail.html', context)
```

- `articles/templates/articles/article_detail.html`

```html
...
<ul>
    {% for comment in comments %}
        <li>
            <p>{{ comment.content }}</p>
        </li>
    {% endfor %}
</ul>
```

- 아래 방법으로 html 작성 시 view 수정하지 않아도 됨

```html
<ul>
    {% for comment in articles.comments.all %}
        <li>
            <p>{{ comment.content }}</p>
        </li>
    {% endfor %}
</ul>
```
