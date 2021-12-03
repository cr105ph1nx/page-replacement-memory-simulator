import re

def setArchitecture():
    page_size = int(input("Quelle est la taille de la page (KO)? "))
    physical_mem = int(
        input("Quelle est la taille de la memoire physique (KO)? "))
    word_mem = int(input("Quelle est la taille du mot memoire (O)? "))

    return([page_size, physical_mem, word_mem])


def getPageFrame(architecture):
    return int(architecture[1]/architecture[0])


def getPageSize(architecture):
    return architecture[0]


def getWordMem(architecture):
    return architecture[2]


def setAdresses():
    adresses = input(
        "Entrer la chaine de reference (separee par une virgule): ")
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


def fillMatrix(page_frame, number_page):
    # Fill Matrix
    matrix = ['X'] * (page_frame+1)
    i = 0

    while(i < page_frame):
        matrix[i] = ['X'] * len(number_page)
        i += 1
    
    matrix[i] = [0] * len(number_page)

    return matrix 

def algoFIFO(page_frame, number_page, matrix):
    def saveState(state, column, matrix):
        for i in range(page_frame):
            matrix[i][column] = state[i]
        return matrix 

    def switchState(state, column, matrix):
        if(column == 0):
            matrix[0][0] = number_page[column]
            # Add defaut 
            matrix[page_frame][column] = 1
            return matrix 
        else: 
            i = page_frame-1
            j = column-1
            # Suppose max
            max = [i, matrix[i][j], 1]
            while(j > 0):
                j = j - 1
                current = matrix[i][j]
                if(current != max[1]):
                    break
                else:
                    max[2] += 1   
            # Iterate over rows
            while(i > 0):
                # Decrement values
                i -= 1
                j = column-1
                temp = [i, matrix[i][j], 1]  

                # Iterate over columns
                while(j > 0):
                    j = j - 1 
                    current = matrix[i][j]
                    if(current != temp[1]):
                        break
                    else:
                        temp[2] += 1
                
                # Compare max and temp
                if(temp[2] >= max[2] and temp[1] == 'X'):
                    for k in range(page_frame):
                        max[k] = temp[k]
                elif(temp[1] != 'X' and max[1] != 'X' and temp[2] >= max[2]):
                    for k in range(page_frame):
                        max[k] = temp[k]
            
            # Once we break out of the loop, our oldest row is in max[0]
            # Let's switch the value of matrix[max[0]][column] with number_page[column]
            matrix[max[0]][column] = number_page[column]
            # Revert old state while saving new value 
            for i in range(page_frame):
                if(i != max[0]):
                    matrix[i][column] = state[i]
            # Add defaut 
            matrix[page_frame][column] = 1
            return matrix 

    for column in range(len(number_page)):
        # Save state of past column
        state = []
        if(column == 0):
            # Replace value
            matrix = switchState(state, column, matrix)
        else:
            for row in range(page_frame):
                state.append(matrix[row][column-1])
            # Replace value
            if(number_page[column] in state):
                # Keep the same state
                matrix = saveState(state, column, matrix)
            else: 
                # Replace value
                matrix = switchState(state, column, matrix)

    # Return result of matrix
    return matrix

def main():
    architecture = setArchitecture()
    page_size = getPageSize(architecture)
    word_mem = getWordMem(architecture)
    adresses = setAdresses()
    pages = getPages(adresses)
    page_frame = getPageFrame(architecture)
    number_page = getNumberPages(pages, page_size, word_mem)
    matrix = fillMatrix(page_frame, number_page)
    matrix = algoFIFO(page_frame, number_page, matrix)
    
    for i in range(page_frame+1):
        print(matrix[i])


if __name__ == "__main__":
    main()
