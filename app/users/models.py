from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


# class CustomUserManager(models.Manager):
#     def create_user(self, email, password, **extra_fields):
#         """
#         Create and save a user with the given email and password.
#         """
#         if not email:
#             raise ValueError(("The Email must be set"))
#         email = self.normalize_email(email)
#         user = self.model(email=email, **extra_fields)
#         user.set_password(password)
#         user.save()
#         return user
#
#     def create_superuser(self, email, password, **extra_fields):
#         """
#         Create and save a SuperUser with the given email and password.
#         """
#         extra_fields.setdefault("is_staff", False)
#         extra_fields.setdefault("is_superuser", False)
#         extra_fields.setdefault("is_active", False)
#
#         if extra_fields.get("is_staff") is not True:
#             raise ValueError(("Superuser must have is_staff=True."))
#         if extra_fields.get("is_superuser") is not True:
#             raise ValueError(("Superuser must have is_superuser=True."))
#         return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractUser):
    id = models.AutoField(primary_key=True)
    users_status = models.IntegerField(default=0)
    token = models.CharField(max_length=255, blank=True, null=True)
    roles_id = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(10)], null=True)

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_set',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        verbose_name='groups'
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_set',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions'
    )
    # objects = CustomUserManager()

    class Meta:
        db_table = "user"
        verbose_name = "Пользователя"
        verbose_name_plural = "Пользователи"

    def __str__(self) -> str:
        if self.username:
            return self.username
        else:
            return str(self.roles_id)
