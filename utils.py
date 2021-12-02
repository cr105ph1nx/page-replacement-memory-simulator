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

def setPages():
    pages = input("Entrer la chaine de reference (separee par une virgule): ")
    # Transform string to list
    pages = re.split(',+', pages)
    # Convert to list of int
    pages = list(map(int, pages))
    # Return list
    return pages

def getNumberShift(pages, page_size, word_mem):
    numberShift = []
    # Convert page size to Byte 
    page_size = page_size * word_mem * 1024
    # Iterate over each page and calculate the number of page and shift
    for page in pages:
        numberShift.append([int(page/page_size), int(page%page_size)])
    # Return result
    return numberShift

def main():
    architecture = setArchitecture()
    page_size = getPageSize(architecture)
    word_mem = getWordMem(architecture)
    pages = setPages()
    numberShift = getNumberShift(pages, page_size, word_mem)

    print(numberShift)

if __name__ == "__main__":
    main()
