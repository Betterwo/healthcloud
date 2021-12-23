# C:\Python27
# -*-coding:utf-8-*-
# @Author:huanghl
# @time :2021/12/1 11:14
import pytest
import os
import sys
import pprint
import time

from tools.yamlControl import get_yaml_data
from tools.getPath import testCasePath
from libs.search import Search
from libs.getIhDoctorInfo import GetIhDoctorInfo
from libs.getPayChannel import GetPayChennel
from libs.submitRevisitDispense import SubmitRevisitDispense
from libs.findRecipeInfoByOrderNo import FindRecipeInfoByOrderNo
from libs.createRecipeOrder import CreateRecipeOrder
from libs.getPayChannel import GetPayChennel
from libs.getOrder import GetOrder
from libs.searchSuppliers import SearchSuppliers
from libs.queryPharmacyChannelListByOrderNo import QueryPharmacyChannelListByOrderNo
from libs.getRecipePrecalculatedFee import GetRecipePrecalculatedFee
from libs.pageList import PageList
from configs.Log_config import Log

reload(sys)
sys.setdefaultencoding('utf-8')

file    =   os.path.basename(sys.argv[0])
log     =   Log(file)
logger  =   log.Logger

@pytest.fixture(scope='session')
def get_doctor_id(get_user_token):
    data_list   = get_yaml_data(testCasePath + '/search.yaml')
    inData      = data_list[0][0]
    expt        = data_list[0][1]
    header      = data_list[0][2]
    casename    = data_list[0][3]

    resp        = Search().search(inData, header,casename,get_user_token)
    id          = resp.json()['body'][0]['list'][0]['id']
    return id

@pytest.fixture(scope='session')
def get_doctor_info(get_user_token,get_doctor_id):
    data_list   = get_yaml_data(testCasePath + '/getIhDoctorInfo.yaml')
    inData      = data_list[0][0]
    expt        = data_list[0][1]
    header      = data_list[0][2]
    casename    = data_list[0][3]

    time.sleep(1)
    resp        = GetIhDoctorInfo().getIhDoctorInfo(inData, header,casename,get_user_token,get_doctor_id)

    price               = resp.json()['body']['doctorOnlineItems'][2]['price']
    doctorId            = resp.json()['body']["doctorId"]
    orgFullName         = resp.json()['body']["orgFullName"]
    orgId               = resp.json()['body']["orgId"]
    standardDeptName    = resp.json()['body']["deptName"]
    standardDeptId      = resp.json()['body']['doctorOrgs'][0]['localDeptId']
    doctorOnlineExtraId = resp.json()['body']['doctorOnlineItems'][0]['doctorOnlineExtraId']
    #id,不是scheduleDayId
    scheduleDay_Id      = resp.json()['body']['doctorOnlineItems'][2]['scheduleDay']['id']
    workDate            = resp.json()['body']['doctorOnlineItems'][2]['scheduleDay']['workDate']#2021-12-01 00:00:00
    startTime           = resp.json()['body']['doctorOnlineItems'][2]['scheduleDay']['startTime']
    workDate            = workDate[0:10]
    HH                  = startTime[0:2]
    MM                  = startTime[3:5]
    SS                  = startTime[6:8]
    scheduleStartTime   = workDate.strip()+" "+startTime

    return [price,doctorId,orgId,standardDeptName,standardDeptId,doctorOnlineExtraId,scheduleDay_Id,scheduleStartTime,orgFullName,workDate,HH,MM,SS,resp]



@pytest.fixture(scope='session')
def get_family_mpiId(get_user_token):
    data_list   = get_yaml_data(testCasePath + '/getFamilyMemberList.yaml')
    inData      = data_list[0][0]
    expt        = data_list[0][1]
    header      = data_list[0][2]
    casename    = data_list[0][3]

    resp        = Search().search(inData, header,casename,get_user_token)
    mpiId       = resp.json()['body'][0]['mpiId']#林靖凯
    return mpiId

