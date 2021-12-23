# C:\Python27
# -*-coding:utf-8-*-
# @Author:huanghl
# @time :2021/12/7 13:55

import pytest

from libs.pageList import PageList
from tools.yamlControl import get_yaml_data
from tools.getPath import testCasePath

class TestPageList:
    """
    get_yaml_data()返回的数据格式是：[(请求1，期望1),(请求2，期望2)]，每个元组是一个用例
    inData：请求1，expt：期望1
    inData：请求2，expt：期望2
    """

    @pytest.mark.skip(reason='跳过一个方法或一个测试用例')
    @pytest.mark.parametrize('inData,expt,header,casename',get_yaml_data(testCasePath+'\pageList.yaml'))
    def test_pageList_001(self,inData,expt,header,casename,get_user_token):
        resp = PageList().pageList(inData,header,casename,get_user_token)
        assert resp.json()['code'] == expt['code']