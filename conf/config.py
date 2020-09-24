import datetime
import os

from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore

CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

USERNAME = 'root'
PASSWORD = 'root'
HOST = '172.17.33.65'
DB = 'jrpt_supervise_report_test'
#mysql://root:密码@localhost:3306/text1
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://%s:%s@%s/%s' % (USERNAME, PASSWORD, HOST, DB)
SQLALCHEMY_TRACK_MODIFICATIONS = False
PERMANENT_SESSION_LIFETIME = datetime.timedelta(minutes=15)

JOBS=[]
# 存储位置
SCHEDULER_JOBSTORES = {
    'default': SQLAlchemyJobStore(url=SQLALCHEMY_DATABASE_URI)}
SCHEDULER_JOB_DEFAULTS = {
    'coalesce': False,
    'max_instances': 3
}

SCHEDULER_API_ENABLED = True