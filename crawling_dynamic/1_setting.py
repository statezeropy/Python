from time import time
# 크롬 버전 확인 후
# 크롬 드라이버 다운로드
# https://chromedriver.chromium.org/downloads
# pip3 install selenium

from selenium import webdriver
import time

browser = webdriver.Chrome("./chromedriver.exe")
browser.get("http://naver.com")
time.sleep(3)
browser.close()