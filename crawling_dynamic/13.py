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

# a tag의 id로 접근 가능
# element가 생성되는 것까지만 확인하기 때문에 클릭이 안되서 오류 발생 가능성 있음
#login_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "a#gnb_login_button")))
# 보이는 것 확인
login_button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a#gnb_login_button")))
print(login_button.text) # 테스트
login_button.click() # 로그인 버튼 클릭

input_id = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input#id")))
input_pw = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input#pw")))


# 캡차에 막힘
#input_id.send_keys("nashirah23")
#input_pw.send_keys("rlawnepd23!")
#input_pw.send_keys("\n") # 로그인을 위한 엔터

# pip install pyperclip
pyperclip.copy("nashirah23")
input_id.send_keys(Keys.CONTROL, "v")
#input_id.send_keys(Keys.COMMAND, "V") # MAC 버전용
pyperclip.copy("passwd")
input_pw.send_keys(Keys.CONTROL, "v")
input_pw.send_keys("\n") # 로그인을 위한 엔터


# 로그인 확인. 로그아웃 버튼확인
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a#gnb_logout_button")))



time.sleep(3)



chrome.close() # 페이지 닫기