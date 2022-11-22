inputList = list(map(int, input('Enter your list: ').split()))
typeNum = int(input("Enter 0 or 1 = "))
for i in range(0,len(inputList)):
    if inputList[i] % 2 == 0 and typeNum == 1:
        inputList[i] += 10
    if inputList[i] % 2 != 0 and typeNum == 0:
        inputList[i] += 5
    print(inputList[i], end=" ")
