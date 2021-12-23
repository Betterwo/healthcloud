# C:\Python27
# -*-coding:utf-8-*-
# @Author:huanghl
# @time :2021/12/20 13:49

#药品订单预结算接口

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

class GetRecipePrecalculatedFee:
    def getRecipePrecalculatedFee(self,inData,header,casename,PatientToken,get_findRecipeInfoByOrderNo_info):
        url                         = '%s/*.jsonRequest' % HOST
        recipeId                    = []
        recipeId.append(get_findRecipeInfoByOrderNo_info[1])
        header['X-Access-Token']    = PatientToken
        inData[0]                   = get_findRecipeInfoByOrderNo_info[2]
        inData[1]                   = recipeId
        payload                     = inData        #[286861, [174511]]


        # 控制台不报异常
        requests.packages.urllib3.disable_warnings()
        try:
            resp = requests.post(url=url,json=payload,headers=header,verify=False)
            logger.info('{} request success'.format(casename))
            return resp
        except Exception as e:
            logger.error("{} request faild,throw error:{}".format(casename,e))