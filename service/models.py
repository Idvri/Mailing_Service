from django.db import models
from django.utils import timezone

NULLABLE = {'null': True, 'blank': True}


# Create your models here.
class Client(models.Model):
    email = models.EmailField(unique=True, verbose_name='электронная почта')
    surname = models.CharField(max_length=20, verbose_name='фамилия')
    name = models.CharField(max_length=20, verbose_name='имя')
    middle_name = models.CharField(max_length=20, verbose_name='отчество', **NULLABLE)

    def __str__(self):
        return f'Клиент: {self.email}.'


class Mailing(models.Model):
    REGULARITY_CHOICES = (
        ('daily', 'Раз в день'),
        ('weekly', 'Раз в неделю'),
        ('monthly', 'Раз в месяц'),
    )

    STATUS_CHOICES = (
        ('created', 'Создана'),
        ('started', 'Запущена'),
        ('completed', 'Завершена'),
    )

    mailing_time = models.DateTimeField(verbose_name='время рассылки')
    regularity = models.CharField(max_length=10, choices=REGULARITY_CHOICES, verbose_name='периодичность')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='created', verbose_name='статус рассылки')
    clients = models.ManyToManyField(Client, related_name='mailings', verbose_name='клиенты')
    mail_theme = models.TextField(max_length=100, verbose_name='тема письма')
    mail_text = models.TextField(max_length=350, verbose_name='тело письма')

    def __str__(self):
        return f'Рассылка {self.mail_theme}.'


class MailingLog(models.Model):
    STATUS_CHOICES = (
        ('success', 'Успешно'),
        ('failed', 'Не удалось'),
    )

    timestamp = models.DateTimeField(default=timezone.now, verbose_name='дата и время попытки')
    status = models.CharField(choices=STATUS_CHOICES, verbose_name='статус попытки')
    server_response = models.TextField(verbose_name='ответ почтового сервера', **NULLABLE)
    client = models.ManyToManyField(Client, related_name='logs', verbose_name='клиент')
    mailing_list = models.ForeignKey(Mailing, on_delete=models.CASCADE, related_name='logs',
                                     verbose_name='рассылка')

    def __str__(self):
        return f'Лог рассылки для "{self.mailing_list}". Статус: "{self.status}".'
