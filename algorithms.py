def saveState(page_frame, state, column, matrix):
    for i in range(page_frame):
        matrix[i][column] = state[i]
    return matrix

def algoOPTIMAL(page_frame, number_page, matrix):
    def switchState(state, column, matrix):
        if('X' in state):
            for i in range(page_frame):
                if(state[i] == 'X'):
                    matrix[i][column] = number_page[column]
                    k = i
                    break
            # Revert old state while saving new value
            for i in range(page_frame):
                if(i != k):
                    matrix[i][column] = state[i]
            # Add defaut
            matrix[page_frame][column] = 1
            return matrix
        elif(state == []):
            matrix[0][column] = number_page[column]
            # Add defaut
            matrix[page_frame][column] = 1
            return matrix
        else:
            # Search for the least recently used number
            columns = len(number_page) - 1
            i = column
            k = page_frame
            temp_state = [j for j in state]

            while(i < columns and k > 1):
                i = i + 1
                if(number_page[i] in temp_state):
                    # Decrement index
                    k = k - 1
                    # Remove the selected value from temp_state
                    temp_state.remove(number_page[i])

            # Check the value 
            # We need to replace the first number in state with new value
            for i in range(page_frame):
                if(state[i] == temp_state[0]):
                    matrix[i][column] = number_page[column]
                else:
                    matrix[i][column] = state[i]

            # Add defaut
            matrix[page_frame][column] = 1

            return matrix

    columns = len(number_page)
    for column in range(columns):
        # Save state of past column
        state = []
        if(column == 0):
            # Replace value
            matrix = switchState(state, column, matrix)
        else:
            # Save state
            for row in range(page_frame):
                state.append(matrix[row][column-1])
            # Replace value
            if(number_page[column] in state):
                # Keep the same state
                matrix = saveState(page_frame, state, column, matrix)
            else:
                # Replace value
                matrix = switchState(state, column, matrix)

    # Return result of matrix
    return matrix

def algoLRU(page_frame, number_page, matrix):
    def switchState(state, column, matrix):
        if('X' in state):
            for i in range(page_frame):
                if(state[i] == 'X'):
                    matrix[i][column] = number_page[column]
                    k = i
                    break
            # Revert old state while saving new value
            for i in range(page_frame):
                if(i != k):
                    matrix[i][column] = state[i]
            # Add defaut
            matrix[page_frame][column] = 1
            return matrix
        elif(state == []):
            matrix[0][column] = number_page[column]
            # Add defaut
            matrix[page_frame][column] = 1
            return matrix
        else:
            # Search for the least recently used number
            i = column
            k = page_frame
            temp_state = [j for j in state]
            while(i > 0 and k > 0):
                i = i - 1
                if(number_page[i] in temp_state):
                    # Update current
                    current = number_page[i]
                    # Decrement index in current
                    k = k - 1
                    # Remove the selected value from temp_state
                    temp_state.remove(current)

            # The least recently used is the number current
            # We need to replace the number of current in state with new value
            for i in range(page_frame):
                if(state[i] == current):
                    matrix[i][column] = number_page[column]
                else:
                    matrix[i][column] = state[i]

            # Add defaut
            matrix[page_frame][column] = 1

            return matrix

    columns = len(number_page)
    for column in range(columns):
        # Save state of past column
        state = []
        if(column == 0):
            # Replace value
            matrix = switchState(state, column, matrix)
        else:
            # Save state
            for row in range(page_frame):
                state.append(matrix[row][column-1])
            # Replace value
            if(number_page[column] in state):
                # Keep the same state
                matrix = saveState(page_frame, state, column, matrix)
            else:
                # Replace value
                matrix = switchState(state, column, matrix)

    # Return result of matrix
    return matrix


def algoFIFO(page_frame, number_page, matrix):
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
                matrix = saveState(page_frame, state, column, matrix)
            else:
                # Replace value
                matrix = switchState(state, column, matrix)

    # Return result of matrix
    return matrix
