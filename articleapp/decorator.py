from django.http import HttpResponseForbidden

from articleapp.models import Article


def article_ownership_required(func):
    def decorated(request, *args, **kwargs):
        article = Article.objects.get(pk=kwargs['pk']) # 요청을 받으면서 pk를 가진 User
        if not article.writer == request.user: # 게시글의 작성자와 접속중인 유저가 다른 경우
            return HttpResponseForbidden()
        return func(request, *args, **kwargs)
    return decorated