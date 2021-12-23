# C:\Python27
# -*-coding:utf-8-*-
# @Author:huanghl
# @time :2021/12/12 18:52

import pytest
import os
import sys
import requests
import pprint


from tools.yamlControl import get_yaml_data
from tools.getPath import testCasePath
from libs.pageList import PageList
from configs.Log_config import Log
from configs.config import REPICE_HOST

reload(sys)
sys.setdefaultencoding('utf-8')

file    =   os.path.basename(sys.argv[0])
log     =   Log(file)
logger  =   log.Logger

@pytest.fixture(scope='session')
def get_repiceId(get_pharmacist_token):
    inData      = get_yaml_data(testCasePath + '/RepiceList.yaml')[0][0]
    expt        = get_yaml_data(testCasePath + '/RepiceList.yaml')[0][1]
    header      = get_yaml_data(testCasePath + '/RepiceList.yaml')[0][2]
    casename    = get_yaml_data(testCasePath + '/RepiceList.yaml')[0][3]

    resp        = PageList().repicePageList(inData, header,casename,get_pharmacist_token)
    recipe_list = resp.json()['body']['data']#待审核状态的处方列表

    if recipe_list :
        #获取了该医生未审核处方列表的第一个，而不是指定处方编号或者指定复诊id
        repiceId = resp.json()['body']['data'][0]['recipeId']#带审核处方列表中的第0个处方id
        return [resp,repiceId]
    else:
        print "该医生没有待审核的处方"
        repiceId = None
        return [resp,repiceId]

@pytest.fixture(scope='session')
def get_durgOrderInfo(get_drugStore_token):
    inData      = get_yaml_data(testCasePath + '/drugOrderList.yaml')[0][0]
    expt        = get_yaml_data(testCasePath + '/drugOrderList.yaml')[0][1]
    header      = get_yaml_data(testCasePath + '/drugOrderList.yaml')[0][2]
    casename    = get_yaml_data(testCasePath + '/drugOrderList.yaml')[0][3]

    print inData

    resp        = PageList().DrugOrderPageList(inData, header,casename,get_drugStore_token)
    orderId = resp.json()['body']['data'][0]['orderId']#发药、查询药师所需

    return orderId


@pytest.fixture(scope='session')
def get_company(get_drugStore_token):
    url = '%s/web/transport/company' % REPICE_HOST
    header = {
        "product-code":"pc"
    }
    header['x-token'] = get_drugStore_token[0]

    resp = requests.get(url=url,headers = header)
    company_list = resp.json()['body']

    for company in company_list:
        if company['transportId'] == 643:
            return company

@pytest.fixture(scope='session')
def get_YS(get_drugStore_token,get_durgOrderInfo):
    url = '%s/web/person/OrderRecipePersons/%s' % (REPICE_HOST,get_durgOrderInfo)
    header = {
        "product-code":"pc"
    }
    header['x-token'] = get_drugStore_token[0]
    param_TJ = {"pharmacyType":3}
    param_HD = {"pharmacyType":4}

    resp_TJ = requests.get(url=url,params = param_TJ, headers = header)
    resp_HD = requests.get(url=url,params = param_HD, headers = header)

    if resp_TJ.json()['body']:
        TJ_personId = resp_TJ.json()['body'][0]['personId']
    else:
        print "不存在调剂药师"
    if resp_HD.json()['body']:
        HD_personId = resp_HD.json()['body'][0]['personId']
    else:
        print "不存在核对药师"
    return [TJ_personId,HD_personId]
