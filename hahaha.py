from selenium import webdriver
import time
import requests
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import requests
from bs4 import BeautifulSoup
import io
from io import BytesIO

driver = webdriver.Chrome()
driver.headers ={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36",}
driver.get("https://sso.nankai.edu.cn/sso/login?service=http%3A%2F%2Feamis.nankai.edu.cn%2Feams%2Flogin.action%3Bjsessionid%3D999EB7768CD5EC5E2E864D9035644E06")
driver.maximize_window()
name = driver.find_element_by_xpath("//ul[@class='loginBox']//input[@class='input n']")
name.send_keys("1911666")
passwo = driver.find_element_by_xpath("//ul[@class='loginBox']//input[@class='input p']")
passwo.send_keys("xdq17516821129")
button = driver.find_element_by_id("btn")

action = ActionChains(driver)
action.drag_and_drop_by_offset(button, 300, 0).perform()

log = driver.find_element_by_class_name("btn")
log.click()
time.sleep(5)
sco = driver.find_element_by_id("main")
sci = sco.find_element_by_xpath("//script")
print(sci.get_attribute("outerHTML"))
time.sleep(5)

#url = driver.current_url

#sco = driver.find_element_by_xpath("//body//table[@id='mainTable']//td//div[@id='menu_panel']//ul[@class='menu collapsible']")
#sco = driver.find_element_by_class_name('scroll_box')
#r = requests.get(url)





