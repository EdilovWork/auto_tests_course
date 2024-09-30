# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import math
# import time
#
# # Расчёт зашифрованного текста
# link_text = str(math.ceil(math.pow(math.pi, math.e) * 10000))
#
# # Открытие страницы и поиск ссылки
# link = "http://suninjuly.github.io/find_link_text"
#
# try:
#     browser = webdriver.Chrome()
#     browser.get(link)
#
#     # Поиск ссылки по зашифрованному тексту и переход по ней
#     secret_link = browser.find_element(By.LINK_TEXT, link_text)
#     secret_link.click()
#
#     # Заполнение формы
#     input1 = browser.find_element(By.TAG_NAME, "input")
#     input1.send_keys("Ivan")
#     input2 = browser.find_element(By.NAME, "last_name")
#     input2.send_keys("Petrov")
#     input3 = browser.find_element(By.CLASS_NAME, "form-control.city")
#     input3.send_keys("Smolensk")
#     input4 = browser.find_element(By.ID, "country")
#     input4.send_keys("Russia")
#     button = browser.find_element(By.CSS_SELECTOR, "button.btn")
#     button.click()
#
# finally:
#     # успеваем скопировать код за 30 секунд
#     time.sleep(30)
#     # закрываем браузер после всех манипуляций
#     browser.quit()
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    browser = webdriver.Chrome()
    browser.get("https://suninjuly.github.io/registration2.html")

    # Заполнение формы
    input1 = browser.find_element(By.NAME, "first_name")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.NAME, "last_name")
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.CLASS_NAME, "city")
    input3.send_keys("Smolensk")
    input4 = browser.find_element(By.ID, "country")
    input4.send_keys("Russia")

    # Поиск кнопки с текстом "Submit" по XPath и клик по ней
    button = browser.find_element(By.XPATH, '//button[text()="Submit"]')
    button.click()

finally:
    # Успеваем скопировать код за 30 секунд
    time.sleep(30)
    # Закрываем браузер после всех манипуляций
    browser.quit()
