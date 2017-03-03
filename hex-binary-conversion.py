#

import math

hexEquivalentsOfBinary = {
    '0000':'0', 
    '0001':'1', 
    '0010':'2', 
    '0011':'3', 
    '0100':'4', 
    '0101':'5', 
    '0110':'6', 
    '0111':'7', 
    '1000':'8', 
    '1001':'9', 
    '1010':'A', 
    '1011':'B', 
    '1100':'C', 
    '1101':'D', 
    '1110':'E', 
    '1111':'F' }

binaryEquivalentsOfHex = {
    '0':'0000', 
    '1':'0001', 
    '2':'0010', 
    '3':'0011', 
    '4':'0100', 
    '5':'0101', 
    '6':'0110', 
    '7':'0111', 
    '8':'1000', 
    '9':'1001', 
    'A':'1010', 
    'B':'1011', 
    'C':'1100', 
    'D':'1101', 
    'E':'1110', 
    'F':'1111' }
MAX_BITS_ALLOWED = 32       #used to limit user input
NIBBLE_SIZE = 4             #half a byte. (4 digits long of 1's and 0's)

def main():
    showWelcomeScreen()

def showWelcomeScreen():
    #while True:
    binaryToHex()
    #userChoice=input('\nHex & Binary Converter \nEnter 1 to convert unsigned binary to hexadecimal \nEnter 2 to convert hexadecimal to unsigned binary \nQuit (any other character) \nYour choice: ')
    #userChoice=userChoice.lstrip(' ')   #remove leading spaces
    #print("|"+userChoice+'|')
    #if(userChoice[0]=='1'):     #check 1st character in string
    #    binaryToHex()
    #elif(userChoice[0]=='2'):
    #    hexToBinary()
    #else:
    #    print('\nProgram Done')
    

def binaryToHex():
    #print('\nbin 2 hex')
    #binaryValue=input('Enter binary number (max 32 bits): ')
    hexEquivalent=''

    binaryValue='1010101110001011'
    binaryValueLength = len(binaryValue)    #string length
    if binaryValueLength%NIBBLE_SIZE !=0:     #if NOT divisible by 4,  add padding 0's to the left
        paddingZeros= NIBBLE_SIZE - binaryValueLength%NIBBLE_SIZE    #find if length is divisible by NIBBLE_SIZE of 4 (remainder). Subtract from 4 to find how many MORE digits need to be added to length IS divisible by 4
        binaryValue = '0'*paddingZeros + binaryValue    #add padding 0's to the left
        binaryValueLength = len(binaryValue)    #recalculate length since we added to it
    print(binaryValue)

    rightIndex=binaryValueLength-1      #end index is 1 less than size (0 based)
    leftIndex=rightIndex -(NIBBLE_SIZE-1)    #NIBBLE_SIZE-1 since we need the 4 consecutive numbers. 0+3=3 but we include 0 and get values 0,1,2,3 (4 values)
    iterations = int(binaryValueLength/NIBBLE_SIZE)   #loop iterates over 4 character at a time until it runs out of the string
    for i in range(iterations):
        nibble = binaryValue[leftIndex:(rightIndex+1)]      #get 4 characters from the string
        hexEquivalent = hexEquivalentsOfBinary[nibble] +hexEquivalent
        rightIndex -=NIBBLE_SIZE      #decrement indexes by 4
        leftIndex -=NIBBLE_SIZE

    print(binaryValue+' binary = '+hexEquivalent+' hex')
    #showWelcomeScreen()     #go back to main program

def hexToBinary():
    print('\nhex 2 bin')
    hexValue=input('Enter a hexadecimal number: ').strip(' ').upper()    #remove leading/trailing spaces & force UPPERCASE
    binaryEquivalent=''
    for char in reversed(hexValue):
        try:
            print(binaryEquivalentsOfHex[char])
            binaryEquivalent= binaryEquivalentsOfHex[char] +binaryEquivalent
        except KeyError:        #if key is not in my list of valid conversions
            print('Error, you entered an invalid hex value. Try again')
            hexToBinary()     #exit loop & try again
    
    print(hexValue+' hex = '+binaryEquivalent+' binary')
    showWelcomeScreen()     #go back to main program

def isValidBinary(string):
    for char in string:         #loop through string & return false if it finds any character other than 0 or 1
        if(ch!='0' and ch!='1'):
            return false
    return true

main()

'''
error checking on length
uppercase
'''
