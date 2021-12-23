# C:\Python27
# -*-coding:utf-8-*-
# @Author:huanghl
# @time :2021/12/1 15:18

import pytest
import pprint
import time
from libs.getIhDoctorInfo import GetIhDoctorInfo
from tools.yamlControl import get_yaml_data
from tools.getPath import testCasePath

class TestGetIhDoctorInfo:
    #@pytest.mark.run(order=3)
    @pytest.mark.skip(reason='跳过test_getIhDoctorInfo_001用例')
    @pytest.mark.parametrize('inData,expt,header,casename', get_yaml_data(testCasePath + '\getIhDoctorInfo.yaml'))
    def test_getIhDoctorInfo_001(self,inData,expt,header,casename,get_user_token,get_doctor_info):
        resp = get_doctor_info[13]
        assert resp.json()['code'] == expt['code']

if __name__ == '__main__':
    pytest.main(['test_getIhDoctorInfo.py','-s'])


