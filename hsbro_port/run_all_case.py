#coding:utf-8
import unittest
import HTMLTestRunner
import os

def all_case():
    # 执行用例目录
    case_dir = "C:\\Python35\\hsbro_prot\\case"
    testCase = unittest.TestSuite()
    discover = unittest.defaultTestLoader.discover(case_dir,pattern="test*.py",top_level_dir=None)

    for test_suite in discover:
        for test_case in test_suite:
            # 添加用例到testCase
            testCase.addTests(test_case)
    print(testCase)
    return testCase
if __name__=="__main__":
    # 返回实例
    runner = unittest.TextTestRunner()
    cwd = os.getcwd()
    fp = open(cwd,"wb")
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,
                                           title=u'自动化测试报告',
                                           description=u'用例执行情况:' )
    runner.run(all_case())
    fp.close()

