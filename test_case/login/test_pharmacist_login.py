# C:\Python27
# -*-coding:utf-8-*-
# @Author:huanghl
# @time :2021/12/10 17:08

from tools.yamlControl import get_yaml_data
from libs.login import LoginRecipe
from tools.getPath import testCasePath
from configs.Log_config import Log
import pprint
import pytest
import os,sys

reload(sys)
sys.setdefaultencoding('utf-8')

file = os.path.basename(sys.argv[0])
log =   Log(file)
logger = log.Logger

class TestLoginPharmacist:
    """
    get_yaml_data()返回的数据格式是：[(请求1，期望1),(请求2，期望2)]，每个元组是一个用例
    inData：请求1，expt：期望1
    inData：请求2，expt：期望2
    """

    """
    以下：
        1、当该测试用例的业务调用在conftest中实现，且在该用例中仅调用了conftest中返回的resp响应时，该测试用例不需要参数化，因为conftest中读取了该用例的数据
        2、该用例使用参数化的原因是 获取用例中的expt期望，做断言
        3、解决该问题的方式：
            1、将该用例的expt期望值写死为固定期望200
            2、将conftest中获取到的expt与resp一起return
    """

    # case_list = get_yaml_data(testCasePath + '\RecipeLoginCase.yaml')
    # @pytest.mark.parametrize('inData,expt,header,casename',case_list)
    # def test_pharmacist_login_001(self,inData,expt,header,casename,get_pharmacist_token):
    #     resp = get_pharmacist_token[1]
    #     assert resp.json()['code'] == expt['code']


    # def test_pharmacist_login_002(self,get_pharmacist_token):
    #     resp = get_pharmacist_token[1]
    #     assert resp.json()['code'] == 200
    #
    def test_pharmacist_login_003(self,get_pharmacist_token):
        resp = get_pharmacist_token[1]
        expt = get_pharmacist_token[2]
        assert resp.json()['code'] == expt['code']


if __name__ == '__main__':
    pytest.main(['test_pharmacist_login.py','-s'])

