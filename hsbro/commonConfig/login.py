# coding:utf-8
from selenium import webdriver
from common.base import Base
import time
import commonConfig.testDate as c
# -------------定位元素信息------------ #
loc1 = ("xpath", "//*[@type='tel']")
loc2 = ("xpath", "//*[@type='password']")
loc3 = ("xpath", "//*[@type='button']")
loc4 = ("xpath", "//*[@type='submit']")
loc5 = ("xpath", "//*[@role='button']")
loc6 = ("xpath","//*[@class='el-badge l-margin-r-x2']")
loc7 = ("xpath","//*[@class='l-margin-b']/div[1]")
text_0 = "消息中心"
text_1 = "门店入网"

# test
# config = {
#     "shopName":"15976427495",
#     "shopPwd":"1",
#     "adminName":"15976427941",
#     "adminPwd":"1",
#     "h5Name":"15976427950",
#     "h5Pwd":"1",
#     "h5path":"http://h5.hsbro.com.cn/?_plat=admin",
# }
#live
config = {
    "shopName":"15976427940",
    "shopPwd":"1",
    "adminName":"15976427940",
    "adminPwd":"1",
    "h5path":"http://h5.hsbro.cn/?_plat=admin",
    "h5Name":"15976427941",
    "h5Pwd":"hsb123",
}
def _loginShop(driver, host ,user=config["shopName"], psw=config["shopPwd"]):
    zen = Base(driver)
    driver.maximize_window()
    driver.get(host+"/?_plat=shop")
    zen.sendKeys(loc1, user)
    zen.sendKeys(loc2, psw)
    zen.click(loc3)
    t = zen.get_text(loc6)
    assert text_0 in t

def _loginAdmin(driver, host, user=config["adminName"], psw=config["adminPwd"]):

    zen = Base(driver)
    driver.maximize_window()
    driver.get(host+"/?_plat=admin")
    zen.sendKeys(loc1, user)
    zen.sendKeys(loc2, psw)
    zen.click(loc3)
    time.sleep(2)
    t = zen.get_text(loc6)
    assert text_0 in t

def _loginH5(driver, user=config["h5Name"], psw=config["h5Pwd"],path=config["h5path"]):

    zen = Base(driver)
    driver.set_window_size(500,1100)
    driver.get(path)
    zen.sendKeys(loc1, user)
    zen.sendKeys(loc2, psw)
    zen.click(loc4)
    time.sleep(2)
    t = zen.get_text(loc7)
    assert t == text_1

if __name__ == "__main__":
    driver = webdriver.Chrome()
    _loginH5(driver)