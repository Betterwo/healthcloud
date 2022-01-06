# C:\Python27
# -*-coding:utf-8-*-
# @Author:huanghl
# @time :2021/12/15 11:02
import pytest
import pprint

from libs.finish import Finish
from tools.yamlControl import get_yaml_data
from tools.getPath import testCasePath

class TestFinish:
    @pytest.mark.skip(reason='跳过test_Finish_001用例')
    @pytest.mark.parametrize('inData,expt,header,casename', get_yaml_data(testCasePath + '\Finish.yaml'))
    def test_Finish_001(self,inData,expt,header,casename,get_orderNo):
        resp = Finish().finish(inData,header,casename,get_orderNo)
        assert resp.json()['code'] == expt['code']

if __name__ == '__main__':
    pytest.main(['test_finish.py' ,'-s'])