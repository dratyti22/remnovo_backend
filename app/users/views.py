from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

import secrets
import requests

from django.contrib.auth import authenticate, login

from app.users.models import CustomUser


class CreateUserView(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        if not email or not password:
            return Response({'error': 'Email and password are required'}, status=status.HTTP_400_BAD_REQUEST)

        url = "http://80.87.104.189:9991/user/create"
        params = {'email': email, 'password': password}
        response = requests.post(url, params=params)

        if response.status_code == 201:
            # Если запрос успешен, создаем пользователя
            user = CustomUser.objects.create_user(email=email, password=password)
            return Response({'message': 'User created successfully'}, status=status.HTTP_201_CREATED)
        else:
            # Для других статусов можно обработать ошибку по-разному
            return Response({'error': 'Failed to create user'}, status=status.HTTP_200_OK)


class LoginUserView(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        if not email or not password:
            return Response({'error': 'Email and password are required'}, status=status.HTTP_400_BAD_REQUEST)
        url = "http://80.87.104.189:9991/user/login"
        params = {'email': email, 'password': password}
        response = requests.post(url, params=params)

        if response.status_code == 200:
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                return Response({'message': 'User logged in successfully'}, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response({'error': 'Failed to login user'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class AuthTokenView(APIView):
    def post(self, request):
        auth_token = request.data.get("auth_token")
        if not auth_token:
            return Response({'error': 'Auth token is required'}, status=status.HTTP_400_BAD_REQUEST)

        user = CustomUser.objects.filter(token=auth_token).first()
        if not user:
            return Response({'error': 'Invalid auth token'}, status=status.HTTP_401_UNAUTHORIZED)
        login(request, user)
        return Response({'message': 'Auth token verified successfully'}, status=status.HTTP_200_OK)


class EmailConfirmationView(APIView):
    ...
