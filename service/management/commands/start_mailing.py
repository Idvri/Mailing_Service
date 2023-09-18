import datetime

from django.core.mail import send_mail
from django.core.management import BaseCommand

from service.models import Mailing, MailingLog


class Command(BaseCommand):
    mailings = Mailing.objects.all()
    logs = MailingLog.objects.all()
    time = datetime.datetime.now()

    def handle(self, *args, **kwargs):

        for mailing in self.mailings:

            if self.get_info_for_mailing_start(mailing, self.logs, self.time):
                related_clients = mailing.clients.all()

                if len(related_clients) == 0:
                    log = MailingLog.objects.create(
                        status='failed',
                        mailing_list=mailing,
                        server_response='Отсутсвуют клиенты для рассылки.',
                    )
                    log.save()
                    break

                for client in related_clients:
                    try:
                        status = send_mail(
                            mailing.mail_theme,
                            mailing.mail_text,
                            None,
                            [client.email],
                            fail_silently=False
                        )
                    except ConnectionRefusedError as error:
                        log = MailingLog.objects.create(
                            status='failed',
                            mailing_list=mailing,
                            server_response=error,
                        )
                        log.client.set([client])
                        log.save()
                    else:

                        if status:
                            log = MailingLog.objects.create(
                                status='success',
                                mailing_list=mailing,
                            )
                            log.client.set([client])
                            log.save()
                        else:
                            log = MailingLog.objects.create(
                                status='failed',
                                mailing_list=mailing,
                            )
                            log.client.set([client])
                            log.save()

            else:
                continue

    @staticmethod
    def get_info_for_mailing_start(mailing, logs, time):
        mailing_latest_log = logs.filter(mailing_list=mailing).all().order_by('-timestamp').first()
        time = time.replace(hour=0, minute=0, second=0, microsecond=0)

        if mailing_latest_log is None:

            if mailing.mailing_time.replace(tzinfo=None).replace(
                    hour=0,
                    minute=0,
                    second=0,
                    microsecond=0,
                    tzinfo=None
            ) <= time:
                return True

        else:

            log_time = mailing_latest_log.timestamp.replace(
                hour=0,
                minute=0,
                second=0,
                microsecond=0,
                tzinfo=None
            )
            time_difference = (time - log_time).days

            if mailing.regularity == 'daily':

                if time_difference == 1:
                    return True

            elif mailing.regularity == 'weekly':

                if time_difference == 7:
                    return True

            else:

                if time_difference == 30:
                    return True