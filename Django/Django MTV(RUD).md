# Django MTV(RUD)

- redirect : 지정한 URL로 되돌리는 것

## PRG 패턴

- Post -> Redirect -> Get

- POST 요청을 서버에서 처리하고 서버에서는 다른 주소로 Redirect하도록 응답하고 브라우저는 GET 방식으로 서버를 호출하여 사용자의 요청이 반영된 것을 보여줌.

- PRG 패턴을 사용해 반복적인 POST 호출을 막을 수 있고 사용자 입장에서도 처리가 끝나고 처음 단계로 돌아간다는 느낌을 받게 됨.

```python
# 삭제 view
def delete(request, pk):
  article = Article.objects.get(pk=pk)
  if request.method == "POST":
      article.delete()
      return redirect("articles")
  return redirect("article_detail", article.pk)
```

```python
# 수정 view
def edit(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        "article": article,
    }
    return render(request, "edit.html", context)
```
