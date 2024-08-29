# User

информация о пользователе


user имеет поля в бд:

    password
    last_login
    is_superuser
    username
    first_name
    last_name
    email
    is_staff
    is_active
    data_joined
    id
    users_status
    token
    roles_id
    points
    succesful_orders
    total_orders_placed



### Create User
нужно:
    
    email
    password

api:
    
    /user/create?email=...&password=...

Если регистрация(но не входит в аккаунт) прошла успешно возвращается:
```Python
{'message': 'User created successfully'}, HTTP_201_CREATED
```
иначе:
```Python
{'error': 'Failed to create user'}, HTTP_400_BAD_REQUEST
```



### Login User
нужно:
    
    email
    password

api:
    
    /user/login?email=...&password=...

Если прошло успешно, пользователя авторезировается и возвращается:
```Python
{'message': 'User logged in successfully'}, HTTP_200_OK
```
если нет то:
```Python
{'error': 'Failed to login user'}, HTTP_500_INTERNAL_SERVER_ERROR
```

### Auth Token
нужно 
    
    auth_token

api:
    
    /user/auth?auth_token=...

Если прошло успешно, пользователя авторезировается и возвращается:
```Python
{"message": "Login successfully"}, HTTP_200_OK
```
если нет то:
```Python
{'error': 'Auth token verified successfully'}, HTTP_401_UNAUTHORIZED
```


### Email Login User
нужно 
    
    code

api:
    
    /user/email-confirmation?code=...

Если прошло успешно, пользователя авторезировается,
is_active меняется на true и возвращается:
```Python
{'message': 'Email confirmed successfully'}, HTTP_200_OK
```
если нет то:
```Python
{'error': 'Failed to confirm email'}, HTTP_400_BAD_REQUEST
```
