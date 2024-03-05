from django.conf import settings
from django.contrib.auth.views import LoginView as BaseLoginView
from django.contrib.auth.views import LogoutView as BaseLogoutView
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView

from users.forms import UserRegisterForm, UserForm
from users.models import User


class LoginView(BaseLoginView):
    template_name = 'users/login.html'


class LogoutView(BaseLogoutView):
    pass


class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    success_url = reverse_lazy('users:login')
    template_name = 'users/register.html'

    def form_valid(self, form):
        new_user = form.save()
        send_mail(
            subject='Поздравляем с регистрацией',
            message='Вы зарегались на нашей платформе!',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[new_user.email]
            )
        return super().form_valid(form)


class UserUpdateView(UpdateView):
    model = User
    success_url = reverse_lazy('users:profile')
    form_class = UserForm

    """Переопределяем метод и избавляемся от параметра pk"""
    def get_object(self, queryset=None):
        return self.request.user


def generate_new_password(request):
    user = request.user
    new_pass = User.objects.make_random_password()
    user.set_password(new_pass)
    user.save()

    send_mail(
        subject='Поздравляем с изменением пароля',
        message='Ваш новый пароль: {}'.format(new_pass),
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[user.email]
    )

    return redirect(reverse('dogs:index'))

    #new_password = ''.join([random.randint(0, 9) for _ in range (12)])
    #send_mail(
    #    subject='Вы изменили Ваш пароль',
    #    message=f'Теперь Ваш новый пароль: {new_password}',
    #    from_email=settings.EMAIL_HOST_USER,
    #    recipient_list=[request.user.email]
    #)
    #request.user.set_password(new_password)
    #request.user.save()
    #return redirect(reverse('dogs:index'))
