import tkinter as tk
from tkinter import ttk
import utils

# 2, 5012, 6200, 8215, 2000, 17800, 50, 13248, 18456, 1203, 5741, 9442, 16524, 23580, 16895, 22630, 123

def create_pages_frame(container):
    frame = ttk.Frame(container)

    # add padding
    frame['padding'] = (0, 0, 0, 20)

    for ligne in range(7):
        for colonne in range(7):
            ttk.Button(frame, text='L%s-C%s' %
                       (ligne, colonne)).grid(row=ligne, column=colonne)

    return frame


def create_options_frame(container):
    frame = ttk.Frame(container)

    ttk.Button(frame, text='FIFO').grid(column=0, row=0)
    ttk.Button(frame, text='LRU').grid(column=0, row=1)
    ttk.Button(frame, text='OPTIMAL').grid(column=0, row=2)
    ttk.Button(frame, text='Renitialiser').grid(column=0, row=3)

    for widget in frame.winfo_children():
        widget.grid(padx=10, pady=3)

    return frame


def create_textfield_frame(container):
    frame = ttk.Frame(container)

    var = tk.StringVar()
    label = tk.Label(frame, text="Nothing to show for now...", relief='sunken', width=40, bg='white').grid(column=0, row=0, padx=10, pady=20)
    var.set("Hey!? How are you doing?")

    return frame


def create_buttons_frame(container):
    frame = ttk.Frame(container)

    ttk.Button(frame, text='Annuler').grid(column=0, row=0, padx=10, pady=20)
    ttk.Button(frame, text='OK').grid(column=1, row=0)

    return frame


def create_main_window():
    # root window
    root = tk.Tk()
    root.title('Remplacement Page')
    root.geometry('700x300')
    root.resizable(0, 0)

    # layout on the root window
    root.columnconfigure(1, weight=1)


    textfield_frame = create_textfield_frame(root)
    textfield_frame.grid(column=0, row=0, sticky='NW')

    buttons_frame = create_buttons_frame(root)
    buttons_frame.grid(column=0, row=0, sticky='NE')

    pages_frame = create_pages_frame(root)
    pages_frame.grid(column=0, row=1, sticky='NW')

    options_frame = create_options_frame(root)
    options_frame.grid(column=1, row=1, sticky='NE')

    root.mainloop()


if __name__ == "__main__":
    create_main_window()
