# C:\Python27
# -*-coding:utf-8-*-
# @Author:huanghl
# @time :2021/12/12 13:58

# C:\Python27
# -*-coding:utf-8-*-
# @Author:huanghl
# @time :2021/12/12 13:16
import pytest

from libs.repiceCheck import RepiceCheck
from tools.yamlControl import get_yaml_data
from tools.getPath import testCasePath

class TestRepicePageList:
    """
    get_yaml_data()返回的数据格式是：[(请求1，期望1),(请求2，期望2)]，每个元组是一个用例
    inData：请求1，expt：期望1
    inData：请求2，expt：期望2
    """
    @pytest.mark.run(order=2)
    @pytest.mark.parametrize('inData,expt,header,casename',get_yaml_data(testCasePath+'\RepiceCheckStatus.yaml'))
    def test_repicePageList_001(self,inData,expt,header,casename,get_pharmacist_token,get_repiceId):
        resp = RepiceCheck().repiceCheck(inData,header,casename,get_pharmacist_token,get_repiceId)
        assert resp.json()['code'] == expt['code']

if __name__ == '__main__':
    pytest.main(['test_repiceCheck.py','-s'])