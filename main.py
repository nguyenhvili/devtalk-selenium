from selenium.webdriver import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time


chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--headless')
chrome_options.add_argument("--disable-notifications")
chrome_options.add_argument("--disable-popup-blocking")
browser = webdriver.Chrome("chromedriver.exe", options=chrome_options)


def test_form():

    browser.get("https://login.szn.cz")

    # username_input = browser.find_element(By.ID, 'login-username')
    # username_input = browser.find_element(By.CSS_SELECTOR, '#login-username')
    username_input = browser.find_element(By.XPATH, '//*[@id="login-username"]')
    username_input.send_keys("test-acc@post.cz")


    browser.find_element(By.XPATH, '//form[@class="login"]/button[@type="submit"]').click()

    WebDriverWait(browser, 30).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '#login-password'))
    )

    browser.find_element(By.ID, 'login-password').send_keys("Test123")

    browser.find_element(By.XPATH, '//form[@class="login"]/button[@type="submit"]').click()
    browser.find_element(By.XPATH, '//form[@class="login"]/button').click()

    WebDriverWait(browser, 30).until(
        EC.presence_of_element_located((By.XPATH, '//a[text()="Napsat e-mail"]'))
    )

    write_email_btb = browser.find_element(By.XPATH, '//a[text()="Napsat e-mail"]')

    assert write_email_btb.is_enabled()
    write_email_btb.click()

    input()


if __name__ == '__main__':
    test_form()
