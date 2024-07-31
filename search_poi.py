import requests
import re

# 读取表格第一列数据，变成列表形式
import pandas as pd

df = pd.read_excel("E:/demo_py/hainan/shujv0426.xlsx",usecols=[0],names=None)  # 读取项目名称列,不要列名
df_li = df.values.tolist()
result = []
for s_li in df_li:
    result.append(s_li[0])
num = len(result)
print(result)

def geocodeB(keywords):
# 输入的URL
    inputUrl = "http://restapi.amap.com/v3/place/text?key=34a86f365d427c77dd482532566d89a7&keywords={keywords}&types=&city=海南&children=0&offset=20&page=1&extensions=all".format(keywords = keywords)
    response = requests.get(inputUrl)
# 返回结果，JSON格式
    resultAnswer = response.json()
# 返回结果中的状态标签，1为成功，0为失败
    resultStatus = resultAnswer['status']
    if resultStatus == '1':  # 返回成功
    # 读取返回的POI列表
        resultList = resultAnswer['pois']
        if len(resultList) == 0:  # 返回的POI列表为空
            print("当前返回结果为空！")
        else:
        # 返回的POI列表不为空
                saveName = str(resultList[0]['name'])  # POI名称
                saveType = str(resultList[0]['type'])  # POI类别
                saveAddress = str(resultList[0]['address'])  # POI地址
                saveLocation = str(resultList[0]['location'])  # POI坐标
        # 将经纬度分割为X，Y
                m = re.search('(.*),(.*)', saveLocation)  # 利用经纬度间的逗号将二者分开
                savelongitude = m.group(1)  # 经度位于第一个括号
                savelatitude = m.group(2)  # 纬度位于第二个括号
                print([saveName, saveType, saveAddress, savelongitude, savelatitude])
    else:
        print("当前返回结果错误！")

# 将表格数据输入到高德API获取地址
for i in range(416, len(result)):
    geocodeB(result[i])


