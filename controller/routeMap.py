from .sql import Sql
import math


sql =Sql()
sql.connect()

def route2(startCity, endCity, city):  # 输入出发与到达市,通过递归  贪心算法  计算出最短路径   只供 route()调用
    statement = f"select 省会城市 from adjacency where {startCity}=1"  # 编辑sql命令
    xlcs = sql.execute_query(statement)
    # print(startCity,'-',endCity,"附近的城市",xlcs)
    statement = f"select longitude,latitude from city where city_name ='{endCity}'"
    jwd0 = sql.execute_query(statement) # 目的地经纬度

    juli = 0  # 初始化两城市之间距离,算法为经度纬度的差值
    city2 = "0"  # 初始化出发城市最近的城市.用来保存最近城市的变量
    for x in xlcs:  # 遍历附近的城市                   #获取附近城市经纬度,比较哪个离目的地最近,如果是目的城市,直接跳出
        statement = f"select longitude,latitude from city where city_name ='{x[0]}'"
        jwd = sql.execute_query(statement)
        a = float(jwd[0][0]) - float(jwd0[0][0])
        b = float(jwd[0][1]) - float(jwd0[0][1])
        juli2 = math.sqrt(pow(a, 2) + pow(b, 2))
        if x[0] == endCity:
            city2 = x[0]
            break
        elif juli2 < juli or juli == 0:
            juli = juli2
            #sqlm = "select capital_city from province where prv_name='" + startCity + "'"
            #shcs = Sql.sql1(sqlm)  # shcs 省会城市
            city2 = x[0]

    if city2 == endCity:  # 如果最近的城市就是目的城市,结束递归,将目的城市添加到路径末尾
        city += city2,
        return city
    else:
        city += city2,  # 不是,将中间城市添加到路径,递归运算
        city = route2(city2, endCity, city)
        return city


def route(startCity, endCity):  # 函数功能是输入2省 计算出最优路径
    if startCity == endCity:  # 如果是本省快递,返回0
        return [startCity]
    else:  # 不是本省快递,调用route2计算最优路径
        statement = f"select capital_city from province where prv_name='{startCity}'"
        shcs = sql.execute_query(statement) # shcs 省会城市

        statement = f"select capital_city from province where prv_name='{endCity}'"
        shcs2 = sql.execute_query(statement)  # shcs 省会城市

        city = shcs[0][0],  # 将出发城市添加到路径表的第一位
        city = route2(shcs[0][0], shcs2[0][0], city)  # 调用函数 计算最短路径列表

        result_city = []
        for item in city:
            statement = f"SELECT prv_name FROM province WHERE capital_city = '{item}'"
            result = sql.execute_query(statement)
            result_city.append(result)

        list_city = [item[0][0] for item in result_city]
        return list_city
