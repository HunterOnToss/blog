from __future__ import absolute_import
from celery import Celery

app = Celery("proj",
             broker="redis://localhost",
             backend="redis://localhost",
             include=["proj.tasks"])

app.conf.update(
    CELERY_TASK_RESULT_EXPIRES=3600,
     CELERY_ROUTES = {
        'proj.tasks.add': {'queue': 'hipri'},
    },
)

if __name__ == '__main__':
    app.start()
