def X_pos(ch1,ch2):
    if ch1 in ch2:
        x=ch2.find(ch1)
        ch21=ch2[x:len(ch2)]
        ch21.find(ch1)


def find_exp(s,fich):
    if "," in s:
        print("hi")




nom1=input("Donner Le nom du programme\n")
nom2=input("Donner Le nom du fichier\n")
al=input("Donner Le nom de l'algorithme :\n")


i=0
z = [[],[],[]]
with open(nom1+".py", "r") as fichier1, open(nom2+".txt", "w") as fichier2:
    fichier2.write("algorithme "+al+"\n")
    fichier2.write("debut\n")
    for s in fichier1:
        if "print" in s :
            x = s.find("print")
            z[i][0] = "ecrire"+s[x+5:len(s)-1]
        elif "input()" in s :
            z[i][0] ="lire("+s[0]+")"
        elif "input(" in s and (s[s.find("input(")+6] == '"' or s[s.find("input(")+6] == "'"):
            z[i][0] = "ecrire("+s[s.find("input(")+6:len(s)]
            z[i][1] = "lire("+s[0]+")"
        else :
            z[i][0] = " "
            print("ERROR on line ")
        i=i+1
    for j in range (i):
        for k in range (2) :
            if z[j][k] != " " :
                fichier2.write("    "+z[j][k]+"\n")

    fichier2.write("\nFin")
