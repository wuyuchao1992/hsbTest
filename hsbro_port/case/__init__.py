
import random,json,re

data = str([{"a":"xxx","c":"xxx"},{"b":"xxx","c":"xxx"}])

def main():
    """因为是[]括起来的data和new_data是个list"""

    # new_data
    new_data = []

    # data
    data = [{"a": "xxx", "c": "xxx"}, {"b": "xxx", "c": "xxx"}]
    print('打印一下data:', end='\t\t')
    print(data)
    print('看看data的类型:', end='\t\t')
    print(type(data))

    for i in data:
        # 使用dumps将list转化为json字符串
        # 并且拼接上父节点的内容
        temp_i = '{"d":' + json.dumps(i) + '}'
        print('打印一下temp_i:', end='\t\t')
        print(temp_i)
        print('看看temp_i的类型:', end='\t')
        print(type(temp_i))

        new_data.append(temp_i)

    print('打印一下new_data:', end='\t')
    print(new_data)
    print('看看new_data的类型:', end='\t')
    print(type(new_data))


if __name__ == '__main__':
    main()