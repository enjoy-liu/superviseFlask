# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, SmallInteger, String
from sqlalchemy.schema import FetchedValue
from supervise import db





class TbReportLoanPlanNew(db.Model):
    __tablename__ = 'tb_report_loan_plan_new'

    id = db.Column(db.BigInteger, primary_key=True, info='主键')
    line_type = db.Column(db.SmallInteger, info='业务线类型:0联名卡金融、1重高ETC、2保险分期、3卡车分期、4新好运条、历史现金贷产品（5好运卡、6提前过大年），7：好运贷')
    plan_id = db.Column(db.String(64), index=True, info='0_业务id:表示不分期计划表id，1_业务id:表示分期计划表id')
    user_id = db.Column(db.String(50), info='用户id')
    user_name = db.Column(db.String(256), info='借款人姓名')
    loan_order_no = db.Column(db.String(36), index=True, info='借款编号')
    stages_index = db.Column(db.String(2), info='还款期数,不分期默认为1')
    plan_time = db.Column(db.String(20), index=True, info='应还日期')
    pay_money = db.Column(db.BigInteger, info='应还本金')
    interest_money = db.Column(db.BigInteger, info='应还利息')
    start_compute_interest_time = db.Column(db.String(20), info='开始计算利息时间')
    end_compute_interest_time = db.Column(db.String(20), info='止息日期')
    status = db.Column(db.SmallInteger, info='还款状态 1:待还款,2:已还款,3:已逾期')
    overdue_money = db.Column(db.BigInteger, info='逾期利息')
    rest_money = db.Column(db.BigInteger, info='剩余本金')
    user_type = db.Column(db.String(2), info='用户类型1个人2企业')
    contract_no = db.Column(db.String(50), info='合同编号')
    create_time = db.Column(db.DateTime, server_default=db.FetchedValue(), info='创建时间')
    update_time = db.Column(db.DateTime, info='更新时间')
    rest_interest_money = db.Column(db.BigInteger, info='剩余利息')

    def to_json(self): # ---------------------
        dict = self.__dict__
        if "_sa_instance_state" in dict:
            del dict["_sa_instance_state"]
        return dict