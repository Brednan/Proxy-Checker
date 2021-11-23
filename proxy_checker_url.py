import requests
from requests.api import post
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options


checked = 0
working = 0
failed = 0


def check_proxy(url, proxy, working_proxies_list, checked_text_var, working_text_var, failed_text_var, timeout, list_len):
    global checked
    global working
    global failed
    proxies = {
    "http": f'http://{proxy}',
    "https": f'http://{proxy}',
    }
    
    res_status = request_url(url, proxies, timeout)

    if res_status >= 200 and res_status <=299:
        working_proxies_list.append(proxy)
        checked = checked + 1
        working = working + 1
        checked_text_var.set(f'Checked: {checked}/{list_len}')
        working_text_var.set(f'Working: {working}')
    else:
        checked  = checked + 1
        failed = failed + 1
        failed_text_var.set(f'Failed: {failed}')
        checked_text_var.set(f'Checked: {checked}/{list_len}')


def request_url(url, proxy, timeout):
    try:
        response = requests.get(url, proxies=proxy, timeout=int(timeout))
        return response.status_code
    except:
        return 400



def selenium_request_url(proxy, timeout):
    try:
        options = Options()
        options.headless = False
        firefox_capabilities = webdriver.DesiredCapabilities.FIREFOX
        firefox_capabilities['marionette'] = True

        firefox_capabilities['proxy'] = {
            "proxyType": "MANUAL",
            "httpProxy": proxy,
            "sslProxy": proxy
        }

        driver = webdriver.Firefox(options=options, capabilities=firefox_capabilities)
        driver.set_page_load_timeout(timeout)
        driver.get('https://www.minecraft.net/')
        WebDriverWait(driver, 2).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="AccountNavMenu"]/a[1]'))
        )
        driver.quit()
        return 200
    except:
        driver.quit()
        return 400
