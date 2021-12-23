# C:\Python27
# -*-coding:utf-8-*-
# @Author:huanghl
# @time :2021/12/14 17:54
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

class TestLoginDrugStore:
    def test_drugStore_login_001(self,get_drugStore_token):
        resp = get_drugStore_token[1]
        expt = get_drugStore_token[2]
        assert resp.json()['code'] == expt['code']
