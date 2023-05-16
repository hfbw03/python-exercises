# tablePrinter

# Assign a list of lists to a variable
tableData = [['apples', 'oranges', 'bananas', 'grapes'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def printTable():

    # Initialize 'max_list' to store the longest word in each list.
    max_list = []

    # Outer loop,  iterate through the lists. 'max_word' is used to store the longest word in each list.
    for list in tableData:
        max_word = ''

        # Inner loop, iterate through the words in each list.
        for word in list:
            
            # Eventually the longest word will be found and stored in max_word.
            if len(word) > len(max_word):
                max_word = word
        max_list.append(max_word)
    print(max_list)
    
    # max_length is used to store the lengths of the longest words in each list as integers.
    max_length = []
    for list_word in max_list:
        max_length.append(len(list_word))
    print(max_length)

    # Iterate through the first word in each columns, and the second and so on.
    for i in range(len(tableData[0])):

        # Printing each row with the max word length in each list as the argument to rjust
        for j, list in enumerate(tableData):
            print(list[i].rjust(max_length[j]), end = ' ') 

        # The output will be a table of all the words in tableData with each column right-justified.
        print()

printTable()