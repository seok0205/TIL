# Django Form

- 유저가 입력하는 데이터는 반드시 유효성 검사가 필요함
- 일부 반복되는 작업과 코드를 줄일 수 있는 django form 제공
- 직접 구현한 Form + View 로직이 필요하다면 사용 안해도 무방

## Django Form Class

1. Form 선언 : app에 `forms.py` 생성

    ```python
    from django import forms


    class ArticleForm(forms.Form):
        title = forms.CharField(max_length=10)
        content = forms.CharField()
    ```

2. Form 적용하기 : 새 글 작성(new.html)에 적용 `{{ form.as_p }}`

    - `as_p` : `<p>`로 감싸져 렌더링
    - `as_div` : `<div>`로 감싸져 렌더링

3. view.py 수정

    ```python
    from.forms import ArticleForm
    ...
    def new(request):
        form = ArticleForm()
        context = {
            "form": form,
        }
        return render(request, "new.html", context)
    ...
    ```

### Form Widget

- 웹 페이지에서 Form Input 요소가 어떻게 렌더링 되어서 보여질지 정의
- Form Fields에 할당해서 사용
- `<input type="text">`에서 썼던 것
- 파라미터에 `widget=forms.Textarea` 형식으로 정의

```python
from django import forms

class ArticleForm(forms.Form):
    title = forms.CharField(max_length=10)
    content = forms.CharField(widget=forms.Textarea)
```

- choice field 적용

```python
from django import forms

class ArticleForm(forms.Form):
    # 앞은 데이터베이스에 저장될 값, 뒤는 사용자에게 보여질 값
    GENRE_CHOICES = [
        ("technology", "Technology"),
        ("life", "Life"),
        ("hobby", "Hobby"),
    ]

    title = forms.CharField(max_length=10)
    content = forms.CharField(widget=forms.Textarea)
    genre = forms.ChoiceField(choices=GENRE_CHOICES)
```

## Django Model Form

- 알아서 Model을 참조해 Form을 만들어주는 Class.
- ModelForm이 사용할 데이터를 Meta 클래스에 명시
- fields 항목에 form으로 만들고 싶은 항목들을 지정 가능

```python
from django import forms

from articles.models import Article


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = "__all__"
        # exclude = ["title"]
```

### Model Form이 제공하는 편의성

- 기본적 유효성 검사등을 처리

```python
...
def create(request):
  form = ArticleForm(request.POST) # form에 request.POST에 있는 데이터 채워
  if form.is_valid(): # form 형식에 맞으면
      article = form.save() # 저장하고 해당 객체 반환 
      return redirect("article_detail", article.id)
  return redirect("new")
...
```

- 아래와 같은 new()함수가 존재할 때, create()와 상당히 흡사함. GET으로 들어오면 비어있는 Form을 보여주고, POST로 들어오면 데이터를 채워서 보내는 것으로 새로운 article을 생성하면 됨.

```python
def new(request):
    form = ArticleForm()
    context = {
        "form": form,
    }
    return render(request, "new.html", context)
```

- new()라는 구조가 필요없는 상태로 만들 수 있으므로, view의 new()함수와 url path를 지움. new.html을 create.html로 변환, new로 표현되어 있던 html의 url들도 모두 create로 변환.

```html
{% extends "base.html" %}

{% block content %}
<h1>New Article</h1>

<form action="{% url 'create' %}" method="POST">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">저장</button>
</form>
{% endblock content %}
```

- new()를 삭제하고 create()로만 기능을 구현했을 때

```python
def create(request):
  if request.method == "POST":
      form = ArticleForm(request.POST)
      if form.is_valid():
          article = form.save()
          return redirect("article_detail", article.id)
  else:
      form = ArticleForm()

  context = {"form": form}
  return render(request, "create.html", context)
```

- edit, update 같은 관계도 update() 하나로 병합 가능. Model Form은 instance라는 속성에 값이 있으면 해당 instance를 수정하고 값이 없으면 새로 생성하는 로직을 수행.

```python
def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == "POST":
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            article = form.save()
            return redirect("article_detail", article.pk)
    else:
        form = ArticleForm(instance=article)
    context = {
        "form": form,
        "article": article,
    }
    return render(request, "update.html", context)
```

- 위의 new, create 관계처럼 edit과 관련된 view 함수, url path를 모두 지우고 edit.html을 update.html로 변경 및 url이 edit인 부분을 모두 update로 변환.

```html
{% extends "base.html" %}

{% block content %}
<h1>Update Article</h1>

<form action="{% url 'update' article.pk %}" method="POST">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">수정</button>
</form>

<a href="{% url 'article_detail' article.pk %}">이전으로</a>
{% endblock content %}
```
