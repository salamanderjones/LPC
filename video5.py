num1 = input("Enter a number: ")
num2 = input("Enter another number: ")
result = num1 + num2 #this is a string, so doesn't work. gotta make a number
print(result)
realresult = int(num1) + int(num2) #converts to whole number
print(realresult)

num3 = input("Enter decimal number: ")
num4= input("Enter another decimal: ")
deciresult = float(num3) + float(num4) #float is for decimals
print(deciresult)