import json

from supervise.util.dateUtil import *
from supervise.util.xulie import *

from supervise import db
from supervise.models.TbReportCreditContract import TbReportCreditContract
from supervise.models.TbReportLoanInfoNew import TbReportLoanInfoNew
from supervise.models.TbReportUser import TbReportUser
from supervise.util.generatorTestData import *


class TbReportLoandInfoView():
    def insertloanInfo(self,data):
        id = random_num(8)
        userId = data['user_id']
        user = TbReportUser()
        user = user.query.filter_by(user_id=userId).first()
        contract = TbReportCreditContract()
        contract = contract.query.filter_by(user_id=userId).first()

        lineType = int(data['line_type'])
        userName = user.user_name
        stagesNum = int(data['stages_num'])
        loanType = '等本等息'
        contractNo = contract.contract_no
        loanOrderNo = data['loan_order_no']
        isStages = 1
        if stagesNum == 1:
            isStages = 0
        term = 0
        loanTime = data['loan_time']
        loanExpired = add_month(data['plan_time'],stagesNum-1)
        interestCalculation = 2 #'等本等息'
        loanMoney = data['loan_money']
        interest = 1.30000
        penalty = 3.00000
        status = 1
        clearTime = None
        userType = 3
        if lineType == 4 :
            userType = 1
        elif lineType =='':
            userType = 2

        createTime = data['create_time']

        tbReportLoanInfo= TbReportLoanInfoNew(id=id,line_type=lineType,user_id =userId,user_name=userName,loan_type=loanType,contract_no=contractNo,loan_order_no=loanOrderNo,
                        is_stages=isStages,stages_num=stagesNum,term=term,loan_time=loanTime,loan_expired=loanExpired,interest_calculation=interestCalculation
        ,loan_money=loanMoney,interest=interest,penalty=penalty,status=status,clear_time=clearTime,user_type=userType,create_time=createTime)

        # db.session.add(tbReportLoanInfo)
        # db.session.commit()
        return tbReportLoanInfo

    def queryLoanInfo(self,data):
        query_list = []
        page = int(data['page'])
        limit = int(data['limit'])
        pages = (page - 1) * limit
        loanOrderNoWhere = ''
        userIdWhere = ''
        if  'loanOrderNo' in data.keys() and data['loanOrderNo'] != '':
            query_list.append(TbReportLoanInfoNew.loan_order_no == data['loanOrderNo'])
            loanOrderNoWhere = "and loan_order_no='{}'".format(data['loanOrderNo'])
        if 'userId' in data.keys() and data['userId'] != '':
            query_list.append(TbReportLoanInfoNew.user_id == data['userId'])
            print('*****',query_list)
            userIdWhere = "and user_id='{}'".format(data['userId'])
        data = {}
        data['code']=0
        data['msg']=""
        sql = "select count(0) from tb_report_loan_info_new where 1 = 1 {} {} limit 1".format(loanOrderNoWhere,userIdWhere)
        counts = db.session.execute(sql)
        #获取数据的个数，分页数据使用
        count = counts.fetchall()[0][0]
        # count = 1
        # if isinstance(counts, list):
        #     count= len(counts)
        #分页并按照每页显示数据的个数查询数据
        result = TbReportLoanInfoNew.query.filter(*query_list).limit(limit).offset(pages).all()

        resultList = []
        #将查询结果转换成json
        if isinstance(result,list):
            for x in result:
                a = x.to_json()
                resultList.append(a)
        else:
            resultList.append(result.to_json())
        data['count'] = count
        data['data'] = resultList
        resultJson = json.dumps(data,cls=ComplexEncoder,ensure_ascii=False)

        return resultJson

    def updateLoanInfoData(self,data):
        id = int(data['id'])
        updateData ={}
        updateData['loan_money'] = int(data['loan_money'])
        updateData['loan_time'] = data['loan_time']
        updateData['stages_num'] = int(data['stages_num'])
        updateData['loan_expired'] = data['loan_expired']
        updateData['clear_time'] = data['clear_time']
        updateData['create_time'] = data['create_time']

        loanInfoView = TbReportLoanInfoNew()
        # loanInfoView = loanInfoView.query.filter_by(id=id).first()
        # loanInfoView.loan_time = loanTime
        # loanInfoView.stages_num = stagesNum
        # loanInfoView.loan_expired = loanExpired
        # loanInfoView.clear_time = clearTime
        # loanInfoView.create_time = createTime
        loanInfoView.query.filter_by(id=id).update(updateData)
        db.session.commit()






if __name__ == '__main__':
    user = TbReportLoandInfoView()
    data={}
    data['limit'] = '10'
    data['page'] = '1'
    data['userId'] = '88888888'

    user.queryLoanInfo(data)

