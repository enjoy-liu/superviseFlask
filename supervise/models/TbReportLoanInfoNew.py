# coding: utf-8

from supervise import db






class TbReportLoanInfoNew(db.Model):
    __tablename__ = 'tb_report_loan_info_new'

    id = db.Column(db.BigInteger, primary_key=True, info='主键')
    line_type = db.Column(db.SmallInteger, info='业务线类型:0联名卡金融、1重高ETC、2保险分期、3卡车分期、4新好运条、历史现金贷产品（5好运卡、6提前过大年）')
    user_id = db.Column(db.String(50), index=True, info='用户id')
    user_name = db.Column(db.String(256), info='借款人姓名')
    loan_type = db.Column(db.String(64), info='借款类型（产品类型）')
    contract_no = db.Column(db.String(50), info='合同编号')
    loan_order_no = db.Column(db.String(36), index=True, info='借款编号')
    is_stages = db.Column(db.String(2), info='是否分期:0代表不分期，1代表分期')
    stages_num = db.Column(db.Integer, info='分期数，不分期默认1，分期取具体业务')
    term = db.Column(db.Integer, info='账期，不分期取具体业务值，分期赋值0')
    loan_time = db.Column(db.String(20), index=True, info='借款时间yyyyMMdd')
    loan_expired = db.Column(db.String(20), info='借款到期时间')
    interest_calculation = db.Column(db.SmallInteger, info='计息方式1：一次性还本付息2：等本等息3：等额本息')
    loan_money = db.Column(db.BigInteger, info='借款金额')
    interest = db.Column(db.Numeric(17, 5), info='月利率%')
    penalty = db.Column(db.Numeric(17, 5), info='逾期月利率%')
    status = db.Column(db.SmallInteger, info='借款状态 1:已放款,2:还款中,3:已逾期,4:已结清')
    clear_time = db.Column(db.String(10), info='结清时间')
    user_type = db.Column(db.String(2), info='用户类型 1 个人 2 企业')
    create_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue(), info='创建时间')

    def to_json(self): # ---------------------
        dict = self.__dict__
        if "_sa_instance_state" in dict:
            del dict["_sa_instance_state"]
        return dict
