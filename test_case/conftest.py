# C:\Python27
# -*-coding:utf-8-*-
# @Author:huanghl
# @time :2021/11/30 19:35
import pytest
import time
import pprint

from libs.login import LoginUser
from libs.login import LoginDoctor
from libs.login import LoginRecipe
from tools.yamlControl import get_yaml_data
from tools.getPath import testCasePath
from libs.pageList import PageList
from libs.finish import Finish

@pytest.fixture(scope='session')
def get_user_token():
    case_list   = get_yaml_data(testCasePath + '/loginCase.yaml')
    inData      = case_list[0][0]
    expt        = case_list[0][1]
    header      = case_list[0][2]
    casename    = case_list[0][3]

    resp        = LoginUser().loginUser(inData, header,casename)
    token       = resp.json()['properties']['accessToken']
    return token

@pytest.fixture(scope='session')
def get_doctor_token():
    case_list   = get_yaml_data(testCasePath + '/doctorLoginCase.yaml')
    inData      = case_list[0][0]
    expt        = case_list[0][1]
    header      = case_list[0][2]
    casename    = case_list[0][3]

    resp        = LoginDoctor().loginDoctor(inData, header,casename)
    token       = resp.json()['properties']['accessToken']
    return token

@pytest.fixture(scope='session')
def get_pharmacist_token():
    case_list   = get_yaml_data(testCasePath + '/RecipeLoginCase.yaml')
    inData      = case_list[0][0]
    expt        = case_list[0][1]
    header      = case_list[0][2]
    casename    = case_list[0][3]

    resp                = LoginRecipe().loginRecipe(inData, header,casename)
    pharmacist_token    = resp.json()['body']['token']
    return [pharmacist_token,resp,expt]

@pytest.fixture(scope='session')
def get_drugStore_token():
    case_list   = get_yaml_data(testCasePath + '/RecipeLoginCase.yaml')
    inData      = case_list[1][0]
    expt        = case_list[1][1]
    header      = case_list[1][2]
    casename    = case_list[1][3]

    resp            = LoginRecipe().loginRecipe(inData, header,casename)
    drugStore_token = resp.json()['body']['token']
    return [drugStore_token,resp,expt]


#清理数据，获取该居民账号复诊中的订单，并且将复诊中的订单结束掉
#autouse 参数的作用是 自动执行，这个 fixture 不用主动调用，它会在相应的作用域中自动执行，并且在同一作用域中优先级最高
@pytest.fixture(scope='session',autouse=True)
def clear(get_user_token):
    data_list   = get_yaml_data(testCasePath + '/pageList.yaml')
    inData      = data_list[1][0]
    expt        = data_list[1][1]
    header      = data_list[1][2]
    casename    = data_list[1][3]
    resp        = PageList().revisitPageList(inData, header,casename,get_user_token)

    revisitList = resp.json()['body']#复诊中列表
    data_list2   = get_yaml_data(testCasePath + '/Finish.yaml')
    inData2      = data_list2[0][0]
    expt2        = data_list2[0][1]
    header2      = data_list2[0][2]
    casename2    = data_list2[0][3]

    if revisitList:
        for revisit in revisitList:
            revisitId = revisit['revisitId']
            print "正在结束复诊中的订单[%s]" % revisitId
            resp = Finish().clearFinish(inData2,expt2,header2,casename2,get_user_token,revisitId)
            print "复诊中的订单[%s]已结束" % revisitId
    else:
        print "该账号不存在复诊中的订单！"

if __name__ == '__main__':
    clear('84721f32-63aa-4e37-8d72-cb67c87086ec')




