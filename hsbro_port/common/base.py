import hashlib,time,unittest,requests,json,uuid
# 获取时间戳并去除小数点
ticks = str(time.time()).replace('.','')
timestamp = ticks[:-4]
# 账号密码
account = "15976427940"
password = "c4ca4238a0b923820dcc509a6f75849b"

class Base():
    # MD5加密
    def md5(self, str, salt='DFHGKZLSE2NFDEHGFHHR4XTGBKHY67EJZ8IK9'):
        str = str + salt
        m = hashlib.md5()
        m.update(str.encode(encoding="utf-8"))
        return m.hexdigest()

    # 按键盘排序用&拼接起来
    def sort(self,params):
        keys = params.keys()
        tmp_list = []
        for item in keys:
            tmp_list.append(item)
        tmp_list.sort()
        tmp_content = ''
        for item in tmp_list:
            tmp_content += item + '=' + str(params[item]) + '&'
        return tmp_content[:-1]

    # 生成唯一UUID
    def create_uid(self):
        return str(uuid.uuid1())

if __name__ == "__main__":
    unittest.main()
