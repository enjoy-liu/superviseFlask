# coding: utf-8
from supervise import db



class TbReportCreditContract(db.Model):
    __tablename__ = 'tb_report_credit_contract'

    id = db.Column(db.BigInteger, primary_key=True, info='主键')
    line_type = db.Column(db.SmallInteger, info='业务线类型:0联名卡金融、1重高ETC、2保险分期、3卡车分期、4新好运条、历史现金贷产品（5好运卡、6提前过大年），7：好运贷')
    user_id = db.Column(db.String(50), info='用户id')
    contract_no = db.Column(db.String(50), info='贷款合同编号')
    user_name = db.Column(db.String(256), info='用户姓名')
    contract_sign_time = db.Column(db.String(20), info='合同签订日期')
    contract_start_time = db.Column(db.String(20), info='合同起效日期')
    contract_end_time = db.Column(db.String(20), info='合同失效日期')
    contract_credit_line = db.Column(db.BigInteger, info='合同信用额度')
    credit_usable = db.Column(db.BigInteger, info='剩余可用额度')
    currency = db.Column(db.String(10), info='币种')
    is_valid = db.Column(db.SmallInteger, info='合同状态:0无效,1有效')
    user_type = db.Column(db.String(2), info='用户类型1个人2企业')
    is_circulate_quota = db.Column(db.Integer, info='是否循环额度')
    comprehensive_quota = db.Column(db.BigInteger, info='综合额度')
    comprehensive_quota_no = db.Column(db.String(256), info='综合额度编号')

