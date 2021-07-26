from django.db import models
from django.urls import reverse
from auth_app.models import User


class Application(models.Model):

    class AppStatus(models.TextChoices):
        OPEN = 'OP', 'Открыта'
        IN_WORK = 'IN', 'В работе'
        CLOSED = 'CL', 'Закрыта'

    class AppType(models.TextChoices):
        ADVICE = 'AD', 'Консультация'
        REPAIR = 'RE', 'Ремонт'
        SERVICE = 'SE', 'Обслуживание'

    title = models.CharField(
        max_length=50,
        verbose_name='Название',
    )
    text = models.TextField(
        max_length=500,
        verbose_name='Текст',
    )

    status = models.CharField(
        max_length=2,
        choices=AppStatus.choices,
        default=AppStatus.OPEN,
        verbose_name='Статус',
    )
    type_app = models.CharField(
        max_length=2,
        choices=AppType.choices,
        default=AppType.ADVICE,
        verbose_name='Тип',
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    client = models.ForeignKey(User, on_delete=models.PROTECT)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('application-detail', args=[str(self.id)])





