# C:\Python27
# -*-coding:utf-8-*-
# @Author:huanghl
# @time :2021/12/1 14:33

import requests
import pprint
import sys
import os

from configs.config import HOST
from configs.Log_config import Log

reload(sys)
sys.setdefaultencoding('utf-8')

file    =   os.path.basename(sys.argv[0])
log     =   Log(file)
logger  =   log.Logger

class SubmitRevisitDispense:
    def submitRevisitDispense(self,inData,header,casename,PatientToken):
        url                         = '%s/common/revisit/submitRevisitDispense' % HOST
        header['X-Access-Token']    = PatientToken
        """
        将数据处理放在业务层：只能满足正常响应的用例，当需要测试异常时，该逻辑不满足要求（将异常用例数据会更新到正常）
        将数据处理放在用例层：在测试类中分为不同的多个测试用例，测试数据用切片的方式实现
        """
        #控制台不报异常
        requests.packages.urllib3.disable_warnings()
        try:
            resp = requests.post(url=url, data=inData, headers=header, verify=False)
            logger.info('{} request success'.format(casename))
            return resp
        except Exception as e:
            logger.error("{} request faild,throw error:{}".format(casename, e))