@pytest.fixture(scope='session')
def get_orderNo(get_user_token,get_doctor_info,get_family_mpiId):
    data_list   = get_yaml_data(testCasePath + '/submitRevisitDispense.yaml')
    inData      = data_list[0][0]
    expt        = data_list[0][1]
    header      = data_list[0][2]
    casename    = data_list[0][3]
    #拼接的时候需要使用字符串格式
    get_family_mpiId_zhong  = str(get_family_mpiId)#林靖凯
    revisitStandardDeptId   = str(get_doctor_info[4])
    price                   = str(get_doctor_info[0])
    goodsId                 = str("5351")
    goodsCode               = str("04")
    doctorOnlineExtraId     = str(get_doctor_info[5])
    docScheduleId           = str(get_doctor_info[6])
    HH                      = str(get_doctor_info[10])
    MM                      = str(get_doctor_info[11])
    SS                      = str(get_doctor_info[12])

    inDataTemp      = "data=%7B%22mpiId%22%3A%22"+get_family_mpiId_zhong+"%22%2C%22revisitStandardDeptName%22%3A%22"+"%E8%80%B3%E9%BC%BB%E5%92%BD%E5%96%89%E7%A7%91"+"%22%2C%22revisitStandardDeptId%22%3A%22"+revisitStandardDeptId+"%22%2C%22price%22%3A"+price+"%2C%22goodsId%22%3A"+goodsId+"%2C%22goodsName%22%3A%22"+"%E5%A4%8D%E8%AF%8A%E9%85%8D%E8%8D%AF"+"%22%2C%22goodsCode%22%3A%22"+goodsCode+"%22%2C%22doctorOnlineExtraId%22%3A"+doctorOnlineExtraId+"%2C%22docScheduleId%22%3A"+docScheduleId+"%2C%22scheduleStartTime%22%3A%22"+get_doctor_info[9]+"%20"+HH+"%3A"+MM+"%3A"+SS+"%22%2C%22diseaseSituation%22%3A%7B%22chiefComplaint%22%3A%22%E6%89%98%E5%B0%94%E6%96%AF%E6%B3%B0%E6%89%98%E5%B0%94%E6%96%AF%E6%B3%B0%22%2C%22preTreatmentFlag%22%3A0%2C%22drugName%22%3A%22%22%7D%7D"+"&fileIds=''"
    time.sleep(1)
    resp            = SubmitRevisitDispense().submitRevisitDispense(inDataTemp,header,casename,get_user_token)
    orderNo         = resp.json()['body']['orderNo']
    orderDetailId   = resp.json()['body']['orderDetailId']
    return [resp,orderNo,orderDetailId]

@pytest.fixture(scope='session')
def get_payChannel(get_user_token,get_doctor_info):
    data_list   = get_yaml_data(testCasePath + '/payChannelByOrg.yaml')
    inData      = data_list[0][0]
    expt        = data_list[0][1]
    header      = data_list[0][2]
    casename    = data_list[0][3]

    resp        = GetPayChennel().getPayChennel(inData, header,casename,get_user_token,get_doctor_info)
    payType     = resp.json()['body'][0]['payType']
    return payType

@pytest.fixture(scope='session')
#查看医嘱列表，并返回待下单且审核通过状态的recipeId
def get_findRecipeInfoByOrderNo_info(get_user_token,RevisitPageList):#get_orderNo
    data_list   = get_yaml_data(testCasePath + '/FindRecipeInfoByOrderNo.yaml')
    inData      = data_list[0][0]
    expt        = data_list[0][1]
    header      = data_list[0][2]
    casename    = data_list[0][3]
    orderNo = "2112210100000013"

    resp        = FindRecipeInfoByOrderNo().findRecipeInfoByOrderNo(inData, header,casename,get_user_token,RevisitPageList)#get_orderNo
    recipe_list = resp.json()['body']

    for recipe in recipe_list:
        if recipe['recipeOrderStatus'] == '0'and recipe['recipeCheckStatus']=='3':
            recipeId    = recipe['recipeId']
            revisitId   =  recipe['revisitId']
            recipeTypeCode = recipe['drugs'][0]['recipeTypeCode']#处方类型：21西药处方

            return [resp,recipeId,revisitId]
        else:
            print "该复诊订单没有待下单的医嘱"

@pytest.fixture(scope='session')
#创建药品订单
def createRecipeOrder(get_user_token,get_drugStoreInfo,getRecipePrecalculatedFee):
    data_list   = get_yaml_data(testCasePath + '/createRecipeOrder.yaml')
    inData      = data_list[0][0]
    expt        = data_list[0][1]
    header      = data_list[0][2]
    casename    = data_list[0][3]

    resp        = CreateRecipeOrder().createRecipeOrder(inData,expt, header,casename,get_user_token,get_drugStoreInfo,getRecipePrecalculatedFee)
    return resp


@pytest.fixture(scope='session')
#获取药品订单info
def getRecipeOrder(get_user_token,createRecipeOrder):
    data_list   = get_yaml_data(testCasePath + '/getOrder.yaml')
    inData      = data_list[0][0]
    expt        = data_list[0][1]
    header      = data_list[0][2]
    casename    = data_list[0][3]
    resp        = GetOrder().getRecipeOrder(inData, header,casename,get_user_token,createRecipeOrder)

    return resp

