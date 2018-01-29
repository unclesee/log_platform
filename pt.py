import re
import time
import subprocess
import os
import hashlib

def file():
    s_file_path = r'E:\Plantform\日志格式\yunfan.baiwucdn.net'
    d_file_path = ''
    cache_file_path = ''
    fs = os.listdir(s_file_path)
    print(fs)
file()

# ip_pattern = '(?<![\.\d])(?:25[0-5]\.|2[0-4]\d\.|[01]?\d\d?\.){3}(?:25[0-5]|2[0-4]\d|[01]?\d\d?)(?![\.\d])'
# dtime_pattern = '(\[([^\[\]]*)\])'
# http_pattern = '(\\"[a-zA-z]+[\s][a-zA-z]+://[^\s]*[\s][a-zA-z]+/[0-9].[0-9]\\")'
# status_pattern = '(\\"\s\d+\s\d+\s\d+\s\d+\s\\")'
# reffer_pattern = '(\\"[a-zA-z]+://[^\s]*\\")'
# in_link_pattern = '(\d+\s)'
# cache_code_pattern = '(\s[a-zA-z]+\s)'
#
# t1 = time.time()
# print(t1)
# with open(r"E:\Plantform\日志格式\yunfan.baiwucdn.net\yunfan.baiwucdn.net_2018_01_25_1700_b3c59616") as f:
#     with open(r"E:\Plantform\日志格式\yunfan.baiwucdn.net\y2018_01_25_17_apache", 'a+') as f2:
#         for i in f.readlines():
#             try:
#                 ip = re.findall(ip_pattern, i)
#                 #获取客户端访问IP
#                 cluster_ip = ip[0]
#                 #获取服务端响应IP
#                 server_ip = ip[-1]
#                 #获取请求时间
#                 dtime = re.search(dtime_pattern, i).group()
#                 #获取请求方法、请求内容
#                 http_content = re.search(http_pattern, i).group()
#                 #获取HTTP请求响应数据
#                 status = re.search(status_pattern, i).group()
#                 status = status.split()
#                 #获取HTTP状态码
#                 http_status = status[1]
#                 #获取HTTP请求处理时间
#                 total_request_time = status[2]
#                 #获取HTTP请求内容大小（不包含请求头内容）
#                 response_size_no_header = status[3]
#                 #获取HTTP请求内容总大小
#                 response_size = status[4]
#                 #获取Reffere
#                 reffer = re.search(reffer_pattern, i).group()
#                 #截取HTTP请求日志，以获取UA信息
#                 status_index = re.search(status_pattern, i).span()
#                 new_i = i[int(status_index[1]):]
#                 new_i = new_i.split('"')
#                 #获取UA信息
#                 user_agent = '"' + new_i[2] + '"'
#                 #获取请求经过的代理IP
#                 proxy_ip = '"' + new_i[4] + '"'
#                 new_status = new_i[-1]
#                 new_status.strip()
#                 #获取Nginxn内部连接码
#                 in_link_code = re.search(in_link_pattern, new_status).group()
#                 #获取Nginx缓存状态
#                 cache_code = re.search(cache_code_pattern, new_status).group()
#                 print(i)
#                 # print(cluster_ip, server_ip)
#                 # print(dtime)
#                 # print(http_content)
#                 # print(status)
#                 # print(reffer)
#                 # print(status_index[1])
#                 # print(new_i)
#                 # print(user_agent)
#                 # print(proxy_ip)
#                 # print(new_status)
#                 # print(in_link_code)
#                 # print(cache_code)
#
#                 #日志格式转换为Apache格式
#                 log = cluster_ip +" - - "+ dtime + " " + http_content + " " + http_status + " " + response_size + " " + reffer + " " + user_agent + "\n"
#                 print(log)
#                 f2.write(log)
#                 # break
#             except Exception as e:
#                 print(e)
#         tn = time.time()
#         tt = tn - t1
#         print("任务执行时间：", tt)
