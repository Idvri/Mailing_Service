# Generated by Django 4.2.5 on 2023-09-19 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0007_alter_client_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='электронная почта'),
        ),
    ]