@pytest.fixture(scope='session')
#获取药店info
def get_drugStoreInfo(get_user_token,get_findRecipeInfoByOrderNo_info):
    data_list   = get_yaml_data(testCasePath + '/searchSuppliers.yaml')
    inData      = data_list[0][0]
    expt        = data_list[0][1]
    header      = data_list[0][2]
    casename    = data_list[0][3]

    resp        = SearchSuppliers().searchSuppliers(inData, header,casename,get_user_token,get_findRecipeInfoByOrderNo_info)

    # body                = resp.json()['body'][0]
    #
    # deliveryMode        = resp.json()['body'][0]['deliveryMode']#2
    # distance            = resp.json()['body'][0]['distance']
    # latitude            = resp.json()['body'][0]['latitude']
    # longitude           = resp.json()['body'][0]['longitude']
    # operateMchId        = resp.json()['body'][0]['operateMchId']#7345
    # orderAmount         = resp.json()['body'][0]['orderAmount']
    # orderWeightAmount   = resp.json()['body'][0]['orderWeightAmount']
    # payType             = resp.json()['body'][0]['payType'][0]#u'1,2'
    # phone               = resp.json()['body'][0]['phone']
    #
    # recipeInfo_details  = resp.json()['body'][0]['recipeInfo'][0]['details'][0]
    #
    # amount              = recipeInfo_details['amount']
    # doseUnit            = recipeInfo_details['doseUnit']
    # drugCode            = recipeInfo_details['drugCode']#15313  #该药品在该药店对应的药品id，下单时需要传入此drugCode。处方info中的drugCode是该药品本身的code
    #
    # drugDays            = recipeInfo_details['drugDays']
    # drugDose            = recipeInfo_details['drugDose']
    # drugName            = recipeInfo_details['drugName']#药品名称
    # drugPathways        = recipeInfo_details['drugPathways']
    # drugRate            = recipeInfo_details['drugRate']
    # isDefault           = recipeInfo_details['isDefault']
    # packQtyOutter       = recipeInfo_details['packQtyOutter']
    # packUnitOutter      = recipeInfo_details['packUnitOutter']
    # price               = recipeInfo_details['price']
    # specDesc            = recipeInfo_details['specDesc']#u'0.4g*36\u7c92' 规格
    # specId              = recipeInfo_details['specId']
    # weight              = recipeInfo_details['weight']
    # weightAmount        = recipeInfo_details['weightAmount']
    #
    # recipeId            = resp.json()['body'][0]['recipeInfo'][0]['recipeId']
    # recipeIdOutter      = resp.json()['body'][0]['recipeInfo'][0]['recipeIdOutter']
    #
    # selfgetFlag         = resp.json()['body'][0]['selfgetFlag']
    # storeIdOutter       = resp.json()['body'][0]['storeIdOutter']
    # storeName           = resp.json()['body'][0]['storeName']
    # testFlag            = resp.json()['body'][0]['testFlag']

    return resp


@pytest.fixture(scope='session')
#预结算接口，返回一些字段是创建药品订单必需的
def getRecipePrecalculatedFee(get_user_token,get_findRecipeInfoByOrderNo_info):
    data_list   = get_yaml_data(testCasePath + '/getRecipePrecalculatedFee.yaml')
    inData      = data_list[0][0]
    expt        = data_list[0][1]
    header      = data_list[0][2]
    casename    = data_list[0][3]

    resp        = GetRecipePrecalculatedFee().getRecipePrecalculatedFee(inData, header,casename,get_user_token,get_findRecipeInfoByOrderNo_info)

    return resp

@pytest.fixture(scope='session')
#获取药店支付方式列表
def queryPharmacyChannelListByOrderNo(get_user_token,createRecipeOrder):
    data_list   = get_yaml_data(testCasePath + '/queryPharmacyChannelListByOrderNo.yaml')
    inData      = data_list[0][0]
    expt        = data_list[0][1]
    header      = data_list[0][2]
    casename    = data_list[0][3]
    resp        = QueryPharmacyChannelListByOrderNo().queryPharmacyChannelListByOrderNo(inData, header,casename,get_user_token,createRecipeOrder)
    print resp.json()['body'][0]['payType']
    return resp


@pytest.fixture(scope='session')
#获取复诊中列表
def RevisitPageList(get_user_token):
    data_list   = get_yaml_data(testCasePath + '/pageList.yaml')
    inData      = data_list[1][0]
    expt        = data_list[1][1]
    header      = data_list[1][2]
    casename    = data_list[1][3]
    resp        = PageList().revisitPageList(inData, header,casename,get_user_token)

    return resp.json()['body'][0]['orderNo']


if __name__ == '__main__':
    queryPharmacyChannelListByOrderNo('9f5309d9-c38e-453b-8a43-46f0da9bea02','20211221000000017')
