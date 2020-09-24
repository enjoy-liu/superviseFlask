from supervise.util.generatorTestData import *
from supervise.models.TbReportCreditContract import TbReportCreditContract
from supervise.models.TbReportUser import TbReportUser
from supervise.util.generatorTestData import *
from supervise import db

class TbReportCreditContractView():

    def insertContract(self,data):
        id = random_num(8)
        lineType = int(data['line_type'])
        userType = 3
        if lineType == 4:
            userType = 1
        elif lineType == '':
            userType = 2
        userId = data['user_id']
        user = TbReportUser()
        user = user.query.filter_by(user_id=userId).first()
        userName = user.user_name
        contractNo = data['contract_no']
        contractSignTime = data['contract_start_time']
        contractStartTime = contractSignTime
        contractEndTime = data['contract_end_time']
        contractCreditLine = data['contract_credit_line']
        creditUsable = data['credit_usable']
        currency = 'CNY'
        isValid = 1
        isCirculateQuota = 1
        comprehensiveQuota =data['comprehensive_quota']
        comprehensiveQuotaNo = data['comprehensive_quota_no']


        tbReportCreditContract = TbReportCreditContract(id=id,line_type=lineType,user_id=userId,contract_no=contractNo,user_name=userName,
                                                        contract_sign_time=contractSignTime,contract_start_time=contractStartTime,contract_end_time=contractEndTime,
                                                        contract_credit_line=contractCreditLine,credit_usable=creditUsable,currency=currency,is_valid=isValid,user_type=userType,
                                                        is_circulate_quota=isCirculateQuota,comprehensive_quota=comprehensiveQuota,comprehensive_quota_no=comprehensiveQuotaNo)

        db.session.add(tbReportCreditContract)
        db.session.commit()
