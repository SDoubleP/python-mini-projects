


def CtoF(celsius):
    return (celsius*9/5)+32

def FtoC(fahrenheit):
    return (fahrenheit -32)*5/9

userChoice = int(input("Please Choose \n 1 : C TO F \n 2 : F TO C"))
if(userChoice == 1):
    Celsius = float(input("Please Enter Celsius to convert to Fahrenheit : "))
    print(CtoF(Celsius))
elif(userChoice==2):
    Fahrenheit = float(input("Please Enter Fahrenheit to convert to Celsius : "))
    print(FtoC(Fahrenheit))
else:
    print("Please Choose 1 or 2")

