#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Generate models from database
Created date: 2018/12/05
Author: Bryan Yang
update date:2020/06/15
update people:lyz
"""

import os
import pathlib

user = 'root'
password = 'root'
address = '172.17.33.65:3306'
dataBase = 'jrpt_supervise_report_test'

def gen_models(tableName):
    plants_path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

    tableNamePy = tableNameSwtich(tableName)
    tableNamePy = tableNamePy+'.py'
    model_path = os.path.join(plants_path, 'supervise\\models\\'+tableNamePy )
    db_url = "mysql://{}:{}@{}/{}?charset=utf8 --tables {} --outfile {}".format(user,password,address,dataBase,tableName,model_path)

    cmd = 'flask-sqlacodegen --flask {}'.format(db_url)

    try:
        print(cmd)
        print(model_path)

        pathlib.Path(model_path).touch()
        # output = os.popen(cmd)
        # print(output.read().decode('utf-8'))
        # with open(model_path, 'w+') as f:
        #     f.write(output)
        os.system(cmd)


        print('Generated database models successfully')

    except Exception as e:
        print(e)

def tableNameSwtich(tableName):
    tableNameList = tableName.split('_')
    newTableName = ''
    for name in tableNameList:
        name =  name.capitalize()
        newTableName = newTableName + name

    return newTableName



if __name__ == '__main__':

    tableName = 'tb_acct_mthly'

    gen_models(tableName)