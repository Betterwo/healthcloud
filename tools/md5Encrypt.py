# C:\Python27
# -*-coding:utf-8-*-
# @Author:huanghl
# @time :2021/11/19 15:23

import hashlib

def get_MD5(pwd):
    hl = hashlib.md5()
    hl.update(pwd.encode(encoding='utf-8'))
    return hl.hexdigest()
