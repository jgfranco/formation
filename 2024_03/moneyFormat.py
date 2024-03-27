'''
You're working on a finance application and need to format monetary amounts in the following manner for accounting purposes. Every number must adhere to a strict set of rules:

1. All amounts are rounded to two decimal places, even if it is .00.
2. A $ precedes the first digit.
3. Thousands, millions, billions, etc have commas between every 3 digits from the left of the decimal.
4. Negative numbers are surrounded by parentheses.
5. If the absolute amount is less than 1, there should still be a zero before the '.'

Write a function that takes a numeric value and outputs the "finance formatted" string representation.

This is a very realistic data processing problem with lots of special cases!
 
0.051602
0.05



1000.04462


10000.00462

function add comas to integer

"1000"



Decimal handling:
5 or greater is rounded up
4 or less is rounded down

assumptions:
well formatted int or floats as input



use round() 

check if the input is an integer or float



convert integers to floats

convert to string 
1.0
"1.0"

for all floats im gonna use round 
    check if i have two decimal places, if not append the missing decimals
add comas
    split by the dot .
    traverse the "int" portion backwards add a coma every three chars

    put back together


add the $ symbol to the string

check if number is positive or Negative 
    wrap the string with parentheses if Negative

return string

'''
def moneyFormat(amount: float):
    number = abs(amount)
    number = float(number) # .0
    number = round(number, 2)

    numberAsString = str(number)

    intPortion, floatPortion = numberAsString.split(".") # O(n)

    # add commas
    formattedIntPortion = ""
    intPortion = intPortion[::-1]

    # 1000 0001
    # counter 0, 1, 2, 3
    # 000,1
    counter = 0
    for i in range(len(intPortion)):
        if counter ==3:
            formattedIntPortion += ","
            counter = 0
        formattedIntPortion += intPortion[i]
        counter += 1
    
    intPortion = formattedIntPortion[::-1]

    ## check if I have two decimal places

    if len(floatPortion) == 1:
        floatPortion += "0"

    numberAsString  = "$" + intPortion + "." + floatPortion

    if amount < 0:
        numberAsString  = "(" + numberAsString + ")"

    return numberAsString



def moneyFormat(amount: float) -> str:
  def padZeros(number, length):
    neededZeros = length - len(str(number))
    return ''.join(['0'] * neededZeros) + str(number)

  # check if the final result needs parentheses
  isNeg = amount < 0
  amount = -amount if isNeg else amount

  # calculate the decimal portion
  amount = round(amount * 100)
  decimalPart = padZeros(amount % 100, 2)
  amount = amount // 100

  # segment the integer into 3 digit portions for adding commas
  parts = []
  while amount > 0:
    nextPart = amount % 1000
    parts.append(str(nextPart))
    amount = amount // 1000

  parts.reverse()

  for i in range(1, len(parts)):
    parts[i] = padZeros(parts[i], 3)

  # special case when the amount < 1
  if len(parts) == 0:
    parts.append('0')

  dollarPart = ','.join(parts)
  digits = f'${dollarPart}.{decimalPart}'

  return f'({digits})' if isNeg else digits
'''

FUNCTION SIGNATURE
function moneyFormat(amount) {
def moneyFormat(amount: float) -> str:



0.045 => 0.04
0.3 =

EXAMPLE(S)
moneyFormat(1) == "$1.00"
moneyFormat(-1) == "($1.00)"
moneyFormat(16) == "$16.00"
moneyFormat(123) == "$123.00"
 
'''

print(moneyFormat(1) == "$1.00")
print(moneyFormat(-1) == "($1.00)")
print(moneyFormat(16) == "$16.00")
print(moneyFormat(123) == "$123.00")


print(moneyFormat(-1000000.0462))



# happy cases
print(moneyFormat(0) == "$0.00")
print(moneyFormat(1) == "$1.00")
print(moneyFormat(-1) == "($1.00)")
print(moneyFormat(16) == "$16.00")
print(moneyFormat(123) == "$123.00")

# decimal variants
print(moneyFormat(0.01) == "$0.01")
print(moneyFormat(.02) == "$0.02")
print(moneyFormat(.3) == "$0.30")
print(moneyFormat(0.0001) == "$0.00")
print(moneyFormat(4.954) == "$4.95")
print(moneyFormat(4.955) == "$4.96")
print(moneyFormat(4.) == "$4.00")

# comma variants
print(moneyFormat(1234) == "$1,234.00")
print(moneyFormat(1001.01) == "$1,001.01")
print(moneyFormat(50000) == "$50,000.00")
print(moneyFormat(6789123456789) == "$6,789,123,456,789.00") # 6.7 trillion

# negative variants
print(moneyFormat(-0.01) == "($0.01)")
print(moneyFormat(-.02) == "($0.02)")
print(moneyFormat(-0.001) == "($0.00)")
print(moneyFormat(-1000) == "($1,000.00)")

# complex variants
print(moneyFormat(-34567) ==  "($34,567.00)")
print(moneyFormat(-12345.67) ==  "($12,345.67)")
print(moneyFormat(-12345.678) ==  "($12,345.68)")