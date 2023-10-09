# Generated by Django 4.2.5 on 2023-09-20 20:07

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, verbose_name='электронная почта')),
                ('surname', models.CharField(max_length=20, verbose_name='фамилия')),
                ('name', models.CharField(max_length=20, verbose_name='имя')),
                ('middle_name', models.CharField(blank=True, max_length=20, null=True, verbose_name='отчество')),
            ],
            options={
                'verbose_name': 'Клиент',
                'verbose_name_plural': 'Клиенты',
            },
        ),
        migrations.CreateModel(
            name='Mailing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mailing_time', models.DateTimeField(verbose_name='время рассылки')),
                ('regularity', models.CharField(choices=[('daily', 'Раз в день'), ('weekly', 'Раз в неделю'), ('monthly', 'Раз в месяц')], max_length=10, verbose_name='периодичность')),
                ('status', models.CharField(choices=[('created', 'Создана'), ('started', 'Запущена'), ('completed', 'Завершена')], default='created', max_length=10, verbose_name='статус рассылки')),
                ('mail_theme', models.TextField(max_length=100, verbose_name='тема письма')),
                ('mail_text', models.TextField(max_length=350, verbose_name='тело письма')),
                ('is_active', models.BooleanField(default=True, verbose_name='признак активности')),
            ],
            options={
                'verbose_name': 'Рассылка',
                'verbose_name_plural': 'Рассылки',
            },
        ),
        migrations.CreateModel(
            name='MailingLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now, verbose_name='дата и время попытки')),
                ('status', models.CharField(choices=[('success', 'Успешно'), ('failed', 'Не удалось')], max_length=10, verbose_name='статус попытки')),
                ('server_response', models.TextField(blank=True, null=True, verbose_name='ответ почтового сервера')),
                ('client', models.ManyToManyField(related_name='logs', to='service.client', verbose_name='клиент')),
                ('mailing_list', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='logs', to='service.mailing', verbose_name='рассылка')),
            ],
            options={
                'verbose_name': 'Лог рассылки',
                'verbose_name_plural': 'Логи рассылок',
            },
        ),
    ]
