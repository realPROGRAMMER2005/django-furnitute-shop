from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib import auth
from django.urls import reverse
from users.forms import UserLoginForm, UserReigstrationForm, ProfileForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages


# Create your views here.


def registration(request):
      if request.method == 'POST':
            form = UserReigstrationForm(data=request.POST)
            if form.is_valid():
                  form.save()
                  user = form.instance
                  auth.login(request, user)
                  messages.success(request, f'Вы успешно зарегистрировались, {user.username}!')
                  return HttpResponseRedirect(reverse('main:index'))
      else:
            form = UserReigstrationForm() 
      context = {
            'title': 'Home - Регистрация',
            'form': form
      }
      return render(request, 'users/registration.html', context=context)


@login_required
def profile(request):
      if request.method == 'POST':
            form = ProfileForm(data=request.POST, instance=request.user, files=request.FILES)
            if form.is_valid():
                  form.save()
                  messages.success(request, 'Ваш профиль успешно обновлен!')
                  return HttpResponseRedirect(reverse('users:profile'))
      else:
            form = ProfileForm(instance=request.user) 
      context = {
            'title': 'Home - Личный кабинет',
            'form': form
      }
      return render(request, 'users/profile.html', context=context)


def login(request):
      if request.method == 'POST':
            
            form = UserLoginForm(data=request.POST)
            if form.is_valid():
                  username = request.POST['username']
                  password = request.POST['password']
                  user = auth.authenticate(username=username, password=password)
                  if user:
                        auth.login(request, user)
                        messages.success(request, f'Добро пожаловать, {username}!')
                        
                  
                        if request.POST.get('next', None):
                              return HttpResponseRedirect(request.POST.get('next'))
                        
                        return HttpResponseRedirect(reverse('main:index'))
      else:
            form = UserLoginForm()
      
      
      context = {
            'title': 'Home - Авторизация',
            'form': form,
      
                 }
      
      return render(request, 'users/login.html', context=context)

@login_required
def logout(request):
      messages.success(request, 'Вы вышли из аккаунта!')
      auth.logout(request) 
      return redirect(reverse('main:index'))


