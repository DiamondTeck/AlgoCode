def X_pos(ch1,ch2):
    x=[]
    i=0
    v=50
    while v>0 :
        x.append(ch2.find(ch1))
        if x[i]!=-1:
            ch2=ch2[x[i]+1:len(ch2)]
            v+=1
        elif x[i]==-1:
            x.pop(-1)
            v=-1
        i+=1
    for j in range(i-1):
        print(x[j])
        if j<i-2:
            x[j+1]=x[j]+x[j+1]+1
    return x





#nom1=input("Donner Le nom du fichier en python\n")
#nom2=input("Donner Le nom pour le fichier en text\n")
#al=input("Donner Le nom de l'algorithme :\n")

nom1="py"
nom2="py"
al="al"

i=0
c=1
z = []

with open(nom1+".py", "r") as fichier1, open(nom2+".txt", "w") as fichier2:
    fichier2.write("algorithme "+al+"\n")
    fichier2.write("debut\n")
    for s in fichier1:
        x=[]
        sc=[]
        b=[]
        d=[]
        h=""
        e=""
        if "\n" in s:
            s=s[0:len(s)-1]
        if "," in s :
            
            x=X_pos(",",s)
            x.insert(0,s.find("("))
            x.append(s.find(")"))
            y=s[0:s.find("(")+1]
            for l in range (len(x)-1):
                sc.append(s[x[l]+1:x[l+1]+1]) #sc.append(s[x[l]+1:x[l+1]]) : pour enlrver les ','
            for j in range (len(sc)):
                if ("'" != sc[j][0] and '"' != sc[j][0]):
                    if "%" in sc[j]:
                        b=X_pos("%",sc[j])
                        d=X_pos("//",sc[j])
                        v=list(sc[j])
                        for k in range (len(b)):
                            v.pop(b[len(b)-k-1]) 
                            v.insert(b[len(b)-k-1]," mod ")
                            for l in range(len(v)):
                                h=h+v[l]
                            
                            sc[j]=h
                    if "//" in sc[j]:
                        k=0
                        w=""
                        for k in range (len(d)):
                            v.pop(d[len(d)-k-1])
                            v.pop(d[len(d)-k-1])
                            v.insert(d[len(d)-1]," div ")
                        k=0
                        for k in range(len(v)):
                            w=w+v[k]
                        k=0
                        for k in range(len(sc)):
                            sc[j]=w
                            e=e+sc[k]
                    s=y+e
        if "print" in s :
            x = s.find("print")
            z.append("ecrire"+s[x+5:len(s)])
        elif "input()" in s :
            z.append("lire("+s[0]+")")
        elif "input(" in s and (s[s.find("input(")+6] == '"' or s[s.find("input(")+6] == "'"):
            z.append("ecrire("+s[s.find("input(")+6:len(s)])
            z.append("lire("+s[0]+")")
            i+=1
        
            
        else :
            if s != "" and s != " ":
                print("ERROR on line ",c)
            
        i+=1
        c+=1
    for j in range (i):
        if z[j] != " " and z[j] != "":
            fichier2.write("    "+z[j]+"\n")

    fichier2.write("Fin")
