import proxy_checker_url as url_check
import time
import threading, queue
from gui_functions.popup_window import popup_message
from save_proxies import save_to_file
from check_for_duplicates import remove_duplicates

status = 'None'

def on_submit(url, proxies, output_file_path, checked, working, failed, max_threads, status_text, timeout):
    global status
    proxies_list = None
    
    url_check.checked = 0
    url_check.failed = 0
    url_check.working = 0
    
    # Check if proxies are able to be split 
    try:
        proxies_list = proxies.rstrip('\n ').split('\n')
        proxies_list = remove_duplicates(proxies_list)
    except:
        # Check if exception is caused by proxies being empty
        if(len(proxies) <= 0):
            popup_message('You Must Submit Proxies!', '!', ['300', '50'], False)
        
        # Check if exception was caused by something else
        else:
            popup_message('There is something wrong with your proxy list!', '!', ['300', '50'], False)

    # Make sure there are proxies
    if(proxies_list != None):
        # Check if url has been submitted
        if len(url.strip()) <= 0:
            popup_message('You must submit a url!', '!', ['300','50'], False)

        # Check if proxies have been submitted    
        elif len(proxies_list) <= 0 or len(proxies_list[0].strip()) <= 0:
            popup_message('You Must Submit Proxies!', '!', ['300', '50'], False)

        # Check if output file has been entered
        elif len(output_file_path.strip()) <= 0:
            popup_message('You must submit an output file!', '!', ['300', '50'], False)
        
        # If everything is submited, then proceed
        else:
            #Make sure that the checker isn't already in progress
            if status == 'None' or status == 'Cancelled' or status == 'Finished':
                status = 'In Progress'
                status_text.set(f'Status: {status}')
                threading.Thread(target=iterate_proxies, args=(url, proxies_list, max_threads, status_text, checked, working, failed, output_file_path, timeout)).start()
            else:
                popup_message("The checker is already in progress! Click on the 'Cancel' button if you want to start", '!', ['300', '50'], False)


def iterate_proxies(url, proxies, max_threads, status_text, checked_text_var, working_text_var, failed_text_var, output_file, timeout):
    global status
    i = 0
    working_proxies = []
    while(i < len(proxies)):
        active_threads = threading.active_count()
        if(active_threads <= max_threads):
            t = threading.Thread(target=url_check.check_proxy, args=(url, proxies[i], working_proxies, checked_text_var, working_text_var, failed_text_var, timeout))
            t.start()
            i += 1
        if(status != 'In Progress'):
            break
    while(threading.active_count() > 2):
        pass
    if status == 'Cancelled':
        status = 'Finished'
        status_text.set(f'Status: {status}')
    else:
        status = 'Finished'
        status_text.set(f'Status: {status}')
        save_to_file(output_file, working_proxies)


def handle_exit(window):
    global status
    status = 'None'
    window.destroy()


def handle_cancel(status_text):
    global status
    if status == 'In Progress':
        status = 'Cancelled'
        status_text.set(f'Status: {status}')