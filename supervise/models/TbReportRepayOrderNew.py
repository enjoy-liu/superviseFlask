# coding: utf-8
from supervise import db






class TbReportRepayOrderNew(db.Model):
    __tablename__ = 'tb_report_repay_order_new'

    id = db.Column(db.BigInteger, primary_key=True, info='主键')
    line_type = db.Column(db.SmallInteger, info='业务线类型:0联名卡金融、1重高ETC、2保险分期、3卡车分期、4新好运条、历史现金贷产品（5好运卡、6提前过大年），7：好运贷')
    user_id = db.Column(db.String(50), info='用户id')
    repay_plan_id = db.Column(db.String(64), index=True, info='还款计划ID，关联计划表的plan_id')
    repayment_order_no = db.Column(db.String(36), info='还款编号')
    actual_time = db.Column(db.String(20), index=True, info='还款日期')
    stages_index = db.Column(db.String(2), info='还款期数,不分期默认为1')
    user_name = db.Column(db.String(256), info='借款人姓名')
    actual_money = db.Column(db.BigInteger, info='还款本金')
    actual_interest_money = db.Column(db.BigInteger, info='还款利息')
    status = db.Column(db.SmallInteger, info='还款类型:1正常，2逾期')
    penalty_money = db.Column(db.BigInteger, info='逾期利息')
    penalty = db.Column(db.Numeric(17, 5), info='逾期利率(%)')
    repayment_type = db.Column(db.SmallInteger, info='扣款方式：0银行代扣,1银联代扣,2现金,3银行转帐,4其它')
    comment = db.Column(db.String(100), info='描述')
    user_type = db.Column(db.String(2), info='用户类型1个人2企业')
    create_time = db.Column(db.DateTime, server_default=db.FetchedValue(), info='创建时间')

    def to_json(self): # ---------------------
        dict = self.__dict__
        if "_sa_instance_state" in dict:
            del dict["_sa_instance_state"]
        return dict

    def selectOrderNoByloanOrderNo(self,data, limit, pages):
        userIdWhere = ''
        loanOrderNoWhere = ''
        if data['loanOrderNo'] != '':
            loanOrderNoWhere = "and p.loan_order_no = '{}'".format(data['loanOrderNo'])
        if data['userId'] != '':
            userIdWhere = "and r.user_id = '{}'".format(data['userId'])

        sql = "select r.*,p.loan_order_no from tb_report_repay_order_new r left join tb_report_loan_plan_new p on r.repay_plan_id=p.plan_id " \
              "where 1 =1 {}{} limit {} offset {} ".format(userIdWhere, loanOrderNoWhere, limit, pages)
        return sql

    def selectOrderNoByloanOrderNoCount(self,data):
        userIdWhere = ''
        loanOrderNoWhere = ''
        if data['loanOrderNo'] != '':
            loanOrderNoWhere = "and p.loan_order_no = '{}'".format(data['loanOrderNo'])
        if data['userId'] != '':
            userIdWhere = "and r.user_id = '{}'".format(data['userId'])

        sql = "select count(0) from tb_report_repay_order_new r left join tb_report_loan_plan_new p on r.repay_plan_id=p.plan_id where 1 = 1 {} {} limit 1".format(
            loanOrderNoWhere, userIdWhere)

        return sql