##Programmer: Joselyne Guillen
##File Name: sentenceCapitalizer.py 
##Date: 3/14/21
##Version: 1.6
##Explanation of Program: 
##This program asks the user to input statements
##that don't have the first characters of each
##sentence capitalized and properly capitalizes
##the user input for them.

def main(): #main function
    userStringInput = input('Enter a statement with the first character of each sentence not capitalized\n') #asks user to input an uncapitalized statement
    print('Here is the statement with appropriate capitalization:') #label
    newString = capitalize(userStringInput) #function-returning call that sends user input as argument to properly capitalize statement
    print(newString) #prints capitalized statement
def capitalize(userString): #function that capitalizes the first character of each sentence
    userStringList = userString.split(' ') #splits input based on sentences and turns each sentence into an element in a list
    newChar = '' #initialize string
    i = 0 #initialize counter
    for sentence in userStringList: #loop to read each sentence element in the list
        sentence = sentence.strip() #strips the sentence element of blank spaces
        for char in sentence:       #loop to read each character in the sentence element
            if char != sentence[0]: #if the read character is not the beginning character
                newChar = newChar + char #add character as is to new string
            else: #if the read character is the beginning character
                if i == 0: #if counter is 0, which signifies the beginning of the sentence element
                    newChar = newChar + char.upper() #convert the character to uppercase character and add it to new string
                    i = i + 1 #increase counter by 1
                    
                else:
                    newChar = newChar + char.lower() #if counter is not 0, meaning it is not the beginning of the sentence element, convert the character to lowercase character and add it to new string
        i = 0 #resets counter for next sentence element in list
                    
        if newChar.endswith('.'): #if string ends with period, leave as is
            newChar = newChar + ''
        elif newChar.endswith('?'): #if string ends with question mark, leave as is
            newChar = newChar + ''
        elif newChar.endswith('!'): #if string ends with exclamation mark, leave as is
            newChar = newChar + ''
        else:
            newChar = newChar + '.' #if string doesn't end with period, add one at the end
    
    return newChar #returns the modified statement
  
main() #function call for main
