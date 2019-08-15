# coding:utf-8
import unittest,random,time, json
from common.page import port
from common.base import Base
from common.data import config as c

# 时间戳
ticks = str(time.time()).replace('.', '')
timestamp = ticks[:-4]
nowTime = time.strftime("%Y-%m-%d", time.localtime())
# 参数
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
class testShop(unittest.TestCase,port,Base):


    # 随机生成手机号码
    account = 19667890000 + random.randint(1001, 9999)
    # account = 19667893578
    password = "1"

    def testOrgVerify(self):
        # 创建账号
        self.postNoData("login_v2/signin",{
            "account":self.account,
            "code":"8432",
            "password":self.password,
            "repassword":self.password,
            "timestamp":self.timestamp,
        })
        print("创建账号：%s" %self.r.json())

        # 登录注册账号
        self.login("login_v2/index",self.account,self.password)
        print("SHOP登录：%s" %self.r.json())

        # 门店提交认证
        self.post("frontend_v2/organization/verify",
        {"name":orgName, # 公司名字
         "licenseCode":licenseCode,# 工商号码
         "corporation":corporation,# 法人姓名
         "securities":image,# 产权证明或租赁合同、租金凭证
         "license":image,# 营业执照
         "image":image,# 公司照片
         "address":"粤海街道高新南九道10号深圳湾科技生态园10栋A座11层1109室", # 公司地址
         "account":"621226201200669865",# 对公账号
         "bankName":"工商银行",# 银行名称
         "bankBranch":"罗湖分行", #支行名称
         "phone":phone,# 法人手机
         "email":email, # 法人邮箱
         "idCard":"130635198510286167",# 法人身份证
         "idCardOn":image, # 法人身份证正面
         "idCardOff":image,# 法人身份证反面
         "isShareHolder":"1", # 法人是否大股东 0：不是 1：是
         "shareHolder":"王五",# 大股东名字
         "shareHolderPhone":"15976427940", # 大股东电话
         "shareHolderEmail":email, # 大股东邮箱
         "shareHolderIdCard":"130635198510286167",# 大股东身份证
         "shareHolderIdCardOn":image, # 大股东身份证正面
         "shareHolderIdCardOff":image, # 大股东身份证反面
         "hasAgent":"1",# 签署人0：法人  1：代理人   为1，则以下字段必填
         "signName":u"吴宇超",# 签署人姓名
         "signPhone":phone, # 签署人手机号码
         "signIdCard":"440785199202226310", # 签署人身份证号码
         "signEmail":email,# 签署人邮箱
         "signIdCardOn":image,# 签署人身份证正面
         "signIdCardOff":image,# 签署人身份证反面
         "certificate":image,# CA证书照片
         "accountType":"1",# 0：委托人账号  1：对公账号
         "consign":"{\"consignIdCard\":\"450423197508186531\",\"account\": \"6222021907005281742\","
                   "\"bankBranch\": \"工商银行\",\"consignName\": \"aupl0401\",\"consignPhone\": \"18675343438\"}",# 委托人银行卡信息
         "consignName":u"余待永",# 委托人姓名
         "consignIdCard":"45032619840627183x", # 委托人身份证
         "consignPhone":phone,# 委托人手机号码
         "verifyAccount":"sam",# 征信账号
         "verifyPwd":"abc`1234",# 征信密码
         "verifyCode":"886",# 征信验证码
         "verifyReport":"http://qiniu.hsbro.cn/1547967789476_1111.rar",# 征信报告
         "other":"[\"{\"title\": \"这是资料标题1\",\"remark\": \"这是资料说明1\",\"images\":\"http://qiniu.hsbro.cn/1545898825805_身份证(1).jpg\"},"
                 "{\"title\": \"这是资料标题2\",\"remark\": \"这是资料说明2\",\"images\":\"http://qiniu.hsbro.cn/1545898825805_身份证(1).jpg\"}]",# 其他资料
         "provinceId": "440000",# 省ID
         "cityId":"440300", # 市ID
         "areaId":"440305",# 区ID
         "provinceName":"广东省",
         "cityName":"深圳市",
         "areaName":"南山区",
         "payroll":image,# 银行流水
         "businessId":"0",# 业务ID  不填写或为0：保理一业务  2：保理二业务
         "utilityBill":image,# 水电单
        })
        print("提交认证：%s" %self.r.json())

    def testOrder2(self):
        # 登录
        self.login(address="login_v2/index",account="19667893203",password="c4ca4238a0b923820dcc509a6f75849b")
        # 导入Excel
        self.upload(address="publics_v2/excelImport",files={'file':('1.xls',open('C:\\Users\\Tony\\Desktop\\1.xls','rb'),'xls'),})
        # Excel返回车辆信息
        carList = self.r.json()["data"]
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

    def testOrder3(self):
        # 参数
        sex = ["男", "女"]
        maritalStatus = ["未婚","已婚无子女","已婚有子女","离异","丧偶","其他"]
        livingCondition = ["商品按揭购房","无按揭购房","公积金按揭购房","自建房","租用","暂住","亲属购房"]
        occupation = ["一般职业","农牧业","渔业","木材森林业","矿业","采石业","交通、运输业","建筑、工程业","制造业","新闻出版、广告业","卫生","娱乐业","文教","宗教","公共事业","商业","金融、保险业","服务业","家庭教育","餐饮、保洁","保姆、护理","特殊护理、室外高空作业","家政其他","家庭管理","治安人员","体育","其他"]
        position = ["高级领导","中级领导","一般员工","其他","未知"]
        companyNature = ["事业机关","国有股份","外资","合资","民营","私营","个体","社会团体"]
        mainSourceIncome = ["经营、租赁所得","工资","投资、佣金","无","其他"]
        carType = ["新车","二手车"]
        powerSystemType = ["新能源","传统动力"]
        netVehiclePrice = random.randrange(100000,100000000,10000)

        if random.choice(carType)=="新车":
            downPayment = netVehiclePrice*0.2
            loanAmount = netVehiclePrice*0.8
        else:
            downPayment = netVehiclePrice * 0.2
            loanAmount = netVehiclePrice * 0.7

        m = random.randrange(1,100000000)
        if m%2==0:
            spouseName = "舒淇"
            spousePhone = phone
            spouseOtherContactMode = "住我家楼下"
            immediateFamilyName = ""
            immediateFamilyPhone = ""
            immediateFamilyRelation = ""
            otherContactName = ""
            otherContactPhone = ""
            otherContactRelation = ""
        elif m%3 == 0:
            spouseName = ""
            spousePhone = ""
            spouseOtherContactMode = ""
            immediateFamilyName = "舒淇"
            immediateFamilyPhone = phone
            immediateFamilyRelation = "兄弟"
            otherContactName = ""
            otherContactPhone = ""
            otherContactRelation = ""
        else:
            spouseName = ""
            spousePhone = ""
            spouseOtherContactMode = ""
            immediateFamilyName = ""
            immediateFamilyPhone =""
            immediateFamilyRelation = ""
            otherContactName = "舒淇"
            otherContactPhone = phone
            otherContactRelation = "兄弟"

        # 登录
        self.login(address="login_v2/index",account="19667893203",password="c4ca4238a0b923820dcc509a6f75849b")
        # 提交保理三订单
        self.post(address="frontend_v2/insuranceorder/saveOrder",params={
            "name":"吴宇超",
            "phone":phone,
            "sex":random.choice(sex),
            "birthday":nowTime,
            "age":18,
            "idCard":"440785199202226310",
            "idCardEffectiveDate":nowTime,
            "idCardBelongAddress":address,
            "maritalStatus":random.choice(maritalStatus),
            "familyPeopleNum":3,
            "householdAddress":address,
            "livingCondition":random.choice(livingCondition),
            "livingAddress":address,
            "jobCompanyName":"宝鸡有一群怀揣着梦想的少年相信在牛大叔的带领下会创造生命的奇",
            "occupation":random.choice(occupation),
            "position":random.choice(position),
            "companyNature":random.choice(companyNature),
            "companyAddress":address,
            "companyPhone":"0755-8888888888",
            "entryDate":nowTime,
            "mainSourceIncome":random.choice(mainSourceIncome),
            "monthlyIncome":1000000000,
            "natureVehicleUse":" 固定自用汽车",
            "brandModel":carName,
            "carType":random.choice(carType),
            "powerSystemType":random.choice(powerSystemType),
            "netVehiclePrice":netVehiclePrice,
            "downPayment":downPayment,
            "loanAmount":loanAmount,
            "loanInstallment":36,
            "spouseName":spouseName,
            "spousePhone":spousePhone,
            "spouseOtherContactMode":spouseOtherContactMode,
            "immediateFamilyName":immediateFamilyName,
            "immediateFamilyPhone":immediateFamilyPhone,
            "immediateFamilyRelation":immediateFamilyRelation,
            "otherContactName":otherContactName,
            "otherContactPhone":otherContactPhone,
            "otherContactRelation":otherContactRelation,
        })

    def test3(self):
        self.login(address="login_v2/index",account="15976427940",password="c4ca4238a0b923820dcc509a6f75849b")
        self.get(address="frontend_v2/insuranceorder/details",params={
            "id":"53",
        })


