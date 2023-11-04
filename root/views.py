from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from root import tasks  

def celery_task(request):

    # result = my_celery_task.apply_async(args=[10, 20])
    result = tasks.background_task.delay(6) 
    # result_value = result.get()  # This will block until the result is ready

    return HttpResponse(f"<h1>Task running in background</h1>")

def main_task(request):

    result = tasks.main_task(6) 
    # result_value = result.get()  # This will block until the result is ready

    return HttpResponse(f"<h1>Task completed</h1>")