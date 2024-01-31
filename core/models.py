from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class BaseModel(models.Model):
    class Meta:
        abstract = True

    object = models.Manager()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, verbose_name='创建人', on_delete=models.DO_NOTHING, related_name='created_by', editable=False)
    updated_by = models.ForeignKey(User, verbose_name='修改人', on_delete=models.DO_NOTHING, related_name='updated_by', editable=False)