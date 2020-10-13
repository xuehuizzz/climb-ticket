import requests

from get_stations import isStations, read

data = []
type_data = []


def query(date, from_station, to_station):
    data.clear()
    # 查询请求地址
    url = 'https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date=2020-07-31&leftTicketDTO.from_station=SHH&leftTicketDTO.to_station=BJP&purpose_codes=ADULT'.format(
        date, from_station, to_station)
    # 发送查询请求
    response = requests.get(url)
    # 将json数据转换为字典类型，通过键值对取数据
    result = response.json()
    result = result['data']['result']
    # 判断车站文件是否存在
    if isStations() == True:
        stations = eval(read())  # 读取所有车站文件并转换为dict类型
        if len(result) != 0:
            for i in result:
                tmp_list = i.split('|')
                from_station = list(stations.key())[list(stations.values()).index(tmp_list[6])]
                to_station = list(stations.key())[list(stations.values()).index(tmp_list[7])]
                seat = [tmp_list[3]], from_station, to_station, tmp_list[8],
                tmp_list[9], tmp_list[10], tmp_list[32], tmp_list[31],
                tmp_list[30], tmp_list[21], tmp_list[23], tmp_list[33],
                tmp_list[28], tmp_list[24], tmp_list[29], tmp_list[26]
                newSeat = []
                for s in seat:
                    if s == '':
                        s = '__'
                    else:
                        s = s
                    newSeat.append(s)
                data.append(newSeat)
            return data


# 获取高铁信息的方法
def g_vehicle():
    if len(data) != 0:
        for g in data:  # 循环所有火车数据
            i = g[0].startswith('G')  # 判断车次首字母是不是高铁
            if i:  # 如果是将该条信息添加到高铁数据中
                type_data.append(g)


# 移除高铁信息的方法
def r_g_vehicle():
    if len(data) != 0:
        for g in data:
            i = g[0].startswith('G')
            if i:  # 移除高铁信息
                type_data.remove(g)


# 获取动车信息的方法
def d_vehicle():
    if len(data) != 0:
        for d in data:  # 循环所有火车数据
            i = d[0].startswith('D')  # 判断车次首字母是不是动车
            if i == True:  # 如果是将该条信息添加到动车数据中
                type_data.append(d)


# 移除动车信息的方法
def r_d_vehicle():
    if len(data) != 0:
        for d in data:
            i = d[0].startswith('D')
            if i == True:  # 移除动车信息
                type_data.remove(d)


# 获取直达车信息的方法
def z_vehicle():
    if len(data) != 0:
        for z in data:  # 循环所有火车数据
            i = z[0].startswith('Z')  # 判断车次首字母是不是直达
            if i == True:  # 如果是将该条信息添加到直达数据中
                type_data.append(z)


# 移除直达车信息的方法
def r_z_vehicle():
    if len(data) != 0:
        for z in data:
            i = z[0].startswith('Z')
            if i == True:  # 移除直达车信息
                type_data.remove(z)


# 获取特快车信息的方法
def t_vehicle():
    if len(data) != 0:
        for t in data:  # 循环所有火车数据
            i = t[0].startswith('T')  # 判断车次首字母是不是特快
            if i == True:  # 如果是将该条信息添加到特快车数据中
                type_data.append(t)


# 移除特快车信息的方法
def r_t_vehicle():
    if len(data) != 0:
        for t in data:
            i = t[0].startswith('T')
            if i == True:  # 移除特快车信息
                type_data.remove(t)


# 获取快速车数据的方法
def k_vehicle():
    if len(data) != 0:
        for k in data:  # 循环所有火车数据
            i = k[0].startswith('K')  # 判断车次首字母是不是快车
            if i == True:  # 如果是将该条信息添加到快车数据中
                type_data.append(k)


# 移除快速车数据的方法
def r_k_vehicle():
    if len(data) != 0:
        for k in data:
            i = k[0].startswith('K')
            if i == True:  # 移除快车信息
                type_data.remove(k)
