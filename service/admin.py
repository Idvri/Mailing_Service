from django.contrib import admin

from service.models import Client, Mailing


# Register your models here.
@admin.register(Client)
class Client(admin.ModelAdmin):
    list_display = ('email', 'surname', 'name', 'middle_name')


@admin.register(Mailing)
class Mailing(admin.ModelAdmin):
    list_display = ('mailing_time', 'regularity', 'status', 'mail_theme', 'mail_text')
