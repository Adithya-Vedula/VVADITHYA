print("============= RESTART: " + r"c:\Users\class11\Documents\VVADITHYA\CODE\ex19.py" + " ============")

#made by adithya
sums = 0
cnt = 0
code = input("Enter your code: ")
for i in code[0:3]:
    if i.isupper() == False:
        cnt += 1
for i in code[3:9]:
    if i.isdigit() == False:
        cnt += 1
    sums += int(i)
if code[9] == "e" and sums%2 != 0 or code[9] == "o" and sums%2 == 0:
    cnt += 1
if cnt > 0:
    print("INVALID CODE")
else:
    print("VALID CODE")

