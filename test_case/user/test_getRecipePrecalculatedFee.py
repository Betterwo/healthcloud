# C:\Python27
# -*-coding:utf-8-*-
# @Author:huanghl
# @time :2021/12/20 14:00

import pytest

from libs.getRecipePrecalculatedFee import GetRecipePrecalculatedFee
from tools.yamlControl import get_yaml_data
from tools.getPath import testCasePath

class TestGetRecipePrecalculatedFee:
    """
    get_yaml_data()返回的数据格式是：[(请求1，期望1),(请求2，期望2)]，每个元组是一个用例
    inData：请求1，expt：期望1
    inData：请求2，expt：期望2
    """
    #预结算药品订单
    @pytest.mark.run(order=2)
    @pytest.mark.parametrize('inData,expt,header,casename',get_yaml_data(testCasePath+'\getRecipePrecalculatedFee.yaml'))
    def test_getRecipePrecalculatedFee_001(self,inData,expt,header,casename,get_user_token,get_findRecipeInfoByOrderNo_info):
        resp = GetRecipePrecalculatedFee().getRecipePrecalculatedFee(inData,header,casename,get_user_token,get_findRecipeInfoByOrderNo_info)
        assert resp.json()['code'] == expt['code']

if __name__ == '__main__':
    pytest.main(['test_getRecipePrecalculatedFee.py','-s'])