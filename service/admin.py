from django.contrib import admin
from service.models import Client, Mailing, MailingLog


# Register your models here.
@admin.register(Client)
class Client(admin.ModelAdmin):
    list_display = ('email', 'surname', 'name', 'middle_name', 'user')


@admin.register(Mailing)
class Mailing(admin.ModelAdmin):
    list_display = ('mailing_time', 'regularity', 'status', 'mail_theme', 'mail_text', 'user')

    def has_change_permission(self, request, obj=None):
        return False


@admin.register(MailingLog)
class MailingLog(admin.ModelAdmin):
    list_display = ('timestamp', 'status', 'server_response', 'get_client_names', 'mailing_list', 'user')

    def get_client_names(self, obj):
        return ", ".join([str(client) for client in obj.client.all()])

    get_client_names.short_description = 'Клиенты'
