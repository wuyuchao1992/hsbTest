# coding:utf-8
from common.base import Base
import pytest
from common.testDate import bathInfo as i
from common.testDate import path as p
from commonConfig.shopPage import orgOperation
from commonConfig.adminPage import bath
import time

# 订单详情定位
loc_amount = ("xpath","//*[@class='_hd l-border-b']/span/i")
loc_carName = ("xpath","/html/body/div/section/section/main/section/main/div[2]/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[2]/div")
loc_creditorAmount = ("xpath","//*[@class='l-layout-left']/div[1]/div[2]/div/div/p[1]/b")
loc_creditorName = ("xpath","//*[@class='l-layout-left']/div[1]/div[2]/div/div/p[2]")
loc_creditorPhone = ("xpath","//*[@class='l-layout-left']/div[1]/div[2]/div/div/p[3]")
loc_creditorIdCard = ("xpath","//*[@class='l-layout-left']/div[1]/div[2]/div/div/p[4]")
loc_contractName = ("xpath","//*[@class='l-layout-left']/div[1]/div[2]/div/div/p[5]")
loc_contractDate = ("xpath","//*[@class='l-layout-left']/div[1]/div[2]/div/div/p[6]")
loc_orgName = ("xpath","//*[@class='l-table-02']/tr[1]/td[2]")
loc_orgAddress = ("xpath","//*[@class='l-table-02']/tr[7]/td[2]")
loc_orgLink = ("xpath","//*[@class='l-table-02']/tr[2]/td[2]")
loc_orgPhone = ("xpath","//*[@class='l-table-02']/tr[3]/td[2]")
loc_orgAccount = ("xpath","//*[@class='l-table-02']/tr[4]/td[2]")
loc_bankName = ("xpath","//*[@class='l-table-02']/tr[5]/td[2]")
loc_payMark = ("xpath","//*[@class='l-table-02']/tr[6]/td[2]")

