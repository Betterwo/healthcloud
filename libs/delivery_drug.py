# C:\Python27
# -*-coding:utf-8-*-
# @Author:huanghl
# @time :2021/12/14 19:30
import requests
import sys
import os

from configs.config import REPICE_HOST
from configs.Log_config import Log

reload(sys)
sys.setdefaultencoding('utf-8')

file    =   os.path.basename(sys.argv[0])
log     =   Log(file)
logger  =   log.Logger

class DeliveryDrug:
    def deliveryDrug(self,inData,header,casename,drugStore_token,get_durgOrderInfo,get_YS,get_company):
        url                         =   '%s/web/recipeOrder/delivery' % REPICE_HOST
        header['x-token']           =   drugStore_token[0]
        inData['orderId']           =   get_durgOrderInfo
        inData['personId']          =   get_YS[0]
        inData['personIddsispense'] =   get_YS[0]
        inData['personIdrecheck']   =   get_YS[1]
        inData['transportId']       =   get_company['transportId']
        payload                     =   inData

        print '##################',payload
        # 控制台不报异常
        requests.packages.urllib3.disable_warnings()
        try:
            resp = requests.put(url=url,data=payload,headers=header,verify=False)
            logger.info('{} request success'.format(casename))
            return resp
        except Exception as e:
            logger.error("{} request faild,throw error:{}".format(casename,e))