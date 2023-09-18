from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
from django.core.management import call_command


def mailing_scheduler():
    call_command('start_mailing')


def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(
        func=mailing_scheduler,
        trigger=CronTrigger(second="*/5"),
        id="mailing_scheduler",
        max_instances=1,
    )
    scheduler.start()
