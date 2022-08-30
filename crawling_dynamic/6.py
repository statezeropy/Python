from selenium import webdriver
import time

chrome = webdriver.Chrome("./chromedriver.exe")
time.sleep(3)
chrome.close()