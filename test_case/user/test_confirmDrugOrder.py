# C:\Python27
# -*-coding:utf-8-*-
# @Author:huanghl
# @time :2021/12/15 10:45

import pytest
import pprint

from libs.confirmDrugOrder import ConfirmDrugOrder
from tools.yamlControl import get_yaml_data
from tools.getPath import testCasePath

class TestConfirmDrugOrder:
    #@pytest.mark.skip(reason='跳过test_confirmDrugOrder_001用例')
    @pytest.mark.parametrize('inData,expt,header,casename', get_yaml_data(testCasePath + '\confirmDrugOrder.yaml'))
    def test_confirmDrugOrder_001(self,inData,expt,header,casename,get_user_token):#,get_recipeOrderNo):
        resp = ConfirmDrugOrder().confirmDrugOrder(inData,header,casename,get_user_token)#,get_recipeOrderNo)
        assert resp.json()['code'] == expt['code']

if __name__ == '__main__':
    pytest.main(['test_confirmDrugOrder.py','-s'])