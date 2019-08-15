from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from commonConfig.testDate import db as d
import pymysql

class Base():
    '''基于原生的selenium做二次封装'''

    def __init__(self, driver):
        self.driver = driver
        self.timeout = 10
        self.t = 0.5

    def findElement(self, locator):
        '''定位到元素,返回元素对象,没定位到,Timeout异常'''
        if not isinstance(locator, tuple):
            print('locator参数类型错误,必须传元祖类型：loc = ("id", "value1")')
        else:
            print("定位方式->%s, value值->%s"%(locator[0], locator[1]))
            ele = WebDriverWait(self.driver, self.timeout, self.t).until(EC.presence_of_element_located(locator))
            return ele

    def findElements(self, locator):
        if not isinstance(locator, tuple):
            print('locator参数类型错误,必须传元祖类型：loc = ("id", "value1")')
        else:
            try:
                print("定位方式->%s, value值->%s"%(locator[0], locator[1]))
                eles = WebDriverWait(self.driver, self.timeout, self.t).until(EC.presence_of_all_elements_located(locator))
                return eles
            except:
                return []

    def sendKeys(self, locator, text=''):
        ele = self.findElement(locator)
        ele.send_keys(text)

    def click(self, locator):
        ele = self.findElement(locator)
        ele.click()

    def clear(self, locator):
        ele = self.findElement(locator)
        ele.clear()

    def isSelected(self, locator):
        '''判断元素是否被选中,返回bool值'''
        ele = self.findElement(locator)
        r = ele.is_selected()
        return r

    def isElementExist(self, locator):
        try:
            self.findElement(locator)
            return True
        except:
            return False

    def is_title(self, _title=''):
        '''返回bool值'''
        try:
            result = WebDriverWait(self.driver, self.timeout, self.t).until(EC.title_is(_title))
            return result
        except:
            return False

    def is_title_contains(self, _title=''):
        '''返回bool值'''
        try:
            result = WebDriverWait(self.driver, self.timeout, self.t).until(EC.title_contains(_title))
            return result
        except:
            return False

    def is_text_in_element(self, locator, _text=''):
        '''返回bool值'''
        if not isinstance(locator, tuple):
            print('locator参数类型错误,必须传元祖类型：loc = ("id", "value1")')
        try:
            result = WebDriverWait(self.driver, self.timeout, self.t).until(EC.text_to_be_present_in_element(locator, _text))
            return result
        except:
            return False

    def is_value_in_element(self, locator, _value=''):
        '''返回bool值, value为空字符串,返回Fasle'''
        if not isinstance(locator, tuple):
            print('locator参数类型错误,必须传元祖类型：loc = ("id", "value1")')
        try:
            result = WebDriverWait(self.driver, self.timeout, self.t).until(EC.text_to_be_present_in_element_value(locator, _value))
            return result
        except:
            return False

    def is_alert(self, timeout=3):
        '''判断alert,存在返回alert实例,不存在,返回false'''
        try:
            result = WebDriverWait(self.driver, timeout, self.t).until(EC.alert_is_present())
            return result
        except:
            return False

    def get_title(self):
        '''获取title'''
        return self.driver.title

    def get_text(self, locator):
        '''获取文本'''
        try:
            t = self.findElement(locator).text
            return t
        except:
            print("获取text失败,返回'' ")
            return ""

    def get_attribute(self, locator, name):
        '''获取属性'''
        try:
            element = self.findElement(locator)
            return element.get_attribute(name)
        except:
            print("获取%s属性失败,返回'' "%name)
            return ""

    def js_focus_element(self, locator):
        '''聚焦元素'''
        target = self.findElement(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", target)

    def js_scroll_top(self):
        '''滚动到顶部'''
        js = "window.scrollTo(0,0)"
        self.driver.execute_script(js)

    def js_scroll_end(self,x=0):
        '''滚动到底部'''
        js = "window.scrollTo(%s,document.body.scrollHeight)"%x
        self.driver.execute_script(js)

    def select_by_index(self, locator, index=0):
        '''通过索引,index是索引第几个,从0开始,默认选第一个'''
        element = self.findElement(locator)  # 定位select这一栏
        Select(element).select_by_index(index)

    def select_by_value(self, locator, value):
        '''通过value属性'''
        element = self.findElement(locator)
        Select(element).select_by_value(value)

    def select_by_text(self, locator, text):
        '''通过文本值定位'''
        element = self.findElement(locator)
        Select(element).select_by_visible_text(text)

    def switch_iframe(self, id_index_locator):
        '''切换iframe'''
        try:
            if isinstance(id_index_locator, int):
                self.driver.switch_to.frame(id_index_locator)
            elif isinstance(id_index_locator, str):
                self.driver.switch_to.frame(id_index_locator)
            elif isinstance(id_index_locator, tuple):
                ele = self.findElement(id_index_locator)
                self.driver.switch_to.frame(ele)
        except:
             print("iframe切换异常")

    def switch_handle(self, value):
        '''切换窗口'''
        handles = self.driver.window_handles
        self.driver.switch_to.window(handles[value])

    def switch_alert(self):
        r = self.is_alert()
        if not r:
            print("alert不存在")
        else:
            return r

    def move_to_element(self, locator):
        '''鼠标悬停操作'''
        ele = self.findElement(locator)
        ActionChains(self.driver).move_to_element(ele).perform()

    def dragAndDrag(self,firstXpath,lastXpath):
        '''元素拉动元素'''
        try:
            ele1 = self.findElement(firstXpath)
            ele2 = self.findElement(lastXpath)
            ActionChains(self.driver).drag_and_drop(ele1,ele2).perform()
        except:
            print("dragAndDrag元素拉动异常")

    def selcetSQL(self,sql):
        # 连接数据库
        hostvalue = d["dbAddress"]
        uservalue = d["user"]
        passwordvalue = d["pswd"]
        dbvalue = d["dbName"]
        portvalue = 3306
        connection = pymysql.connect(host=hostvalue, user=uservalue, password=passwordvalue, db=dbvalue,
                             port=portvalue, charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
        # 通过cursor创建游标
        cursor = connection.cursor()
        # 创建sql 语句,并执行
        sqlvalue = sql  # "select * from user"
        cursor.execute(sqlvalue)
        result = cursor.fetchone()  # 查询数据库单条数据
        # result = cursor.fetchall() #查询数据库多条数据
        cursor.close()
        return result

    def getUrl(self, url):
        try:
            self.driver.get(url)  # 地址栏输入url
        except:
            print("打开地址异常：%s"%url)

if __name__ == "__main__":

    driver = webdriver.Firefox()
    web = Base(driver)
    driver.get("https://home.cnblogs.com/u/yoyoketang")
    loc_1 = ("id", "header_user_left")
    t = web.get_text(loc_1)
    print(t)

