from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import os
import pyperclip # 클립보드 사용

options = webdriver.ChromeOptions()
options.add_argument("windows-size=1000,1000") 
options.add_argument("no-sandbox") 

chrome = webdriver.Chrome("C:\python\crawling_dynamic\chromedriver.exe", options=options)
chrome.get("https://shopping.naver.com") # 페이지 이동

wait = WebDriverWait(chrome, 10) # 최대로 기다리는 시간이 10초
short_wait = WebDriverWait(chrome, 3) # 최대로 기다리는 시간이 3초


""" login_button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a#gnb_login_button")))
login_button.click() # 로그인 버튼 클릭

input_id = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input#id")))
input_pw = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input#pw")))

pyperclip.copy("nashirah23")
input_id.send_keys(Keys.CONTROL, "v")
pyperclip.copy("passwd")
input_pw.send_keys(Keys.CONTROL, "v")
input_pw.send_keys("\n") # 로그인을 위한 엔터
 """

# 검색창
search = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[class=_searchInput_search_input_QXUFf]")))
search.send_keys("아이폰 케이스")
time.sleep(1) # 1초 대기. 원인 모를 에러 발생
search.send_keys("\n") # 검색


# 검색 후 보일때 까지 대기 후 클릭
#wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div[class^=basicList_info_area__")))
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a[class^=basicList_link__"))).click()
time.sleep(2)

#print(chrome.window_handles)
# 두번째 텝으로 이동
chrome.switch_to.window(chrome.window_handles[1])
#print(chrome.title) # 텝이동 후 텝 제목 출력

# 옵션 선택
# 기다리기
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "select[id^=product_option_id]")))
# 클릭
options = chrome.find_elements(By.CSS_SELECTOR, "select[id^=product_option_id]")


options[0].click()
time.sleep(0.1)

# 옵션 선택 방법 -두가지
chrome.find_element((By.CSS_SELECTOR, "select[id^=product_option_id] li:nth-child(3)")).click()
#chrome.find_elements(By.CSS_SELECTOR, "select[id^=product_option_id] option[*]")[3].click()

options[1].click()
time.sleep(0.1)

# 구매 버튼


time.sleep(3)
#chrome.close() # 페이지 닫기
chrome.quit() # 크롬 전체를 끔