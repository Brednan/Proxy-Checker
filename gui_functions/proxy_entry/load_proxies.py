from tkinter.filedialog import askopenfilename
from ..popup_window import popup_message


def proxy_loader(proxy_entries):
    proxy_file_dir = None

    try:
        proxy_file_dir = askopenfilename()
        try:
            proxies = open(proxy_file_dir, 'r')
            proxy_entries.insert('1.0', proxies.read())
        except:
            popup_message('Invalid File!', '!', (200,50), False)

    except FileNotFoundError:
        pass
