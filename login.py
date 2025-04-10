import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from getCreds import d365_preview_cred
def d365_login(driver, username, password):
    driver.get("https://dynamicsd365fando.operations.dynamics.com/?cmp=usmf&mi=DefaultDashboard")
    time.sleep(3)

    driver.find_element(By.XPATH, "//input[@type='email']").send_keys(username + Keys.RETURN)
    time.sleep(3)

    driver.find_element(By.XPATH, "//input[@type='password']").send_keys(password + Keys.RETURN)
    time.sleep(3)

    try:
        driver.find_element(By.ID, "idSIButton9").click()
    except:
        print("No 'Stay signed in' prompt detected.")


def login(driver):
    secrets = d365_preview_cred()
    username = secrets["username"]
    password = secrets["password"]
    print("Username:", username)
    print("Password:", password)
    # Login
    d365_login(driver, username, password)
    print("Login Successful!")