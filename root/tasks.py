from celery import shared_task 
import time
  
@shared_task
def background_task(x):
    time.sleep(x)
    return x


def main_task(x):
    time.sleep(x)
    return x