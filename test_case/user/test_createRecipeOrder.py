# C:\Python27
# -*-coding:utf-8-*-
# @Author:huanghl
# @time :2021/12/13 18:05
import pytest

from tools.yamlControl import get_yaml_data
from tools.getPath import testCasePath
from libs.createRecipeOrder import CreateRecipeOrder

class TestCreateRecipeOrder:
    #创建药品订单3
    @pytest.mark.run(order=4)
    #@pytest.mark.skip(reason='test_createRecipeOrder_001')
    @pytest.mark.parametrize('inData,expt,header,casename', get_yaml_data(testCasePath + '\createRecipeOrder.yaml'))
    def test_createRecipeOrder_001(self,inData,expt,header,casename,createRecipeOrder):
        resp = createRecipeOrder
        assert resp.json()['code'] == expt['code']

if __name__ == '__main__':
    pytest.main(['test_createRecipeOrder.py','-s'])