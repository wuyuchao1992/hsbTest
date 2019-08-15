# coding:utf-8
import time
import random
s = random.randint(1001,9999)
x = 19767890000
phone = s+x
timerStr = time.strftime("%Y-%m-%d")

orderInfo = {
    "frameNumber":"LHGGM6665K2023191",
    "carName":u"广汽本田",
    "style":u"锋范 2018款 1.5L CVT 型动版",
    "color":u"珍珠白",
    "interiorColor":u"黑色",
    "purchasePrice":"40,000",        # 4S采购价
    "paidDeposit":"1,000",           # 已付4S订金
    "price":"38,000",                # 客户购买价
    "deposit":"2,000",               # 客户已付订金
    "guidePrice":"98,000",           # 官方指导价
    "userName":u"唐宛如",           # 上牌方姓名
    "phone":"18888888888",          # 上牌方联系电话
    "idCard":"43012119821012484X",  # 上牌方身份证
    "address":u"深圳市南山区深圳湾83栋A座",        # 上牌方地址
    "adjustAmount":"22,000",                        # 垫资金额
    "shopName":u"梅州市嘉骏贸易有限公司",          # 4S店联系账户名
    "orgAddress":u"广东省梅州市梅县区政府200米",   # 4S店联系地址
    "orgLink":u"王国富",                           # 4S店联系人
    "orgPhone":"18888888888",                      # 4S店联系人电话
    "account":"6212262012002653779",               # 对公收款账户
    "bankBranch":u"南山区创维支行",                 # 支行名称
    "bankName":u"国家开发银行",
    "rate":u"0.2",
    "remark":u"没毛病",
    "payRemark":u"替xxxx打款",
    "gearbox":u"手动",
    "type":u"标配",
    "contractName":u"汽车购销合同0000482",
}

enterInfo = {
    "frameNumber":"LHGGM6665K2023191",
    "carName":u"广汽本田",
    "style":u"锋范 2018款 1.5L CVT 型动版",
    "color":u"珍珠白",
    "interiorColor":u"黑色",
    "purchasePrice":"40000",        # 4S采购价
    "paidDeposit":"1000",           # 已付4S订金
    "price":"38000",                # 客户购买价
    "deposit":"2000",               # 客户已付订金
    "guidePrice":"98000",           # 官方指导价
    "userName":u"唐宛如",           # 上牌方姓名
    "phone":"18888888888",          # 上牌方联系电话
    "idCard":"43012119821012484X",  # 上牌方身份证
    "address":u"深圳市南山区深圳湾83栋A座",        # 上牌方地址
    "adjustAmount":"22000",                        # 垫资金额
    "shopName":u"梅州市嘉骏贸易有限公司",          # 4S店联系账户名
    "orgAddress":u"广东省梅州市梅县区政府200米",   # 4S店联系地址
    "orgLink":u"王国富",                           # 4S店联系人
    "orgPhone":"18888888888",                      # 4S店联系人电话
    "account":"6212262012002653779",               # 对公收款账户
    "bankBranch":u"南山区创维支行",                 # 支行名称
    "bankName":u"国家开发银行",
    "rate":u"0.2",
    "remark":u"没毛病",
    "payRemark":u"替xxxx打款",
    "gearbox":u"手动",
    "type":u"标配",
    "contractName":u"汽车购销合同0000482",
    "datumName_1":u"请款资料",
    "datumDescription_1":u"蓝晓玉请款资料",
    "day":u"15",
    "logisticsName":u"中汽物流",
    "logisticsNumber":"粤J8888",
    "otherFee":"100",
    "reduceFee":"0.1",
}

bathInfo = {
    "amount":"117,920",
    "carName":u"广汽丰田 雷凌 2017款 185T G CVT 精英版",
    "creditorAmount":"22,000",
    "creditorName":u"唐宛如",
    "creditorPhone":"18888888888",
    "creditorIdCard":"43012119821012484X",
    "contractName":"汽车购销合同0000482",
    "contractDate":timerStr,
    "orgName":u"梅州市嘉骏贸易有限公司",
    "orgAddress":u"广东省梅州市梅县区政府200米",
    "orgLink":u"王国富",
    "orgPhone":"18888888888",
    "orgAccount":u"6212262012002653779",
    "bankName":u"国家开发银行",
    "payMark":u"替xxxx打款",
}

path = {
    "admin":"http://admin.hsbro.com.cn/?_plat=admin",
    "shop":"http://admin.hsbro.com.cn/?_plat=shop",
    "h5":"http://h5.hsbro.com.cn/?_plat=admin",
}

orgInfo = {
    "account":phone,
    "orgName":u"深圳市花生兄弟网络科技有限公司",
    "orgAddress":u"南山区海街道高新南九道10号深圳湾科技生态园10栋A座11层1109室",
    "licenseCode":"91440300MA5EYH9X8H",
    "orgAccount":"6212262012002653779",
    "orgBankBranch":"中国工商银行国才支行",
    "orgCorporation":"徐康",
    "orgIdCard":"440785199202226310",
    "orgEmail":"123456@163.com",
    "verify":u"123abcxxx",
    "signName":u"吴宇超",
    "signPhone":"15976427940",

}

# Config = {
#     "adminUse":"15976427940",
#     "adminPwd":"1",
#     "shopUse":"19967890007",
#     "shopPwd":"hsb123456",
#     "h5Use":"15976427941",
#     "h5Pwd":"hsb123",
#     "host":"http://admin.hsbro.cn",
#     "h5Host":"http://h5.hsbro.cn",
# }

db={
    "dbAddress":"rm-wz983ak9fczo42c563o.mysql.rds.aliyuncs.com",
    "dbName":"peanut_online",
    "user":"peanut_test",
    "pswd":"ivystudio2018"
}
