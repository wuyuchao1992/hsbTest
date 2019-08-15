# coding:utf-8
from common.base import Base
from commonConfig.adminPage import bath
from common.testDate import path as p
import time as t

import pytest

class TestAddOrg():

    @pytest.fixture(scope='function',autouse=True)
    def base(self,driver):
        self.driver = Base(driver)
        self.o = bath(driver)
    @pytest.mark.addOrg
    @pytest.mark.usefixtures("loginAdmin_0")
    def test_addOrg(self,driver):
        print("\n-------- 区域经理添加门店&业务支持 --------")
        self.o.adminAreaManagerAddOrg()

    # @pytest.mark.managerVerifyOrg
    # @pytest.mark.usefixtures("loginH5")
    # def test_verifyOrg(self,driver):
    #     print("\n-------- 总经理添审核门店 --------")
    #     self.o.h5VerifyOrg()
    #     driver.delete_all_cookies()
    #
    #
    # @pytest.mark.signC1B1Admin
    # def test_signC1B1Admin(self,driver):
    #     print("\n-------- 后台签署C1B1 --------")
    #     driver.maximize_window()
    #     driver.get(p["admin"])
    #     self.o.adminOrgDetial()
    #     self.o.signC1B1()
    #     print("\n-------- 门店签署C1B1 --------")
    #     loc1 = ("xpath", "//*[@type='tel']")
    #     loc2 = ("xpath", "//*[@type='password']")
    #     loc3 = ("xpath", "//*[@type='button']")
    #     loc4 = ("xpath","//*[@class='l-table-02']/tr[1]/td[2]")
    #     account = self.driver.get_text(loc4)
    #     password = account[5:11]
    #     driver.get(p["shop"])
    #     self.driver.sendKeys(loc1,account)
    #     self.driver.sendKeys(loc2,password)
    #     self.driver.click(loc3)
    #     t.sleep(2)
    #     self.o.shopOrgDetial()
    #     self.o.signC1B1()
if __name__ == "__main__":
    pytest.main(["-v", "-s","--count==10","--repeat-scope=class","test_AddOrg2.py"])