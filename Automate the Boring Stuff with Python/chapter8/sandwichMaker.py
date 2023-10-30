# sandwichMaker.py
# very spaghetti code

import pyinputplus as pyip

breadMenu = {
    "wheat": 2.00,
    "white": 2.50,
    "sourdough": 3.00,
}

proteinMenu = {
    "chicken": 2.00,
    "turkey": 2.50,
    "ham": 3.00,
    "tofu": 2.00,
}

cheeseTypeMenu = {
    "cheddar": 2.00,
    "swiss": 2.50,
    "mozzarella": 3.00,
}

totalCost = 0
promptBread = 'Please choose your bread type:\n'
responseBread = pyip.inputMenu(['wheat', 'white', 'sourdough'])

promptProtein = 'Please choose your protein type:\n'
responseProtein = pyip.inputMenu(['chicken', 'turkey', 'ham', 'tofu'])

promptCheese = 'Do you want cheese on your bread?\n'
responseCheese = pyip.inputYesNo(promptCheese)

if responseCheese == 'yes':
    promptCheeseType = 'What kind of cheese would you like?\n'
    responseCheeseType = pyip.inputMenu(['cheddar', 'swiss', 'mozzarella'])

promptSauce = 'Do you want mayo, mustard, lettuce, and tomato on your bread?\n'
responseSauce = pyip.inputYesNo(promptSauce)

promptAmount = 'How many sandwiches would you like to order?\n'
responseAmount = pyip.inputInt(promptAmount, greaterThan=0)

optionPriceYes = [breadMenu[responseBread], proteinMenu[responseProtein], cheeseTypeMenu[responseCheeseType], 
                2.00]
optionPriceNo = [breadMenu[responseBread], proteinMenu[responseProtein], cheeseTypeMenu[responseCheeseType], 
                2.00]

orderDataSauceYes = [[responseBread, responseProtein, responseCheeseType, "sauce = " + responseSauce, 
                    responseAmount],
                    [breadMenu[responseBread], proteinMenu[responseProtein], cheeseTypeMenu[responseCheeseType],
                    2.00, sum(optionPriceYes) * responseAmount]]

orderDataSauceNo =  [[responseBread, responseProtein, responseCheeseType, "sauce = " + responseSauce, 
                    responseAmount],
                    [breadMenu[responseBread], proteinMenu[responseProtein], cheeseTypeMenu[responseCheeseType],
                    0.00, (sum(optionPriceNo) * responseAmount)]]

def printTable():

    # Initialize 'max_list' to store the longest word in each list.
    max_list = []

    # Outer loop,  iterate through the lists. 'max_word' is used to store the longest word in each list.
    for list in orderDataSauceYes or orderDataSauceNo:
        max_word = ''

        # Inner loop, iterate through the words in each list.
        for word in list:
            
            # Eventually the longest word will be found and stored in max_word.
            if len(str(word)) > len(str(max_word)):
                max_word = word
        max_list.append(max_word)
    
    # max_length is used to store the lengths of the longest words in each list as integers.
    max_length = []
    for list_word in max_list:
        max_length.append(len(str(list_word)))

    # Iterate through the first word in each columns, and the second and so on.
    for i in range(len(orderDataSauceYes[0] or orderDataSauceNo[0])):

        # Printing each row with the max word length in each list as the argument to rjust
        for j, list in enumerate(orderDataSauceYes or orderDataSauceNo):
            print(str(list[i]).rjust(max_length[j]), end = ' ') 

        # The output will be a table of all the words in tableData with each column right-justified.
        print()

printTable()
print("Your order will be " + str(sum(optionPriceNo) * responseAmount) + ".")