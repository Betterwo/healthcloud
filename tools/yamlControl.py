# C:\Python27
# -*-coding:utf-8-*-
# @Author:huanghl
# @time :2021/11/17 16:00

import yaml
import pprint
import io
def get_yaml_data(fileDir):
    resList = []#[(请求1，期望1),(请求2，期望2)]

    #1.读取文件--磁盘-->内存
    fo = io.open(fileDir,'r',encoding='utf-8')
    res = yaml.load(fo,Loader=yaml.FullLoader)

    for one in res:
        resList.append((one['data'],one['expt'],one['header'],one['casename']))
    return resList

if __name__ == '__main__':
    data_yaml         = get_yaml_data('../data/createRecipeOrder.yaml')
    pprint.pprint(data_yaml)

