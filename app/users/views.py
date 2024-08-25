from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from app.users.models import CustomUser


class CreateUserView(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        if not email or not password:
            return Response({'error': 'Email and password are required'}, status=status.HTTP_400_BAD_REQUEST)

        CustomUser.objects.create_user(email=email, password=password)
        return Response({'message': 'User created successfully'}, status=status.HTTP_201_CREATED)


class LoginUserView(APIView):
    ...


class AuthTokenView(APIView):
    ...


class EmailConfirmationView(APIView):
    ...
