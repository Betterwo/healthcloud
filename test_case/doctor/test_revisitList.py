# C:\Python27
# -*-coding:utf-8-*-
# @Author:huanghl
# @time :2021/12/8 19:18

import pytest
import pprint

from tools.yamlControl import get_yaml_data
from tools.getPath import testCasePath
from libs.doctorRevisitList import DoctorRevisiList

class TestDoctorRevisiList:
    @pytest.mark.run(order=1)
    @pytest.mark.parametrize('inData,expt,header,casename', get_yaml_data(testCasePath + '\doctorRevisiList.yaml'))
    def test_doctorRevisiList_001(self,inData,expt,header,casename,get_revisit_01_info):
        resp = get_revisit_01_info[0]
        assert resp.json()['code'] == expt['code']

if __name__ == '__main__':
    pytest.main(['test_revisitList.py','-s'])