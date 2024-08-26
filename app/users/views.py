from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

import secrets

from django.contrib.auth import authenticate, login

from app.users.models import CustomUser


class CreateUserView(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        if not email or not password:
            return Response({'error': 'Email and password are required'}, status=status.HTTP_400_BAD_REQUEST)

        user = CustomUser.objects.create_user(email=email, password=password)
        user.token = secrets.token_urlsafe(150)
        user.save()
        return Response({'message': 'User created successfully'}, status=status.HTTP_201_CREATED)


class LoginUserView(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        if not email or not password:
            return Response({'error': 'Email and password are required'}, status=status.HTTP_400_BAD_REQUEST)
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return Response({'message': 'User logged in successfully'}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)


class AuthTokenView(APIView):
    ...


class EmailConfirmationView(APIView):
    ...
