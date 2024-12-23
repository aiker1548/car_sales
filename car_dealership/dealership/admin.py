from django.contrib import admin
from .models import CustomUser, Car, ContactMessage, Request

# Настройка отображения кастомной модели пользователя
@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'role', 'is_staff', 'is_active')
    search_fields = ('username', 'email')
    list_filter = ('role', 'is_staff', 'is_active')
    ordering = ('username',)

# Настройка отображения модели машин
@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'description')
    search_fields = ('name', 'description')
    ordering = ('name',)

# Настройка отображения сообщений из "Контакты"
@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('user', 'email', 'message', 'created_at')
    search_fields = ('user__username', 'email', 'message')
    ordering = ('-created_at',)

# Настройка отображения заявок
@admin.register(Request)
class RequestAdmin(admin.ModelAdmin):
    list_display = ('user', 'car', 'request_type', 'status', 'created_at')
    list_filter = ('request_type', 'status', 'created_at')
    search_fields = ('user__username', 'car__name', 'request_type')
    ordering = ('-created_at',)
