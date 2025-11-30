

try:
 columns = int(input("Enter an amount of columns: "))
 rows = int(input("Enter an amount of rows: "))
 symbol = input("Enter a symbol: ")

 for i in range(columns):
    for j in range(rows):
        print(symbol,end="")
    print()
except ValueError:
   print("please enter a correct value".upper())