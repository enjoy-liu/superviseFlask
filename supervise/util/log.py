import os,logbook
from logbook.more import ColorizedStderrHandler

check_path='.'
LOG_DIR = os.path.join(check_path, 'testlog')
file_stream = False
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)
    file_stream = True

def get_logger(name='supervise', file_log=file_stream, level=''):
    logbook.set_datetime_format('local')
    ColorizedStderrHandler(bubble=False, level=level).push_thread()
    logbook.TimedRotatingFileHandler(
            os.path.join(LOG_DIR, '%s.log' % name),
            date_format='%Y-%m-%d-%H-%M', bubble=True, encoding='utf-8').push_thread()
    return logbook.Logger(name)

LOG = get_logger(file_log=file_stream, level='INFO')