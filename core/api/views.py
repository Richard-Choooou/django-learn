from django.contrib.auth.models import User
from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response

from core.api.serializers import UserSerializer, UserRegisterSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    @action(detail=False, methods=['post'], serializer_class=UserRegisterSerializer, permission_classes=[permissions.AllowAny])
    def register(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            print(serializer.validated_data)
            username = serializer.validated_data.get('username')
            password = serializer.validated_data.get('password')
            confirm_password = serializer.validated_data.get('confirm_password')
            if password != confirm_password:
                return Response(status=status.HTTP_400_BAD_REQUEST, data=dict(error='Passwords do not match'))
            is_has_same_username = User.objects.filter(username=username).exists()
            if is_has_same_username:
                return Response(status=status.HTTP_400_BAD_REQUEST, data=dict(error='用户名重复'))
            User.objects.create_user(username=username, password=password)
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
