import selenium.webdriver.firefox.webdriver
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service

username = '学号'
password = '密码'
browser_path = 'C:\\Program Files\\Mozilla Firefox\\firefox.exe'  # 火狐浏览器路径
driver_path = 'D:\\WebDriver\\geckodriver-v0.31.0-win32\\geckodriver.exe'  # 火狐浏览器webdriver路径

driver: selenium.webdriver.firefox.webdriver.WebDriver

def connect():
    global driver
    try:
        url = 'http://192.168.9.8/srun_portal_pc?ac_id=1&theme=pro'

        option = webdriver.FirefoxOptions()
        option.headless = False
        option.binary_location = browser_path
        print('正在打开浏览器')
        driver = webdriver.Firefox(
            service=Service(executable_path=driver_path),
            options=option
        )

        print('正在进入网页')
        WAIT = WebDriverWait(driver, 10)
        driver.get(url)

        print('输入账号密码')
        username_input = WAIT.until(
            ec.presence_of_element_located((By.CSS_SELECTOR, '#username'))
        )
        password_input = WAIT.until(
            ec.presence_of_element_located((By.CSS_SELECTOR, '#password'))
        )
        username_input.send_keys(username)
        password_input.send_keys(password)

        print('正在获取登录按钮')
        btn = WAIT.until(
            ec.presence_of_element_located((By.CSS_SELECTOR, '#login-account'))
        )
        print('点击登录')
        btn.click()

        print('登录成功')
        driver.close()
    except:
        driver.close()
        connect()


if __name__ == '__main__':
    connect()
