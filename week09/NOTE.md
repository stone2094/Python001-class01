学习笔记
### 注册用户
'''
    python manage.py shell
    >>>from django.contrib.auto.models import User 
    >>>user = User.objects.create_usser('stone','stone@gmail.com','stone2020')
'''
### 定时任务的实现
'''
    1.Redis

    ``安装和启动

    2.安装

    Celery

    pip install celery

    pip install redis==3.5.3

    pip install celery-with-redis

    pip install django-celery

    3.添加app

    django-admin startproject MyDjango

    python manager.py startapp djcron

    INSTALL_APPS=[ 'djcelery', 'djcron' ]

    4.迁移生成表

    python manage.py makemigrations

    python manage.py migrate

    5.配置django时区

    from celery.schedules import crontab

    from celery.schedules import timedelta

    import djcelery

    djcelery.setup_loader()

    BROKER_URL = 'redis://:123456@127.0.0.1:6379/' # 代理人

    CELERY_IMPORTS = ('djcron.tasks') # app

    CELERY_TIMEZONE = 'Asia/Shanghai' # 时区

    CELERYBEAT_SCHEDULER = 'djcelery.schedulers.DatabaseScheduler' # 定时任务调度器

    6.在MyDjango下建立celery.py

    import os from celery import Celery, platforms

    from django.conf import settings

    os.environ.setdefault('DJANGO_SETTINGS_MODULE','MyDjango.settings')

    app = Celery('MyDjango')

    app.config_from_object('django.conf:settings')

    app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

    platforms.C_FORCE_ROOT = True

    在__init__.py 增加
'''
