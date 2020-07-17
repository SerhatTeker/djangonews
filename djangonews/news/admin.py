from django.contrib import admin

from .models import Comment, Story

admin.site.register(Story)
admin.site.register(Comment)
