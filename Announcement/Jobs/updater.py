from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from .annoucement import changeStatus, tagStatus

def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(changeStatus , 'interval', seconds=60, id='item', replace_existing=True)
    scheduler.add_job(tagStatus , 'interval', days=1, id='tagNew', replace_existing=True)
    scheduler.start()
   

