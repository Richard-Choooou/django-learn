from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.contrib.admin import register

from todo_list.models import Todo


# Register your models here.

@register(Todo)
class TodoAdmin(admin.ModelAdmin):
    pass