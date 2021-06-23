
class Utility:
    driver = None
    # 从指定的路径中读取json文件内容
    @classmethod
    def get_json(cls,path):
        import json
        with open(path,encoding='utf8') as file:
           contents = json.load(file)
        return contents

    # 获取driver并打开初始url
    @classmethod
    def get_driver(cls,path):
        from selenium import webdriver
        if cls.driver == None:
            contents = cls.get_json(path)
            # 根据模块找到该模块名字为browser的对象
            driver = getattr(webdriver, contents['browser'])()
            driver.implicitly_wait(10)
            driver.get(contents['URL'])
        return driver

    # 对输入文本框执行点击、清理及输入三步操作
    @classmethod
    def input(cls,ele,value):
        ele.click()
        ele.clear()
        ele.send_keys(value)

    # 从excel读取测试信息。path是excel的路径，sheet_name是sheet页的名字，r,s是从第几行到第几行，m是测试数据，n是预期结果
    @classmethod
    def get_xls(cls, path, sheet_name, r, s, m, n):
        import xlrd
        workbook = xlrd.open_workbook(path)
        contents = workbook.sheet_by_name(sheet_name)
        test_data = []

        for i in range(r, s):
            data = contents.cell(i, m).value
            expect = contents.cell(i, n).value
            temp = data.split('\n')
            d = {}
            for t in temp:
                d[t.split('=')[0]] = t.split('=')[1]
            d['expect'] = expect
            test_data.append(d)

        return test_data

    # 根据不同方式判断某个元素是否存在
    @classmethod
    def is_element_present(cls, driver, how, what):
        from selenium.common.exceptions import NoSuchElementException
        try:
            driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    # 断言两个字符串是否相同
    @classmethod
    def assert_equal(cls,expect,actual):
        if expect == actual:
            return True
        else:
            return False
if __name__ == '__main__':
    test_data = Utility.get_xls('..\\testdata\\woniusales_test_cases.xlsx','login',1,5,3,4)
    print(test_data)