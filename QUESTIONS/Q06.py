
#made by adithya
libraryRecord =  [
["105MS" , "Marcus" , "Smith" , 25 ],
["103AZ" , "Anthony" , "Zarrent" , 5 ],
["108MW" , "Matt" , "White" , 12 ],
["112DB" , "Denise" , "Bilton" , 58 ],
["124MK" , "Malcolm" , "Kelly" , 26 ],
["116UK" , "Uzere" , "Kevill" , 29 ],
["127AL" , "Abduraheim" , "Leahy" , 94 ],
["124LS" , "Laura" , "Sampras" , 50 ],
["121AP" , "Azra" , "Potter" , 61 ],
["115AC" , "Anthony" , "Calik" , 10 ],
["117PI" , "Pablo" , "Iilyas" , 49 ],
["113MM" , "Mark" , "Montgomerie" , 68 ],
["130FH" , "Felicity" , "Heath" , 11 ],
["132JA" , "Jill" , "Alexander" , 61 ],
["123SG" , "Sara" , "Grimstow" , 9 ],
["134KD" , "Kevin" , "Dawson" , 74 ],
["122AB" , "Andrew" , "Bertwistle" , 42 ],
["125JF" , "Jaide" , "Feehily" , 55 ],
["128JS" , "Justin" , "Slater" , 68 ],
["126CG" , "Colleen" , "Grohl" , 39 ]
]
# ----------------------------------------------
# Write your code below this line
less_than_10 = [] ; books = []
total = 0
students_count = len(libraryRecord)
for student in libraryRecord:
    total += student[-1]
    if student[-1] < 10:
        students_count.append(student[0])
    books.append(student[-1])

books = sorted(books)
gold,silver,bronze = books[-1] , books[-2] , books[-3]
average = total / students_count

print("TOTAL BOOKS READ: " , total)
print("AVERAGE BOOKS READ: " , average)
print(f"GOLD -> {gold} , SILVER -> {silver} , BRONZE -> {bronze}")
for x in less_than_10:
    print(x , end=" ")
    
    

