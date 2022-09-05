from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

options = webdriver.ChromeOptions()
options.add_argument("windows-size=1000,1000") 
options.add_argument("no-sandbox") 
#options.add_argument("headless") # 팝업 스킵

chrome = webdriver.Chrome("C:\python\crawling_dynamic\chromedriver.exe", options=options)
#chrome.get("https://naver.com") # 페이지 이동
chrome.get("https://shopping.naver.com") # 페이지 이동

#chrome.back() # 페이지 뒤로가기
#chrome.forward() # 페이지 앞으로가기

# 로딩할때 대기 하는 방법
#time.sleep(3)
#chrome.implicitly_wait(3)


# 원하는게 로딩될 때까지 대기
#WebDriverWait(chrome, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[name=query")))

# id
# 강의와 버전이 달라서 문법이 달라짐
el = chrome.find_element(By.CSS_SELECTOR, 'input[class="_searchInput_search_input_QXUFf"]')

# tiem wait + id - 강의랑 문법이랑 CSS_SELECTOR 값이 달라서 모르겠다
#wait = WebDriverWait(chrome, 10)
#el = wait.until(chrome.find_element(By.CSS_SELECTOR, 'input[class="_searchInput_search_input_QXUFf"]'))
print(el)
chrome.close() # 페이지 닫기