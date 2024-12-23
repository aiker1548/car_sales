from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Car, ContactMessage, Request
from .forms import ContactMessageForm, RequestForm
from django.contrib.auth import logout
from django.views import View
from .forms import CustomUserCreationForm
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages

def update_request_status(request, pk):
    if request.method == 'POST':
        user_request = get_object_or_404(Request, pk=pk)
        new_status = request.POST.get('status')
        if new_status in ['new', 'approved', 'rejected']:  # Проверка допустимых значений
            user_request.status = new_status
            user_request.save()
            messages.success(request, 'Статус заявки успешно обновлен.')
        else:
            messages.error(request, 'Недопустимое значение статуса.')
    return redirect('manage_requests')  # Вернуться на список заявок


class RegisterView(View):
    def get(self, request):
        form = CustomUserCreationForm()
        return render(request, 'register.html', {'form': form})

    def post(self, request):
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Перенаправление на страницу входа
        return render(request, 'register.html', {'form': form})

# Проверка роли пользователя
def is_support(user):
    return user.role == 'support'

def is_manager(user):
    return user.role == 'manager'

def custom_logout_view(request):
    logout(request)
    return redirect('/')

# Главная страница
def home(request):
    if not request.user.is_authenticated:
        return redirect('login')
    cars = Car.objects.all()
    return render(request, 'home.html', {'cars': cars})

# Контакты
def contact(request):
    if request.method == 'POST':
        form = ContactMessageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ContactMessageForm()
    return render(request, 'contact.html', {'form': form})

# Оставить заявку (авторизованные пользователи)
@login_required
def create_request(request):
    if request.method == 'POST':
        form = RequestForm(request.POST)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            return redirect('home')
    else:
        form = RequestForm()
    return render(request, 'create_request.html', {'form': form})

# Заявки для менеджеров
@login_required
@user_passes_test(is_manager)
def manage_requests(request):
    requests = Request.objects.all()
    return render(request, 'manage_requests.html', {'requests': requests})

# Сообщения для поддержки
@login_required
@user_passes_test(is_support)
def support_messages(request):
    messages = ContactMessage.objects.all()
    return render(request, 'support_messages.html', {'messages': messages})
