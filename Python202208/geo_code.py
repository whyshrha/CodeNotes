# -*- coding:utf-8 -*-

import numpy as np
import pandas as pd
import time
import datetime
import requests

##### 注意
##### 注意
##### 注意
##### 注意
##### 注意下面的join需要reset_index    ##############################################################################

# Baidu
########################################################################################################################
def geocode_baidu(address,city):
    ak = 'ECGYUCeGLXAjzeMWOUOAfSnav2HkOHeC'
    url='http://api.map.baidu.com/geocoder/v2/?address=%s&city=%s&output=json&ak=%s' %(address,city,ak)
    res = requests.get(url)
    resu = res.json()
    return resu


def xiugainame(data,name):
    data = pd.DataFrame(data)
    data.columns = [name]
    return data

def geo_baidu(data,feature_name,city_name):
    '''
    # 结果状态
    # 返回几个结果
    # 返回状态
    # 返回经纬度
    # 返回省份
    
    '''
    length_data = len(data)
    starttime = datetime.datetime.now()
    
    status_bd = []        # 成功返回0
    comprehension_bd = [] # 地理理解程度
    confidence_bd = []    # 可信度
    level_bd = []         # 地址类型 
    lat_bd = []           # 维度值
    lng_bd = []           # 经度值
    precise_bd = []       # 附加信息是否精确查找

    for i in range(length_data):
        try:
            resu = geocode_baidu(data[feature_name].iloc[i],data[city_name].iloc[i])
            status_bd.append(resu['status'])
            comprehension_bd.append(resu['result']['comprehension'])
            confidence_bd.append(resu['result']['confidence'])
            level_bd.append(resu['result']['level'])
            lat_bd.append(resu['result']['location']['lat'])
            lng_bd.append(resu['result']['location']['lng'])
            precise_bd.append(resu['result']['precise'])
        except:
            status_bd.append(None)
            comprehension_bd.append(None)
            confidence_bd.append(None)
            level_bd.append(None)
            lat_bd.append(None)
            lng_bd.append(None)
            precise_bd.append(None)
            
        if i%1000 == 0:
            endtime = datetime.datetime.now()
            print ('已经完成 %d 个地理编码，时间占用 %s' % (i,(endtime - starttime).seconds))

    status_bd = xiugainame(status_bd,'status_bd')
    comprehension_bd = xiugainame(comprehension_bd,'comprehension_bd')
    confidence_bd = xiugainame(confidence_bd,'confidence_bd')
    level_bd = xiugainame(level_bd,'level_bd')
    lat_bd = xiugainame(lat_bd,'lat_bd')
    lng_bd = xiugainame(lng_bd,'lng_bd')
    precise_bd = xiugainame(precise_bd,'precise_bd')

    output = data.join([status_bd,comprehension_bd,confidence_bd,level_bd,lat_bd,lng_bd,precise_bd])
    
    return output

########################################################################################################################


def geo_error_baidu(output,feature_name):
    '''
    function: 对百度未转化成功的，再用百度进行编码
    input:  output 为第一次转化的数据，
            feature_name 为地址的字段名
    output: 为输出结果
    '''
    # 检测未转化字段
    error_data = output[output['status']!='OK']
    output_succeed = output[pd.isnull(output['lat'])==False]
    for j in error_data.index:
        try:
            g = geocoder.baidu(error_data.loc[j,feature_name],key = 'DbGLZALs3Sr8UZMxUKBHyG2GwfHj1spd')
            error_data.loc[j,'status']=g.status
            error_data.loc[j,'confidence']=g.confidence
            error_data.loc[j,'lat']=g.lat
            error_data.loc[j,'lng']=g.lng
            error_data.loc[j,'quality']=g.quality
        except:
            pass

    # 将再次转化数据添加到成功数据中
    output = output_succeed.append(error_data)

    return output

