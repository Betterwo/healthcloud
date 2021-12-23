# C:\Python27
# -*-coding:utf-8-*-
# @Author:huanghl
# @time :2021/12/7 10:49

import pytest
import time

from tools.yamlControl import get_yaml_data
from tools.getPath import testCasePath
from libs.commonPayOrder import CommonPayOrder

class TestcommonPayOrder:
    #@pytest.mark.run(order=5)
    @pytest.mark.skip(reason='跳过test_commonPayOrder_001用例')
    @pytest.mark.parametrize('inData,expt,header,casename', get_yaml_data(testCasePath + '\commonPayOrder.yaml'))
    def test_commonPayOrder_001(self,inData,expt,header,casename,get_user_token,get_orderNo,get_payChannel):#get_orderNo
        time.sleep(1)
        resp = CommonPayOrder().commonPayOrder(inData,header,casename,get_user_token,get_orderNo,get_payChannel)
        print resp.text
        assert resp.json()['code'] == expt['code']

    #药品订单支付5
    @pytest.mark.run(order=7)
    #@pytest.mark.skip(reason='跳过test_commonRecipePayOrder_001用例')
    @pytest.mark.parametrize('inData,expt,header,casename', get_yaml_data(testCasePath + '\commonPayOrder.yaml'))
    def test_commonRecipePayOrder_001(self,inData,expt,header,casename,get_user_token,createRecipeOrder,getRecipeOrder,queryPharmacyChannelListByOrderNo):
        resp = CommonPayOrder().commonPayRecipeOrder(inData,header,casename,get_user_token,createRecipeOrder,getRecipeOrder,queryPharmacyChannelListByOrderNo)
        assert resp.json()['code'] == expt['code']


if __name__ == '__main__':
    pytest.main(['test_commonPayOrder.py','-s'])