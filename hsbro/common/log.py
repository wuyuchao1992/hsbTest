# coding=utf-8
import time,os
import importlib,sys
importlib.reload(sys)

now = time.strftime("%Y-%m-%d")
current_dir = os.getcwd()
layer_dir = os.path.dirname(os.getcwd())

# 判断当前执行用例所在路径是否  ./case 或 ./page
if current_dir.endswith("case") or current_dir.endswith("page"):
    logPath = "../testReport/"
elif current_dir.endswith("case"): # 判断当前执行用例所在路径是否  ./case
    logPath = "./testReport/"
elif layer_dir.endswith("page"): # 判断当前执行用例所在上一层路径是否  ./page
    logPath = "../../testReport/"
else:
    print("获取日志文件路径失败")


def mkdir(path):
    # 去除首位空格
    path = path.strip()
    # 去除尾部 \ 符号
    path = path.rstrip("\\")
    # 判断路径是否存在 存在   True 不存在   False
    isExists = os.path.exists(path)

    # 判断结果
    if not isExists:
        # 如果不存在则创建目录
        # 创建目录操作函数
        os.makedirs(path)
        print (path + ' 创建成功')
        return True
    else:
        # 如果目录存在则不创建,并提示目录已存在
        # print path + ' 目录已存在'
        return False

# 调用函数

ScreenshotPath = logPath +"Screenshot_"+now+"/"

# 新建log文件
def log(temp):
    logTime = time.strftime("%Y-%m-%d %H:%M:%S")
    # 创建日志文件,每天一个文件,追加写入
    lp = logPath + "log" + now + ".log"
    f = open(lp, 'a')
    f.write(str(logTime) + "  " + temp + "\n")

# 新建elog文件
def elog(temp):
    logTime = time.strftime("%Y-%m-%d %H:%M:%S")
    # 创建异常日志文件,每天一个文件,追加写入
    lp = logPath + "elog" + now + ".log"
    f = open(lp, 'a')
    f.write(str(logTime) + "  " + temp + "\n")

# 截图保存
def getScreenshotAsFile(driver,name):
    mkdir(ScreenshotPath)
    t = time.strftime("%Y-%m-%d_%H%M%S")
    # imgName = t +"_"+ funcName +"aaaa.png"
    imgName = t + "_" + name + ".png"
    path = ScreenshotPath + imgName
    try:
        driver.get_screenshot_as_file(path)
        log("图片【"+imgName+"】保存成功,保存路径【"+path+"】")
    except:
        log("截图保存失败！")

# 执行报错,输出错误日志及报错行号公共用例
def runError(driver,testCaseName,testStepName):
    exc_type, exc_obj, exc_tb = sys.exc_info()
    item = "Error,用例【" + testCaseName + "】第【"+str(exc_tb.tb_lineno)+"】行执行失败,请重新调试！"
    print(item)
    log(item)
    getScreenshotAsFile(driver, testStepName)
    elog(item)
    driver.quit()  # 关闭浏览器
    log("关闭浏览器")