########################################################################################################################
def geo_error_google(output,feature_name):
    '''
    function: 对baidu中可信度小于40的进行转化
    input:  output 为第一次转化的数据，
            feature_name 为地址的字段名
    output: 为输出结果
    '''
    # 检测未转化字段
    error_data = output[output['confidence']<40]
    output_succeed = output[output['confidence']>=40]
    for j in range(len(error_data)):
        try:
            g = geocoder.google(error_data[feature_name].iloc[j])
            error_data['status'].iloc[j]=g.status
            error_data['confidence'].iloc[j]=g.confidence
            error_data['lat'].iloc[j]=g.lat
            error_data['lng'].iloc[j]=g.lng
            error_data['quality'].iloc[j]=g.quality
        except:
            status.append(None)
            confidence.append(None)
            lat.append(None)
            lng.append(None)
            quality.append(None)

    # 将再次转化数据添加到成功数据中
    output = output_succeed.append(error_data)
    google_code = error_data

    return google_code,output

def geo_fail_google(output,feature_name):
    '''
    function: 对google未成功的再转化
    input:  output 为第一次转化的数据，
            feature_name 为地址的字段名
    output: 为输出结果
    '''
    # 检测未转化字段
    error_data = output[output['status']!='OK']
    output_succeed = output[pd.isnull(output['lat'])==False]
    for j in range(len(error_data)):
        try:
            g = geocoder.google(error_data[feature_name].iloc[j])
            error_data['status'].iloc[j]=g.status
            error_data['confidence'].iloc[j]=g.confidence
            error_data['lat'].iloc[j]=g.lat
            error_data['lng'].iloc[j]=g.lng
            error_data['quality'].iloc[j]=g.quality
        except:
            status.append(None)
            confidence.append(None)
            lat.append(None)
            lng.append(None)
            quality.append(None)

    # 将再次转化数据添加到成功数据中
    output = output_succeed.append(error_data)
    google_fail_code = error_data

    return google_fail_code,output


################################################################################################
# 下面调用的是tencent
# #######考虑添加定位的city
def geocode_tencent(address):
    url = 'https://apis.map.qq.com/ws/geocoder/v1/'
    params = {'key':'NRYBZ-4VXK4-VWNUS-DNTN6-SWCQ2-X2BMG', 'address': address}
    r = requests.get(url, params=params)
    res = r.json()
    return res

def geo_all_tencent(data,feature_name):


    length_data = len(data)
    starttime = datetime.datetime.now()
    title_t = []
    status_t = []
    message_t = []
    province_t = []
    city_t = []
    district_t = []
    reliability_t = []
    level_t = []
    lat_t = []
    lng_t = []

    for i in range(length_data):
        try:
            res = geocode_tencent(data[feature_name].iloc[i])
            title_t.append(res['result']['title'])
            status_t.append(res['status'])
            message_t.append(res['message'])
            province_t.append(res['result']['address_components']['province'])
            city_t.append(res['result']['address_components']['city'])
            district_t.append(res['result']['address_components']['district'])
            reliability_t.append(res['result']['reliability'])
            level_t.append(res['result']['level'])
            lat_t.append(res['result']['location']['lat'])
            lng_t.append(res['result']['location']['lng'])
        except:
            title_t.append(None)
            status_t.append(None)
            message_t.append(None)
            province_t.append(None)
            city_t.append(None)
            district_t.append(None)
            reliability_t.append(None)
            level_t.append(None)
            lat_t.append(None)
            lng_t.append(None)
        if i%1000 == 0:
            endtime = datetime.datetime.now()
            print ('已经完成 %d 个地理编码，时间占用 %s' % (i,(endtime - starttime).seconds))
        
    title_t = pd.DataFrame(title_t)
    title_t.columns=['title_t']
    status_t = pd.DataFrame(status_t)
    status_t.columns=['status_t']
    message_t = pd.DataFrame(message_t)
    message_t.columns = ['message_t']
    province_t = pd.DataFrame(province_t)
    province_t.columns =['province_t']
    city_t =pd.DataFrame(city_t)
    city_t.columns = ['city_t']
    district_t =pd.DataFrame(district_t)
    district_t.columns = ['district_t']
    reliability_t =pd.DataFrame(reliability_t)
    reliability_t.columns = ['reliability_t']
    level_t =pd.DataFrame(level_t)
    level_t.columns = ['level_t']
    lat_t =pd.DataFrame(lat_t)
    lat_t.columns = ['lat_t']
    lng_t =pd.DataFrame(lng_t)
    lng_t.columns = ['lng_t']
    
    output = data.join([title_t, status_t, message_t, province_t, city_t, district_t, reliability_t, level_t, lat_t,lng_t])
    
    return output

########################################################################################
# 天地图

