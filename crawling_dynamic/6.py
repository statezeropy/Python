from selenium import webdriver
import time

options = webdriver.ChromeOptions()
options.add_argument("windows-size=1000,1000") 
options.add_argument("no-sandbox") 
#options.add_argument("headless") # 팝업 스킵

chrome = webdriver.Chrome("C:\python\crawling_dynamic\chromedriver.exe", options=options)
chrome.get("https://naver.com")
chrome.get("https://shopping.naver.com")
chrome.back()
chrome.forward()

time.sleep(3)
chrome.close()