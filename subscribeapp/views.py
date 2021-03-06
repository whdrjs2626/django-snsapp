from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import RedirectView, ListView

from articleapp.models import Article
from projectapp.models import Project
from subscribeapp.models import Subscription


@method_decorator(login_required, 'get')
class SubscriptionView(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        return reverse('projectapp:detail', kwargs={'pk': self.request.GET.get('project_pk')})
    def get(self, request, *args, **kwargs):
        project = get_object_or_404(Project, pk=self.request.GET.get('project_pk')) # project_pk를 가진 project를 찾되 없으면 404를 돌려줌 - 없는 프로젝트의 구독에 대한 응답
        user = self.request.user
        subscription = Subscription.objects.filter(user=user, project=project) # 요청에서 받은 user내용과 project내용을 토대로 해당 유저가 해당 프로젝트를 구독했는지에 대한 구독 정보(subscription)을 가져옴

        if subscription.exists():
            subscription.delete() # 구독 중이라면? = 구독이 존재한다면? - 구독 해제
        else:
            Subscription(user=user, project=project).save() # 구독을 안했다면 - 구독

        return super(SubscriptionView, self).get(request, *args, **kwargs)

@method_decorator(login_required, 'get')
class SubscriptionListView(ListView):
    model = Article
    context_object_name = 'article_list'
    template_name = 'subscribeapp/list.html'
    paginate_by = 5

    def get_queryset(self): # 구독정보 조건을 달아줌
       projects = Subscription.objects.filter(user=self.request.user).values_list('project') # subscribe 모델이 가진 속성 중 project로 리스트를 만든다.
       # 즉 요청을 한 user가 구독한 모든 project 정보를 projects로 만듦
       article_list = Article.objects.filter(project__in=projects) # field lookup 기능 WHERE project IN - projects안에 있는 project 각각의 article
       return article_list
