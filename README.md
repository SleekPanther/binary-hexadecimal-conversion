# Binary Hexadecimal Conversion
Convert hex to binary and binary to hex by slicing inputs & outputs into 4-bit nibbles

##Notes
- Choose to which direction to convert
- Option to enter more conversions unless you quit

##Limitations
- 32-bit binary input  
Not really an issue, since you can simply change `MAX_BITS_ALLOWED` to allow infinite sequences of 0's and 1's

##Code Details
- Uses 2 dictionaries of 4-bit nibbles to convert both ways
- Robust error handling checks:
  - Binay input is <= 32 bits
  - Empty string input is correctly returns 0000 binary or 0 hex
  - Hex is converted to uppercase to avoid duplicate dictionary keys for lowercase
  - Binary input is validated to make sure it is only 0's and 1's
  - Hex input catches KeyErrors if the input is not a value 0-9 or A-F
