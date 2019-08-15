import pytest
from commonConfig.loginPage import _loginAdmin
from commonConfig.loginPage import _loginShop
from commonConfig.loginPage import _loginH5

@pytest.fixture(scope='session')
def loginAdmin_0(driver, host):
    _loginAdmin(driver, host)

@pytest.fixture(scope='session')
def loginAdmin_1(driver, host):
    _loginAdmin(driver, host)

@pytest.fixture(scope='session')
def loginAdmin_2(driver, host):
    _loginAdmin(driver, host)

@pytest.fixture(scope='session')
def loginAdmin_3(driver, host):
    _loginAdmin(driver, host)

@pytest.fixture(scope='session')
def loginAdmin_4(driver, host):
    _loginAdmin(driver, host)

@pytest.fixture(scope='session')
def loginAdmin_5(driver, host):
    _loginAdmin(driver, host)

@pytest.fixture(scope='session')
def loginAdmin_6(driver, host):
    _loginAdmin(driver, host)

@pytest.fixture(scope='session')
def loginShop_0(driver, host):
    _loginShop(driver, host)

@pytest.fixture(scope='session')
def loginShop_1(driver, host):
    _loginShop(driver, host)

@pytest.fixture(scope='session')
def loginShop_2(driver, host):
    _loginShop(driver, host)

@pytest.fixture(scope='session')
def loginShop_3(driver, host):
    _loginShop(driver, host)

@pytest.fixture(scope='session')
def loginShop_4(driver, host):
    _loginShop(driver, host)

@pytest.fixture(scope='session')
def loginShop_5(driver, host):
    _loginShop(driver, host)

@pytest.fixture(scope='session')
def loginShop_6(driver, host):
    _loginShop(driver, host)

@pytest.fixture(scope='session')
def loginH5_0(driver):
    _loginH5(driver)

@pytest.fixture(scope='session')
def loginH5_1(driver):
    _loginH5(driver)

@pytest.fixture(scope='session')
def loginH5_2(driver):
    _loginH5(driver)
