# coding: utf-8
from supervise import db



class TbAcctMthly(db.Model):
    __tablename__ = 'tb_acct_mthly'

    id = db.Column(db.BigInteger, primary_key=True)
    cust_id = db.Column(db.String(64), nullable=False, info='客户号')
    dept_code = db.Column(db.String(16), nullable=False, info='机构代码')
    corp_code = db.Column(db.String(16), nullable=False, info='法人机构')
    info_up_date = db.Column(db.Date, info='业务发生日期')
    acct_no = db.Column(db.String(45), nullable=False, info='账户合同号')
    month = db.Column(db.String(7), nullable=False, info='月份')
    sett_date = db.Column(db.Date, info='结算/应还款日')
    acct_status = db.Column(db.String(2), nullable=False, info='账户状态')
    acct_bal = db.Column(db.BigInteger, nullable=False, info='余额')
    prid_acct_bal = db.Column(db.BigInteger, info='本期账单余额')
    used_amt = db.Column(db.BigInteger, info='已使用额度')
    not_isu_bal = db.Column(db.BigInteger, info='未出单的大额专项分期余额')
    rem_rep_prd = db.Column(db.Integer, info='剩余还款期数')
    five_cate = db.Column(db.String(1), nullable=False, info='五级分类')
    five_cate_adj_date = db.Column(db.Date, nullable=False, info='五级分类认定日期')
    rpy_status = db.Column(db.String(1), nullable=False, info='当前还款状态')
    rpy_prct = db.Column(db.Integer, info='实际还款百分比')
    overd_prd = db.Column(db.Integer, info='当前逾期期数')
    tot_overd = db.Column(db.BigInteger, info='当前逾期总额')
    overd_princ = db.Column(db.BigInteger, info='当前逾期本金')
    oved31_60princ = db.Column(db.BigInteger, info='逾期31-60天未归还本金')
    oved61_90princ = db.Column(db.BigInteger, info='逾期61-90天未归还本金')
    oved91_180princ = db.Column(db.BigInteger, info='逾期91-180天未归还本金')
    oved_princ180 = db.Column(db.BigInteger, info='逾期180天以上未归还本金')
    ovedraw_ba_ove180 = db.Column(db.BigInteger, info='透支180天以上未归还余额')
    cur_rpy_amt = db.Column(db.BigInteger, info='本月应还款金额')
    act_rpy_amt = db.Column(db.BigInteger, nullable=False, info='本月实际还款金额')
    lat_rpy_date = db.Column(db.Date, nullable=False, info='最近一次实际还款日期')
    close_date = db.Column(db.Date, info='账户关闭日期')
    line_type = db.Column(db.Integer, info='业务类型')
    change_flag = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否修改')
    report_status = db.Column(db.String(1), nullable=False, server_default=db.FetchedValue(), info='报送状态 0：未报送  1：报送成功  2：报送失败')
    report_date = db.Column(db.String(10), info='上报日期')
    create_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue(), info='创建时间')

    def to_json(self): # ---------------------
        dict = self.__dict__
        if "_sa_instance_state" in dict:
            del dict["_sa_instance_state"]
        return dict
