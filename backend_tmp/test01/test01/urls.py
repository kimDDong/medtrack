from django.contrib import admin
# from django.urls import path

# Django의 내장함수를 import
from django.urls import re_path

# 각 url에 매핑시킬 뷰들을 bookmark의 views.py에서 가져와 import
from testapp.views import *
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

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
    #여기부터 우리거
    re_path(r'^signup/$', TestView2, name='signup'),
    re_path(r'^index/$', login, name='login'),
    re_path(r'^add-medication/$', add_medication, name='add_medication'),
    re_path(r'^settings/$', change_settings, name='change_settings'),
    re_path(r'^add-daily/$', add_daily, name='add_daily'),
    re_path(r'^main/$', after_add_daily, name='after_add_daily'),
    re_path(r'^change-notification-sound/$', change_notification_sound, name='change_sound'),
    re_path(r'^medication-info/$', medication_info, name='medication_info'),
    re_path(r'^patient-info/$', patient_info, name='patient_info'),
    re_path(r'^scan-qr/$', scan_qr, name='scan_qr'),
    re_path(r'^scan-qr-patient/$', scan_qr_patient, name='scan_qr_patient'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)