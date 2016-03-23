"""ask URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
admin.autodiscover()
from qa import views

urlpatterns = [
    url(r'^$', views.questions_all, name='questions_all'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/$', views.test, name='test'),
    url(r'^signup/$', views.test, name='test'),
    url(r'^question/(?P<question_id>\d+)/$', views.question_details, name='question_details'),
    url(r'^ask/$', views.question_add, name='question_add'),
#    url(r'^answer'), views.answer
    url(r'^popular/$', views.popular_questions, name='popular_questions'),
    url(r'^new/$', views.test, name='test'),

]
