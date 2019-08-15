# coding:utf-8
from selenium import webdriver
from datetime import datetime
from py.xml import html
import pytest
import commonConfig.testDate as c

_driver = None

def pytest_addoption(parser):
    '''添加命令行参数--browser、--host'''
    parser.addoption(
        "--browser", action="store", default="firefox", help="browser option: firefox or chrome"
             )
    # 添加host参数,设置默认测试环境地址
    parser.addoption(
        "--host", action="store", default="http://admin.hsbro.com.cn", help="test host->http://admin.hsbro.com.cn"
    )

@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
    当测试失败的时候,自动截图,展示到html报告中
    :param item:
    """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_")+".png"
            screen_img = _capture_screenshot()
            if file_name:
                html = '<div><img src="data:image/png;base64,%s" alt="screenshot" style="width:600px;height:300px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % screen_img
                extra.append(pytest_html.extras.html(html))
        report.extra = extra
        report.description = str(item.function.__doc__)
        report.nodeid = report.nodeid.encode("utf-8").decode("unicode_escape")


@pytest.mark.optionalhook
def pytest_html_results_table_header(cells):
    cells.insert(1, html.th('Description'))
    cells.insert(2, html.th('Test_nodeid'))
    cells.pop(2)

@pytest.mark.optionalhook
def pytest_html_results_table_row(report, cells):
    cells.insert(1, html.td(report.description))
    cells.insert(2, html.td(report.nodeid))
    cells.pop(2)


# @pytest.mark.hookwrapper
# def pytest_runtest_makereport(item, call):
#     outcome = yield
#     report = outcome.get_result()
#     report.description = str(item.function.__doc__)

def _capture_screenshot():
    '''
    截图保存为base64
    :return:
    '''
    return _driver.get_screenshot_as_base64()

@pytest.fixture(scope='session')
def driver(request):
    '''定义全局driver参数'''
    global _driver
    if _driver is None:
        name = request.config.getoption("--browser")
        if name == "firefox":
            _driver = webdriver.Firefox()
        elif name == "chrome":
            _driver = webdriver.Chrome()
        else:
            _driver = webdriver.Firefox()
        print("\n正在启动浏览器名称：%s" % name)

    def fn():
        print("\n当全部用例执行完之后：teardown quit driver！")
        _driver.quit()
    request.addfinalizer(fn)
    return _driver

@pytest.fixture(scope='session')
def host(request):
    '''全局host参数'''
    return request.config.getoption("--host")