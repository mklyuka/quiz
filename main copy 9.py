from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random
import pytest

chrome_options = webdriver.ChromeOptions()
chrome_options.headless = False
chrome_options.add_argument('--start-maximized')
browser = webdriver.Chrome(options=chrome_options)

# ожидание кликабельности элемента по селектору
def el_to_be_clickable(CSS_SELECTOR):
    en_af = WebDriverWait(browser, 1200, 1).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, CSS_SELECTOR))
        )

def el_to_be_clicable_XP(XPATH):
    en_af = WebDriverWait(browser, 100, 1).until(
            EC.element_to_be_clickable((By.XPATH, XPATH))
        )

def el_not_clicable_XP(XPATH):
    en_af = WebDriverWait(browser, 100, 1).until(
            EC.element_to_be_clickable((By.XPATH, XPATH))
        )

def not_presence_el_loc(CSS_SELECTOR):
    WebDriverWait(browser, 1200).until_not(
        EC.presence_of_element_located((By.CSS_SELECTOR, CSS_SELECTOR))
    )

#Словарь имен
names = ['Максим', 'Михаил', 'Александр', 'Дмитрий', 'Денис', 'Илья', 'Андрей', 'Даниил', 'Артём', 'Иван', 'Алексей', 'Никита',
         'Павел', 'Евгений', 'Анна', 'Мария', 'Юлия', 'Алёна', 'Анастасия', 'Екатерина', 'Дарья', 'Ксения', 'Кристина', 'Алиса',
         'Shura', '@Marshal@', 'Park Gorkogo', 'Антон Палыч Чехов', 'Достоевский Ф. М.']

try:
    link = 'https://start.1t.ru/1tquiz/#/reg'
    browser.get(link)

    # Ввод имени в поле ввода
    el_to_be_clickable('[aria-label="Ваше имя или никнейм"]')
    browser.find_element(By.CSS_SELECTOR, '[aria-label="Ваше имя или никнейм"]').send_keys(random.choice(names))

    # Клик по кнопке ДАЛЕЕ
    el_to_be_clickable('.q-btn__content')
    browser.find_element(By.CSS_SELECTOR, '.q-btn__content').click()

    for i in range(50):
        el_to_be_clickable('[style=""]')
        time.sleep(random.randint(4, 12))

        browser.find_element(By.CSS_SELECTOR, '.flex.fit>.col>button:nth-child({})'.format(random.randint(1, 4))).click()

        el_to_be_clicable_XP("//div[text()=' Ожидайте следующий вопрос ']")
        el_not_clicable_XP("//div[text()=' Ожидайте следующий вопрос ']")



finally:
    time.sleep(5)
    browser.quit()