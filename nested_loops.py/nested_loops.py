#nested loops = A loop within ia npther loop ( outer, inner )
#              outer loop:
#                   inner loop:
for x  in range (1,10) :
    print(x, end =" ") # prints all together

for x in range (5):
    for y in range(1,10):
        print(y, end =" ")
    print()

    rows = int(input("enter the # of rows :"))
    colums = int(input("enter the # of colums :"))
    symbols = int(input("enter the # of symbols :"))

    for x in range (rows):
        for y in range(colums):
            print(symbols, end =" ")
    print() 