num = int(input())
reversed = 0
print("Current number: " + str(num))

while num != 0: #1234 
    digit = num % 10
    reversed = reversed * 10 + digit 
    num //= 10

print("Reversed Number: " + str(reversed))