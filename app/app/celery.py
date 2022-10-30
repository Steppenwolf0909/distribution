import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'app.settings')
from celery import Celery
from celery.schedules import crontab


app = Celery('celery')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()


@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(10.0, log.s(), name=f'loging')

@app.task
def log():
    from service import models

    logs = models.RequestCount.objects.all()
    f = open('./logs/app_log.txt', 'w')
    for log in logs:
        f.write(f'\n Server {log.server_port} made {log.count} requests - {log.updated}')
    f.close()

