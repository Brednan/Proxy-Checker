from tkinter.filedialog import askopenfilename
from .popup_window import popup_message

def get_output_dir(output_entry):
    file_dir = None

    try:
        file_dir = askopenfilename()
    except FileNotFoundError:
        pass
    
    try:
        file = open(file_dir, 'r')
        file.read()
        output_entry.delete('0', 'end')
        output_entry.insert('0', file_dir)
    except:
        popup_message('Invalid File!', '!', (200,50), False)
