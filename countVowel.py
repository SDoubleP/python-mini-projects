userInput = input("Please Enter words to count vowel : ")
count = 0
for x in userInput:
    if(x == "a" or x =="e" or x =="i" or x =="o" or x =="u"):
        count = count+1

print("Total number of vowels in your words : ",count)