def geocode_tianditu(address):
    tk = 'e2977464a0c02991fcea15e0c0043284' # yansong
    url = 'http://api.tianditu.gov.cn/geocoder?ds={"keyWord":"%s"}&tk=%s' % (address, tk)
    res = requests.get(url)
    resu = res.json()
    return resu

def xiugainame(data,name):
    data = pd.DataFrame(data)
    data.columns = [name]
    return data

def geo_tianditu(data,feature_name):
    
    length_data = len(data)
    starttime = datetime.datetime.now()
    msg_tdt = [] 
    status_tdt = [] 
    level_tdt = [] 
    lat_tdt = [] 
    lng_tdt = [] 

    for i in range(length_data):
        try:
            res = geocode_tianditu(data[feature_name].iloc[i])
            msg_tdt.append(res['msg'])
            status_tdt.append(res['status'])
            level_tdt.append(res['location']['level'])
            lat_tdt.append(res['location']['lat'])
            lng_tdt.append(res['location']['lon'])
        except:
            msg_tdt.append(None)
            status_tdt.append(None)
            level_tdt.append(None)
            lat_tdt.append(None)
            lng_tdt.append(None)
        if i%1000 == 0:
            endtime = datetime.datetime.now()
            print ('已经完成 %d 个地理编码，时间占用 %s' % (i,(endtime - starttime).seconds))

    msg_tdt = xiugainame(msg_tdt,'msg_tdt')
    status_tdt = xiugainame(status_tdt,'status_tdt')
    level_tdt = xiugainame(level_tdt,'level_tdt')
    lat_tdt = xiugainame(lat_tdt,'lat_tdt')
    lng_tdt = xiugainame(lng_tdt,'lng_tdt')

    output = data.join([msg_tdt,status_tdt,level_tdt,lat_tdt,lng_tdt])
    
    return output


##############################################################################
# amap 高德地图
# address='北京市朝阳区阜通东大街6号'
# amap
def geocode_amap(address,city):
    key = '0f7af7723323653136b939405e58b6d5'
    url='https://restapi.amap.com/v3/geocode/geo?address=%s&city=%s&key=%s' %(address,city,key)
    res = requests.get(url)
    resu = res.json()
    return resu



def geo_amap(data,feature_name,city_name):
    '''
    # 结果状态
    # 返回几个结果
    # 返回状态
    # 返回经纬度
    # 返回省份
    
    '''
    length_data = len(data)
    starttime = datetime.datetime.now()
    
    formatted_address_amap = []
    status_amap = []
    count_amap = []
    info_amap = []
    location_amap = []
    province_amap = []
    city_amap = []
    district_amap = []

    for i in range(length_data):
        try:
            resu = geocode_amap(data[feature_name].iloc[i],data[city_name].iloc[i])
            formatted_address_amap.append(resu['geocodes'][0]['formatted_address'])
            status_amap.append(resu['status'])
            count_amap.append(resu['count'])
            info_amap.append(resu['info'])
            location_amap.append(resu['geocodes'][0]['location'])
            province_amap.append(resu['geocodes'][0]['province'])
            city_amap.append(resu['geocodes'][0]['city'])
            district_amap.append(resu['geocodes'][0]['district'])
        except:
            formatted_address_amap.append(None)
            status_amap.append(None)
            count_amap.append(None)
            info_amap.append(None)
            location_amap.append(None)
            province_amap.append(None)
            city_amap.append(None)
            district_amap.append(None)
            
        if i%1000 == 0:
            endtime = datetime.datetime.now()
            print ('已经完成 %d 个地理编码，时间占用 %s' % (i,(endtime - starttime).seconds))

    formatted_address_amap = xiugainame(formatted_address_amap,'formatted_address_amap')
    status_amap = xiugainame(status_amap,'status_amap')
    count_amap = xiugainame(count_amap,'count_amap')
    info_amap = xiugainame(info_amap,'info_amap')
    location_amap = xiugainame(location_amap,'location_amap')
    province_amap = xiugainame(province_amap,'province_amap')
    city_amap = xiugainame(city_amap,'city_amap')
    district_amap = xiugainame(district_amap,'district_amap')

    output = data.join([formatted_address_amap,status_amap,count_amap,info_amap,location_amap,province_amap,city_amap,district_amap])
    
    return output















