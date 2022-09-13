from tokenize import group
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import os
import pyperclip # 클립보드 사용
from datetime import datetime # 날짜

dt = datetime.now()
DATE = dt.strftime("%m%d")
print(DATE)

options = webdriver.ChromeOptions()
options.add_argument("windows-size=1000,1900") 
options.add_argument("no-sandbox")
options.add_argument("--ignore-certificate-errors")
options.add_argument("--ignore-ssl-errors")


chrome = webdriver.Chrome("C:\python\crawling_dynamic\chromedriver.exe", options=options)
chrome.get("https://117.52.152.4/") # 페이지 이동

wait = WebDriverWait(chrome, 10) # 최대로 기다리는 시간이 10초
short_wait = WebDriverWait(chrome, 3) # 최대로 기다리는 시간이 3초

# 로그인
input_id = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input#txtUserId")))
input_pw = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input#txtUserPw")))

pyperclip.copy("kimjy")
input_id.send_keys(Keys.CONTROL, "v")
pyperclip.copy("youhost8287!")
input_pw.send_keys(Keys.CONTROL, "v")
input_pw.send_keys("\n")

# 관리 메뉴 선택
chrome.get("https://117.52.152.4/mng/report/list.do")
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a[class=btn_sm]"))).click()

# 팝업된 텝으로 이동
chrome.switch_to.window(chrome.window_handles[1])
#print(chrome.current_url)

# 제목 입력
#wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input#report_name")))
report_name = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input#report_name")))
report_name.send_keys("biddata_CPU_", DATE)

# 기간설정 주단위
week = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[value=WEEK]")))
week.click()

# 그룹 선택 # 빅데이터
#group = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="tree"]/ul/li/ul/li/ul/li[7]/span/a')))
#print(group.text)
group = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="tree"]/ul/li/ul/li/ul/li[7]/span/span[2]')))
group.click()

# 보고서 생성하기
create = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="makeReport"]/span')))
create.click()
time.sleep(2)

# 알람 처리
alert = chrome.switch_to.alert
alert.accept()
time.sleep(1)
alert.accept()
time.sleep(1)

# 탭 전환
chrome.switch_to.window(chrome.window_handles[0])
print(chrome.current_url)

# 보고서 검색하기
time.sleep(10)
search_report = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="con_area"]/div/table[1]/tbody/tr/td[3]/a/span')))
search_report.click()

# 보고서 다운로드
wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="row0"]/td[3]/a/span'))).click()

# 보고서 삭제
wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="row0"]/td[5]/a'))).click()
alert = chrome.switch_to.alert
alert.accept()
time.sleep(1)
alert.accept()
time.sleep(5)

#chrome.close() # 페이지 닫기
chrome.quit() # 크롬 전체를 끔