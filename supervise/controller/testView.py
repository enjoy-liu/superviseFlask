from flask_login import login_required

from supervise.service.TbReportLoanInfoView import TbReportLoandInfoView
from supervise.service.TbReportLoanPlanView  import TbReportLoanPlanView
from supervise.service.TbReportRepayOrderView  import TbReportRepayOrderView
from supervise.service.TbAcctMthlyView  import TbAcctMthlyView

from flask import  render_template, request

import json
from flask import current_app


class LoanInfo():
    @login_required
    def loan_info_query(self):
        return render_template('/index/loanInfo/loan_info_query.html')


    def loan_info_data(self):
        recv_data = json.loads(request.get_data(as_text=True))
        loanInfo = TbReportLoandInfoView()
        return loanInfo.queryLoanInfo(recv_data)


    def loan_info_edit(self):
        return render_template('/index/loanInfo/loan_info_edit.html')


    def loan_info_update(self):
        response = {}
        try:
            recv_data = json.loads(request.get_data(as_text=True))
            current_app.logger.info("借款数据修改，入参{}".format(recv_data))
            loanInfo = TbReportLoandInfoView()
            loanInfo.updateLoanInfoData(recv_data)
            response['code'] = 0
            return response
        except Exception as e:
            current_app.logger.error("借款数据修改失败，失败原因{}".format(e))
            response['code'] = 1
            errorInfo = "{}".format(e)
            current_app.log.error(errorInfo)
            response['error'] = errorInfo
            return response


class LoanPlan():
    @login_required
    def loan_plan_query(self):
        return render_template('/index/loanPlan/loan_plan_query.html')


    def loan_plan_data(self):
        recv_data = json.loads(request.get_data(as_text=True))
        loanPlan = TbReportLoanPlanView()
        return loanPlan.queryLoanPlan(recv_data)

    def loan_plan_edit(self):
        return render_template('/index/loanPlan/loan_plan_edit.html')

    def loan_plan_update(self):
        response = {}
        try:
            recv_data = json.loads(request.get_data(as_text=True))
            current_app.logger.info("还款计划数据修改，入参{}".format(recv_data))
            loanPlan = TbReportLoanPlanView()
            loanPlan.updateLoanPlanData(recv_data)
            response['code'] = 0
            return response
        except Exception as e:
            current_app.logger.error("还款计划修改失败，失败原因{}".format(e))
            response['code'] = 1
            errorInfo = "{}".format(e)
            current_app.log.error(errorInfo)
            response['error'] = errorInfo
            return response

class RepayOrder():
    @login_required
    def repay_order_query(self):
        return render_template('/index/repayOrder/repay_order_query.html')


    def repay_order_data(self):
        recv_data = json.loads(request.get_data(as_text=True))
        repayOrder = TbReportRepayOrderView()
        return repayOrder.queryRepayOrder(recv_data)

    def repay_order_edit(self):
        return render_template('/index/repayOrder/repay_order_edit.html')

    def repay_order_update(self):
        response = {}
        try:
            recv_data = json.loads(request.get_data(as_text=True))
            current_app.logger.info("实际还款数据修改，入参{}".format(recv_data))
            repayOrder = TbReportRepayOrderView()
            repayOrder.updateRepayOrderData(recv_data)
            response['code'] = 0
            return response
        except Exception as e:
            current_app.logger.error("实际还款修改失败，失败原因{}".format(e))
            response['code'] = 1
            errorInfo = "{}".format(e)
            current_app.log.error(errorInfo)
            response['error'] = errorInfo
            return response

class Rh():
    @login_required
    def mthlyView(self):
        return render_template('/index/mthly.html')
    def mthlyData(self):
        recv_data = json.loads(request.get_data(as_text=True))
        mthly = TbAcctMthlyView()
        return mthly.queryMthly(recv_data)

def add_new_routes(app):
    loanInfo =LoanInfo()
    loanPlan = LoanPlan()
    repayOrder = RepayOrder()
    rh = Rh()
    #loan_info表view
    app.add_url_rule('/loan/info/query', view_func=loanInfo.loan_info_query)
    app.add_url_rule('/loan/info',methods=['POST'], view_func=loanInfo.loan_info_data)
    app.add_url_rule('/loan/info/edit', view_func=loanInfo.loan_info_edit)
    app.add_url_rule('/loan/info/editData',methods=['POST'], view_func=loanInfo.loan_info_update)
    #loan_plan表view
    app.add_url_rule('/loan/plan/query', view_func=loanPlan.loan_plan_query)
    app.add_url_rule('/loan/plan',methods=['POST'], view_func=loanPlan.loan_plan_data)
    app.add_url_rule('/loan/plan/edit', view_func=loanPlan.loan_plan_edit)
    app.add_url_rule('/loan/plan/editData',methods=['POST'], view_func=loanPlan.loan_plan_update)
    #repay_order表view
    app.add_url_rule('/repay/order/query', view_func=repayOrder.repay_order_query)
    app.add_url_rule('/repay/order',methods=['POST'], view_func=repayOrder.repay_order_data)
    app.add_url_rule('/repay/order/edit', view_func=repayOrder.repay_order_edit)
    app.add_url_rule('/repay/order/editData',methods=['POST'], view_func=repayOrder.repay_order_update)

    #rh报送表view
    app.add_url_rule('/rh/mthly/data',methods=['POST'], view_func=rh.mthlyData)
    app.add_url_rule('/rh/mthly/view', view_func=rh.mthlyView)