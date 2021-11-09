import requests


checked = 0
working = 0
failed = 0


def check_proxy(url, proxy, working_proxies_list, checked_text_var, working_text_var, failed_text_var, timeout):
    global checked
    global working
    global failed
    proxies = {
    "http":proxy,
    "https":proxy
    }
    res_status = request_url(url, proxies, timeout)
    if res_status >= 200 and res_status <=299:
        working_proxies_list.append(proxy)
        checked = checked + 1
        working = working + 1
        checked_text_var.set(f'Checked: {checked}')
        working_text_var.set(f'Working: {working}')
    else:
        checked  = checked + 1
        failed = failed + 1
        failed_text_var.set(f'Failed: {failed}')
        checked_text_var.set(f'Checked: {checked}')


def request_url(url, proxy, timeout):
    try:
        response = requests.get(url, proxies=proxy, timeout=int(timeout))
        return response.status_code
    except:
        return 400
