import requests
from bs4 import BeautifulSoup
import pandas as pd
from random import choice
from string import ascii_letters, digits
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


# 生成随机用户名
def generate_username(length):
    characters = ascii_letters + digits
    return "".join(choice(characters) for _ in range(length))


# 生成随机密码
def generate_password(length):
    characters = ascii_letters + digits
    return "".join(choice(characters) for _ in range(length))


# 注册网站账号
def register_account(driver, username, password):
    # 注册地址
    register_url = "https://xxx.register"

    # 打开注册页面
    driver.get(register_url)

    # 填写用户名、密码和确认密码
    driver.find_element_by_id("userName").send_keys(username)
    driver.find_element_by_id("password").send_keys(password)
    driver.find_element_by_id("confirmPassword").send_keys(password)

    # 提交注册表单
    driver.find_element_by_id("submit").click()  # 修改这里

    # 等待网站成功并继续下一步操作
    sleep(3)  # 可根据网速和网站响应时间进行调整


# 主函数
def main():
    # 创建一个空的DataFrame用于保存用户名和密码
    df = pd.DataFrame(columns=["Username", "Password"])

    # 注册计数器
    count = 0

    # 创建ChromeOptions对象
    options = Options()
    options.add_argument("--incognito")

    # 设置Chrome驱动程序路径
    chrome_driver_path = r"chromedriver.exe"

    # 指定Chrome驱动程序路径并传递ChromeOptions对象
    driver = webdriver.Chrome(executable_path=chrome_driver_path, options=options)

    while count < 100:
        # 自动生成用户名和密码
        username = generate_username(8)
        password = generate_password(10)

        # 注册账号
        register_account(driver, username, password)

        # 将用户名和密码添加到DataFrame
        df = df.append({"Username": username, "Password": password}, ignore_index=True)

        # 递增计数器
        count += 1

    # 将DataFrame保存为CSV文件
    df.to_csv("user_accounts.csv", index=False)

    # 关闭浏览器
    driver.quit()


# 执行主函数
if __name__ == "__main__":
    main()
