# C:\Python27
# -*-coding:utf-8-*-
# @Author:huanghl
# @time :2021/12/20 16:32

import requests
import sys
import os

from configs.config import HOST
from configs.config import REPICE_HOST
from configs.Log_config import Log

reload(sys)
sys.setdefaultencoding('utf-8')

file    =   os.path.basename(sys.argv[0])
log     =   Log(file)
logger  =   log.Logger

class QueryPharmacyChannelListByOrderNo:
    def queryPharmacyChannelListByOrderNo(self,inData, header,casename,Token,recipeOrderNo):
        url                         = '%s/*.jsonRequest' % HOST
        header['X-Access-Token']    = Token

        inData[0]                   = recipeOrderNo.json()['body']#药品orderNo
        payload                     = inData

        print payload
        print header

        # 控制台不报异常
        requests.packages.urllib3.disable_warnings()
        try:
            resp = requests.post(url=url,json=payload,headers=header,verify=False)
            logger.info('{} request success'.format(casename))
            return resp
        except Exception as e:
            logger.error("{} request faild,throw error:{}".format(casename,e))