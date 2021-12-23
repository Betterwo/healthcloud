# C:\Python27
# -*-coding:utf-8-*-
# @Author:huanghl
# @time :2021/12/12 13:56

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
class RepiceCheck:
    def repiceCheck(self,inData,header,casename,Token,get_repiceId):
        url                 = '%s/web/recipe/checkStatus' % REPICE_HOST
        header['x-token']   = Token[0]
        if get_repiceId[1]  == None:
            logger.info("该医生没有待审核处方")
        else:
            inData['recipeId']  = get_repiceId[1]
            payload             = inData
            # 控制台不报异常
            requests.packages.urllib3.disable_warnings()
            try:
                resp = requests.put(url=url,params=payload,headers=header,verify=False)
                logger.info('{} request success'.format(casename))
                return resp
            except Exception as e:
                logger.error("{} request faild,throw error:{}".format(casename,e))