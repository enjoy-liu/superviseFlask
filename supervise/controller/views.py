import json

from flask_login import login_required

from supervise.service.TbReportLoanInfoView import TbReportLoandInfoView
from supervise.service.TbReportLoanPlanView import TbReportLoanPlanView
from supervise.service.TbReportRepayOrderView import TbReportRepayOrderView
from supervise.service.TbReportUserView import TbReportUserView
from supervise.service.TbReportCreditContractView import TbReportCreditContractView
from flask import  render_template, request
from supervise import app
from supervise import db
from supervise.controller.testView import add_new_routes
from supervise.controller.loginView import add_login_view
from supervise.controller.jobView import add_job_view

from flask import current_app

add_new_routes(app)
add_login_view(app)
add_job_view(app)


@app.route('/',methods=['GET'])
@login_required
def index():
    return render_template("/index/index.html")


@app.route('/user',methods=['GET'])
@login_required
def user():
    return render_template('/index/user.html')



@app.route('/contract',methods=['GET'])
@login_required
def contract():
    return render_template('/index/contract.html')


@app.route('/loan',methods=['GET'])
@login_required
def loan():
    return render_template('/index/loan.html')


@app.route('/repay',methods=['GET'])
@login_required
def repay():
    return render_template('/index/repay.html')
@app.route('/add/user',methods=['POST'])
def add_user_data():
    response = {}
    try:
        recv_data = json.loads(request.get_data(as_text=True))
        current_app.logger.info("用户数据生成开始，入参{}".format(recv_data))
        user = TbReportUserView()
        user.insertUser(recv_data)
        response['code'] = 0
        return response
    except Exception as e:
        db.session.rollback()

        response['code'] = 1
        errorInfo = "{}".format(e)
        current_app.logger.error("用户数据生成失败，失败原因{}".format(errorInfo))
        response['error'] = errorInfo
        return response


@app.route('/add/contract', methods=['POST'])
def add_contract_data():
    response = {}
    try:
        recv_data = json.loads(request.get_data(as_text=True))
        current_app.logger.info("合同数据生成开始，入参{}".format(recv_data))
        contract = TbReportCreditContractView()
        contract.insertContract(recv_data)
        response['code'] = 0
        return response
    except Exception as e:
        db.session.rollback()
        current_app.logger.error("合同数据生成失败，失败原因{}".format(e))
        response['code'] = 1
        errorInfo = "{}".format(e)
        current_app.log.error(errorInfo)
        response['error'] = errorInfo
        return response


@app.route('/add/loan',methods=['POST'])
def add_loan_data():
    response = {}
    try:
        recv_data = json.loads(request.get_data(as_text=True))
        current_app.logger.info("借款数据生成开始，入参{}".format(recv_data))

        loanIndoView = TbReportLoandInfoView()
        tbReportLoanPlanView = TbReportLoanPlanView()
        tbReportLoanInfo = loanIndoView.insertloanInfo(recv_data)
        db.session.add(tbReportLoanInfo)
        tbReportLoanPlanList = tbReportLoanPlanView.insertLoanPlan(recv_data)
        for tbReportLoanPlan in tbReportLoanPlanList:
            db.session.add(tbReportLoanPlan)
        db.session.commit()
        response['code'] = 0
        return response
    except Exception as e:
        db.session.rollback()
        current_app.logger.error("借款数据生成失败，失败原因{}".format(e))
        response['code'] = 1
        errorInfo = "{}".format(e)
        current_app.log.error(errorInfo)
        response['error'] = errorInfo
        return response


@app.route('/add/repay', methods=['POST'])
def add_repay_data():
    response = {}
    try:
        recv_data = json.loads(request.get_data(as_text=True))

        current_app.logger.info("还款数据生成开始，入参{}".format(recv_data))
        repayOrderView = TbReportRepayOrderView()
        tbReportRepayOrderList = repayOrderView.insertRepayOrder(recv_data)
        for tbReportRepayOrder in tbReportRepayOrderList:
            db.session.add(tbReportRepayOrder)
        db.session.commit()
        response['code'] = 0
        return response
    except Exception as e:
        db.session.rollback()
        current_app.logger.error("还款数据生成失败，失败原因{}".format(e))
        response['code'] = 1
        errorInfo = "{}".format(e)
        current_app.logger.error(errorInfo)
        response['error'] = errorInfo
        return response