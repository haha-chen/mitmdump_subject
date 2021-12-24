

def request(flow):
    "抓取 request 请求值"
    # print(flow.request.headers)
    # resultstr = flow.request.host
    # print("flow.response.get_text()",type(resultstr),resultstr)
    # print("def request", flow.response.get_text())
    # flow.request.url = "http://apigp1.caikuh.com/mcstat/9?client_lang=zh-tw&year=2021&period=348"  # 修改请求地址
    pass


def response(flow):
    #抓取 response 返回值
    resURL = flow.request.url #获取请求的 url
    # print("response:resURL",resURL)
    # print("flow:response",flow.response.text)
    # print("def request", flow.response.get_text())
    # flow.response = flow.response.make(500) #修改影响代码
    # flow.request.url = "http://www.baidu.com" #修改请求地址
    # text = "1232"
    # flow.response.set_text(text) #修改返回值
    print(flow.response.get_text())

