# C:\Python27
# -*-coding:utf-8-*-
# @Author:huanghl
# @time :2021/12/2 10:50
import pytest
import pprint
import time

from libs.submitRevisitDispense import SubmitRevisitDispense
from tools.yamlControl import get_yaml_data
from tools.getPath import testCasePath

class TestSubmitRevisitDispense:
    #@pytest.mark.run(order=4)
    @pytest.mark.skip(reason='跳过test_submitRevisitDispense_001用例')
    @pytest.mark.parametrize('inData,expt,header,casename', get_yaml_data(testCasePath + '\submitRevisitDispense.yaml'))
    def test_submitRevisitDispense_001(self,inData,expt,casename,header,get_orderNo):
        resp = get_orderNo[0]
        assert resp.json()['code']  == expt['code']
if __name__ == '__main__':
    pytest.main(['test_submitRevisitDispense.py','-s'])