# 订单详情测试数据
orderInfo_data = [
    (loc_amount, i["amount"]),
    (loc_carName,i["carName"]),
    (loc_creditorAmount,i["creditorAmount"]),
    (loc_creditorName,i["creditorName"]),
    (loc_creditorPhone,i["creditorPhone"]),
    (loc_creditorIdCard,i["creditorIdCard"]),
    (loc_contractName,i["contractName"]),
    (loc_contractDate,i["contractDate"]),
    (loc_orgName,i["orgName"]),
    (loc_orgAddress,i["orgAddress"]),
    (loc_orgLink,i["orgLink"]),
    (loc_orgPhone,i["orgPhone"]),
    (loc_orgAccount,i["orgAccount"]),
    (loc_bankName,i["bankName"]),
    (loc_payMark,i["payMark"]),
]
class TestAddOrder():

    loc_01 = ("xpath", "//*[@type='button']")
    loc_02 = ("xpath","//*[@class='van-tab van-tab--active']/span")
    loc_03 = ("xpath","//*[@class='l-form']/div[1]/span")
    text_01 = "登录"
    text_02 = "待处理"
    text_03 = "登录账号"

    @pytest.fixture(scope="function",autouse=True)
    def base(self,driver):
        self.driver = Base(driver)
        self.o = bath(driver)

    @pytest.mark.addB2
    @pytest.mark.usefixtures("loginShop_0")
    def test_addOrder(self,driver):
        print("-------- 保理2下单测试 --------")
        o = orgOperation(driver)
        o.orderBath()

    @pytest.mark.orderInfo
    @pytest.mark.parametrize("loc_orderInfo_x, text", orderInfo_data)
    def test_checkOrderInfo(self, loc_orderInfo_x, text,driver):
        '''汽贸店详情-用例'''
        t = self.driver.get_text(loc_orderInfo_x)
        assert text in t

    def test_logout(self,driver):
        driver.delete_all_cookies()
        self.o.Drop()
        t = self.driver.get_text(self.loc_01)
        assert t in self.text_01

    @pytest.mark.verifyOrder
    @pytest.mark.usefixtures("loginAdmin_0")
    def test_virfyOrder(self, driver):
        print("\n-------- 保理2审核测试 --------")
        self.o.adminVerifyB2()
        driver.delete_all_cookies()
        self.o.Drop()
        t = self.driver.get_text(self.loc_01)
        assert t in self.text_01

    @pytest.mark.managerVerify
    @pytest.mark.usefixtures("loginH5_0")
    def test_managerVerify(self,driver):
        print("\n-------- 总经理审核测试 ---------")
        self.o.h5VerifyOrder_B2()
        t1 = self.driver.get_text(self.loc_02)
        assert t1 in self.text_02
        driver.delete_all_cookies()
        self.o.h5Drop()
        t2 = self.driver.get_text(self.loc_03)

    @pytest.mark.signC2
    @pytest.mark.usefixtures("loginAdmin_1")
    def test_signC2(self,driver):
        print("/n-------- 后台C2签署测试 ---------")
        self.o.adminB2Detail()
        self.o.signC2()
        driver.delete_all_cookies()
        self.o.Drop()
        t = self.driver.get_text(self.loc_01)
        assert t in self.text_01

    @pytest.mark.signC2C3
    @pytest.mark.usefixtures("loginShop_1")
    def test_signC2C3(self,driver):
        print("/n--------- 门店C2C3签署测试 ---------")
        self.o.shopB2Detail()
        self.o.signC2Shop()
        self.o.signC3Shop()
        driver.delete_all_cookies()
        self.o.Drop()
        t = self.driver.get_text(self.loc_01)
        assert t in self.text_01

    @pytest.mark.logistics
    @pytest.mark.usefixtures("loginAdmin_2")
    def test_logistics(self,driver):
        print("/n---------- 物流下单以及验车 ---------")
        # driver.get(p["admin"])
        self.o.adminLogistics()
        driver.delete_all_cookies()
        self.o.Drop()
        t = self.driver.get_text(self.loc_01)
        assert t in self.text_01

    @pytest.mark.checkCarVerify
    @pytest.mark.usefixtures("loginShop_2")
    def test_checkCarVerify(self,driver):
        print("/n-------- 门店验车 --------")
        self.o.shopCheckCar()
        driver.delete_all_cookies()
        self.o.Drop()
        t = self.driver.get_text(self.loc_01)
        assert t in self.text_01

    @pytest.mark.verifyTicket
    @pytest.mark.usefixtures("loginAdmin_3")
    def test_verifyTicket(self,driver):
        print("/n--------- 收齐票证 --------")
        self.o.adminReceiveTicket()
        self.o.signC3_1()
        driver.delete_all_cookies()
        self.o.Drop()
        t = self.driver.get_text(self.loc_01)
        assert t in self.text_01

    @pytest.mark.signC3_1Shop
    @pytest.mark.usefixtures("loginShop_3")
    def test_signC3_1Shop(self,driver):
        print("/n-------- 门店签署C3 --------")
        # driver.get(p["shop"])
        self.o.shopB2Detail()
        self.o.signC3_1Shop()
        driver.delete_all_cookies()
        self.o.Drop()
        t = self.driver.get_text(self.loc_01)
        assert t in self.text_01

    @pytest.mark.managerVerifyLoan
    @pytest.mark.usefixtures("loginH5_1")
    def test_managerVerifyLoan(self,driver):
        print("/n-------- 总经理同意放款 --------")
        # driver.set_window_size(500,1100)
        # driver.get(p["h5"])
        self.o.h5VerifyLoan()
        driver.delete_all_cookies()
        self.o.h5Drop()
        t2 = self.driver.get_text(self.loc_03)
        assert t2 in self.text_03

    @pytest.mark.confirm
    @pytest.mark.usefixtures("loginAdmin_4")
    def test_confirm(self,driver):
        print("/n-------- 财务确认放款 --------")
        # driver.maximize_window()
        # driver.get(p["admin"])
        self.o.adminConfirmLoan()
        driver.delete_all_cookies()
        self.o.Drop()
        t = self.driver.get_text(self.loc_01)
        assert t in self.text_01

    @pytest.mark.shopSettlement
    @pytest.mark.usefixtures("loginShop_4")
    def test_shopSettlement(self,driver):
        print("/n-------- 结算申请 --------")
        # driver.get(p["shop"])
        self.o.shopSettlement()
        driver.delete_all_cookies()
        self.o.Drop()
        t = self.driver.get_text(self.loc_01)
        assert t in self.text_01

    @pytest.mark.adminSettlement
    @pytest.mark.usefixtures("loginAdmin_5")
    def test_adminVerifySettlement(self,driver):
        print("/n-------- 审核结算 --------")
        # driver.get(p["admin"])
        self.o.adminVerifySettlement()
        driver.delete_all_cookies()
        self.o.Drop()
        t = self.driver.get_text(self.loc_01)
        assert t in self.text_01

    @pytest.mark.h5allowCar
    @pytest.mark.usefixtures("loginH5_2")
    def test_h5AllowCar(self,driver):
        print("/n-------- 同意放车 --------")
        self.o.h5AllowCar()
        driver.delete_all_cookies()
        self.o.h5Drop()
        t2 = self.driver.get_text(self.loc_03)
        assert t2 in self.text_03

    @pytest.mark.sendTicket
    @pytest.mark.usefixtures("loginAdmin_6")
    def test_sendTicket(self, driver):
        print("/n-------- 寄出票证 --------")
        self.o.adminSendTicket()
        driver.delete_all_cookies()
        self.o.Drop()
        t = self.driver.get_text(self.loc_01)
        assert t in self.text_01


if __name__ == "__main__":
    pytest.main(["-v", "test_Order2.py"])