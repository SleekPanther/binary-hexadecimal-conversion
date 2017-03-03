#comments

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

def main():
    print(hexEquivalentsOfBinary['0001'])
    print(binaryEquivalentsOfHex['F'])
    
    showWelcomeScreen()

def showWelcomeScreen():
    print('Hex & Binary Converter \nEnter 1 to convert unsigned binary to hexadecimal \nEnter 2 to convert hexadecimal to unsigned binary \nQuit (any other character) \nYour choice: ')
    

main()

'''
error checking on length
uppercase
left 0 padding
'''
