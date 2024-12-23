from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('create-request/', views.create_request, name='create_request'),
    path('manage-requests/', views.manage_requests, name='manage_requests'),
    path('support-messages/', views.support_messages, name='support_messages'),
    path('logout/', views.custom_logout_view, name='logout'),
    path('login/', auth_views.LoginView.as_view(template_name='custom_login.html'), name='login'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('requests/<int:pk>/update-status/', views.update_request_status, name='update_request_status'),

]