# C:\Python27
# -*-coding:utf-8-*-
# @Author:huanghl
# @time :2021/12/13 18:06

import requests
import sys
import os
import pprint

from configs.config import HOST
from configs.Log_config import Log

reload(sys)
sys.setdefaultencoding('utf-8')

file    =   os.path.basename(sys.argv[0])
log     =   Log(file)
logger  =   log.Logger

class CreateRecipeOrder:
    def createRecipeOrder(self,inData,expt,header,casename,userToken,get_drugStoreInfo,getRecipePrecalculatedFee):
        url                                                 =   '%s/*.jsonRequest' % HOST
        header['X-Access-Token']                            =   userToken
        payload                                             = []
        recipeDetailList                                    = []
        inData['recipeDetailList']['orgId']                 = getRecipePrecalculatedFee.json()['body']['details'][0]['orgId']
        inData['recipeDetailList']['recipeId']              = getRecipePrecalculatedFee.json()['body']['details'][0]['recipeId']

        inData['recipeDetailList']['itemName']              = getRecipePrecalculatedFee.json()['body']['details'][0]['itemName']
        inData['recipeDetailList']['drugSpecifications']    = getRecipePrecalculatedFee.json()['body']['details'][0]['drugSpecifications']

        #inData['recipeDetailList']['drugCodeStandard']      = getRecipePrecalculatedFee.json()['body']['details'][0]['drugCodeStandard']#药品本身drugcode

        inData['recipeDetailList']['itemNo']                = get_drugStoreInfo.json()['body'][0]['recipeInfo'][0]['details'][0]['drugCode']
        inData['recipeDetailList']['drugCodeStandard']      = getRecipePrecalculatedFee.json()['body']['details'][0]['itemNo']#药品在该药店对应的drugcode


        inData['recipeDetailList']['detailId']              = getRecipePrecalculatedFee.json()['body']['details'][0]['detailId']
        inData['recipeDetailList']['itemType']              = getRecipePrecalculatedFee.json()['body']['details'][0]['itemType']
        inData['recipeDetailList']['itemOrder']             = getRecipePrecalculatedFee.json()['body']['details'][0]['itemOrder']
        inData['recipeDetailList']['quantity']              = getRecipePrecalculatedFee.json()['body']['details'][0]['quantity']
        inData['recipeDetailList']['price']                 = getRecipePrecalculatedFee.json()['body']['details'][0]['price']
        inData['recipeDetailList']['medicineMethod']        = getRecipePrecalculatedFee.json()['body']['details'][0]['medicineMethod']


        recipeDetailList.append(inData['recipeDetailList'])
        inData["recipeDetailList"]                          = recipeDetailList
        inData['shopId']                                    = getRecipePrecalculatedFee.json()['body']['details'][0]['orgId']
        inData['quantity']                                  = getRecipePrecalculatedFee.json()['body']['details'][0]['quantity']
        inData['recipeUnionId']                             = getRecipePrecalculatedFee.json()['body']['details'][0]['recipeId']

        inData['storeId']                                   = get_drugStoreInfo.json()['body'][0]['storeIdOutter']
        inData['storeName']                                 = get_drugStoreInfo.json()['body'][0]['storeName']
        inData['storePhone']                                = get_drugStoreInfo.json()['body'][0]['phone']
        inData['storeAddress']                              = get_drugStoreInfo.json()['body'][0]['orgAddress']
        inData['storeMchId']                                = get_drugStoreInfo.json()['body'][0]['operateMchId']
        inData['longitude']                                 = get_drugStoreInfo.json()['body'][0]['longitude']
        inData['latitude']                                  = get_drugStoreInfo.json()['body'][0]['latitude']
        inData['deliveryMode']                              = get_drugStoreInfo.json()['body'][0]['deliveryMode']#1：在线支付，2：货到付款
        payload.append(inData)

        # 控制台不报异常
        requests.packages.urllib3.disable_warnings()
        try:
            resp = requests.post(url=url,json=payload,headers=header,verify=False)
            logger.info('{} request success'.format(casename))
            return resp
        except Exception as e:
            logger.error("{} request faild,throw error:{}".format(casename,e))