# C:\Python27
# -*-coding:utf-8-*-
# @Author:huanghl
# @time :2021/12/7 13:50

import requests
import sys
import os
import pprint

from configs.config import HOST
from configs.config import REPICE_HOST
from configs.Log_config import Log

reload(sys)
sys.setdefaultencoding('utf-8')

file    =   os.path.basename(sys.argv[0])
log     =   Log(file)
logger  =   log.Logger

class PageList:
    def pageList(self,inData,header,casename,Token):
        url                         = '%s/*.jsonRequest' % HOST
        header['X-Access-Token']    = Token
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

    def revisitPageList(self,inData,header,casename,Token):
        url                         = '%s/*.jsonRequest' % HOST
        header['X-Access-Token']    = Token
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

    #待审核的处方列表
    def repicePageList(self,inData,header,casename,Token):
        url = '%s/web/recipe/pageList' % REPICE_HOST
        header['x-token'] = Token[0]
        payload = inData


        # 控制台不报异常
        requests.packages.urllib3.disable_warnings()
        try:
            resp = requests.post(url=url,json=payload,headers=header,verify=False)
            logger.info('{} request success'.format(casename))
            return resp
        except Exception as e:
            logger.error("{} request faild,throw error:{}".format(casename,e))

    #待处理的药品列表
    def DrugOrderPageList(self,inData,header,casename,Token):
        url = '%s/web/recipeOrder/pageList' % REPICE_HOST
        header['x-token'] = Token[0]
        payload = inData
        # 控制台不报异常
        #payload = {"orderNo":"","orderIdOutter":"","pageNo":1,"pageSize":10,"deliveryType":"","orderStatus":"04","deliveryStatus":"","getDrugCode":"","voiceNeed":"","voiceExit":"","payType":"","startTime":"2021-11-22 00:00:00","endTime":"2021-12-21 23:59:59","mchId":"","storeId":"","orderType":"","userName":"林靖凯","testFlag":"","drugStoreMchId":92,"status":1}
        requests.packages.urllib3.disable_warnings()
        try:
            resp = requests.post(url=url,json =payload,headers=header,verify=False)
            logger.info('{} request success'.format(casename))
            return resp
        except Exception as e:
            logger.error("{} request faild,throw error:{}".format(casename,e))
