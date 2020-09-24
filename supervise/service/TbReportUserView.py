from random import choice

from supervise import db
from supervise.controller.commonApi import dataEncryption
from supervise.models.TbReportUser import TbReportUser
from supervise.util.generatorTestData import *


class TbReportUserView():

    def randomChoice(self,list):
        return choice(list)

    def insertUser(self,data):
        id = random_num(8)
        lineType = int(data['line_type'])
        userType = 3
        if lineType == 4:
            userType = 1
        elif lineType == '':
            userType = 2
        userName = dataEncryption(data['user_name'])
        userId = data['user_id']
        idCard = dataEncryption(id_card())
        phone = dataEncryption(random_phone_number())
        gender = self.randomChoice([0,1])
        birthDate =random_date()
        maritalStatus = '已婚'
        maxEducation = '本科'
        maxDegree = '学士学位'
        mateName = dataEncryption(random_name_female())
        mateCard = dataEncryption(id_card())
        mateCardType = '1'
        mateJob = random_company()
        matePhone = dataEncryption(random_phone_number())
        telephone = dataEncryption(random_phone_number())
        jobPhone = dataEncryption(random_phone_number())
        email = random_email()
        postalAddress = random_address()
        postalcode = random_postcode()
        idCardAddress = random_address()
        job = '自由'
        companyName = random_company()
        companyBusiness = '金融'
        commentAddress = random_address()
        commentPost = random_postcode()
        jobBeginTime = '20190401'
        jobDuty = '测试'
        jobTitle = '测试'
        annualIncome  = '10000'
        residentialAddress = random_address()
        residentialPostNo = random_postcode()
        residentialStatus = '舒适'
        idCardStartDate = '2012-01-01'
        idCardEndData = '2022-01-01'
        idCardIssueOrganization = '中华人民共和国'

        tbReportUser = TbReportUser(id=id,line_type=lineType,user_type=userType,user_id=userId,user_name=userName,id_card=idCard,phone=phone,gender=gender,birth_date=birthDate,marital_status=maritalStatus,
                                    max_education=maxEducation,max_degree=maxDegree,mate_name=mateName,mate_card=mateCard,mate_card_type=mateCardType,mate_job=mateJob,mate_phone=matePhone,telephone=telephone,
                                    job_phone=jobPhone,email=email,postal_address=postalAddress,postalcode=postalcode,id_card_address=idCardAddress,job=job,company_name=companyName,company_business=companyBusiness,
                                    comment_address=commentAddress,comment_post=commentPost,job_begin_time=jobBeginTime,job_duty=jobDuty,job_title=jobTitle,annual_income=annualIncome,residential_address=residentialAddress,
                                    residential_post_no=residentialPostNo,residential_status=residentialStatus,id_card_start_date=idCardStartDate,id_card_end_data=idCardEndData,id_card_issue_organization=idCardIssueOrganization)

        db.session.add(tbReportUser)
        db.session.commit()




