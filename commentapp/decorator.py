from django.http import HttpResponseForbidden

from commentapp.models import Comment


def comment_ownership_required(func):
    def decorated(request, *args, **kwargs):
        comment = Comment.objects.get(pk=kwargs['pk']) # 요청을 받으면서 pk를 가진 User
        if not comment.writer == request.user: # 댓글 작성자가 요청한 유저인지 확인
            return HttpResponseForbidden()
        return func(request, *args, **kwargs)
    return decorated