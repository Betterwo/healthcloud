# C:\Python27
# -*-coding:utf-8-*-
# @Author:huanghl
# @time :2021/11/17 20:26
from tools.yamlControl import get_yaml_data
from libs.login import LoginDoctor
from tools.getPath import testCasePath
from configs.Log_config import Log
import pprint
import pytest
import os
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

file    =   os.path.basename(sys.argv[0])
log     =   Log(file)
logger  =   log.Logger

class TestLoginDoctor:
    """
    get_yaml_data()返回的数据格式是：[(请求1，期望1),(请求2，期望2)]，每个元组是一个用例
    inData：请求1，expt：期望1
    inData：请求2，expt：期望2
    """
    case_list = get_yaml_data(testCasePath + '\doctorLoginCase.yaml')
    @pytest.mark.parametrize('inData,expt,header,casename',case_list)
    def test_doctor_login_001(self,inData,expt,header,casename):
        resp = LoginDoctor().loginDoctor(inData,header,casename)
        assert resp.json()['code'] == expt['code']


if __name__ == '__main__':
    pytest.main(['test_doctor_login.py','-s'])

