#   Q07

#   Structure of sales record is
#   StaffID, First name, Last name, January sales, February sales,
#   March sales, April sales, May sales, June sales

staffSales = [
["101TGY" , "George" , "Taylor" , 6009 , 5262 , 3745 , 7075 , 1943 , 4432],
["103FCY" , "Fehlix" , "Chayne" , 8717 , 2521 , 5777 , 6189 , 5089 , 6957],
["102SBY" , "Sumren" , "Bergen" , 5012 , 1063 , 7937 , 9560 , 1115 , 5499],
["104SBK" , "Samira" , "Beckle" , 1140 , 9206 , 3898 , 8544 , 5937 , 8705],
["105NBT" , "Nellie" , "Bogart" , 3017 , 3342 , 5939 , 2479 , 3374 , 2297],
["106CGT" , "Cheryl" , "Grouth" , 9620 , 7160 , 5113 , 4803 , 5492 , 2195],
["107DGT" , "Danuta" , "Graunt" , 1583 , 7450 , 1026 , 7463 , 2390 , 6509],
["108JDN" , "Jaiden" , "Deckle" , 4064 , 4978 , 2984 , 3159 , 1464 , 4858],
["109JCK" , "Jimran" , "Caliks" , 6253 , 7962 , 2732 , 7504 , 2771 , 5193],
["110DDN" , "Deynar" , "Derran" , 6305 , 8817 , 5200 , 3647 , 3365 , 1256]]

#--------------------------------------------------------------------------
#   Write your code below this line
allsale=list(staffSales)
sumall=0
sales=[]
for i in range(len(staffSales)):
    sumeach=0
    for j in range(3,len(staffSales[0])):
                   sumeach+=staffSales[i][j]
    print("Sales made by",staffSales[i][1],"=",sumeach)
    sales.append(sumeach)
    allsale[i][-1]=sumeach
print("Sales made by entire team=",sum(sales))

salearrange=sorted(allsale, key=lambda x: x[-1], reverse=True)
print(salearrange)
print("HIGHEST SALES MADE BY:")
for i in range(2):
    print(salearrange[i][1],salearrange[i][2])
