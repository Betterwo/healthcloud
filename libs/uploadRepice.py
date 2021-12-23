# C:\Python27
# -*-coding:utf-8-*-
# @Author:huanghl
# @time :2021/12/9 10:45
import requests,sys,os
from configs.config import HOST
from configs.Log_config import Log
reload(sys)
sys.setdefaultencoding('utf-8')

file    =   os.path.basename(sys.argv[0])
log     =   Log(file)
logger  =   log.Logger

class UploadRepice:
    def uploadRepice(self,inData,expt,header,casename,DoctorToken,get_revisit_01_info):
        url                         = '%s/*.jsonRequest' % HOST
        header['X-Access-Token']    =   DoctorToken
        payload                     = []
        data_dict                   = {}
        drugs                       = []
        mzDiagnoses                 = []

        data_yaml                   = inData
        drugs.append(data_yaml['drugs'])
        mzDiagnoses.append(data_yaml['mzDiagnoses'])

        data_dict['drugs']          = drugs
        data_dict['mzDiagnoses']    = mzDiagnoses
        data_dict['revisitId']      = get_revisit_01_info[1]
        data_dict['recipeTypeCode'] = data_yaml['recipeTypeCode']

        payload.append(data_dict)
        # 控制台不报异常
        requests.packages.urllib3.disable_warnings()
        try:
            resp = requests.post(url=url,json=payload,headers=header,verify=False)
            logger.info('{} request success'.format(casename))
            return resp
        except Exception as e:
            logger.error("{} request faild,throw error:{}".format(casename,e))