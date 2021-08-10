from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")
    button=browser.find_element_by_id('book')
    book=WebDriverWait(browser,12).until(
        EC.text_to_be_present_in_element((By.ID,'price'),'$100')
    )
    button.click()
    browser.execute_script('window.scrollBy(0,100);')

    x=browser.find_element_by_id('input_value').text
    x_element=calc(x)
    input1=browser.find_element_by_name('text')
    input1.send_keys(x_element)
    button2=browser.find_element_by_id('solve').click()

finally:
    alert=browser.switch_to.alert
    print(alert.text)
    alert.accept()


