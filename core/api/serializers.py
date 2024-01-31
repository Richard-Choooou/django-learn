from django.contrib.auth.models import Group, User
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class UserRegisterSerializer(serializers.Serializer):
    username = serializers.CharField(label="账户", max_length=24, required=True, help_text="用户名")
    password = serializers.CharField(label="密码", max_length=24, required=True, help_text="密码")
    confirm_password = serializers.CharField(label="确认密码", max_length=24, required=True)

    class Meta:
        fields = ('username', 'password', 'confirm_password')