class testAdmin(unittest.TestCase,port,Base):

    def testOrgVerify(self):
        # 登录
        self.login(address="work_v2/login",account="15976427941",password="c4ca4238a0b923820dcc509a6f75849b")

        # 门店列表
        self.orgList(params={"keywords":orgName})

        # 门店详情
        self.get(address="work_v2/organization/detail",params={"orgId":self.orgId})

        # 获取详情参数
        self.caId = self.r.json()["data"]["caInfo"]["caId"]
        self.companyName = self.r.json()["data"]["name"]
        self.licenseCode = self.r.json()["data"]["licenseCode"]
        self.corporation = self.r.json()["data"]["corporation"]
        self.phone = self.r.json()["data"]["phone"]
        self.idCard = self.r.json()["data"]["idCard"]
        self.businessLicense = self.r.json()["data"]["license"][0]
        self.idCardOn = self.r.json()["data"]["idCardOn"]
        self.idCardOff = self.r.json()["data"]["idCardOff"]
        self.authorizationUrl = self.r.json()["data"]["certificate"]
        self.authorizationLink = self.url1+  "ca/auth?_plat=shop&auth=sms"
        self.signName = self.r.json()["data"]["signName"]
        self.signPhone = self.r.json()["data"]["signPhone"]
        self.signIdCard = self.r.json()["data"]["signIdCard"]
        self.signIdCardOn = self.r.json()["data"]["signIdCardOn"]
        self.signIdCardOff = self.r.json()["data"]["signIdCardOff"]

        # 区域经理列表
        self.get("work_v2/user/clerkList")
        self.clerkId = self.r.json()["data"][0]["id"]
        self.clerkName = self.r.json()["data"][0]["userName"]

        # 框架合同列表
        self.get("work_v2/organization/businessContract")
        self.contractTitle01 = self.r.json()["data"][0]["contract"][0]["contractTitle"]
        self.contractUrl01 = self.r.json()["data"][0]["contract"][0]["contractUrl"]
        self.contractType01 = self.r.json()["data"][0]["contract"][0]["contractType"]
        self.businessType01 = self.r.json()["data"][0]["businessType"]
        self.contractTitle02 = self.r.json()["data"][1]["contract"][0]["contractTitle"]
        self.contractUrl02 = self.r.json()["data"][1]["contract"][0]["contractUrl"]
        self.contractType02 = self.r.json()["data"][1]["contract"][0]["contractType"]
        self.businessType02 = self.r.json()["data"][1]["businessType"]

       # 发送CA授权
        self.post("work_v2/systemconfig/createCa",{
            "type":1, # 1企业 2个人
            "orgId":self.orgId,
            "companyName":self.companyName,
            "licenseCode":self.licenseCode,
            "corporation":self.corporation,
            "phone":self.phone,
            "idCard":self.idCard,
            "businessLicense":self.businessLicense,
            "idCardOn":self.idCardOn,
            "idCardOff":self.idCardOff,
            "authorizationUrl":self.authorizationUrl,
            "authorizationLink":self.authorizationLink,
            "caId":self.caId,
            "signName":self.signName,
            "signPhone":self.signPhone,
            "signIdCard":self.signIdCard,
            "signIdCardOn":self.signIdCardOn,
            "signIdCardOff":self.signIdCardOff,
        })

        # 短信授权申请CA
        self.postNoData("publics_v2/shortMessAuth",{
            "caId":self.caId,
            "phone":self.phone,
            "code":"8432",
            "timestamp":self.timestamp,
        })

        # 业务审核
        contractList = json.dumps([{"contractTitle":self.contractTitle01,
                             "contractUrl":self.contractUrl01,
                             "contractType":self.contractType01,
                             "guid":self.create_uid(),
                             "businessType":self.businessType01,
                             "visible":"false",
                             "contractNo":"",
                             "isUpload":0,
                             "signMethod":0,
                             "caIds":self.caId
                             },{
                             "contractTitle": self.contractTitle02,
                             "contractUrl": self.contractUrl02,
                             "contractType": self.contractType02,
                             "guid":self.create_uid(),
                             "businessType": self.businessType02,
                             "visible":"false",
                             "contractNo": "",
                             "isUpload": 0,
                             "signMethod": 0,
                             "caIds": self.caId}])
        self.post("work_v2/organization/verify",{
            "orgId":self.orgId,
            "clerkId":self.clerkId,
            "clerkName":self.clerkName,
            "contract":contractList,
            "state":1, # -1  拒绝  1：通过
            "remark":u"审核通过",
            "attachment":"",
            "amount":"0",
            "sort":"",
        })

        # 风控审核
        self.post("work_v2/organization/riskVerify",{
            "orgId":self.orgId,
            "state":"1",
            "remark":"审核通过",
            "attachment":Excel,
        })

        # 风控总监审核
        self.post("work_v2/organization/riskDirectorVerify",{
            "orgId": self.orgId,
            "state": "1",
            "remark": "审核通过",
            "attachment": Excel,
            "amount":1000000
        })

        # 运营总监审核
        self.post("work_v2/organization/operationDirectorVerify",{
            "orgId": self.orgId,
            "state": "1",
            "remark": "审核通过",
            "attachment": Excel,
            "amount": 1000000
        })

        # 总经理审核
        self.post("h5_v2/organization/managerVerify",{
            "orgId": self.orgId,
            "state": "1",
            "remark": "审核通过",
            "attachment": Excel,
            "amount": 1000000
        })

    def testVerifyAmount(self):
        self.login(address="work_v2/login",account="15976427941",password="c4ca4238a0b923820dcc509a6f75849b")
        # 保理2业务支持审核结算
        self.post(address="work_v2/orderbatch/verifyAmount",params={
            "settleDate":"2019-08-05",
            "serviceCharge":"46",
            "otherFee":"0.1",
            "reduceFee":"0.68",
            "amount":"395074",
            "batchId":"597",
            "settleId":"59",
            "state":"1",
        })

if __name__=="__main__":
    t = testShop()
    # t.testOrgVerify()
    t.testOrder2()
    # t.test3()
    b = testAdmin()
    # b.testOrgVerify()
    # b.testVerifyAmount()