import re
import time
import subprocess
import os

s_file_path = '/hskj/test/spath/'
d_file_path = '/hskj/test/dpath/'


def deal_file():
    cache_file_path = './cache_file'
    #cache_list用于存放已经处理过的文件名称
    cache_list = []
    new_cache = []
    with open(cache_file_path) as cache_file:
        ccfile = cache_file.readlines()
        for c in ccfile:
            c = c.rstrip("\n")
            cache_list.append(c)
    # 遍历文件，确认文件是否已经被处理
    fs = os.listdir(s_file_path)
    for f in fs:
        if f in cache_list:
            pass
        else:
            #解压文件到指定目录
            child = subprocess.Popen(['gunzip', '%s%s'%(s_file_path,f)], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            child.wait()
            if child.returncode == 0:
                f = f.rstrip('gz')
                print("文件 %s 解压成功"% f, time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
                new_cache.append(f)
            else:
                print("文件 %s 解压失败"% f, time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
                print("stderr is " + child.stderr.read().decode('utf8'))


    #将本次任务新处理的文件写入cache文件
    with open(cache_file_path,'a+') as wf:
        for k in new_cache:
            s = k + " " + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + "\n"
            wf.write(s)


#文件转换函数
def format_file():
    #需要提取的字段的正则表达式如下
    ip_pattern = '(?<![\.\d])(?:25[0-5]\.|2[0-4]\d\.|[01]?\d\d?\.){3}(?:25[0-5]|2[0-4]\d|[01]?\d\d?)(?![\.\d])'
    dtime_pattern = '(\[([^\[\]]*)\])'
    http_pattern = '(\\"[a-zA-z]+[\s][a-zA-z]+://[^\s]*[\s][a-zA-z]+/[0-9].[0-9]\\")'
    status_pattern = '(\\"\s\d+\s\d+\s\d+\s\d+\s\\")'
    reffer_pattern = '(\\"[a-zA-z]+://[^\s]*\\")'
    in_link_pattern = '(\d+\s)'
    cache_code_pattern = '(\s[a-zA-z]+\s)'

    #记录任务开始时间
    t1 = time.time()
    wait_format_file = os.listdir(s_file_path)
    for b in wait_format_file:
        with open(s_file_path+b) as f:
            with open(d_file_path+b, 'a+') as f2:
                for i in f.readlines():
                    try:
                        ip = re.findall(ip_pattern, i)
                        #获取客户端访问IP
                        cluster_ip = ip[0]
                        #获取服务端响应IP
                        server_ip = ip[-1]
                        #获取请求时间
                        dtime = re.search(dtime_pattern, i).group()
                        #获取请求方法、请求内容
                        http_content = re.search(http_pattern, i).group()
                        #获取HTTP请求响应数据
                        status = re.search(status_pattern, i).group()
                        status = status.split()
                        #获取HTTP状态码
                        http_status = status[1]
                        #获取HTTP请求处理时间
                        total_request_time = status[2]
                        #获取HTTP请求内容大小（不包含请求头内容）
                        response_size_no_header = status[3]
                        #获取HTTP请求内容总大小
                        response_size = status[4]
                        #获取Reffere
                        if re.search(reffer_pattern, i):
                            reffer = re.search(reffer_pattern, i).group()
                        else:
                            reffer = '"-"'

                        #截取HTTP请求日志，以获取UA信息
                        status_index = re.search(status_pattern, i).span()
                        new_i = i[int(status_index[1]):]
                        new_i = new_i.split('"')
                        #获取UA信息
                        user_agent = '"' + new_i[2] + '"'
                        #获取请求经过的代理IP
                        proxy_ip = '"' + new_i[4] + '"'
                        new_status = new_i[-1]
                        new_status.strip()
                        #获取Nginxn内部连接码
                        in_link_code = re.search(in_link_pattern, new_status).group()
                        #获取Nginx缓存状态
                        cache_code = re.search(cache_code_pattern, new_status).group()
                        # print(i)
                        # print(cluster_ip, server_ip)
                        # print(dtime)
                        # print(http_content)
                        # print(status)
                        # print(reffer)
                        # print(status_index[1])
                        # print(new_i)
                        # print(user_agent)
                        # print(proxy_ip)
                        # print(new_status)
                        # print(in_link_code)
                        # print(cache_code)

                        #日志格式转换为Apache格式
                        log = cluster_ip +" - - "+ dtime + " " + http_content + " " + http_status + " " + response_size + " " + reffer + " " + user_agent + "\n"
                        f2.write(log)
                        # break
                    except Exception as e:
                        # print(s_file_path+b)
                        # print(i)
                        # print(e)
                        pass

        os.rename(s_file_path+b,s_file_path+b+".completed")
    tn = time.time()
    tt = tn - t1
    print("任务执行时间：", tt)


def rmfile():
    child = subprocess.Popen(['rm', '-rf', '%s*.completed'%s_file_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    child.wait()
    if child.returncode == 0:
        print("源文件清理完毕")
    else:
        print(child.stderr.readlines().decode("utf8"))





deal_file()
format_file()
rmfile()

