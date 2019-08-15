# coding:utf-8
import requests,time,unittest,json,random
from common.base import Base
class port():
    # 全局变量
    url = "http://api.hsbro.com.cn/"
    url1 = "http://h5.hsbro.com.cn/"
    # 账号密码
    account = "15976427940"
    password = "c4ca4238a0b923820dcc509a6f75849b"
    # 时间戳
    ticks = str(time.time()).replace('.', '')
    timestamp = ticks[:-4]
    # 头部信息
    # headers = {
    #     # "User-Agent": "Chrome/75.0.3770.142",
    #     # "Accept": "application/json, text/plain, */*",
    #     # "Accept-Encoding": "gzip, deflate",
    #     # "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
    #     # "Connection": "keep-alive",
    # }
    # 登录用例
    # address：接口地址
    # account：登录账号
    # password：登录密码（MD5加密）
    def login(self,address,account,password):
        # 访问路径
        path = self.url + address
        # 要排序参数
        params = {"account": account, "password": password, "timestamp": self.timestamp}
        # 参数按键盘排序,排序后加密
        sign = Base().md5(Base().sort(params))
        # 请求参数加上sign
        params["sign"] = sign
        # 请求接口
        self.r = requests.post(url=path, data=params)
        # 保存token
        self.token = self.r.json()["data"]["token"]
        # 保存userId
        self.userId = self.r.json()["data"]["userId"]
        # cookies
        self.Cookie = {}
        self.Cookie["Cookie"]= self.r.headers.get("Set-Cookie")
        if self.r.json()["resultCode"] == 200:
            print("【请求成功】：你很棒 \n【接口地址】：%s \n【请求结果】：%s" %(address,self.r.json()))
        else:
            print("【请求异常】：请检查 \n【接口地址】：%s \n【报错信息】：%s" %(address,self.r.text))
            return False

    # Get请求
    # address：接口地址
    # params：请求参数，可以为空
    def get(self, address, params=''):
        # 访问路径
        path = self.url + address
        # 请求参数
        loginData = {"token": self.token, "userId": self.userId, "timestamp": self.timestamp}
        loginData.update(params)
        # 参数按键盘排序,排序后MD5加密
        sign = Base().md5(Base().sort(loginData))
        # 加上sign
        loginData["sign"] = sign
        # 请求接口
        self.r = requests.get(url=path, params=loginData, headers=self.Cookie)
        if self.r.json()["resultCode"] == 200:
            print("【请求成功】：你很棒 \n【接口地址】：%s \n【请求结果】：%s" %(address,self.r.json()))
        else:
            print("【请求异常】：请检查 \n【接口地址】：%s \n【报错信息】：%s" %(address,self.r.text))
            return False

    # Post请求
    # address：接口地址
    # params：请求参数
    def post(self, address, params):
        # 访问路径
        path = self.url + address
        # 登录返回参数
        loginData = {"token": self.token, "userId": self.userId, "timestamp": self.timestamp}
        # 请求参数
        loginData.update(params)
        # 参数按键盘排序,排序后MD5加密
        sign = Base().md5(Base().sort(loginData))
        #  加上sign
        loginData["sign"] = sign
        # 请求方式
        self.r = requests.post(url=path, data=loginData,headers=self.Cookie)
        if self.r.json()["resultCode"] == 200:
            print("【请求成功】：你很棒 \n【接口地址】：%s \n【请求结果】：%s" %(address,self.r.json()))
        else:
            print("【请求异常】：请检查 \n【接口地址】：%s \n【报错信息】：%s" %(address,self.r.text))
            return False

    def crearAccount(self,account,password,address="login_v2/signin"):
        path = self.url + address
        params = {"account":account,"code":8432,"password":password,"repassword":password,"timestamp":self.ticks}
        sign = Base().md5(Base().sort(params))
        params["sign"] = sign
        self.r = requests.post(url=path,data=params,headers=self.Cookie)
        if self.r.json()["resultCode"] == 200:
            print("【请求成功】：你很棒 \n【接口地址】：%s \n【请求结果】：%s" %(address,self.r.json()))
        else:
            print("【请求异常】：请检查 \n【接口地址】：%s \n【报错信息】：%s" %(address,self.r.text))
            return False

    def postNoData(self, address, params):
        # 访问路径
        path = self.url + address
        # 登录返回参数
        # 参数按键盘排序,排序后MD5加密
        sign = Base().md5(Base().sort(params))
        #  加上sign
        params["sign"] = sign
        # 请求方式
        self.r = requests.post(url=path, data=params, headers=self.Cookie)
        if self.r.json()["resultCode"] == 200:
            print("【请求成功】：你很棒 \n【接口地址】：%s \n【请求结果】：%s" %(address,self.r.json()))
        else:
            print("【请求异常】：请检查 \n【接口地址】：%s \n【报错信息】：%s" %(address,self.r.text))
            return False

    def orgList(self,address="work_v2/organization/index",params=""):
    # 门店列表
        self.get(address,params)
        self.orgId = self.r.json()["data"]["list"][0]["id"]
        if self.r.json()["resultCode"] == 200:
            print("【请求成功】：你很棒 \n【接口地址】：%s \n【请求结果】：%s" %(address,self.r.json()))
        else:
            print("【请求异常】：请检查 \n【接口地址】：%s \n【报错信息】：%s" %(address,self.r.text))
            return False

    def upload(self, address, files):
        # 访问路径
        path = self.url + address
        # 登录返回参数
        self.r = requests.post(url=path, files=files)
        if self.r.json()["resultCode"] == 200:
            print("【请求成功】：你很棒 \n【接口地址】：%s \n【请求结果】：%s" %(address,self.r.json()))
        else:
            print("【请求异常】：请检查 \n【接口地址】：%s \n【报错信息】：%s" %(address,self.r.text))
            return False

if __name__=="__main__":
    unittest.main()