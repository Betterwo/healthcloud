# C:\Python27
# -*-coding:utf-8-*-
# @Author:huanghl
# @time :2021/12/8 11:19

import logging
import os
import time

datetime = time.strftime("%Y-%m-%d", time.localtime())

def create_file():
    #prj_path =os.path.dirname(os.path.abspath('..'))+"\\Logs"#F:\API_TEST\auto\python\healthcloud\Logs
    prj_path ="F:\\API_TEST\\auto\\python\\healthcloud\\Logs"
    if not os.path.exists(prj_path):
        os.makedirs(prj_path)
    else:
        pass
    log_file = prj_path +"\\"+ datetime + '.log'
    return log_file

class Log():
    def __init__(self,name,level='DEBUG'):
        """name为实例化是的入参：实例化文件的文件名xxx.py"""
        self.__name = name
        self.__path = create_file()
        self.__level = level
        self.__logger = logging.getLogger(self.__name)
        self.__logger.setLevel(self.__level)


    def __init_handler(self):
        """初始化handle"""
        stream_handler = logging.StreamHandler()
        file_handler = logging.FileHandler(self.__path,encoding='utf-8')
        return stream_handler,file_handler

    def __set_handler(self,stream_handler,file_handler,level='DEBUG'):
        """设置handler级别并添加到logger收集器"""
        stream_handler.setLevel(level)
        file_handler.setLevel(level)
        self.__logger.addHandler(stream_handler)
        self.__logger.addHandler(file_handler)

    def __set_formatter(self,stream_handler,file_handler):
        """设置日志输出格式"""
        formatter = logging.Formatter('%(asctime)s-%(name)s-%(filename)s-[line:%(lineno)d]'
                                      '-%(levelname)s-[日志信息]: %(message)s',
                                      datefmt='%a, %d %b %Y %H:%M:%S')
        stream_handler.setFormatter(formatter)
        file_handler.setFormatter(formatter)

    def __close_handler(self,stream_handler,file_handler):
        """关闭handler"""
        stream_handler.close()
        file_handler.close()

    @property
    def Logger(self):
        """构造收集器，返回logger"""

        #判断是否已创建handler，没有就创建，已创建就直接返回，避免日志重复
        if not self.__logger.handlers:
            stream_handler,file_handler = self.__init_handler()
            self.__set_handler(stream_handler,file_handler)
            self.__set_formatter(stream_handler,file_handler)
            self.__close_handler(stream_handler,file_handler)

        return self.__logger
        # stream_handler,file_handler = self.__init_handler()
        # self.__set_handler(stream_handler,file_handler)
        # self.__set_formatter(stream_handler,file_handler)
        # self.__close_handler(stream_handler,file_handler)
        #
        # return self.__logger



if __name__ == '__main__':
    create_file()



