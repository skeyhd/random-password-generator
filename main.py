# Password Generator
import random
import time

# Shuffles string
def shuffle(string):
  tempList = list(string)
  random.shuffle(tempList)
  return ''.join(tempList)

# Random Uppercase Letter
def generateUppercase():
    global uppercaseLetter
    uppercaseLetter = chr(random.randint(65,90))
    return uppercaseLetter

# Random Lowercase Letter
def generateLowercase():
    global lowercaseLetter
    lowercaseLetter = chr(random.randint(97,122)) 
    return lowercaseLetter

# Random Digit 
def generateDigit():
    global digit
    digit = str(random.randint(0,9))
    return digit

# Random Punctuation Sign
def generatePunctuation():
    global punctuationSign
    punctuationSign = chr(random.randint(33,47)) 
    return punctuationSign

# While Loop Conditions
validLength = False
uppercaseNumLength = False
lowercaseNumLength = False
digitNumLength = False

# User Inputs Password Length
while validLength == False:
    passwordLength = int(input("How long do you want your password to be? (7-50): "))
    remainingChar = passwordLength

    # Password Length Validation
    if passwordLength < 7 or passwordLength > 50:
        print("Invalid Length.")
        validLength = False
    else:
        validLength = True
    
# Input Number of Uppercase Letters and Validate
while uppercaseNumLength == False:
    uppercaseNum = int(input(f"How many Uppercase Letters? You have {remainingChar} characters left: "))
    if uppercaseNum > remainingChar or remainingChar < uppercaseNum:
        print("Invalid.")
        uppercaseNumLength = False
    else:
        remainingChar -= uppercaseNum
        uppercaseNumLength = True

# Input Number of Lowercase Letters and Validate
while lowercaseNumLength == False:
    lowercaseNum = int(input(f"How many Lowercase Letters? You have {remainingChar} characters left: "))
    if lowercaseNum > remainingChar or remainingChar < lowercaseNum:
        print("Invalid.")
        lowercaseNumLength = False
    else:
        remainingChar -= lowercaseNum
        lowercaseNumLength = True

# Input Number of Digits and Validate
while digitNumLength == False:
    digitNum = int(input(f"How many Digits? You have {remainingChar} characters left: "))
    if digitNum > remainingChar or remainingChar < digitNum:
        print("Invalid.")
        digitNumLength = False
    else:
        remainingChar -= digitNum
        digitNumLength = True

# Remaing Characters = Number of Punctuation Signs
time.sleep(1)
print(f"You will have {remainingChar} punctuation signs.")
time.sleep(1)
punctuationNum = remainingChar
remainingChar -= punctuationNum


# Create Unsorted Password
password = ""

for i in range(0,uppercaseNum):
    password += generateUppercase()
for i in range(0,lowercaseNum):
    password += generateLowercase()
for i in range(0,digitNum):
    password += generateDigit()
for i in range(0,punctuationNum):
    password += generatePunctuation()

# Sort and Ouput
print(f"Your password is : {shuffle(password)}")
