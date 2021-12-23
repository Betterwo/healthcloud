# C:\Python27
# -*-coding:utf-8-*-
# @Author:huanghl
# @time :2021/12/9 10:23

import pytest
import pprint

from tools.yamlControl import get_yaml_data
from tools.getPath import testCasePath
from libs.uploadRepice import UploadRepice
class TestUploadRepice:
    @pytest.mark.parametrize('inData,expt,header,casename', get_yaml_data(testCasePath + '\uploadRepice.yaml'))
    @pytest.mark.run(order=3)
    def test_uploadRepice_001(self,inData,expt,header,casename,get_doctor_token,get_revisit_01_info):
        resp = UploadRepice().uploadRepice(inData,expt,header,casename,get_doctor_token,get_revisit_01_info)
        assert resp.json()['code'] == expt['code']

if __name__ == '__main__':
    pytest.main(['test_uploadRepice.py','-s'])