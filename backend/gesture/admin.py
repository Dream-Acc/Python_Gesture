from django.contrib import admin
from .models import UserInfo, Word, Translate
# Register your models here.
admin.site.register(UserInfo)
admin.site.register(Word)
admin.site.register(Translate)
admin.site.site_header = '手语翻译平台后台管理系统'
admin.site.index_title = '首页'