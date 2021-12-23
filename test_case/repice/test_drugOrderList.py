# C:\Python27
# -*-coding:utf-8-*-
# @Author:huanghl
# @time :2021/12/14 18:25

import pytest

from libs.pageList import PageList
from tools.yamlControl import get_yaml_data
from tools.getPath import testCasePath

class TestRepicePageList:
    """
    get_yaml_data()返回的数据格式是：[(请求1，期望1),(请求2，期望2)]，每个元组是一个用例
    inData：请求1，expt：期望1
    inData：请求2，expt：期望2
    """
    #@pytest.mark.skip(reason='跳过test_repicePageList_001用例')
    @pytest.mark.parametrize('inData,expt,header,casename',get_yaml_data(testCasePath+'\drugOrderList.yaml'))
    def test_repicePageList_001(self,inData,expt,header,casename,get_drugStore_token,get_durgOrderInfo):
        resp = get_durgOrderInfo
        assert resp.json()['code'] == expt['code']

if __name__ == '__main__':
    pytest.main(['test_drugOrderList.py','-s'])



