# Ali Hooman
# alhooman@ucsc.edu
#
# Programming Assignment 7
#
# Spell out numbers from 0 to 999,999,999
#

# numberIn() inputs a number, checks preconditions, and returns as int
def numberIn():
    result = input("Enter a number from 0 to 999,999,999: ")
    result = result.replace(",","") 
    result = int(result)
    while result < 0 or result > 999999999:
        result = numberIn()
    return result

# Print selected number as digits
number = numberIn()
print("Number is: ", number)

# sayDigit() returns a text string for number from 0 to 9
def sayDigit(number):
    numWords = {"0":"zero", "1":"one", "2":"two", "3":"three",
                "4":"four", "5":"five", "6":"six", "7":"seven",
                "8":"eight", "9":"nine"}
    if type(number) is str:
        number = int(number)
    numberStr = str(number)
    result = numWords[numberStr]
    return result

# sayTeen() returns a text string for number from 0 to 19
def sayTeen(number):
    numWordsTeens = {"10":"ten", "11":"eleven", "12":"twelve", "13":"thirteen",
                     "14":"fourteen", "15":"fifteen", "16":"sixteen", "17":"seventeen",
                     "18":"eighteen", "19":"nineteen"}
    if type(number) is str:
        number = int(number)
    numberStr = str(number)
    result = ""

    if number < 10:
        result = sayDigit(number)

    elif number >= 10:
        result = numWordsTeens[numberStr]

    return result

# sayTens() returns a text string for number from 20 to 99
def sayTens(number):
    numWordsTens = {"20":"twenty", "30":"thirty", "40":"forty", "50":"fifty",
                    "60":"sixty", "70":"seventy", "80":"eighty", "90":"ninety"}
    if type(number) is str:
        number = int(number)
    numberStr = str(number)
    result = ""

    if number < 10:
        result = sayDigit(numberStr)

    elif number >= 10 and number < 20:
        result = sayTeen(numberStr)

    elif number >= 20 and number < 100:
        result = numWordsTens[numberStr]

    return result

# sayHundreds() returns a text string for number from 100 to 999
def sayHundreds(number):
    if type(number) is str:
        number = int(number)
    numberStr = str(number)
    result = []
    tempInt = number
    length = len(number)
    
    for i in range(1,-(length+1)):
        endNum = number % i
        answer = sayTens(endNum)
        result.insert(0,answer)
    
    return result

print(sayHundreds(number))
