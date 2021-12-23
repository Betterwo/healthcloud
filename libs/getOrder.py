# C:\Python27
# -*-coding:utf-8-*-
# @Author:huanghl
# @time :2021/12/7 10:01

import requests
import sys
import os

from configs.config import HOST
from configs.Log_config import Log

reload(sys)
sys.setdefaultencoding('utf-8')

file    =   os.path.basename(sys.argv[0])
log     =   Log(file)
logger  =   log.Logger
class GetOrder:
    def getOrder(self,inData,header,casename,PatientToken,orderNo):
        url                         = '%s/*.jsonRequest' % HOST
        header['X-Access-Token']    = PatientToken
        inData[0]                   = orderNo[1]
        payload                     = inData

        # 控制台不报异常
        requests.packages.urllib3.disable_warnings()
        try:
            resp = requests.post(url=url,json=payload,headers=header,verify=False)
            logger.info('{} request success'.format(casename))
            return resp
        except Exception as e:
            logger.error("{} request faild,throw error:{}".format(casename,e))

    def getRecipeOrder(self, inData, header, casename, PatientToken, RecipeorderNo):
        url = '%s/*.jsonRequest' % HOST
        header['X-Access-Token'] = PatientToken
        inData[0] = RecipeorderNo.json()['body']
        payload = inData

        # 控制台不报异常
        requests.packages.urllib3.disable_warnings()
        try:
            resp = requests.post(url=url, json=payload, headers=header, verify=False)
            logger.info('{} request success'.format(casename))
            return resp
        except Exception as e:
            logger.error("{} request faild,throw error:{}".format(casename, e))