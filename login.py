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
import io
from io import BytesIO





driver = webdriver.Chrome()
driver.headers ={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36",}
driver.get("http://www.taobao.com")
login = driver.find_element_by_xpath("//div[@class='site-nav-sign']//a")
print(login.get_attribute("outerHTML"))
login.click()
time.sleep(2)
loo = driver.find_element_by_id("fm-login-id")
loo.send_keys("17516821129")
loo = driver.find_element_by_id("fm-login-password")
loo.send_keys("17516821129xdq")
com = driver.find_element_by_class_name("fm-btn")
print(com.get_attribute("outerHTML"))
slider = driver.find_element_by_xpath("//span[contains(@class, 'btn_slide')]")
print(slider.get_attribute("outerHTML"))
action = ActionChains(driver)
time.sleep(10)
if not slider.is_displayed():
    print("4546")
    #action.click_and_hold(slider).perform()
    #action.move_to_element_with_offset(slider, 300, 0).perform()
    action.drag_and_drop_by_offset(slider, 300, 0).perform()
    action.pause(0.5)
    action.release().perform()
com.click()


#com.click()
#blo = driver.find_element_by_id("baxia-password")
#print(blo.get_attribute("outerHTML"))
#blo.click()
'''time.sleep(3)
slider = driver.find_element_by_class_name("nc_iconfont")
action = ActionChains(driver)
if slider.is_displayed():
    action.click_and_hold(on_element=slider).perform()
    action.move_by_offset(xoffset=300, yoffset=0).perform()
    action.pause(0.5).release().perform()
'''
#com.click()
#print(driver.find_element_by_class_name("nc_iconfont").get_attribute("outerHTML"))

#button = driver.find_element_by_id("baxia-password")
#button = driver.find_element_by_xpath("//div[@class='baxia-container tb-login']")
#print(aaa.get_attribute("outerHTML"))
#action.move_to_element(button).click_and_hold(button)
#action.drag_and_drop_by_offset(button, 300, 0).perform()
#action.release()
#loo.click()
