from flask import  render_template, request

import json
from flask import current_app
from flask_login import login_required

from supervise.controller.commonApi import reportJob

from supervise import scheduler
from supervise.job.testJob import job_first


def addJob():
    scheduler.add_job(func=job_first, id='1',trigger='cron', second=5, misfire_grace_time=3
,replace_existing=True)
    return 'success'

def pauseJob():
    scheduler.pause_job('1')
    return "Success!"

def resumeJob():
    scheduler.resume_job('1')
    return "Success!"

def modifyJob():
    scheduler.modify_job('1',trigger='cron',second=10)
    return "Success!"

@login_required
def rhReportJobView():
    return render_template('/index/rh_job.html')

def reportJobView():
    recv_data = json.loads(request.get_data(as_text=True))
    result = reportJob(recv_data)
    response={}
    if result == 200:
        response['code']=0

    else:
        response['code'] = 1
    return response




def add_job_view(app):
    app.add_url_rule('/job/addJob',methods=['POST','GET'], view_func=addJob)
    app.add_url_rule('/job/pauseJob',methods=['POST','GET'], view_func=pauseJob)
    app.add_url_rule('/job/resumeJob',methods=['POST','GET'], view_func=resumeJob)
    app.add_url_rule('/job/modifyJob',methods=['POST','GET'], view_func=modifyJob)
    app.add_url_rule('/rh/reportJob',methods=['POST','GET'], view_func=reportJobView)
    app.add_url_rule('/rh/reportJob/view',methods=['POST','GET'], view_func=rhReportJobView)