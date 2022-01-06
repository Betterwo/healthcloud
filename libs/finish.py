# C:\Python27
# -*-coding:utf-8-*-
# @Author:huanghl
# @time :2021/12/15 11:03

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

class Finish:
    def finish(self,inData,expt,header,casename,UserToken,revisitId):
        url                         =   '%s/*.jsonRequest' % HOST
        header['X-Access-Token']    =   UserToken
        inData[0]                   =   revisitId[1]#复诊编号revisitId,而不是orderNo
        payload                     =   inData

        # 控制台不报异常
        requests.packages.urllib3.disable_warnings()
        try:
            resp = requests.post(url=url,json=payload,headers=header,verify=False)
            logger.info('{} request success'.format(casename))
            return resp
        except Exception as e:
            logger.error("{} request faild,throw error:{}".format(casename,e))

    def clearFinish(self,inData,expt,header,casename,UserToken,revisitId):
        url                         =   '%s/*.jsonRequest' % HOST
        header['X-Access-Token']    =   UserToken
        inData[0]                   =   revisitId
        payload                     =   inData

        # 控制台不报异常
        requests.packages.urllib3.disable_warnings()
        try:
            resp = requests.post(url=url,json=payload,headers=header,verify=False)
            logger.info('{} request success'.format(casename))
            return resp
        except Exception as e:
            logger.error("{} request faild,throw  error:{}".format(casename,e))