from selenium import webdriver
from multiprocessing import Pool
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random

# I remove global driver because you cannot use shared driver in multiprocess.
def driver():  
    driver = webdriver.Chrome()
    return driver
 
def test_func(link):
    driver = driver()
    print('start')
    names = ['Максим', 'Михаил', 'Александр', 'Дмитрий', 'Денис', 'Илья', 'Андрей', 'Даниил', 'Артём', 'Иван', 'Алексей', 'Никита',
        'Павел', 'Евгений', 'Анна', 'Мария', 'Юлия', 'Алёна', 'Анастасия', 'Екатерина', 'Дарья', 'Ксения', 'Кристина', 'Алиса',
        'Shura', '@Marshal@', 'Park Gorkogo', 'Антон Палыч Чехов', 'Достоевский Ф. М.']
    driver.get(link)
    # Ввод имени в поле ввода
    en_af = WebDriverWait(driver, 1200, 1).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '[aria-label="Ваше имя или никнейм"]')))
    driver.find_element(By.CSS_SELECTOR, '[aria-label="Ваше имя или никнейм"]').send_keys(random.choice(names))

    # Клик по кнопке ДАЛЕЕ
    en_af = WebDriverWait(driver, 1200, 1).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '[aria-label="Ваше имя или никнейм"]')))
    driver.find_element(By.CSS_SELECTOR, '.q-btn__content').click()

    for i in range(50):
        en_af = WebDriverWait(driver, 1200, 1).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '[style=""]')))
        time.sleep(random.randint(4, 12))
        driver.find_element(By.CSS_SELECTOR, '.flex.fit>.col>button:nth-child({})'.format(random.randint(1, 4))).click()
        en_af = WebDriverWait(driver, 100, 1).until(
            EC.element_to_be_clickable((By.XPATH, "//div[text()=' Ожидайте следующий вопрос ']"))
        )
        en_af = WebDriverWait(driver, 100, 1).until_not(
            EC.element_to_be_clickable((By.XPATH, "//div[text()=' Ожидайте следующий вопрос ']"))
        )



def multip():
    links = ["https://start.1t.ru/1tquiz/#/reg", "https://start.1t.ru/1tquiz/#/reg", "https://start.1t.ru/1tquiz/#/reg", "https://start.1t.ru/1tquiz/#/reg"]
    pool = Pool(processes=4)
    for i in range(0, len(links)):  
        pool.apply_async(test_func, args={links[i]})

    pool.close()
    pool.join()

if __name__ == '__main__':
     multip()