from tkinter import *
from tkinter import messagebox
from utils import getPages, getNumberPages, getColumns, fillMatrix, algoFIFO

# 2, 5012, 6200, 8215, 2000, 17800, 50, 13248, 18456, 1203, 5741, 9442, 16524, 23580, 16895, 22630, 123
fields = ('Taille de la page (KO)', 'Taille de la memoire physique (KO)',
          'Taille du mot memoire (O)', 'La chaine de reference (separee par une virgule)')
data = {
    "page_size": 4,
    "physical_mem": 12,
    "word_mem": 1,
    "page_frame": 3,
    "number_pages": [0, 1, 1, 2, 0, 4, 0, 3, 4, 0, 1, 2, 4, 5, 4, 5, 0]
}

show = False

def setInput(root, entries):
    global data, show

    try:
        page_size = int(entries['Taille de la page (KO)'].get())
        physical_mem = int(entries['Taille de la memoire physique (KO)'].get())
        word_mem = int(entries['Taille du mot memoire (O)'].get())
        adresses = entries['La chaine de reference (separee par une virgule)'].get(
        )
        page_frame = int(physical_mem/page_size)
        pages = getPages(adresses)
        number_pages = getNumberPages(pages, page_size, word_mem)

        data = {
            "page_size": page_size,
            "physical_mem": physical_mem,
            "word_mem": word_mem,
            "page_frame": page_frame,
            "number_pages": number_pages
        }
        initializeTable(root)

    except:
        messagebox.showerror(
            "Données incorrectes !", "Il semble que les données que vous avez saisies soient incorrectes, veuillez remplir le formulaire avec des données valides...")


def makeform(root, fields):
    entries = {}
    for field in fields:
        row = Frame(root)
        lab = Label(row, width=40, text=field+": ", anchor='w')
        ent = Entry(row)
        ent.insert(0, "0")
        row.pack(side=TOP, fill=X, padx=5, pady=5)
        lab.pack(side=LEFT)
        ent.pack(side=RIGHT, expand=YES, fill=X)
        entries[field] = ent
    return entries


def create_form_frame(container):
    frame = Frame(container)

    ents = makeform(frame, fields)
    ok_button = Button(frame, text='OK',
                       command=(lambda e=ents: setInput(container, e)))
    ok_button.pack(side=RIGHT, padx=5, pady=5)
    cancel_button = Button(frame, text='Annuler', command=container.quit)
    cancel_button.pack(side=RIGHT, padx=5, pady=5)

    return frame


def create_simulation_frame(container):
    global table_frame

    table_frame = Frame(container, bg='white')
    table_frame.grid(padx=(5, 0))

    columns = getColumns(data['number_pages'])
    columns_len = len(columns)
    rows_len = data['page_frame'] + 2

    # Initialize first row
    for j in range(columns_len):
        Button(table_frame, text=columns[j]).grid(row=0, column=j)
    # Initialize first column
    for i in range(rows_len):
        if(i == rows_len - 1):
            Button(table_frame, text="Defauts").grid(row=i, column=0)
        elif(i != 0):
            Button(table_frame, text=("Page %d" % i)).grid(row=i, column=0)

    return table_frame


def create_options_frame(container):
    frame = Frame(container)

    Button(frame, text='FIFO', width=8, command=lambda: handleFIFO(
        container)).grid(column=0, row=0)
    Button(frame, text='LRU', width=8).grid(column=0, row=1)
    Button(frame, text='OPTIMAL', width=8).grid(column=0, row=2)
    Button(frame, text='Renitialiser', width=8,
           command=lambda: initializeTable(container)).grid(column=0, row=3)

    for widget in frame.winfo_children():
        widget.grid(padx=10, pady=3, sticky='NW')

    return frame


def initializeTable(root):
    simulation_frame = create_simulation_frame(root)
    simulation_frame.grid(column=0, row=1, sticky='NW', pady=(20, 0))

    options_frame = create_options_frame(root)
    options_frame.grid(column=1, row=1, sticky='NW',
                       pady=(20, 0), padx=(0, 5))


def handleFIFO(container):
    global table_frame 

    columns = getColumns(data['number_pages'])
    columns_len = len(columns)
    page_frame = data['page_frame']
    rows_len = page_frame + 2

    # Create a matrix of data
    number_page = data['number_pages']
    matrix = fillMatrix(page_frame, number_page)
    matrix = algoFIFO(page_frame, number_page, matrix)

    # Fill table
    for column in range(columns_len):
        for row in range(rows_len):
            if(row != 0 and column != 0):
                # Add defauts buttons 
                if(row == rows_len - 1):
                    Button(table_frame, text=matrix[row-1][column-1],
                       bg="red").grid(row=row, column=column)
                else:
                    # Add regular buttons
                    Button(table_frame, text=matrix[row-1][column-1],
                       bg="white").grid(row=row, column=column)


    return table_frame


if __name__ == '__main__':
    root = Tk()
    root.title('Remplacement Page')
    root.geometry('800x410')
    # layout on the root window
    root.columnconfigure(1, weight=1)

    form_frame = create_form_frame(root)
    form_frame.grid(column=0, row=0, sticky='NW')

    root.mainloop()
