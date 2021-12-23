# C:\Python27
# -*-coding:utf-8-*-
# @Author:huanghl
# @time :2021/12/12 20:50

import pytest
import pprint

from libs.findRecipeInfoByOrderNo import FindRecipeInfoByOrderNo
from tools.yamlControl import get_yaml_data
from tools.getPath import testCasePath

class TestFindRecipeInfoByOrderNo:
    #查看医嘱1
    @pytest.mark.run(order=1)
    #@pytest.mark.skip(reason='跳过test_findRecipeInfoByOrderNo_001用例')
    @pytest.mark.parametrize('inData,expt,header,casename', get_yaml_data(testCasePath + '\FindRecipeInfoByOrderNo.yaml'))
    def test_findRecipeInfoByOrderNo_001(self,inData,expt,header,casename,get_findRecipeInfoByOrderNo_info):
        resp = get_findRecipeInfoByOrderNo_info[0]
        assert resp.json()['code'] == expt['code']

if __name__ == '__main__':
    pytest.main(['test_findRecipeInfoByOrderNo.py','-s'])