def save_to_file(file_path, proxies_list):
    txt_file = open(f'{file_path}', 'w')
    for p in proxies_list:
        txt_file.write(f'{p}\n')
    txt_file.close()