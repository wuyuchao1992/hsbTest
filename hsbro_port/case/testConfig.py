# coding:utf-8
import unittest, time
from common.page import port
from common.base import Base

class editConfig(unittest.TestCase,port,Base):

    # 时间戳
    ticks = str(time.time()).replace('.', '')
    timestamp = ticks[:-4]

    def testContract(self):

        self.login("work_v2/login", "15976427941", "c4ca4238a0b923820dcc509a6f75849b")
        # image：接口参数
        file = {'image':('R1.pdf',open('D:\\sysContract\\R1.pdf','rb'),'pdf'),}
        # 上传文件接口
        self.upload("publics_v2/upload",file)
        self.ContractUrl = self.r.json()["data"]["url"]
        # 上传文件到法大大
        self.postNoData("publics_v2/uploadTemplate",{"template":self.ContractUrl,"timestamp":self.timestamp},)
        self.TemplateId = self.r.json()["data"]
        # 修改合同配置
        self.post("work_v2/config/create",{
            "name":"Contract",
            "key":"R1",
            "subkey[Title]":"R1投保单",
            "subkey[TemplateId]":self.TemplateId,
            "subkey[Template]":self.ContractUrl,
            "remark":"R1投保单",
            "subkey[SignKeyword]":u"签章处",
        })

    def testSendSms(self):
        self.login("work_v2/login", "15976427941", "c4ca4238a0b923820dcc509a6f75849b")
        self.post("work_v2/config/create", {
            "name": "send_sms",
            "key": "risk_control",
            "subkey[0]": "18811103837",
            # "subkey[1]": "18811103837",
            # "subkey[2]": "18811103837",
            "remark": "这是给风控发送短信配置",            # "subkey[3]": "13556823051",

        })


if __name__ == "__main__":
    editConfig().testSendSms()