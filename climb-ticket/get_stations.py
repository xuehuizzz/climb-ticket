import requests
import os
import re


def getStation():
    # 发送请求获取所有车站名称，通过输入的站名称转换为查询地址的参数
    url = "https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.9142"
    response = requests.get(url, verify=True)  # 请求并进行验证
    # 获取需要的车站名称
    stations = re.findall(u"([\u4e00-\u9fa5]+)\|([A-Z]+)", response.text)
    stations = dict((stations))   # 转换为字典类型
    stations = str(stations)      # 转换为字符串类型，否则无法写入文件
    write(stations)               # 调用写入方法


def write(stations):
    file = open("stations.text", "w", encoding="utf_8_sig")     # 以只写模式打开文件
    file.write(stations)                                       # 写入文件
    file.close()


def read():
    file = open("stations.text", "r", encoding="utf_8_sig")     # 以只读模式打开文件
    data = file.readline()                                     # 读取文件
    file.close()
    return data


def isStations():
    isStations = os.path.exists("stations.text")               # 判断车站文件是否存在
    return isStations
