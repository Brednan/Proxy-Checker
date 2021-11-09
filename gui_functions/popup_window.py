import tkinter as tk

def popup_message(msg, title, size, is_resizable):
    root = tk.Tk()
    root.resizable(height = is_resizable, width = is_resizable)
    root.geometry(f'{size[0]}x{size[1]}')
    root.title(title)

    message_text = tk.Label(root, text=msg, font=('default', 15))
    message_text.place(x=int(size[0])/2, y=int(size[1])/2, anchor=tk.CENTER)

    root.mainloop()