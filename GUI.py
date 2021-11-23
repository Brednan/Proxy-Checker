import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinter.constants import CENTER, W
from gui_functions.proxy_entry.load_proxies import proxy_loader
from gui_functions.proxy_entry.clear_proxies import clear_proxy_entries
from gui_functions.set_output_file import get_output_dir
import event_manager

window = tk.Tk()
window.geometry('600x800')
window.title('Proxy Checker')
window.resizable(False, False)


proxies_checked = tk.StringVar(value='Checked: 0')
proxies_working = tk.StringVar(value='Working: 0')
proxies_failed = tk.StringVar(value='Failed: 0')


app_title = tk.Label(window, text='PROXY CHECKER', font=('default', 40))
app_title.place(x=70, y=20)

status_text_var = tk.StringVar(value=f'Status: {event_manager.status}')

#Create the URL checker tab
entries_frame = tk.Frame(window, width=500, height=535, borderwidth=3, relief=tk.RIDGE)
entries_frame.place(x=300, y=375, anchor=CENTER)


#Set URL checking frame
url_entry_label = tk.Label(entries_frame, text='URL:', font=('default', 16))
url_entry_label.place(anchor=W, x=5, y=60)
url_entry = tk.Entry(entries_frame, font=('default', 16), width=28)
url_entry.place(x=140, y=60, anchor=W)


proxy_entry_label = tk.Label(entries_frame, text='Proxies:', font=('default', 16))
proxy_entry_label.place(anchor=W, x=5, y=160)
proxy_entry = scrolledtext.ScrolledText(entries_frame, font=('default', 16), width=19, height=4)
proxy_entry.place(anchor=W, x=140, y=189)
load_proxies_button = tk.Button(entries_frame, text='Load', font=('default', 14), width=8, height=1, command=lambda: proxy_loader(proxy_entry))
load_proxies_button.place(anchor=W, x=390, y=159)
clear_proxies_button = tk.Button(entries_frame, text='Clear', font=('default', 14), width=8, height=1, command=lambda: clear_proxy_entries(proxy_entry))
clear_proxies_button.place(anchor=W, x=390, y=209)


max_threads_label = tk.Label(entries_frame, text='Max Threads:', font=('default', 16))
max_threads_label.place(x=5, y=292, anchor=W)
max_threads_entry = tk.Scale(entries_frame, from_=0, to=450, orient=tk.HORIZONTAL, length=242)
max_threads_entry.set(64)
max_threads_entry.place(anchor=W, x=140, y=284)


timeout_label = tk.Label(entries_frame, text='Timeout:', font=('default', 16))
timeout_label.place(x=5, y=352, anchor=W)
timeout_entry = tk.Scale(entries_frame, from_=0, to=10, orient=tk.HORIZONTAL, length=242)
timeout_entry.set(10)
timeout_entry.place(anchor=W, x=140, y=344)


output_entry_label = tk.Label(entries_frame, text='Output File:', font=('default', 16))
output_entry_label.place(anchor=W, x=5, y=415)
output_entry = tk.Entry(entries_frame, font=('default', 16), width=20)
output_entry.place(anchor=W, x=140, y=417)
set_output_button = tk.Button(entries_frame, text='...', font=('default', 14), width=8, height=1, command=lambda: get_output_dir(output_entry))
set_output_button.place(anchor=W, x=390, y=415)


start_button = tk.Button(entries_frame, text='Start', font=('default', 20), width=10, command=lambda: event_manager.on_submit(url=url_entry.get(), proxies=proxy_entry.get('0.0', 'end'), output_file_path=output_entry.get(), checked=proxies_checked, working=proxies_working, failed=proxies_failed, max_threads=max_threads_entry.get(), status_text=status_text_var, timeout=timeout_entry.get()))
start_button.place(anchor=CENTER, x=250, y=490)


status_frame = tk.Frame(window, width=500, height=100, borderwidth=3, relief=tk.RIDGE)
status_frame.place(x=300,y=700, anchor=CENTER)


status_display = tk.Label(status_frame, textvariable=status_text_var, font=('default', 15))
status_display.place(x=10, y=10)


checked = tk.Label(status_frame, textvariable=proxies_checked, font=('default', 15))
checked.place(x=10, y=50)


working = tk.Label(status_frame, textvariable=proxies_working, font=('default', 15))
working.place(x=360, y=10)


failed = tk.Label(status_frame, textvariable=proxies_failed, font=('default', 15))
failed.place(x=360, y=50)


cancel = tk.Button(status_frame, text='Cancel', font=('default', 17), width=7, height=1, command=lambda: event_manager.handle_cancel(status_text_var))
cancel.place(x=243, y=50, anchor=CENTER)


window.protocol('WM_DELETE_WINDOW', lambda: event_manager.handle_exit(window))
window.mainloop()