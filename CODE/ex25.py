print("============= RESTART: " + r"c:\Users\class11\Documents\VVADITHYA\CODE\ex25.py" + " ============")

#Q06

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
ascrecord=sorted(libraryRecord, key=lambda x: x[3], reverse=True)
tot=0
print("ID of students reading less than 10 books:")
num=len(libraryRecord)
for i in range(num):
    tot+=libraryRecord[i][3]
    if libraryRecord[i][3]<10:
        print(libraryRecord[i][0])
avg=tot/num
print("Total number of books read by pupils=",tot)
print("Average number of books read by each pupil=",avg)
medals=["Gold","Silver","Bronze"]
print("MEDAL","\t","ID","\t"," NAME")
for i in range(3):
    print(medals[i],end="\t")
    for j in range(3):
        print(ascrecord[i][j],end=" ")
    print()





