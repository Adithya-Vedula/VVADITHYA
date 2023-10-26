print("============= RESTART: " + r"c:\Users\class11\Documents\VVADITHYA\CODE\ex16.py" + " ============")

#made by adithya
sym=input("Enter a symbol (+,-,*,/): ")
n=int(input("Enter a natural no. "))

print(sym, "|", end=" ")
for i in range(n+1):
    print(i, end=" ")
print()
print("---------------------")
for i in range(n+1):
    print(i,"|",end=" ")
    for j in range(n+1):
        print(j+i, end=" ")
    print()
