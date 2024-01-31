from django.contrib.auth.views import LoginView
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView

from common.views import TitleMixin
from users.forms import UserLoginForm, UserProfileForm, UserRegistrationForm
from users.models import EmailVerification, User


class UserLoginView(TitleMixin, LoginView):
    template_name = 'users/login.html'
    form_class = UserLoginForm
    title = 'Establishment-Store User Authorization'
  

class UserRegistrationView(TitleMixin, SuccessMessageMixin, CreateView):
    #по факту просто переопределям нужные атрибуты класса и там под капотом работает
    #почти такой же функционал как и в функциях-контроллерах
    model = User
    #работа с формрй идет под капотом просто передаем имя модели а вызыов под капотами
    form_class = UserRegistrationForm
    template_name = 'users/registration.html'
    success_url = reverse_lazy('users:login')
    success_message = 'Поздравляем! Вы успешно зарегестрировались!'
    title = 'Establishment-Store User Registration'


class UserProfileView(TitleMixin, SuccessMessageMixin, UpdateView):
    model = User
    form_class = UserProfileForm
    template_name = 'users/profile.html'
    success_message = 'Профиль успешно обновлен!'
    title = 'Establishment-Store User Profile'

    #при обновлении данных пользователя редирект на ту же страницу
    def get_success_url(self):
        return reverse_lazy('users:profile', args=(self.object.id,))



class EmmailVerificationView(TitleMixin, TemplateView):
    title = 'Email verification'
    template_name = 'users/email_verification.html'

    def get(self, request, *args, **kwargs):
        code = kwargs['code']
        user = User.objects.get(email=kwargs['email'])
        email_verifications = EmailVerification.objects.filter(user=user, code=code)

        #если кверисет не пустой и срок ссылки не истек
        if email_verifications.exists() and not email_verifications.first().is_expired():
            user.is_verified_email = True
            user.save()
            return super(EmmailVerificationView, self).get(request, *args, **kwargs)
        else:
            HttpResponseRedirect(reverse('products:index'))

