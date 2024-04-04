from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random
import string

chrome_options = webdriver.ChromeOptions()
chrome_options.headless = False
chrome_options.add_argument('--start-maximized')

# ожидание кликабельности элемента по селектору
def el_to_be_clickable(CSS_SELECTOR):
    en_af = WebDriverWait(browser, 1200, 1).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, CSS_SELECTOR))
        )

def el_to_be_clicable_XP(XPATH):
    en_af = WebDriverWait(browser, 1200, 1).until(
            EC.element_to_be_clickable((By.XPATH, XPATH))
        )

def el_not_clicable_XP(XPATH):
    en_af = WebDriverWait(browser, 1200, 1).until(
            EC.element_to_be_clickable((By.XPATH, XPATH))
        )

def not_presence_el_loc(CSS_SELECTOR):
    WebDriverWait(browser, 1200).until_not(
        EC.presence_of_element_located((By.CSS_SELECTOR, CSS_SELECTOR))
    )

def random_alphanumeric_string(length):
    return ''.join(
        random.choices(
            string.ascii_letters + string.digits,
            k=length
        )
    )

def do_something_quiz(link, i=0):
    
    if i:
        browser.execute_script("window.open('');")
        browser.switch_to.window(browser.window_handles[i])
    browser.get(link)
    el_to_be_clickable('[aria-label="Ваше имя или никнейм"]')
    browser.find_element(By.CSS_SELECTOR, '[aria-label="Ваше имя или никнейм"]').send_keys(random_alphanumeric_string(15))

    # Клик по кнопке ДАЛЕЕ
    el_to_be_clickable('.q-btn__content')
    browser.find_element(By.CSS_SELECTOR, '.q-btn__content').click()


def open_n_tabs(n, link):
    try:
        for i in range(n):
            do_something_quiz(link, i)
        for _ in range(50):
            el_to_be_clickable('[style=""]')
            for i in range(n):
                browser.switch_to.window(browser.window_handles[i])
                browser.find_element(By.CSS_SELECTOR,
                                '.flex.fit>.col>button:nth-child({})'.format(random.randint(1, 4))).click()
                time.sleep(0.2)
            el_to_be_clicable_XP("//div[text()=' Ожидайте следующий вопрос ']")
    finally:
        time.sleep(5)

browser = webdriver.Chrome(options=chrome_options)
link = 'https://start.1t.ru/1tquiz/#/reg'
open_n_tabs(5, link)
