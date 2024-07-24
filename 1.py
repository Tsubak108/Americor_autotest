
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


@pytest.fixture
def driver():
    options = Options()
    options.add_argument('--incognito')
    options.add_experimental_option("excludeSwitches", ["ignore-certificate-errors"])
    options.add_argument("--disable-cache")
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-notifications")
    options.add_argument(f"--window-size=1980,1080")

    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()

@pytest.mark.parametrize(
    "creds",
             [('demo','demo'),
              ('demo123','demo123'),
              ('123','321')])

def test_login(driver,creds):
    login, passw = creds
    driver.get("https://idemo.bspb.ru/auth?response_type=code&client_id=1&redirect_uri=https%3A%2F%2Fidemo.bspb.ru%2Flogin%2Fsuccess&prefetch_uri=https%3A%2F%2Fidemo.bspb.ru%2Flogin%2Fprefetch&force_new_session=true")
    username_field = driver.find_element(By.ID, "username")
    username_field.send_keys(login)
    password_field = driver.find_element(By.NAME, "password")
    password_field.send_keys(passw)
    login_button = driver.find_element(By.ID, "login-button")
    login_button.click()
   # WebDriverWait(driver, 60)
    #ok = driver.find_element(By.ID, "otp-code-test")
   # assert ('Отправили СМС код на ваш номер телефона' == ok)


