# coding:utf-8
import unittest,json,random,time,warnings
from common.logger import Log
from common.page import requestMethod
timestamp = (str(time.time()).replace('.', ''))[:-4]
nowTime = time.strftime("%Y-%m-%d", time.localtime())
orgName = "上海游戏乐投资咨询有限公司"
licenseCode = "91310115695751424K"
corporation = "王贞匀"
image = "http://qiniu.hsbro.cn/1545898825805_身份证(1).jpg"
email = "550535582@qq.com"
phone = "15976427940"
idCard = "440981199602164628"
Excel = "http://qiniu.hsbro.cn/1564122444913_中山珠峰汽车维修有限公司资质审核表.xlsx"
rar = "http://qiniu.hsbro.cn/1564558039473_1561341162079_%E8%B4%A7%E7%89%A9%E4%BF%9D%E9%99%A9%E5%90%88%E5%90%8C.rar"
address = "安徽省合肥市巢湖市安徽省合肥市滨湖区万达未来塔B座3303-3308室工号155"
carName = "2018款MAXU V80 2.5T 6挡傲运通长轴高顶6座"
class Test(unittest.TestCase,requestMethod):

    # 随机生成手机号码
    account = 19667890000 + random.randint(1001, 9999)
    password = "1"
    log = Log()
    def testOrder2(self):
        self.log.info("------START--------")
        # remove the warning
        warnings.simplefilter('ignore', ResourceWarning)
        # 登录
        self.login(address="login_v2/index",account="19667893203",password="c4ca4238a0b923820dcc509a6f75849b")
        # 导入Excel
        self.upload(address="publics_v2/excelImport",files={'file':('1.xls',open('C:\\Users\\Tony\\Desktop\\1.xls','rb'),'xls'),})
        # Excel返回车辆信息
        carList = self.s.json()["data"]
        newCarList = []
        for i in carList:
            i["doing"] = "false"
            # 使用dumps将list转化为json字符串
            # 并且拼接上父节点的内容
            temp_i = '{"carsInfo":' + json.dumps(i,ensure_ascii=False) + '}'
            newCarList.append(temp_i)
        newCarList = str(newCarList)
        newCarList = newCarList.replace("'","")
        # print(newCarList)
        # 提交订单
        self.post(address="frontend_v2/orderbatch/create",params={
            "act":"add",
            "carList":newCarList,
            "creditorList":json.dumps([{"name": "胡歌", "phone": phone, "idCard": idCard, "amount": "1000000000","contractName": "卖身契", "contractDate": nowTime,"contractUrl": image}],ensure_ascii=False),
            "companyName":orgName,
            "address":"广东省深圳市",
            "linkName":"谢天华",
            "linkPhone":phone,
            "account":"62122620120026537796212262012002653779",
            "reAccount":"62122620120026537796212262012002653779",
            "payRemark":"替xxx打款",
            "provinceName":"浙江省",
            "cityName":"杭州市",
            "bankName":"中国建设银行",
            "bankBranch":"国才支行",
            "accept":1,
            "other":json.dumps([{"title":"附件1","remark":"","images":rar},{"title":"附件2","remark":"","images":rar}],ensure_ascii=False),
            "totalAmount":4000,
            "creditAmount":1000000000
        })
        self.log.info("------END--------")

if __name__=="__main__":
    unittest.main()