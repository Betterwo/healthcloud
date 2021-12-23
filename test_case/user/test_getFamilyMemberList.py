# C:\Python27
# -*-coding:utf-8-*-
# @Author:huanghl
# @time :2021/12/2 14:07

import pytest
import pprint
import time

from libs.getFamilyMemberList import GetFamilyMemberList
from tools.yamlControl import get_yaml_data
from tools.getPath import testCasePath

class TestGetFamilyMemberList:
    #@pytest.mark.run(order=2)
    @pytest.mark.skip(reason='跳过test_getFamilyMemberList_001用例')
    @pytest.mark.parametrize('inData,expt,header,casename', get_yaml_data(testCasePath + '\getFamilyMemberList.yaml'))
    def test_getFamilyMemberList_001(self,inData,expt,header,casename,get_user_token):
        time.sleep(1)
        resp = GetFamilyMemberList().getFamilyMemberList(inData,header,casename,get_user_token)
        assert resp.json()['code'] == expt['code']

if __name__ == '__main__':
    pytest.main(['test_getFamilyMemberList.py','-s'])