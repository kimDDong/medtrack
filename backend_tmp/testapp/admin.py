from django.contrib import admin
from testapp.models import Bookmark


class BookmarkAdmin(admin.ModelAdmin):
    list_display = ('name', 'url') # admin 사이트에 출력할 칼럼들

admin.site.register(Bookmark, BookmarkAdmin)