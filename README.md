用脚本在电脑开机时自动登录校园网。

安装Firefox和对应webdriver： https://github.com/mozilla/geckodriver/releases

在py文件中修改：

```python
username = '学号'
password = '密码'
browser_path = 'C:\\Program Files\\Mozilla Firefox\\firefox.exe'  # 火狐浏览器路径
driver_path = 'D:\\WebDriver\\geckodriver-v0.31.0-win32\\geckodriver.exe'  # 火狐浏览器webdriver路径
```

将`auto-connect.bat`文件加入windows的自动任务：

1. 右键点击“此电脑”，选择“管理”，打开“任务计划程序”：
![image](https://github.com/Foreverddb/uestc-auto-connect/assets/60093071/7b44ace6-96b4-4b1a-86a5-4a6610530d57)

2. 点击创建任务，选择对应的脚本文件路径，设定在windows用户登陆时触发即可。一般来说输完密码进入桌面就已经连上了：
![image](https://github.com/Foreverddb/uestc-auto-connect/assets/60093071/949662d0-8e38-462b-835e-2fdca951a8b5)

