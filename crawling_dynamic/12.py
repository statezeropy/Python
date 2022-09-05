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
chrome.get("https://shopping.naver.com") # 페이지 이동

# 원하는게 로딩될 때까지 대기
#WebDriverWait(chrome, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[name=query")))

# id
# 강의와 버전이 달라서 문법이 달라짐
#el = chrome.find_element(By.CSS_SELECTOR, 'input[class="_searchInput_search_input_QXUFf"]')

# tiem wait + id - 강의랑 문법이랑 CSS_SELECTOR 값이 달라서 모르겠다
#time.sleep(3)
wait = WebDriverWait(chrome, 3)
#el = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[class=_searchInput_search_input_QXUFf]")))


def find(wait, CSS_selector):
    return wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, CSS_selector)))
search = find(wait, "input[class=_searchInput_search_input_QXUFf]")
search.send_keys("아이폰 케이스\n") # \n 엔터를 침
time.sleep(3)

# 엔터치면 구현 불필요
#button = find(wait, "button[class=_searchInput_button_search_1n1aw]")
#button.click()
#time.sleep(3)

chrome.close() # 페이지 닫기