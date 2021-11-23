def remove_duplicates(proxies_list):
    proxies_list = list(dict.fromkeys(proxies_list))
    return proxies_list