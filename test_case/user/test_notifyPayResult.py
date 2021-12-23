# C:\Python27
# -*-coding:utf-8-*-
# @Author:huanghl
# @time :2021/12/7 11:25

import pytest
import time

from libs.getOrder import GetOrder
from tools.yamlControl import get_yaml_data
from tools.getPath import testCasePath
from libs.notifyPayResult import NotifyPayResult

class TestNotifyPayResult:
    """
    get_yaml_data()返回的数据格式是：[(请求1，期望1),(请求2，期望2)]，每个元组是一个用例
    inData：请求1，expt：期望1
    inData：请求2，expt：期望2
    """

    @pytest.mark.skip(reason='跳过test_notifyPayResult_001用例')
    #@pytest.mark.run(order=6)
    @pytest.mark.parametrize('inData,expt,header,casename',get_yaml_data(testCasePath+'\NotifyPayResult.yaml'))
    def test_notifyPayResult_001(self,inData,expt,header,casename,get_user_token,get_orderNo):
        time.sleep(2)
        resp = NotifyPayResult().notifyPayResult(inData,header,casename,get_user_token,get_orderNo)
        assert resp.json()['code'] == expt['code']

    #通过第三方查询药品订单支付结果6    0: 交易失败, 3: 交易成功,  2: 获取交易结果出错, 状态未知.
    #@pytest.mark.skip(reason='跳过test_RecipeNotifyPayResult_001用例')
    @pytest.mark.run(order=8)
    @pytest.mark.parametrize('inData,expt,header,casename', get_yaml_data(testCasePath + '\NotifyPayResult.yaml'))
    def test_RecipeNotifyPayResult_001(self, inData, expt, header, casename, get_user_token,createRecipeOrder):
        resp = NotifyPayResult().notifyPayResult(inData, header, casename, get_user_token,createRecipeOrder)
        assert resp.json()['code'] == expt['code']

if __name__ == '__main__':
    pytest.main(['test_notifyPayResult.py','-s'])