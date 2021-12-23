# C:\Python27
# -*-coding:utf-8-*-
# @Author:huanghl
# @time :2021/12/7 10:49

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

class CommonPayOrder:
    def commonPayOrder(self,inData,header,casename,PatientToken,get_orderNo,get_payChannel):
        url                         = '%s/*.jsonRequest' % HOST
        header['X-Access-Token']    = PatientToken
        inData['orderNo']           = get_orderNo[1]
        inData["payChannel"]        = get_payChannel
        payload                     = []
        payload.append(inData)

        # 控制台不报异常
        requests.packages.urllib3.disable_warnings()

        try:
            resp = requests.post(url=url,json=payload,headers=header,verify=False)
            logger.info('{} request success'.format(casename))
            return resp
        except Exception as e:
            logger.error("{} request faild,throw error:{}".format(casename,e))

    def commonPayRecipeOrder(self,inData,header,casename,PatientToken,createRecipeOrder,getRecipeOrder,queryPharmacyChannelListByOrderNo):
        url                         = '%s/*.jsonRequest' % HOST

        header['X-Access-Token']    = PatientToken
        inData['orderNo']           = createRecipeOrder.json()['body']

        inData["payChannel"]        = queryPharmacyChannelListByOrderNo.json()['body'][0]['payType']#获取药店第0个支付方式
        inData['payAmount']         = getRecipeOrder.json()['body']['needPayAmount']
        inData["goodsCategory"]     = getRecipeOrder.json()['body']['goodsCategory']

        payload                     = []
        payload.append(inData)

        # 控制台不报异常
        requests.packages.urllib3.disable_warnings()
        try:
            resp = requests.post(url=url,json=payload,headers=header,verify=False)
            logger.info('{} request success'.format(casename))
            return resp
        except Exception as e:
            logger.error("{} request faild,throw error:{}".format(casename,e))



