# -------------------------------------------------------------------
# Global variables
# -------------------------------------------------------------------

#  First Name, Last Name,Year of birth
ArtistList = [["Cashin","Bonnie",1962],
            ["Cheruit","Madeleine",1950],
            ["Chanel","Coco",1980],
            ["Gres","Madame",1930],
            ["Hamnett","Katharine",2000],
            ["Herrera","Carolina",1967],
            ["Hulanicki","Barbara",1928],
            ["Johnson","Betsey",2001],
            ["Lanvin","Jeanne",1950],
            ["McCardell","Claire",1995],
            ["Paquin","Jeanne",1934],
            ["Quant","Mary",1902],
            ["Rykiel","Sonia",1977],
            ["Schiaparelli","Elsa",1980],
            ["Schlee","Valentina",1976],
            ["Vionnet","Madeleine",1942],
            ["Von Furstenberg","Diane",1993],
            ["Wang","Vera",2004],
            ["Westwood","Vivienne",1947]]

# -------------------------------------------------------------------
# Main program
# -------------------------------------------------------------------
theLabels=[]
artarrange=sorted(ArtistList, key=lambda x: x[-1])

for i in range(len(ArtistList)):
    label=ArtistList[i][1][0]+ArtistList[i][0][1]+ArtistList[i][2]
    theLabels.append(label)

    print("Label of",ArtistList[i][0],ArtistList[i][1],"is",theLabels[i])

print("Youngest Member:",artarrange[0][0],artarrange[0][1],"-",artarrange[0][2])
