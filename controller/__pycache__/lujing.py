from ..sql import Sql
import math

def lujing2(chufa, mudi, chengshi, b):  # 输入出发与到达市,通过递归  贪心算法  计算出最短路径   只供 lujing()调用
    sql = Sql()
    sqlm = "select 省会城市 from adjacency where " + chufa + "=1"  # 编辑sql命令
    xlcs = sql.execute_query(sqlm)
    # print(chufa,'-',mudi,"附近的城市",xlcs)
    sqlm = "select latitude,longitude from city where city_name ='" + mudi + "'"
    jwd0 = sql.execute_query(sqlm)  # 目的地经纬度

    juli = 0  # 初始化两城市之间距离,算法为经度纬度的差值
    chengshi2 = "0"  # 初始化出发城市最近的城市.用来保存最近城市的变量
    for x in xlcs:  # 遍历附近的城市                   #获取附近城市经纬度,比较哪个离目的地最近,如果是目的城市,直接跳出
        sqlm = "select latitude,longitude from city where city_name ='" + x[0] + "'"
        jwd = sql.execute_query(sqlm)
        a = float(jwd[0][0]) - float(jwd0[0][0])
        b = float(jwd[0][1]) - float(jwd0[0][1])
        juli2 = math.sqrt(pow(a, 2) + pow(b, 2))
        if x[0] == mudi:
            chengshi2 = b
            break
        elif juli2 < juli or juli == 0:
            juli = juli2
            sqlm = "select prv_name from province where capital_city ='" + x[0] + "'"
            prv = sql.execute_query(sqlm)  # prv 路径上的省名
            chengshi2 = prv,

    if chengshi2 == b:  # 如果最近的城市就是目的城市,结束递归,将目的城市添加到路径末尾
        chengshi += chengshi2,
        return chengshi
    else:
        chengshi += chengshi2,  # 不是,将中间城市添加到路径,递归运算
        chengshi = lujing2(chengshi2, mudi, chengshi, b)
        return chengshi

def lujing(chufa, mudi):  # 函数功能是输入2省 计算出最优路径
    sql = Sql()
    if chufa == mudi:  # 如果是本省快递,返回0
        return ('0',)
    else:  # 不是本省快递,调用lujing2计算最优路径
        sqlm = "select capital_city from province where prv_name='" + chufa + "'"
        shcs = sql.execute_query(sqlm)  # shcs 省会城市

        sqlm = "select capital_city from province where prv_name='" + mudi + "'"
        shcs2 = sql.execute_query(sqlm)  # shcs 省会城市

        chengshi = chufa,  # 将出发城市添加到路径表的第一位
        chengshi = lujing2(shcs[0][0], shcs2[0][0], chengshi, mudi)  # 调用函数 计算最短路径列表
        chengshi = mudi,

        return chengshi