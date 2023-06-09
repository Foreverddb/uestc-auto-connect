用脚本在电脑开机时自动登录校园网。

安装Firefox和对应webdriver： https://github.com/mozilla/geckodriver/releases

在py文件中修改：

```python
username = '学号'
password = '密码'
browser_path = 'C:\\Program Files\\Mozilla Firefox\\firefox.exe'  # 火狐浏览器路径
driver_path = 'D:\\WebDriver\\geckodriver-v0.31.0-win32\\geckodriver.exe'  # 火狐浏览器webdriver路径
```

将`.bat`文件加入windows的自动任务：


