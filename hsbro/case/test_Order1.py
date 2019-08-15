# coding:utf-8
from common.base import Base
import pytest
from commonConfig.testDate import orderInfo as i
from commonConfig.shopPage import orgOperation

class TestAddOrder():
    # loctor
    loc_amount=("xpath","//*[@class='l-panel-item l-margin-b']/div[1]/span/i")
    loc_carName=("xpath","//*[@class='l-panel-item l-margin-b']/div[2]/div[1]/p/b")
    loc_productDate=("xpath","//*[@class='l-panel-item l-margin-b']/div[2]/div[1]/div[1]/p[1]/span[1]")
    loc_gearbox=("xpath","//*[@class='l-panel-item l-margin-b']/div[2]/div[1]/div[1]/p[1]/span[2]")
    loc_type=("xpath","//*[@class='l-panel-item l-margin-b']/div[2]/div[1]/div[1]/p[1]/span[3]")
    loc_color=("xpath","//*[@class='l-panel-item l-margin-b']/div[2]/div[1]/div[1]/p[2]/span[1]")
    loc_interiorColor=("xpath","//*[@class='l-panel-item l-margin-b']/div[2]/div[1]/div[1]/p[2]/span[2]")
    loc_guidePrice=("xpath","//*[@class='l-panel-item l-margin-b']/div[2]/div[1]/div[1]/p[2]/span[3]/i")
    loc_purchasePrice=("xpath","//*[@class='l-panel-item l-margin-b']/div[2]/div[1]/div[2]/p[1]/span[1]/i")
    loc_paidDeposit=("xpath","//*[@class='l-panel-item l-margin-b']/div[2]/div[1]/div[2]/p[1]/span[2]/i")
    loc_price=("xpath","//*[@class='l-panel-item l-margin-b']/div[2]/div[1]/div[2]/p[2]/span[1]/i")
    loc_deposit=("xpath","//*[@class='l-panel-item l-margin-b']/div[2]/div[1]/div[2]/p[2]/span[2]/i")
    loc_userName=("xpath","//*[@class='l-layout-left l-margin-r']/div[1]/div[2]/table/tr[1]/td[2]")
    loc_phone=("xpath","//*[@class='l-layout-left l-margin-r']/div[1]/div[2]/table/tr[2]/td[2]")
    loc_idCard=("xpath","//*[@class='l-layout-left l-margin-r']/div[1]/div[2]/table/tr[3]/td[2]")
    loc_address=("xpath","//*[@class='l-layout-left l-margin-r']/div[1]/div[2]/table/tr[4]/td[2]")
    loc_orgName=("xpath","//*[@class='l-layout-left l-margin-r']/div[2]/div[2]/table/tr[1]/td[2]")
    loc_orgAddress=("xpath","//*[@class='l-layout-left l-margin-r']/div[2]/div[2]/table/tr[2]/td[2]")
    loc_orgLink=("xpath","//*[@class='l-layout-left l-margin-r']/div[2]/div[2]/table/tr[3]/td[2]")
    loc_orgPhone=("xpath","//*[@class='l-layout-left l-margin-r']/div[2]/div[2]/table/tr[4]/td[2]")
    loc_orgAccount=("xpath","//*[@class='l-layout-left l-margin-r']/div[2]/div[2]/table/tr[5]/td[2]")
    loc_bankName=("xpath","//*[@class='l-layout-left l-margin-r']/div[2]/div[2]/table/tr[6]/td[2]")
    loc_payMark=("xpath","//*[@class='l-layout-left l-margin-r']/div[2]/div[2]/table/tr[7]/td[2]")

    # info
    orderInfo_data = [
        (loc_amount, i["adjustAmount"]),
        (loc_carName, i["carName"] + " " + i["style"]),
        (loc_gearbox, i["gearbox"]),
        (loc_type, i["type"]),
        (loc_color, i["color"]),
        (loc_interiorColor, i["interiorColor"]),
        (loc_guidePrice, i["guidePrice"]),
        (loc_purchasePrice, i["purchasePrice"]),
        (loc_paidDeposit, i["paidDeposit"]),
        (loc_price, i["price"]),
        (loc_deposit, i["deposit"]),
        (loc_userName, i["userName"]),
        (loc_phone, i["phone"]),
        (loc_idCard, i["idCard"]),
        (loc_address, i["address"]),
        (loc_orgName, i["shopName"]),
        (loc_orgAddress, i["orgAddress"]),
        (loc_orgLink, i["orgLink"]),
        (loc_orgPhone, i["orgPhone"]),
        (loc_orgAccount, i["account"]),
        (loc_bankName, i["bankName"] + " " + i["bankBranch"]),
        (loc_payMark, i["payRemark"])
    ]

    @pytest.fixture(scope="function",autouse=True)
    def base(self,driver):
        self.shop = Base(driver)
        self.o = orgOperation(driver)

    @pytest.mark.addOrder
    @pytest.mark.usefixtures("loginShop_0")
    def test_addOrder(self,driver):
        print("-------- 保理1下单测试 --------")
        self.o.order()

    @pytest.mark.orderInfo
    @pytest.mark.parametrize("loc_orderInfo_x, text", orderInfo_data)
    def test_checkOrderInfo(self, loc_orderInfo_x, text):
        """汽贸店详情-用例"""

        t1 = self.shop.get_text(loc_orderInfo_x)
        assert text in t1

if __name__ == "__main__":
    pytest.main(["-v", "test_Order1.py"])