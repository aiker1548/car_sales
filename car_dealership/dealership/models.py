from django.db import models
from django.contrib.auth.models import AbstractUser

# Кастомная модель пользователя
class CustomUser(AbstractUser):
    ROLES = (
        ('user', 'Пользователь'),
        ('support', 'Поддержка'),
        ('manager', 'Менеджер'),
        ('admin', 'Администратор'),
    )
    role = models.CharField(max_length=20, choices=ROLES, default='user')

# Модель машин
class Car(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    pic = models.CharField(max_length=255)

    def __str__(self):
        return self.name

# Модель сообщений в "Контакты"
class ContactMessage(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, blank=True)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

# Модель заявок
class Request(models.Model):
    REQUEST_TYPES = (
        ('buy', 'Покупка'),
        ('test_drive', 'Тест-драйв'),
    )
    STATUS_CHOICES = (
        ('pending', 'В ожидании'),
        ('approved', 'Одобрено'),
        ('rejected', 'Отклонено'),
    )
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    request_type = models.CharField(max_length=20, choices=REQUEST_TYPES)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
