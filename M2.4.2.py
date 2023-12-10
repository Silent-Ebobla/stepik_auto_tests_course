from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "https://suninjuly.github.io/explicit_wait2.html"
try: 
    browser = webdriver.Chrome()
    browser.get(link)
    

    # Ваш код, который заполняет обязательные поля
    ...
    First = WebDriverWait(browser, 10).until(
       EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
    but = browser.find_element(By.CLASS_NAME, "btn-primary")
    but.click()

    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)

    browser.execute_script("window.scrollTo(0, 200)")
    input = browser.find_element(By.CLASS_NAME, "form-control")
    input.send_keys(y)

    sub = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.ID, "solve"))
    )
    sub.click()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
    