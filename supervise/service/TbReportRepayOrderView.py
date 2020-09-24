import datetime
import json
from decimal import Decimal, ROUND_UP

from supervise.util.xulie import ComplexEncoder

from supervise import db
from supervise.models.TbReportLoanPlanNew import TbReportLoanPlanNew
from supervise.models.TbReportRepayOrderNew import TbReportRepayOrderNew
from supervise.models.TbReportUser import TbReportUser
from supervise.util.generatorTestData import *


class TbReportRepayOrderView():

    def getRepayOrderNo(self):
        nowDate = datetime.datetime.now().strftime('%Y%m%d%H%M%S%f')
        return 'HK'+ nowDate[:-4]

    def insertRepayOrder(self,data):
        tbReportRepayOrderList = []
        status = 1
        penaltyMoney = 0
        penalty = 0.006
        repaymentType = 3
        comment = '测试'
        userId = data['user_id']
        lineType = int(data['line_type'])
        ifMerge = data['close']
        user = TbReportUser()
        user = user.query.filter_by(user_id=userId).first()
        userName = user.user_name
        loanPlan = TbReportLoanPlanNew()
        loanOrderNo = data['loan_order_no']
        userType = 3
        if lineType == 4:
            userType = 1
        elif lineType == '':
            userType = 2
        stagesIndexs = data['stages_index']
        stagesIndexs = stagesIndexs.split(',')
        num = len(stagesIndexs)
        actualTimes = data['actual_time'].split(',')
        actualTimeNum = len(actualTimes)
        actualMoney = data['actual_money']
        actualInterestMoney = data['actual_interest_money']
        repaymentOrderNo = self.getRepayOrderNo()

        actualMoney = Decimal(actualMoney) / Decimal(str(num))
        actualMoney = int(actualMoney.quantize(Decimal('1.'), rounding=ROUND_UP))
        actualInterestMoney = Decimal(actualInterestMoney) / Decimal(str(num))
        actualInterestMoney = int(actualInterestMoney.quantize(Decimal('1.'), rounding=ROUND_UP))
        for stagesIndex in range(num):
            id = random_num(6)
            if ifMerge == 'off':
                repaymentOrderNo = self.getRepayOrderNo()
            if stagesIndex<actualTimeNum:
                actualTime = actualTimes[stagesIndex]
            else:
                actualTime = actualTimes[-1]

            createTime = actualTime
            stagesIndex = stagesIndexs[stagesIndex]
            loanPlan = loanPlan.query.filter_by(user_id=userId,loan_order_no=loanOrderNo,stages_index=stagesIndex).first()
            repayPlanId = loanPlan.plan_id

            tbReportRepayOrder = TbReportRepayOrderNew(id=id,line_type=lineType,user_id=userId,repay_plan_id=repayPlanId,repayment_order_no=repaymentOrderNo,actual_time=actualTime,stages_index=stagesIndex,user_name=userName,actual_money=actualMoney,actual_interest_money=actualInterestMoney,
                                                    status=status,penalty_money=penaltyMoney,penalty=penalty,repayment_type=repaymentType,comment=comment,user_type=userType,create_time=createTime)
            tbReportRepayOrderList.append(tbReportRepayOrder)
        return tbReportRepayOrderList


    def queryRepayOrder(self,data):
        tbReportRepayOrder =TbReportRepayOrderNew()
        page = int(data['page'])
        limit = int(data['limit'])
        pages = (page - 1) * limit
        if  'loanOrderNo' not in data.keys():
            data['loanOrderNo'] = ''
        if 'userId' not in data.keys() :
            data['userId'] = ''

        response = {}
        response['code']=0
        response['msg']=""
        sqlCount = tbReportRepayOrder.selectOrderNoByloanOrderNoCount(data)
        counts = db.session.execute(sqlCount)
        #获取数据的个数，分页数据使用
        count = counts.fetchall()[0][0]
        # count = 1
        # if isinstance(counts, list):
        #     count= len(counts)
        #分页并按照每页显示数据的个数查询数据
        # result = TbReportRepayOrder.query.filter(*query_list).limit(limit).offset(pages).all()
        sqlQuery = tbReportRepayOrder.selectOrderNoByloanOrderNo(data,limit,pages=pages)
        result = db.session.execute(sqlQuery).fetchall()
        emp_json_list = [dict(zip(item.keys(), item)) for item in result]
        # resultList = []
        # #将查询结果转换成json
        # if isinstance(result,list):
        #     for x in result:
        #         a = x.to_json()
        #         resultList.append(a)
        # else:
        #     resultList.append(result.to_json())
        response['count'] = count
        response['data'] = emp_json_list
        resultJson = json.dumps(response,cls=ComplexEncoder,ensure_ascii=False)

        return resultJson

    def updateRepayOrderData(self,data):
        id = int(data['id'])
        updateData ={}
        updateData['actual_time'] = data['actual_time']
        updateData['actual_money'] = data['actual_money']
        updateData['actual_interest_money'] = data['actual_interest_money']
        updateData['stages_index'] = data['stages_index']
        updateData['create_time'] = data['create_time']

        repayOrderView = TbReportRepayOrderNew()
        repayOrderView.query.filter_by(id=id).update(updateData)
        db.session.commit()


if __name__ == '__main__':
    test = TbReportRepayOrderView()
    data = {}
    data['limit'] = 10
    data['page'] = 1
    test.queryRepayOrder(data)


