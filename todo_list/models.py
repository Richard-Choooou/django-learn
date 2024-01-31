from django.contrib.auth.models import User
from django.db import models

from core.models import BaseModel


# Create your models here.

class Todo(BaseModel):
    title = models.CharField(verbose_name='标题', max_length=24)
    content = models.TextField(verbose_name='内容')
    done = models.BooleanField(verbose_name='完成', default=False)
    user = models.ForeignKey(User, verbose_name='所属用户', on_delete=models.CASCADE)

    class Meta:
        verbose_name = '待办项'
        verbose_name_plural = '待办列表'
