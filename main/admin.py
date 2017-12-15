from django.contrib import admin
from .models import AuthorInfo,BookInfo
# Register your models here.

admin.site.register(AuthorInfo)
admin.site.register(BookInfo)