# coding: utf-8

from supervise import db


class TbReportUser(db.Model):
    __tablename__ = 'tb_report_user'

    id = db.Column(db.BigInteger, primary_key=True, info='主键')
    line_type = db.Column(db.SmallInteger, info='业务线类型:0联名卡金融、1重高ETC、2保险分期、3卡车分期、4新好运条、历史现金贷产品（5好运卡、6提前过大年）')
    user_type = db.Column(db.String(20), info='用户类型 1 个人 2 企业')
    user_id = db.Column(db.String(50), index=True, info='用户id')
    user_name = db.Column(db.String(256), info='用户姓名')
    id_card = db.Column(db.String(128), index=True, info='用户身份证号')
    phone = db.Column(db.String(64), info='用户手机号')
    gender = db.Column(db.SmallInteger, info='性别:0男性，1女性')
    birth_date = db.Column(db.String(20), info='出生日期')
    marital_status = db.Column(db.String(20), info='婚姻状况')
    max_education = db.Column(db.String(20), info='最高学历')
    max_degree = db.Column(db.String(20), info='最高学位')
    mate_name = db.Column(db.String(256), info='配偶姓名')
    mate_card = db.Column(db.String(128), info='配偶证件号码')
    mate_card_type = db.Column(db.String(20), info='配偶证件类型')
    mate_job = db.Column(db.String(50), info='配偶工作单位')
    mate_phone = db.Column(db.String(128), info='配偶联系电话')
    telephone = db.Column(db.String(128), info='住宅电话')
    job_phone = db.Column(db.String(128), info='单位电话')
    email = db.Column(db.String(64), info='电子邮件地址')
    postal_address = db.Column(db.String(50), info='通讯地址')
    postalcode = db.Column(db.String(10), info='通讯邮政编码')
    id_card_address = db.Column(db.String(255), info='户籍地址')
    job = db.Column(db.String(20), info='职业')
    company_name = db.Column(db.String(50), info='单位名称')
    company_business = db.Column(db.String(20), info='单位所属行业')
    comment_address = db.Column(db.String(50), info='单位地址')
    comment_post = db.Column(db.String(20), info='单位邮政编码')
    job_begin_time = db.Column(db.String(20), info='本单位工作起始年份')
    job_duty = db.Column(db.String(20), info='本人职务')
    job_title = db.Column(db.String(50), info='本人职称')
    annual_income = db.Column(db.String(50), info='年收入')
    residential_address = db.Column(db.String(50), info='居住地址')
    residential_post_no = db.Column(db.String(20), info='居住地址邮政编码')
    residential_status = db.Column(db.String(10), info='居住状况')
    id_card_start_date = db.Column(db.Date)
    id_card_end_data = db.Column(db.Date)
    id_card_issue_organization = db.Column(db.String(512))

    # def __repr__(self):
    #     return 'TbReportUser:%s' % self.user_name
