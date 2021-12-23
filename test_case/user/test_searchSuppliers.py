# C:\Python27
# -*-coding:utf-8-*-
# @Author:huanghl
# @time :2021/12/13 17:03
import pytest
import pprint

from libs.getOrder import GetOrder
from tools.yamlControl import get_yaml_data
from tools.getPath import testCasePath
from libs.searchSuppliers import SearchSuppliers

class TestSearchSuppliers:
    """
    get_yaml_data()返回的数据格式是：[(请求1，期望1),(请求2，期望2)]，每个元组是一个用例
    inData：请求1，expt：期望1
    inData：请求2，expt：期望2
    """
    #药店查询2
    @pytest.mark.run(order=3)
    #@pytest.mark.skip(reason='跳过test_searchSuppliers_001用例')
    @pytest.mark.parametrize('inData,expt,header,casename',get_yaml_data(testCasePath+'\searchSuppliers.yaml'))
    def test_searchSuppliers_001(self,inData,expt,header,casename,get_user_token,get_findRecipeInfoByOrderNo_info):
        resp = SearchSuppliers().searchSuppliers(inData,header,casename,get_user_token,get_findRecipeInfoByOrderNo_info)
        assert resp.json()['code'] == expt['code']

if __name__ == '__main__':
    pytest.main(['test_searchSuppliers.py','-s'])