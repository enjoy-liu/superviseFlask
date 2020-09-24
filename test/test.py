import os
# output1 = os.popen('flask-sqlacodegen --flask mysql://root:root@172.17.33.65:3306/jrpt_supervise_report_lyz?charset=utf8 --tables tb_report_loan_plan')
# o1=str(output1.read())
# print(output1)
import pathlib

model_path =r'E:\study\flask\superviseFlask\superviseFlask\models\TbReportLoanPlan.py'
pathlib.Path(model_path).touch()