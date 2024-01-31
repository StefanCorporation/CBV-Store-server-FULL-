from django.contrib.auth.models import AbstractUser
from django.core.mail import send_mail
from django.db import models
from django.urls import reverse
from django.utils.timezone import now

from store import settings


class User(AbstractUser):
    image = models.ImageField(upload_to='users_images', null=True, blank=True)
    is_verified_email = models.BooleanField(default=False)


class EmailVerification(models.Model):
    code = models.UUIDField(unique=True)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    expiration = models.DateTimeField()

    def __str__(self):
        return f'EmailVerificationObject for {self.user.email}'
    
    #в этой модели у нас логика отправки эл почты
    def send_verifivation_email(self):
        link = reverse('users:email_verification', kwargs={
            'email': self.user.email,
            'code': self.code            
            })
        
        verification_link = f'{settings.DOMAIN_NAME}{link}'
        subject = f'Подтверждение учетной записи для {self.user.username}'
        message = (f'Для подтверждения учетной записи {self.user.username} '
                   f'Перейдите по ссылке: {self.user.email, verification_link}')

        send_mail(
            subject=subject,
            message=message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[self.user.email],
            fail_silently=False
        )

    
    #если срок ссылки истек
    def is_expired(self):
        return True if now() >= self.expiration else False