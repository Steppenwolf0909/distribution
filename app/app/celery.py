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
    sender.add_periodic_task(10.0, log.s(), name=f'loging for node1')

@app.task
def log():
    from service.views import counter
    import datetime
    from service import models
    
    logs = models.RequestCounter.objects.all()
    f = open('../logs/app_log.txt', 'w')
    for log in logs:
        f.write(f'\n Server {log.count} made {log.count} requests - {log.datetime}')
    f.close()
