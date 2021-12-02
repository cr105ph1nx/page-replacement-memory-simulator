import re 

def setArchitecture():
    page_size = int(input("Quelle est la taille de la page (KO)? "))
    physical_mem = int(input("Quelle est la taille de la memoire physique (KO)? "))
    word_mem = int(input("Quelle est la taille du mot memoire (O)? "))

    return([page_size, physical_mem, word_mem])

def getPageFrame(architecture):
    return architecture[1]/architecture[0]

def getPageSize(architecture):
    return architecture[0]

def getWordMem(architecture):
    return architecture[2]

def setAdresses():
    adresses = input("Entrer la chaine de reference (separee par une virgule): ")
    return adresses

def getPages(adresses):
    # Transform string to list
    adresses = re.split(',+', adresses)
    # Convert to list of int
    pages = list(map(int, adresses))
    # Return list
    return pages

def getNumberPages(pages, page_size, word_mem):
    number_pages = []
    # Convert page size to Byte 
    page_size = page_size * word_mem * 1024
    # Iterate over each page and calculate the number of page
    for page in pages:
        number_pages.append(int(page/page_size))
    # Return result
    return number_pages

def getColumns(number_pages):
    columns = ['Chaine']

    for number_page in number_pages:
        value = str(number_page)
        columns.append(value)

    return columns
