# cmd 명령어 실행
# 도커 실행
# docker run -p 4444:4444 selenium/standalone-chrome

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

browser = webdriver.Remote("http://127.0.0.1:4444/wb/hub", DesiredCapabilities.CHROME)
browser.get("http:naver.com")
print(browser.title)
browser.close()