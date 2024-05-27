from django.contrib import admin
# from django.urls import path

# Django의 내장함수를 import
from django.urls import re_path

# 각 url에 매핑시킬 뷰들을 bookmark의 views.py에서 가져와 import
from testapp.views import BookmarkListView, BookmarkDetailView, TestView, TestView2, login


"""
re_path(regex, view, name): re_path()는 주로 세 개의 인자를 사용합니다.
                            regex는 정규식, view는 해당 url 패턴에 매핑시킬 뷰,
                            name은 해당 url 패턴에 붙일 이름을 의미합니다.
"""
urlpatterns = [
    # path('admin/', admin.site.urls),
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^bookmark/$', BookmarkListView, name='list'),
    re_path(r'^bookmark/(?P<id>\d+)/$', BookmarkDetailView, name='detail'),
    re_path(r'^createform/$', TestView, name='createform'),
    re_path(r'^signup/$', TestView2, name='signup'),
    re_path(r'^index/$', login, name='login'),
]