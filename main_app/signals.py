from main_app.models import Application
from django.dispatch import receiver
from django.db.models.signals import post_save, post_init
from auth_app.models import User
import requests


@receiver(post_init, sender=Application)
def migrate_notify_init(instance, **kwargs):
    instance.old_status = instance.status


@receiver(post_save, sender=Application)
def migrate_notify_post(instance, created, **kwargs):
    if created or instance.old_status != instance.status:
        telegram_id = User.objects.filter(username=instance.client)[0].telegram_id
        if telegram_id:
            bot_token = bot_token
            url = f'https://api.telegram.org/bot{bot_token}/sendmessage'
            params = {
                'chat_id': telegram_id,
                'text': f'У вашей заявки \'{instance}\' статус \'{instance.get_status_display()}\''
            }
            requests.get(url, params)
