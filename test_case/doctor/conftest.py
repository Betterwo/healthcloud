# C:\Python27
# -*-coding:utf-8-*-
# @Author:huanghl
# @time :2021/12/8 19:28
import pytest
import pprint
import json

from tools.yamlControl import get_yaml_data
from tools.getPath import testCasePath
from libs.doctorRevisitList import DoctorRevisiList

#待接诊
@pytest.fixture(scope='session')
def get_revisit_01_info(get_doctor_token):
    inData      = get_yaml_data(testCasePath + '/doctorRevisiList.yaml')[0][0]
    expt        = get_yaml_data(testCasePath + '/doctorRevisiList.yaml')[0][1]
    header      = get_yaml_data(testCasePath + '/doctorRevisiList.yaml')[0][2]
    casename    = get_yaml_data(testCasePath + '/doctorRevisiList.yaml')[0][3]
    resp    = DoctorRevisiList().doctorRevisiList(inData, header,casename,get_doctor_token)

    revisitId = resp.json()['body'][0]['revisitId']
    return [resp,revisitId]






