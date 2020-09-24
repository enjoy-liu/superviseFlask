import json
from decimal import Decimal, ROUND_UP

from supervise.util.dateUtil import *
from supervise.util.xulie import ComplexEncoder

from supervise import db
from supervise.models.TbReportCreditContract import TbReportCreditContract
from supervise.models.TbReportLoanPlanNew import TbReportLoanPlanNew
from supervise.models.TbReportUser import TbReportUser
from supervise.util.generatorTestData import *


class TbReportLoanPlanView():
    def insertLoanPlan(self,data):
        tbReportLoanPlanList = []
        userId = data['user_id']
        lineType = int(data['line_type'])
        user = TbReportUser()
        user = user.query.filter_by(user_id=userId).first()
        contract = TbReportCreditContract()
        contract = contract.query.filter_by(user_id=userId).first()
        stagesNum = int(data['stages_num'])
        payMoney = Decimal(data['loan_money']) / Decimal(str(stagesNum))
        payMoney = int(payMoney.quantize(Decimal('1.'), rounding=ROUND_UP))
        interestMoney = Decimal(data['interest_money']) / Decimal(str(stagesNum))
        interestMoney = int(interestMoney.quantize(Decimal('1.'), rounding=ROUND_UP))
        startComputeInterestTime = data['loan_time']
        contract_no = contract.contract_no
        userName = user.user_name
        for i in range(stagesNum):
            num = i+1
            id = random_num(8)

            loanOrderNo = data['loan_order_no']
            planId = str(num)+ '_'+ loanOrderNo
            stagesIndex = num
            planTime = add_month(data['plan_time'],i)
            startComputeInterestTime = add_month(startComputeInterestTime,i)
            endComputeInterestTime = planTime
            status = 1
            overdueMoney = 0
            restMoney = payMoney
            userType = 3
            if lineType == 4:
                userType = 1
            elif lineType == '':
                userType = 2

            createTime =  data['create_time']
            updateTime = str(currentTime())

            tbReportLoanPlan = TbReportLoanPlanNew(id=id,line_type=lineType,plan_id=planId,user_id=userId,user_name=userName,
                                                loan_order_no=loanOrderNo,stages_index=stagesIndex,plan_time=planTime,pay_money=payMoney,
                                                interest_money=interestMoney,start_compute_interest_time=startComputeInterestTime,
                                                end_compute_interest_time=endComputeInterestTime,status=status,overdue_money=overdueMoney,
                                                rest_money=restMoney,user_type=userType,contract_no=contract_no,create_time=createTime,update_time=updateTime)

            tbReportLoanPlanList.append(tbReportLoanPlan)
            # db.session.add(tbReportLoanPlan)
            # db.session.commit()
        return tbReportLoanPlanList

    def queryLoanPlan(self,data):
        query_list = []
        page = int(data['page'])
        limit = int(data['limit'])
        pages = (page - 1) * limit
        loanOrderNoWhere = ''
        userIdWhere = ''
        if  'loanOrderNo' in data.keys() and data['loanOrderNo'] != '':
            query_list.append(TbReportLoanPlanNew.loan_order_no == data['loanOrderNo'])
            loanOrderNoWhere = "and loan_order_no='{}'".format(data['loanOrderNo'])
        if 'userId' in data.keys() and data['userId'] != '':
            query_list.append(TbReportLoanPlanNew.user_id == data['userId'])
            userIdWhere = "and user_id='{}'".format(data['userId'])
        data = {}
        data['code']=0
        data['msg']=""
        sql = "select count(0) from tb_report_loan_plan_new where 1 = 1 {} {} limit 1".format(loanOrderNoWhere,userIdWhere)
        counts = db.session.execute(sql)
        #获取数据的个数，分页数据使用
        count = counts.fetchall()[0][0]
        # count = 1
        # if isinstance(counts, list):
        #     count= len(counts)
        #分页并按照每页显示数据的个数查询数据
        result = TbReportLoanPlanNew.query.filter(*query_list).limit(limit).offset(pages).all()

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

    def updateLoanPlanData(self,data):
        id = int(data['id'])
        updateData ={}
        updateData['plan_time'] = data['plan_time']
        updateData['pay_money'] = data['pay_money']
        updateData['interest_money'] = data['interest_money']
        updateData['stages_index'] = data['stages_index']
        updateData['create_time'] = data['create_time']

        loanPlanView = TbReportLoanPlanNew()
        loanPlanView.query.filter_by(id=id).update(updateData)
        db.session.commit()




