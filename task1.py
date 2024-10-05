number = int(input("Enter range number :"))
randomnum = []


for x in range(number):
    givenumber = int(input("Enter Number : "))
    if givenumber > 0:
        print("Positive")
    elif givenumber < 0:
        print("negative")
    randomnum.append(givenumber)
    print(randomnum)

for i in randomnum:
    if i > 0:
        print(i, "this number is positive")
    elif i < 0:
        print(i, "this number is negative")
    
