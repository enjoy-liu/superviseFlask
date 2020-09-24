import requests
import json



def dataEncryption(data):
    enUrl = 'http://172.17.33.64:8080/jrpt-jgbs/test/enc?ciphertext={}'.format(data)
    result = json.loads(requests.get(url=enUrl).text)
    return result['data']

# def reportJob(data):
#     reportUrl = "http://172.17.33.64:8080/jrpt-jgbs/test/rh?param={},{}".format(data['report_date_start'],data['report_date_end'])
#     result = requests.get(url=reportUrl).text
#     return result

def reportJob(data):
    urllogin = 'http://172.17.33.64:8081/xxl-job-admin/login'
    urltask = 'http://172.17.33.64:8081/xxl-job-admin/jobinfo/trigger'
    header = {
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Connection': 'keep-alive',
        'Accept-Language': 'zh-CN,zh;q=0.9'
    }
    user = {'userName': 'admin', 'password': '123456'}
    dateTime = "{},{}".format(data['report_date_start'],data['report_date_end'])
    data1 = {'executorParam': dateTime, 'id': '61'}
    s = requests.Session()
    s.post(url=urllogin, data=user, headers=header)
    result = json.loads(s.post(url=urltask, data=data1).text)

    return result['code']