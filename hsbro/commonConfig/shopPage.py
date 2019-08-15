# coding:utf-8
from selenium import webdriver
from common.base import Base
from pykeyboard import PyKeyboard
from common.testDate import enterInfo as i
import time
k = PyKeyboard()

"""
page/orderBatch.py
"""

class orgOperation(Base): # inherit Base

    # locator path
    loanButton = ("xpath", ".//span[contains(text(),'申请垫资（保理一 / 保理二 / 投保单）')]")
    businessMode = ("xpath", ".//div[@class='_item'][2]")
    importExcel = ("xpath",".//*[@class='el-button el-button--primary el-button--mini']")
    creditorUserName = ("xpath","//*[@class='l-creditor-list']/div/div[1]/div/div/input")
    creditorPhone = ("xpath","//*[@class='l-creditor-list']/div/div[2]/div/div/input")
    creditorIdCard = ("xpath","//*[@class='l-creditor-list']/div/div[3]/div/div/input")
    creditorAmount = ("xpath","//*[@class='l-creditor-list']/div/div[4]/div/div/input")
    contractName = ("xpath","//*[@class='l-creditor-list']/div/div[5]/div/div/input")
    contractDate = ("xpath","//*[@class='l-creditor-list']/div/div[6]/div/div/input")
    toDayPath = ("xpath","//*[@class='el-date-table']/tbody/tr/td[@class='available today']")
    uploadContract = ("xpath","//*[@class='_btn-plus l-flex-vhc']")
    orgName = ("xpath","//*[@for='companyName']/following-sibling::div/div[1]/input")
    orgLink = ("xpath","//*[@for='linkName']/following-sibling::div/div[1]/input")
    orgPhone = ("xpath","//*[@for='linkPhone']/following-sibling::div/div[1]/input")
    orgAccount = ("xpath","//*[@for='account']/following-sibling::div/div[1]/input")
    orgReAccount = ("xpath","//*[@for='reAccount']/following-sibling::div/div[1]/input")
    orgPayRemark = ("xpath","//*[@for='payRemark']/following-sibling::div/div[1]/input")
    orgProvinceName = ("xpath","//*[@for='provinceName']/following-sibling::div")
    orgProvince = ("xpath","//*[@class='el-cascader-menus el-popper']/ul[1]/li[1]")
    orgCity = ("xpath","//*[@class='el-cascader-menus el-popper']/ul[2]/li[1]")
    orgBank = ("xpath","//*[@placeholder='如：中国工商银行']")
    orgBankName = ("xpath","//*[@class='el-scrollbar__view el-autocomplete-suggestion__list']/li[1]")
    orgBankBranch = ("xpath","//*[@placeholder='如：深圳生态园支行']")
    orgAddress = ("xpath","//*[@placeholder='省市区街道门牌号等']")
    consent = ("xpath","//*[@class='el-checkbox__label']")
    addAgent = ("xpath","//*[@class='_add l-flex-vhc']")
    datumName_1 = ("xpath","//*[@class='l-other-data l-margin-t']/div[1]/div[1]/input")
    datumDescription_1 = ("xpath","//*[@class='l-other-data l-margin-t']/div[1]/div[2]/textarea")
    datumUpload_1 = ("xpath","//*[@class='l-other-data l-margin-t']/div[1]/p/div/div/div/span")
    datumName_2 = ("xpath", "//*[@class='l-other-data l-margin-t']/div[2]/div[1]/input")
    datumDescription_2 = ("xpath", "//*[@class='l-other-data l-margin-t']/div[2]/div[2]/textarea")
    datumUpload_2 = ("xpath", "//*[@class='l-other-data l-margin-t']/div[2]/p/div/div/div/span")
    submit = ("xpath",".//button[@class='el-button el-button--success el-button--small']")
    succ = ("xpath", "//*[@class='l-alert-warn']")

    ExcelPath = ("1.xls")
    picturePath = ("\"2.jpg\" \"1.jpg\"")

    # locator path
    loc01 = ("xpath", ".//span[contains(text(),'申请垫资（保理一 / 保理二 / 投保单）')]")  # 垫资按钮
    loc02 = ("xpath", ".//div[@class='_item'][1]")  # 保理模式
    loc03 = ("xpath", ".//input[@placeholder='请输入车辆车架号']")  # 车架号
    loc04 = ("xpath", ".//input[@placeholder='请输入车辆品牌，车系信息']")  # 车辆品牌,车系
    loc05 = ("xpath", ".//input[@placeholder='选择年月']")  # 车辆生产年份
    loc06 = ("xpath", ".//a[contains(text(),'六月')]")  # 车辆生产月份
    loc07 = ("xpath", ".//input[@placeholder='请输入车身颜色']")  # 车身颜色
    loc08 = ("xpath", ".//input[@placeholder='请输入车辆型号']")  # 车身型号
    loc09 = ("xpath", ".//input[@placeholder='请选择车辆变速箱类型']")  # 变速箱
    loc10 = ("xpath", ".//span[contains(text(),'手动')]")  # 变速箱
    loc11 = ("xpath", ".//input[@placeholder='请输入内饰颜色']")  # 内色
    loc12 = ("xpath", ".//input[@placeholder='请输入与4S店的采购价']")  # 采购价
    loc13 = ("xpath", ".//input[@placeholder='请输入与买方的实际成交价']")  # 实际成交价
    loc14 = ("xpath", ".//input[@placeholder='请输入已付给4S店金额']")  # 已付4S定金
    loc15 = ("xpath", ".//input[@placeholder='请输入买方已交金额']")  # 车主已交定金
    loc16 = ("xpath", ".//input[@placeholder='选择日期']")  # 提车日期
    loc17 = ("xpath", "//*[@x-placement='top-start']/div/div/div[2]/table[1]/tbody//td[@class='available today']")  # 选择当天
    loc18 = ("xpath", ".//input[@placeholder='请输入需要垫资的金额']")  # 垫资金额
    loc19 = ("xpath", ".//div[@class='l-panel-item l-margin-t']/div/div/div[16]/div/div/div/div/div/div/div[2]/a")  # 上传定金凭证
    loc20 = ("xpath", ".//div[@class='l-panel-item l-margin-t']/div/div/div[17]/div/div/div/div/div/div/div[2]/a")  # 上车购车合同
    loc21 = ("xpath", ".//div[@class='l-panel-item'][1]/div[2]/div/div[1]/div/div/input")  # 上牌方姓名
    loc22 = ("xpath", ".//div[@class='l-panel-item'][1]/div[2]/div/div[2]/div/div/input")  # 上牌方手机号码
    loc23 = ("xpath", ".//div[@class='l-panel-item'][1]/div[2]/div/div[3]/div/div/input")  # 上牌方身份证号码
    loc24 = ("xpath", ".//div[@class='l-panel-item'][1]/div[2]/div/div[4]/div/div/input")  # 上牌方地址
    loc25 = ("xpath", ".//div[@class='l-panel-item'][2]/div[2]/div/div[1]/div/div/input")  # 4S店户名
    loc26 = ("xpath", ".//div[@class='l-panel-item'][2]/div[2]/div/div[2]/div/div/input")  # 4S店联系人
    loc27 = ("xpath", ".//div[@class='l-panel-item'][2]/div[2]/div/div[3]/div/div/input")  # 4S店联系人电话
    loc28 = ("xpath", ".//div[@class='l-panel-item'][2]/div[2]/div/div[4]/div/div/input")  # 4S地址
    loc29 = ("xpath", ".//input[@placeholder='请输入公司对公收款账号']")  # 4S对公账户
    loc30 = ("xpath", ".//input[@placeholder='请再次输入对公收款账号']")  # 4S对公账户
    loc31 = ("xpath", ".//span[@class='el-cascader__label']")  # 收款账号所属省市
    loc32 = ("xpath", ".//*[@class='el-cascader-menus el-popper']/ul[1]/li[3]")  # 河北省
    loc33 = ("xpath", ".//*[@class='el-cascader-menus el-popper']/ul[2]/li[3]")  # 石家庄
    loc34 = ("xpath", ".//input[@placeholder='如：中国工商银行']")  # 收款账号银行名称
    loc35 = ("xpath", ".//ul[@class='el-scrollbar__view el-autocomplete-suggestion__list']/li[1]")  # 国家开发银行
    loc36 = ("xpath", ".//input[@placeholder='如：深圳生态园支行']")  # 支行名称
    loc37 = ("xpath", ".//input[@placeholder='请输入打款备注']")  # 打款备注
    loc38 = ("xpath", ".//label[@class='el-checkbox']")  # 同意协议
    loc39 = ("xpath", ".//button[@class='el-button el-button--success el-button--small']")  # 提交
    loc40 = ("xpath", ".//input[@placeholder='请输入车辆官方指导价']")  # 指导价
    loc41 = ("xpath",".//span[@class='el-checkbox__inner']")
    loc_new = ("xpath", "/html/body/div[1]/section/section/main/section/main/form")


    # module_1
    def order(self):
        self.click(self.loc01)
        time.sleep(1)
        self.click(self.loc02)
        self.sendKeys(self.loc03,i["frameNumber"])
        self.sendKeys(self.loc04,i["carName"])
        self.click(self.loc05)
        self.click(self.loc06)
        self.sendKeys(self.loc07,i["color"])
        self.sendKeys(self.loc08,i["style"])
        self.click(self.loc09)
        self.click(self.loc10)
        self.sendKeys(self.loc11,i["interiorColor"])
        self.sendKeys(self.loc12,i["purchasePrice"])
        self.sendKeys(self.loc13,i["price"])
        self.sendKeys(self.loc14,i["paidDeposit"])
        self.sendKeys(self.loc40,i["guidePrice"])
        self.sendKeys(self.loc15,i["deposit"])
        self.click(self.loc16)
        time.sleep(1)
        self.click(self.loc17)
        self.sendKeys(self.loc18,i["adjustAmount"])
        self.click(self.loc19)
        time.sleep(1)
        k.type_string(self.picturePath)
        time.sleep(1)
        k.tap_key(k.enter_key)
        time.sleep(1)
        self.click(self.loc20)
        k.type_string(self.picturePath)
        time.sleep(1)
        k.tap_key(k.enter_key)
        time.sleep(1)
        self.js_focus_element(self.loc38)
        self.sendKeys(self.loc21,i["userName"])
        self.sendKeys(self.loc22,i["phone"])
        self.sendKeys(self.loc23,i["idCard"])
        self.sendKeys(self.loc24,i["address"])
        self.sendKeys(self.loc25,i["shopName"])
        self.sendKeys(self.loc26,i["orgLink"])
        self.sendKeys(self.loc27,i["orgPhone"])
        self.sendKeys(self.loc28,i["orgAddress"])
        self.sendKeys(self.loc29,i["account"])
        self.sendKeys(self.loc30,i["account"])
        self.click(self.loc31)
        self.click(self.loc32)
        self.click(self.loc33)
        self.click(self.loc34)
        self.click(self.loc35)
        self.sendKeys(self.loc36,i["bankBranch"])
        self.sendKeys(self.loc37,i["payRemark"])
        self.click(self.loc41)
        self.click(self.loc39)

    # module_2
    def orderBath(self):
        self.click(self.loanButton)
        time.sleep(1)
        self.click(self.businessMode)
        time.sleep(1)
        self.click(self.importExcel)
        time.sleep(1)
        k.type_string(self.ExcelPath)
        time.sleep(1)
        k.tap_key(k.enter_key)
        self.sendKeys(self.creditorUserName,i["userName"])
        self.sendKeys(self.creditorPhone,i["phone"])
        self.sendKeys(self.creditorIdCard,i["idCard"])
        self.sendKeys(self.creditorAmount,i["adjustAmount"])
        self.sendKeys(self.contractName,i["contractName"])
        self.click(self.contractDate)
        time.sleep(1)
        self.click(self.toDayPath)
        self.click(self.uploadContract)
        time.sleep(2)
        k.type_string(self.picturePath)
        time.sleep(2)
        k.tap_key(k.enter_key)
        self.js_focus_element(self.consent)
        self.sendKeys(self.orgName,i["shopName"])
        self.sendKeys(self.orgLink,i["orgLink"])
        self.sendKeys(self.orgPhone,i["orgPhone"])
        self.sendKeys(self.orgAccount,i["account"])
        self.sendKeys(self.orgReAccount,i["account"])
        self.sendKeys(self.orgPayRemark,i["payRemark"])
        self.click(self.orgProvinceName)
        self.click(self.orgProvince)
        self.click(self.orgCity)
        self.click(self.orgBank)
        self.click(self.orgBankName)
        self.sendKeys(self.orgBankBranch,i["bankBranch"])
        self.sendKeys(self.orgAddress,i["orgAddress"])
        self.click(self.consent)
        # self.click(self.addAgent)
        self.click(self.submit)
        time.sleep(6)

    def is_add_order_sucess(self,_text):
        return self.is_text_in_element(self.succ, _text)

if __name__ == "__main__":
    from commonConfig.login import _loginShop
    driver = webdriver.Firefox()
    _loginShop(driver, "http://admin.hsbro.cn")
    bug = orgOperation(driver)
    bug.orderBath()
    time.sleep(10)
