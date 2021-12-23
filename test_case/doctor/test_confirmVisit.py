# C:\Python27
# -*-coding:utf-8-*-
# @Author:huanghl
# @time :2021/12/8 20:25
import pytest
from tools.yamlControl import get_yaml_data
from tools.getPath import testCasePath
from libs.doctor_confirmVisit import DoctorConfirmVisit

class TestConfirmVisit:
    @pytest.mark.run(order=2)
    @pytest.mark.parametrize('inData,expt,header,casename', get_yaml_data(testCasePath + '\doctorConfirmVisit.yaml'))
    def test_confirmVisit_001(self,inData,expt,header,casename,get_doctor_token,get_revisit_01_info):
        resp = DoctorConfirmVisit().doctorConfirmVisit(inData,expt,header,casename,get_doctor_token,get_revisit_01_info)
        assert resp.json()['code'] == expt['code']

if __name__ == '__main__':
    pytest.main(['-s'])