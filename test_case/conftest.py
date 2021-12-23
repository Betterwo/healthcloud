# C:\Python27
# -*-coding:utf-8-*-
# @Author:huanghl
# @time :2021/11/30 19:35
import pytest
import time

from libs.login import LoginUser
from libs.login import LoginDoctor
from libs.login import LoginRecipe
from tools.yamlControl import get_yaml_data
from tools.getPath import testCasePath

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