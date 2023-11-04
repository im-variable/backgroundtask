
from django.urls import path
from .views import main_task, celery_task

urlpatterns = [
    path('main', main_task, name="main"),
    path('celery', celery_task, name="celery"),
]
