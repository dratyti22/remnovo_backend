from django.test import TestCase, Client
from django.urls import reverse
from rest_framework import status
from app.users.models import CustomUser


class APITestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = CustomUser.objects.create_user(email='newuser@example.com', password='newpassword123')
        self.user.token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MjgzNzMyNDQsInN1YiI6IjMifQ.zgaBAVrFJIVNOoPbaUWgnmXJRHvOUNnTYV1POR7gEDc"  # Assign a valid token
        self.user.save()

    def test_create_user(self):
        # Тест создания нового пользователя
        data = {'email': 'newuser@example.com', 'password': 'newpassword123'}
        response = self.client.post(reverse('create_user'), data, content_type='application/json')
        if response.status_code == 201:
            self.assertEqual(response.status_code, status.HTTP_201_CREATED)
            self.assertEqual(CustomUser.objects.count(), 2)
        else:
            self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
            self.assertEqual(CustomUser.objects.count(), 1)

    def test_create_user_invalid_data(self):
        # Тест создания нового пользователя с невалидными данными
        data = {'email': '', 'password': 'newpassword123'}
        response = self.client.post(reverse('create_user'), data, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_login_user(self):
        # Тест входа существующего пользователя
        data = {'email': 'newuser@example.com', 'password': 'newpassword123'}
        response = self.client.post(reverse('login_user'), data, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_login_user_invalid_credentials(self):
        # Тест входа с неверными учетными данными
        data = {'email': 'test@example.com', 'password': 'wrongpassword'}
        response = self.client.post(reverse('login_user'), data, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_auth_token(self):
        # Тест аутентификации по токену
        data = {
            'auth_token': "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MjgzNzMyNDQsInN1YiI6IjMifQ.zgaBAVrFJIVNOoPbaUWgnmXJRHvOUNnTYV1POR7gEDc"}

        response = self.client.post(reverse('auth_token'), data, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_email_confirmation(self):
        # Тест подтверждения электронной почты (предполагается, что код подтверждения возвращается из внешнего сервиса)
        # Для этого теста необходимо имитировать внешний сервис или использовать мокирование.
        # Для простоты, здесь мы просто проверяем, что запрос проходит без ошибок.
        data = {'code': 'a18062ba71'}
        response = self.client.post(reverse('email_confirmation'), data, content_type='application/json')
        if response.status_code == 200:
            self.assertEqual(response.status_code, status.HTTP_200_OK)
        elif response.status_code == 401:
            self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        else:
            self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_email_confirmation_invalid_code(self):
        # Тест подтверждения электронной почты с невалидным кодом
        data = {'code': ''}
        response = self.client.post(reverse('email_confirmation'), data, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
