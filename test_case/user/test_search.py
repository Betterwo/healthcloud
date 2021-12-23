# C:\Python27
# -*-coding:utf-8-*-
# @Author:huanghl
# @time :2021/11/30 16:23
import pytest
import pprint
from libs.search import Search
from tools.yamlControl import get_yaml_data
from tools.getPath import testCasePath

class TestSearch:
    """
    get_yaml_data()返回的数据格式是：[(请求1，期望1),(请求2，期望2)]，每个元组是一个用例
    inData：请求1，expt：期望1
    inData：请求2，expt：期望2
    """

    #@pytest.mark.run(order=1)
    @pytest.mark.skip(reason='跳过test_getIhDoctorInfo_001用例')
    @pytest.mark.parametrize('inData,expt,header,casename',get_yaml_data(testCasePath+'\search.yaml'))
    def test_search_001(self,inData,expt,header,casename,get_user_token):
        resp = Search().search(inData,header,casename,get_user_token)
        assert resp.json()['code'] == expt['code']

if __name__ == '__main__':
    #pytest.main(['test_search.py','-s'])
    pytest.main(['-s'])
