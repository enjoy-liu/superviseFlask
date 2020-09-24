
from supervise.util.xulie import *
from supervise import db
from supervise.models.TbAcctMthly import TbAcctMthly


class TbAcctMthlyView():

    def queryMthly(self,data):
        query_list = []
        page = int(data['page'])
        limit = int(data['limit'])
        pages = (page - 1) * limit
        acctNoWhere = ''
        userIdWhere = ''
        if  'acctNo' in data.keys() and data['acctNo'] != '':
            query_list.append(TbAcctMthly.acct_no == data['acctNo'])
            acctNoWhere = "and acct_no='{}'".format(data['acctNo'])
        if 'userId' in data.keys() and data['userId'] != '':
            query_list.append(TbAcctMthly.cust_id == data['userId'])
            userIdWhere = "and cust_id='{}'".format(data['userId'])
        data = {}
        data['code']=0
        data['msg']=""
        sql = "select count(0) from tb_acct_mthly where 1 = 1 {} {} limit 1".format(acctNoWhere,userIdWhere)
        print(sql)
        counts = db.session.execute(sql)
        #获取数据的个数，分页数据使用
        count = counts.fetchall()[0][0]
        # count = 1
        # if isinstance(counts, list):
        #     count= len(counts)
        #分页并按照每页显示数据的个数查询数据
        result = TbAcctMthly.query.filter(*query_list).limit(limit).offset(pages).all()

        resultList = []
        #将查询结果转换成json
        if isinstance(result,list):
            for x in result:
                a = x.to_json()
                resultList.append(a)
        else:
            resultList.append(result.to_json())
        data['count'] = count
        data['data'] = resultList
        resultJson = json.dumps(data,cls=ComplexEncoder,ensure_ascii=False)

        return resultJson