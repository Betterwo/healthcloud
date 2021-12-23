# C:\Python27
# -*-coding:utf-8-*-
# @Author:huanghl
# @time :2021/12/14 11:04

import pytest

from libs.getOrder import GetOrder
from tools.yamlControl import get_yaml_data
from tools.getPath import testCasePath

class TestGetOrder:
    """
    get_yaml_data()返回的数据格式是：[(请求1，期望1),(请求2，期望2)]，每个元组是一个用例
    inData：请求1，expt：期望1
    inData：请求2，expt：期望2
    """
    #提交药品订单4
    @pytest.mark.run(order=6)
    #@pytest.mark.skip(reason='跳过test_getRecipeOrder_001用例')
    @pytest.mark.parametrize('inData,expt,header,casename',get_yaml_data(testCasePath+'\getRecipeOrderNo.yaml'))
    def test_getRecipeOrder_001(self,inData,expt,header,casename,getRecipeOrder):
        resp =  getRecipeOrder
        assert resp.json()['code'] == expt['code']
