"""
以下内容来自：https://blog.csdn.net/weixin_39943586/article/details/110487564

-q：屏蔽mitmdump默认的控制台日志，只显示自己脚本中的

-s：入口脚本文件

-p：更改端口，默认为8080

修改脚本文件时，不用重启也会生效

针对 HTTP 生命周期的事件

请求：def request(self, flow: mitmproxy.http.HTTPFlow):

响应：def response(self, flow: mitmproxy.http.HTTPFlow):

其它：

def http_connect(self, flow: mitmproxy.http.HTTPFlow):

def requestheaders(self, flow: mitmproxy.http.HTTPFlow):

def responseheaders(self, flow: mitmproxy.http.HTTPFlow):

def error(self, flow: mitmproxy.http.HTTPFlow):

#####################请求：def request()##################################

请求：def request(flow:flow)

flow.request.headers

获取所有头信息，包含Host、User-Agent、Content-type等字段

flow.request.url

完整的请求地址，包含域名及请求参数，但是不包含放在body里面的请求参数

flow.request.host

域名

flow.request.method

请求方式：POST、GET等

flow.request.scheme

请求类型：http、https

flow.request.path

请求的路径，URL除域名之外的内容

flow.request.get_text()

请求中body的内容，有一些http会把请求参数放在body里面，可通过此方法获取，返回字典类型

flow.request.get_content()

结果如flow.request.get_text()，返回bytes类型

flow.request.raw_content

结果如flow.request.get_content()，返回bytes类型

flow.request.urlencoded_form

MultiDictView，content-type：application/x-www-form-urlencoded的请求参数，不包含url直接带的键值参数

flow.request.multipart_form

MultiDictView，content-type：multipart/form-data

flow.request.query

返回MultiDictView类型的数据，URL的键值参数

flow.request.query.get('wd')

取得请求参数wd的值

flow.request.query.keys()

取得所有请求参数

flow.request.query.set_all(key,[value])

修改请求参数

from mitmproxy.http import flow

def request(flow:flow):

# 获取所有头信息，包含Host、User-Agent、Content-type等字段

# print(flow.request.headers)

# 域名

# print(flow.request.host)

# 请求方式：POST、GET等

# print(flow.request.method)

# 请求类型：http、https

# print(flow.request.scheme)

# 请求的路径，URL除域名之外的内容

# print(flow.request.path)

# 请求中body的内容，有一些http会把请求参数放在body里面，可通过此方法获取，返回字典类型

# print(flow.request.get_text())

# 返回MultiDictView类型的数据，URL的键值参数

# print(flow.request.query)

# 完整的请求地址，包含域名及请求参数，但是不包含放在body里面的请求参数

if 'https://www.baidu.com' in flow.request.url:

# 取得请求参数wd的值

# print(flow.request.query.get('wd'))

# 取得所有请求参数

print(list(flow.request.query.keys()))

# 修改请求参数

flow.request.query.set_all('wd',['python'])

# 打印修改过后的参数

print(flow.request.query.get('wd'))


#######################响应：def response()#############################
响应：def response(flow: flow)

flow.response.status_code

状态码

flow.response.text

返回内容，已解码

flow.response.content

返回内容，Bytes类型

flow.response.get_text()

取得响应的文本

flow.response.set_text()

修改响应的文本

flow.response = flow.response.make(404)

返回404

from mitmproxy.http import flow #可以不需要写

import json

import re

def response(flow: flow):#可以不需要写 flow: flow

# 状态码

# print(flow.response.status_code)

# 返回内容，已解码

# print(flow.response.text)

# 返回内容，Bytes类型

# print(flow.response.content)

# 取得响应的文本

# print(flow.response.get_text())

# 修改响应的文本

# flow.response.set_text('123')

# 返回404

# flow.response = flow.response.make(404)

# 修改淘宝对selenium的js检测文件

targetUrl = 'https://g.alicdn.com/AWSC/uab/122.js'

if targetUrl in flow.request.url:

taobao_js =flow.response.get_text()

taobao_js = taobao_js.replace('!function(){function','!function (){Object.defineProperties(navigator,{webdriver: {get: () => false}})function')

flow.response.set_text(taobao_js)

print('已修改')

# 淘宝搜索商品时，自动打印商品信息

if 'https://s.taobao.com/search' in flow.request.url:

start = flow.response.text.strip().index('{')

end = -2

print(json.loads(flow.response.text.strip()[start: end])['mods']['itemlist']['data']['auctions'])

# 空气质量网，修改检测F12的JS

# https://www.aqistudy.cn/historydata

if 'https://www.aqistudy.cn/historydata/monthdata.php' in flow.request.url:

js = flow.response.text

js = re.sub(r'endebug.*?}\);','',js,flags=re.S)

flow.response.set_text(js)

print('已正常')
"""