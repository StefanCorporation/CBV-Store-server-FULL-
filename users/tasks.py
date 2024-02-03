import uuid
from django.utils.timezone import now
from datetime import timedelta
from celery import shared_task
from users.models import User, EmailVerification


@shared_task
def send_email_verification(user_id):
    user = User.objects.get(id=user_id)
    #ссылка будет доступна 48ч now это от отправки + сколько доступна будет
    expiration = now() + timedelta(hours=48)
    record = EmailVerification.objects.create(code=uuid.uuid4(), user=user, expiration=expiration)
    record.send_verifivation_email()