# sign() 模版:clnt.tpl() 语音:clnt.voice() 流量:clnt.flow()from yunpian_python_sdk.model import constant as YC
# # # from yunpian_python_sdk.ypclient import YunpianClient
# # # # 初始化client,apikey作为所有请求的默认值
# # # clnt = YunpianClient('apikey')
# # # param = {YC.MOBILE:'18616020***',YC.TEXT:'【云片网】您的验证码是1234'}
# # # r = clnt.sms().single_send(param)
# # # # 获取返回结果, 返回码:r.code(),返回码描述:r.msg(),API结果:r.data(),其他说明:r.detail(),调用异常:r.exception()
# # # # 短信:clnt.sms() 账户:clnt.user() 签名:clnt.


import requests
import json

class YunPian(object):

    def __init__(self, api_key):
        self.api_key = api_key
        self.single_send_url = "https://sms.yunpian.com/v2/sms/single_send.json"

    def send_sms(self, code, mobile):
        #需要传递的参数
        parmas = {
            "apikey": self.api_key,
            "mobile": mobile,
            "text": "【云片网】您的验证码是{code}。如非本人操作，请忽略本短信".format(code=code)
        }

        response = requests.post(self.single_send_url, data=parmas)
        re_dict = json.loads(response.text)
        return re_dict

if __name__ == "__main__":
    #例如：9b11127a9701975c734b8aee81ee3526
    yun_pian = YunPian("2e87d1xxxxxx7d4bxxxx1608f7c6da23exxxxx2")
    yun_pian.send_sms("2020", "手机号码")