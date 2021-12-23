# C:\Python27
# -*-coding:utf-8-*-
# @Author:huanghl
# @time :2021/11/17 11:08

import requests
import time
import os
import sys

from configs.config import HOST,REPICE_HOST
from tools.md5Encrypt import get_MD5
from configs.Log_config import Log

reload(sys)
sys.setdefaultencoding('utf-8')

file    =   os.path.basename(sys.argv[0])
log     =   Log(file)
logger  =   log.Logger

class LoginUser:
    def loginUser(self,inData,header,casename):
        """
        :param inData: 入参数据
        :return: 返回token或者响应数据
        """
        url             = '%s/logon/login' % HOST
        inData['pwd']   = get_MD5(inData['pwd'])
        payload         = inData
        # 控制台不报异常
        requests.packages.urllib3.disable_warnings()
        try:
            resp = requests.post(url=url,json=payload,headers=header,verify=False)
            logger.info('{} request success'.format(casename))
            return resp
        except Exception as e:
            logger.error("{} request faild,throw error:{}".format(casename,e))


class LoginDoctor:
    def loginDoctor(self,inData,header,casename):
        """
        :param inData: 入参数据
        :return: 返回token或者响应数据
        """
        url             = '%s/logon/login' % HOST
        inData['pwd']   = get_MD5(inData['pwd'])
        payload         = inData
        # 控制台不报异常
        requests.packages.urllib3.disable_warnings()
        time.sleep(1)

        try:
            resp = requests.post(url=url,json=payload,headers=header,verify=False)
            logger.info('{} request success'.format(casename))
            return resp
        except Exception as e:
            logger.error("{} request faild,throw error:{}".format(casename,e))

class LoginRecipe:
    def loginRecipe(self,inData,header,casename):
        """
        :param inData: 入参数据
        :return: 返回token或者响应数据
        """
        url                 = '%s/login/web' % REPICE_HOST
        inData['password']  = get_MD5(inData['password'])
        payload             = inData
        # 控制台不报异常
        requests.packages.urllib3.disable_warnings()
        try:
            resp = requests.post(url=url,params=payload,headers=header,verify=False)
            logger.info('{} request success'.format(casename))
            return resp
        except Exception as e:
            logger.error("{} request faild,throw error:{}".format(casename,e))

