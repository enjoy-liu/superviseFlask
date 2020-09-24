import datetime
import time
import dateutil.relativedelta


def currentTime():
    nowDate = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return nowDate

def add_month(date,num):
    d = datetime.datetime.strptime(date, "%Y%m%d")

    d2 = d + dateutil.relativedelta.relativedelta(months=num)

    return d2.strftime('%Y%m%d')

#日期格式转换
def date_format_conversion(str):
    timeStruct = time.strptime(str, "%Y%m%d")
    strTime = time.strftime("%Y-%m-%d %H:%M:%S", timeStruct)
    return strTime





if __name__ == '__main__':
    # print(type(add_month('20200612',2)))
    print(currentTime())
